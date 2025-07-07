# Crypto JARVIS Telegram Bot 🤖

A smart Telegram bot that tracks BTC, SOL, and ETH in real-time and gives buy/sell signals using Delta Exchange API.

## Features
- /start → activates bot
- /price BTC → live market price
- /entry SOL → gives entry, SL, TP
- /status → trade summary

## Deploy on Render
1. Connect this repo on Render.com
2. Use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python jarvis_bot.py`
3. Done! Bot is live on Telegram.

## Requirements
See `requirements.txt` for dependencies:
- requests
- pyTelegramBotAPI
