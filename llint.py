"""
Lints a target Python file using with an LLM.
"""

# Standard imports
import argparse
import json

# Library imports
from jinja2 import Template
from openai import OpenAI

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

# Initialize cliente
client = OpenAI()

# Retrieve rules
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

# Process response
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=args.model,
    temperature=0.0,
)

print(response.choices[0].message.content)
