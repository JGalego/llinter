## LLinter 🧶

> ⚠️ **For demo purposes only:** use with caution!

Lint your codebase using LLMs:
- extracts rules using [ScrapeGraphAI](https://scrapegraphai.com/)
- creates prompt templates with [Jinja2](https://jinja.palletsprojects.com/en/stable/)
- reviews code via [OpenAI API](https://platform.openai.com/docs/overview) calls
- processes findings with [inspector](https://github.com/instructor-ai/instructor)

![](llinter.gif)

## Getting Started

1. Install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

2. (*Optional*) Scrape lint rules

    ```bash
    python scrape.py
    ```

3. Run LLM linter

    ```bash
    python llint.py examples/bad.py
    ```

**Output:**

```
🚨 Alert, linter found 2 violations!
+-------+-----------------------+-----------------------+---------------------------------------------------------------------------+
|   ID  |          Name         |          Code         |                                  Comments                                 |
+-------+-----------------------+-----------------------+---------------------------------------------------------------------------+
| W0301 | unnecessary-semicolon | print("hello world"); | The semicolon at the end of the print statement is unnecessary in Python. |
| W0123 |       eval-used       |        eval(x)        | The use of eval is considered dangerous as it can execute arbitrary code. |
+-------+-----------------------+-----------------------+---------------------------------------------------------------------------+
```

## Examples

### Scraper

```bash
usage: LintScraper [-h] [-s SOURCE] [-p PROMPT] [-m MODEL] [-o OUTPUT]

Extract lint rules with ScrapeGraphAI.

options:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
  -p PROMPT, --prompt PROMPT
  -m MODEL, --model MODEL
  -o OUTPUT, --output OUTPUT
```

### Linter

```bash
usage: LLinter [-h] [-r RULES] [-p PROMPT] [-m MODEL] script

Lints a target file using LLMs.

positional arguments:
  script

options:
  -h, --help            show this help message and exit
  -r RULES, --rules RULES
  -p PROMPT, --prompt PROMPT
  -m MODEL, --model MODEL
```

## References

### Articles

* (Fang *et al.*, 2025) [LintLLM: An Open-Source Verilog Linting Framework Based on Large Language Models](https://arxiv.org/abs/2502.10815)

### Code

* [`gptlint/gptlint`](https://github.com/gptlint/gptlint): use LLMs to enforce best practices across your codebase
* [`lintrule/lintrule`](https://github.com/lintrule/lintrule): a new kind of linter and test framework