# Pirate Chat CLI

A command-line AI assistant that can interact with local files using tools like `ls`, `cat`, `grep`, and `calculate`.


## Badges

![Doctests](https://github.com/abedoya-norena/lab-more-project-setup-Public/actions/workflows/doctest.yml/badge.svg)
![Integration](https://github.com/abedoya-norena/lab-more-project-setup-Public/actions/workflows/integration.yml/badge.svg)
![Flake8](https://github.com/abedoya-norena/lab-more-project-setup-Public/actions/workflows/flake8.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/cmc-csci005-alejandro)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)


## Demo

![Demo GIF](demo.gif)


## Usage Examples

### Markdown Compiler

This example demonstrates how the chat tool can analyze a codebase by searching for specific patterns across files.

```bash
cd test_projects/Markdown-to-HTML-compiler
chat
chat> does this project use regular expressions?
No. I grepped the project files and did not find any use of the `re` library.
```
### Ebay Scraper

This example demonstrates how the agent can summarize a project and answer higher-level questions about its purpose and implications.

```bash
cd test_projects/Ebay_webscrapping
chat
chat> tell me about this project
The project is designed to scrape product information from eBay listings.

chat> is this legal?
In general, scraping public webpages is often legal, although using an official API is usually more reliable and efficient.
```

### Personal Website

This example demonstrates how the tool can interpret and summarize the contents of a non-Python project.

```bash
cd test_projects/abedoya-norena.github.io
chat
chat> what does this project contain?
This project contains the files for a personal website, including HTML and related assets.
```
