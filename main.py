from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
import os

# === Load Token dari Environment (Secrets) ===
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


# === Command Bot ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya adalah bot Telegram SMPIT Pondok Duta 🤝") # Mengganti karakter emoji agar tidak menimbulkan masalah encoding


async def penilaiankinerja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Perbaikan di sini: Menggunakan tiga tanda kutip ganda (""") untuk string multi-baris
    message = """📋 *PENILAIAN KINERJA DIKTENDIK*

1. Penilaian Antar rekan:
https://forms.gle/oWbXrJX3VncVWLDe9

2. Laporan Update Eflyer Sosmed:
https://forms.gle/5SeuC8XTp6SzWoBo9"""
    await update.message.reply_text(message, parse_mode="Markdown")


async def passwordwifi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Perbaikan di sini: Menggunakan tiga tanda kutip ganda (""") untuk string multi-baris
    message = """💡 *PASSWORD WIFI SEKOLAH*

*Lantai 1:*
Nama WiFi: Lantai1 Ruang1 / Lantai1 Ruang2
Password: `B4tuttaS1na`

*Lantai 2:*
Nama WiFi: Lantai2 Ruang1 / Lantai2 Ruang2 / LAB KOM
Password: `Kh0ldunN4fis`

*Lantai 3:*
Nama WiFi: Lantai3 Ruang1 / Lantai3 Ruang2 / LAB IPA
Password: `M4j4hRusdh`

*Kantor TU:*
`lagierror`

*SMPIT PONDOK DUTA:*
`l4girus4k`"""
    await update.message.reply_text(message, parse_mode="Markdown")


async def inventaris(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *INVENTARIS SEKOLAH*\n\nhttps://inventaris.smpitpondokduta.sch.id/", # Menggunakan \n untuk baris baru
        parse_mode="Markdown")


async def databasesekolah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗂️ *DATABASE SEKOLAH*\n\nhttps://drive.google.com/drive/folders/1BMQgUNBSbDlLw7TaEp-vdJNGW61y6nbI", # Menggunakan \n untuk baris baru
        parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Perbaikan di sini: Menggunakan tiga tanda kutip ganda (""") untuk string multi-baris
    pesan_help = """➡️ *Perintah yang tersedia adalah:*

/start - Ucapan Selamat Datang
/penilaiankinerja - Link Penilaian Diktendik
/passwordwifi - Password WiFi Sekolah
/inventaris - Link Inventaris Sekolah
/databasesekolah - Link Database Guru & Raport"""
    await update.message.reply_text(pesan_help, parse_mode="Markdown")


# === Setup Bot ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("penilaiankinerja", penilaiankinerja))
app.add_handler(CommandHandler("passwordwifi", passwordwifi))
app.add_handler(CommandHandler("inventaris", inventaris))
app.add_handler(CommandHandler("databasesekolah", databasesekolah))
app.add_handler(CommandHandler("help", help_command))

# === Flask (agar tetap hidup) ===
flask_app = Flask('')


@flask_app.route('/')
def home():
    return "Bot Telegram SMPIT Pondok Duta aktif!"


def run():
    # Pastikan port yang digunakan adalah $PORT dari environment Koyeb
    # atau port default yang diharapkan oleh Koyeb, misal 8080.
    # Namun, karena ini adalah Thread terpisah, pastikan aplikasi utama tidak terblokir.
    # Untuk Koyeb, seringkali disarankan untuk memiliki satu proses utama yang mendengarkan.
    # Jika Anda menggunakan bot polling, Flask app ini berfungsi sebagai "keep-alive" saja.
    port = int(os.environ.get("PORT", 8080)) # Ambil port dari variabel lingkungan PORT
    flask_app.run(host='0.0.0.0', port=port)


Thread(target=run).start()

# === Jalankan Bot ===
print("Bot sedang berjalan...")
# Untuk deployment ke Koyeb, jika Anda menggunakan polling, pastikan ini tidak menghalangi Flask app.
# Alternatif yang lebih umum untuk deployment adalah menggunakan webhook,
# namun untuk kasus Anda yang saat ini menggunakan polling dan Flask sebagai keep-alive,
# ini mungkin bisa berjalan.
app.run_polling()
