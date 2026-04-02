import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👤 About Me", callback_data='about')],
        [InlineKeyboardButton("🎬 My Work", callback_data='work')],
        [InlineKeyboardButton("📦 Services", callback_data='services')],
        [InlineKeyboardButton("💰 Pricing", callback_data='pricing')],
        [InlineKeyboardButton("📞 Contact", callback_data='contact')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 Welcome to The Artisan Cut 🚀\n\n👇 Choose an option:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await query.edit_message_text("👤 Professional Video Editor 🎬\nThe Artisan Cut")

    elif query.data == 'work':
        await query.edit_message_text("🎬 Portfolio:\nhttps://drive.google.com/drive/folders/1uhpoUFy0KwfKJ9Z3_NJVixkUy9Dkqz73")

    elif query.data == 'services':
        await query.edit_message_text("📦 Services:\nVideo Editing\nAds\nReels")

    elif query.data == 'pricing':
        await query.edit_message_text("💰 1500৳/min\nCustom project available")

    elif query.data == 'contact':
        await query.edit_message_text("📞 WhatsApp:\nhttps://wa.me/8801810875771")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
