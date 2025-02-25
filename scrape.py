"""
Extract Pylint rules with ScrapeGraphAI
"""

import json
import os

from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    'llm': {
        'api_key': os.getenv('OPENAI_API_KEY'),
        'model': "openai/gpt-4o-mini",
    },
    'verbose': True,
    'headless': False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract all basic checker and format checker rules (id, name, description and message).",
    source="https://pylint.readthedocs.io/en/latest/user_guide/checkers/features.html",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

# Display the results
rules = json.dumps(result, indent=4)
with open("rules.json", "w", encoding="utf-8") as f:
    print(rules)
    f.write(rules)
