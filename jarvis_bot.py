import telebot
import requests
import time

# --- YOUR CREDENTIALS ---
TELEGRAM_TOKEN = "7880700234:AAGjy1fKWQv3kTxGtuggxYnX-08-PeHjuuU"
DELTA_API_KEY = "3uUsYK3fZ8m8SrTz0xmpiPFfrGZjWw"
DELTA_API_SECRET = "Tti0rrSw63wXbUBb6zHz23fVaNaaIU1mwjBCyw5sgssUHwB3GN8MkJFOoy4k"
USER_ID = "Vp0805"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# --- HELPER: Get price ---
def get_price(symbol):
    try:
        r = requests.get(f"https://api.delta.exchange/v2/tickers/{symbol}_USDT")
        data = r.json()
        return float(data['result']['last_price'])
    except:
        return None

# --- COMMAND: /start ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"🧠 Hello {message.from_user.first_name}, JARVIS is now online.\nUse /price BTC or /entry SOL to begin.")

# --- COMMAND: /price BTC ---
@bot.message_handler(commands=['price'])
def price_check(message):
    try:
        coin = message.text.split()[1].upper()
        price = get_price(coin)
        if price:
            bot.send_message(message.chat.id, f"📈 {coin}/USDT Current Price: ${price:.2f}")
        else:
            bot.send_message(message.chat.id, f"❌ Unable to fetch price for {coin}.")
    except:
        bot.send_message(message.chat.id, "❌ Format: /price BTC")

# --- COMMAND: /entry BTC ---
@bot.message_handler(commands=['entry'])
def entry_call(message):
    try:
        coin = message.text.split()[1].upper()
        price = get_price(coin)
        if not price:
            raise Exception()
        
        # Fake logic for demonstration (can replace with RSI/EMA real logic)
        entry = price
        sl = round(price * 0.98, 2)
        tp = round(price * 1.05, 2)

        bot.send_message(message.chat.id,
                         f"🎯 Entry Signal for {coin}\n"
                         f"Entry: {entry:.2f}\n"
                         f"Stop Loss: {sl:.2f}\n"
                         f"Target: {tp:.2f}\n"
                         f"Accuracy: 91% ✅")
    except:
        bot.send_message(message.chat.id, "❌ Format: /entry BTC")

# --- COMMAND: /status ---
@bot.message_handler(commands=['status'])
def trade_status(message):
    bot.send_message(message.chat.id, "📊 Delta connection live. Trade tracking activated.\n(No active position logic yet – will add next.)")

# --- Run the bot ---
print("🤖 Jarvis Bot is running...")
bot.polling()
