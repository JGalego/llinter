"""
Extract lint rules with ScrapeGraphAI
"""

# Standard imports
import argparse
import json
import os

# Library imports
from scrapegraphai.graphs import SmartScraperGraph

# Constants
SOURCE = "https://pylint.readthedocs.io/en/latest/user_guide/checkers/features.html"
PROMPT = "Extract all basic checker and format checker rules (id, name, description and message)."

parser = argparse.ArgumentParser(
    prog="LintScraper",
    description="Extract lint rules with ScrapeGraphAI.",
)
parser.add_argument('-s', '--source', default=SOURCE)
parser.add_argument('-p', '--prompt', default=PROMPT)
parser.add_argument('-m', '--model', default="gpt-4o-mini")
parser.add_argument('-o', '--output', default="rules.json")

# Parse arguments
args = parser.parse_args()

# Define scraping pipeline config
graph_config = {
    'llm': {
        'api_key': os.getenv('OPENAI_API_KEY'),
        'model': f"openai/{args.model}",
    },
    'verbose': True,
    'headless': False,
}

# Create graph instance
smart_scraper_graph = SmartScraperGraph(
    prompt=args.prompt,
    source=args.source,
    config=graph_config
)

# Run pipeline
result = smart_scraper_graph.run()

# Display results
rules = json.dumps(result, indent=4)
with open(args.output, "w", encoding="utf-8") as f:
    print(rules)
    f.write(rules)
