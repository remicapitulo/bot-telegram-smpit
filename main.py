from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
import os

# === Load Token dari Environment ===
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


# === Command Bot ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya adalah bot Telegram SMPIT Pondok Duta 🤝"
    )


async def portalguru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "📋 *PORTAL GURU*\n\n"
        "1. Portal Guru:\n"
        "https://guru.smpitpondokduta.sch.id/\n"
        "login menggunakan NIK Diktendik\n"
        "username: NIK Diktendik\n"
        "password: guru123"
    )
    await update.message.reply_text(message, parse_mode="Markdown")


async def passwordwifi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "💡 *PASSWORD WIFI SEKOLAH*\n\n"
        "*Lantai 1:*\n"
        "Nama WiFi: Lantai1 Ruang1 / Lantai1 Ruang2\n"
        "Password: `B4tuttaS1na`\n\n"
        "*Lantai 2:*\n"
        "Nama WiFi: Lantai2 Ruang1 / Lantai2 Ruang2 / LAB KOM\n"
        "Password: `Kh0ldunN4fis`\n\n"
        "*Lantai 3:*\n"
        "Nama WiFi: Lantai3 Ruang1 / Lantai3 Ruang2 / LAB IPA\n"
        "Password: `M4j4hRusdh`\n\n"
        "*Kantor TU:*\n"
        "`lagierror`\n\n"
        "*SMPIT PONDOK DUTA:*\n"
        "`l4girus4k`"
    )
    await update.message.reply_text(message, parse_mode="Markdown")


async def inventaris(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *INVENTARIS SEKOLAH*\n\nhttps://inventaris.smpitpondokduta.sch.id/",
        parse_mode="Markdown",
    )


async def databasesekolah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗂️ *DATABASE SEKOLAH*\n\nhttps://drive.google.com/drive/folders/1BMQgUNBSbDlLw7TaEp-vdJNGW61y6nbI",
        parse_mode="Markdown",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan_help = (
        "➡️ *Perintah yang tersedia adalah:*\n\n"
        "/start - Ucapan Selamat Datang\n"
        "/portalguru - Link Portal Guru\n"
        "/passwordwifi - Password WiFi Sekolah\n"
        "/inventaris - Link Inventaris Sekolah\n"
        "/databasesekolah - Link Database Guru & Raport"
    )
    await update.message.reply_text(pesan_help, parse_mode="Markdown")


# === Setup Bot ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("portalguru", portalguru))
app.add_handler(CommandHandler("passwordwifi", passwordwifi))
app.add_handler(CommandHandler("inventaris", inventaris))
app.add_handler(CommandHandler("databasesekolah", databasesekolah))
app.add_handler(CommandHandler("help", help_command))

# === Flask Server (Health Check untuk Koyeb) ===
flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "Bot Telegram SMPIT Pondok Duta aktif!", 200


def run():
    # Gunakan default port 8000 sesuai setting forwarding di Koyeb
    port = int(os.environ.get("PORT", 8000))
    flask_app.run(host="0.0.0.0", port=port)


# Jalankan Flask di background thread
Thread(target=run, daemon=True).start()

# === Jalankan Polling Telegram ===
if __name__ == "__main__":
    print("Bot sedang berjalan...")
    app.run_polling()
