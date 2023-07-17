# Discord Chat Exporter

A simple Python script that exports a Discord channel's chat history into a static website that mimics the look of Discord's dark theme.

## Preview
![Screenshot](./unnamed.png)

## Features

- Fetches all messages from a specified Discord channel.
- Exports the messages into a JSON file.
- Generates a static website from the JSON file with Flask and Jinja.
- The website includes avatar images, author names, messages, and timestamps for each message.
- The website's design imitates Discord's dark theme.

## Requirements

- Python 3.6+
- Discord.py
- Flask
- Jinja2

## Usage

1. Clone this repository and navigate into the directory:

```bash
git clone https://github.com/yourusername/discord-chat-exporter.git
cd discord-chat-exporter
```
add the bot token , channel id and server id to the scraper.py then run the script