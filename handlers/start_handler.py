# from telegram import Update
from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Halo selamat datang di sistem pengecekan nomor NRK\n\nKetik /help untuk melihat fitur penggunaan bot ini.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if "Bagaimana cara menggunakan bot ini?" in update.message.text:
        help_text = "Anda dapat menggunakan perintah seperti di bawah ini:\n\n/cek <nomor karyawan>\n/cek <nomor hp> "
        keyboard = [
            [InlineKeyboardButton("/cek <nomor karyawan>", callback_data='cek_nrk')],
            [InlineKeyboardButton("/cek <nomor hp>", callback_data='cek_nohp')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(help_text, reply_markup=reply_markup)
        await update.message.reply_text('Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor karyawan>')
        await update.message.reply_text('Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor hp>')

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = "Anda dapat menggunakan perintah seperti di bawah ini:\n\n/cek <nomor karyawan>\n/cek <nomor hp> "
    keyboard = [
        [InlineKeyboardButton("/cek <nomor karyawan>", callback_data='cek_nrk')],
        [InlineKeyboardButton("/cek <nomor hp>", callback_data='cek_nohp')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(help_text, reply_markup=reply_markup)
    await update.message.reply_text('Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor karyawan>')
    await update.message.reply_text('Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor hp>')

    

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'cek_nrk':
        await query.message.reply_text("Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor karyawan>")
    elif query.data == 'cek_nohp':
        await query.message.reply_text("Untuk menggunakan perintah ini, anda dapat mengetikkan:\n/cek <nomor hp>")
