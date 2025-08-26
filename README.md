# SCAMHUNTER Demo

SCAMHUNTER is a community-driven initiative to crowdsource and share information about scam cryptocurrency addresses. This repository contains a demo implementation of the SCAMHUNTER project.

## Features

* **Open database** of known scam addresses stored in `scammers.json`.
* **API** built with Flask to check whether an address appears in the database.
* **Command-line interface** (`scamhunter_cli.py`) for quick lookups.
* **Telegram bot** (`telegram_bot.py`) that lets users query addresses via Telegram.

## Getting Started

1. Clone the repository and install dependencies: `pip install flask python-telegram-bot`.
2. Run the API server: `python scamhunter_api.py`.
3. Check an address using the CLI: `python scamhunter_cli.py --address 0x123`.

## Contributing

Feel free to contribute additional scam addresses to the `scammers.json` file via pull requests.

## Funding

If this project helps you or your community, consider sponsoring us or making a donation. Check the `FUNDING.yml` file for donation addresses.
