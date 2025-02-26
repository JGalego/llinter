"""
Lints a target file using an LLM.
"""

# Standard imports
import argparse
import json

from typing import Iterable, Optional

# Library imports
import instructor

from jinja2 import Template
from openai import OpenAI
from prettytable import PrettyTable
from pydantic import BaseModel

parser = argparse.ArgumentParser(
    prog="LLinter",
    description="Lints a target file using LLMs.",
)
parser.add_argument("script")
parser.add_argument('-r', '--rules', default="rules.json")
parser.add_argument('-p', '--prompt', default="prompt.j2")
parser.add_argument('-m', '--model', default="gpt-4o")

# Parse arguments
args = parser.parse_args()

# Define desired output structure
class Finding(BaseModel):
    """Linter finding base class"""
    id: str
    name: str
    code: Optional[str] = None
    comments: Optional[str] = None

# Patch OpenAI client
client = instructor.from_openai(OpenAI())

# Retrieve lint rules
with open(args.rules, "r", encoding="utf-8") as rules_f:
    rules_scraped = json.load(rules_f)

rules = []
for section in rules_scraped.keys():
    rules.extend(rules_scraped[section])

# Get script content
with open(args.script, "r", encoding="utf-8") as script_f:
    script = script_f.read()

# Prepare prompt
with open(args.prompt, "r", encoding="utf-8") as template_f:
    template = Template(template_f.read())
prompt = template.render(rules=rules, script=script)
print(prompt)

# Run LLM linter
findings = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=args.model,
    response_model=Optional[Iterable[Finding]],
    temperature=0.0,
)

# Process response
findings = list(findings) if findings else []
if (n := len(findings)) > 0:
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Code", "Comments"]
    for finding in findings:
        table.add_row([
            finding.id,
            finding.name,
            finding.code,
            finding.comments
        ])
    print(f"🚨 Alert, linter found {n} violations!")
    print(table)
else:
    print("✅ Code clear, no violations found!")
