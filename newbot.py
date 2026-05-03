import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes

TOKEN = os.environ.get("8781310059:AAFVO9t4TDkTcT22FGTQPIEpUVZmo2WqZ3k")

app = Flask(__name__)
application = ApplicationBuilder().token(TOKEN).build()

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(), application.bot)
    await application.process_update(update)
    return "ok"