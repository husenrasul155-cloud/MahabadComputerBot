import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")


# =========================
# Render Health Server
# =========================

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Mahabad Computer Bot is Online!")

    def log_message(self, format, *args):
        pass


def start_server():
    port = int(os.getenv("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


# =========================
# Main Menu
# =========================

def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📱 خزمەتگوزاری مۆبایل",
                callback_data="mobile"
            )
        ],
        [
            InlineKeyboardButton(
                "💻 کۆمپیوتەر و لەپتۆپ",
                callback_data="computer"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 سۆفتوێر و Activation",
                callback_data="software"
            )
        ],
        [
            InlineKeyboardButton(
                "👻 Snapchat / SS06",
                callback_data="snapchat"
            )
        ],
        [
            InlineKeyboardButton(
                "🍎 iPhone / iCloud",
                callback_data="iphone"
            )
        ],
        [
            InlineKeyboardButton(
                "🔧 Repair / چاککردنەوە",
                callback_data="repair"
            )
        ],
        [
            InlineKeyboardButton(
                "🛒 فرۆشتن",
                callback_data="sales"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 پەیوەندی",
                callback_data="contact"
            ),
            InlineKeyboardButton(
                "📍 شوێن",
                callback_data="location"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# Start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "👋 بەخێربێیت بۆ\n"
        "🖥️ *Mahabad Computer*\n\n"
        "📱 Mobile & Computer Services\n\n"
        "لە Mahabad Computer ئەم خزمەتگوزارییانە پێشکەش دەکرێن:\n\n"
        "📱 مۆبایل\n"
        "💻 کۆمپیوتەر و لەپتۆپ\n"
        "🔐 سۆفتوێر و Activation\n"
        "👻 Snapchat / SS06\n"
        "🍎 iPhone / iCloud\n"
        "🔧 Repair\n"
        "🛒 فرۆشتن\n\n"
        "👇 تکایە بەشێک هەڵبژێرە:"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )


# =========================
# Mobile
# =========================

async def mobile_menu(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "🔧 چاککردنەوەی مۆبایل",
                callback_data="mobile_repair"
            )
        ],
        [
            InlineKeyboardButton(
                "🔄 Flash / Software",
                callback_data="mobile_flash"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 FRP / Google Account",
                callback_data="frp"
            )
        ],
        [
            InlineKeyboardButton(
                "🔓 Bootloader",
                callback_data="bootloader"
            )
        ],
        [
            InlineKeyboardButton(
                "📲 Android Problems",
                callback_data="android"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 گەڕانەوە",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        "📱 *خزمەتگوزاری مۆبایل*\n\n"
        "تکایە خزمەتگوزارییەکەت هەڵبژێرە:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# =========================
# Computer
# =========================

async def computer_menu(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "🪟 Windows",
                callback_data="windows"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 Microsoft Office",
                callback_data="office"
            )
        ],
        [
            InlineKeyboardButton(
                "💻 Laptop Repair",
                callback_data="laptop"
            )
        ],
        [
            InlineKeyboardButton(
                "🦠 Virus / Malware",
                callback_data="virus"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Wi-Fi / Network",
                callback_data="network"
            )
        ],
        [
            InlineKeyboardButton(
                "💾 HDD / SSD / RAM",
                callback_data="hardware"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 گەڕانەوە",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        "💻 *کۆمپیوتەر و لەپتۆپ*\n\n"
        "خزمەتگوزارییەکان:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# =========================
# Software
# =========================

async def software_menu(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "🪟 Windows Activation",
                callback_data="windows_activation"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 Office Activation",
                callback_data="office_activation"
            )
        ],
        [
            InlineKeyboardButton(
                "🔑 Online Activation",
                callback_data="online_activation"
            )
        ],
        [
            InlineKeyboardButton(
                "🛠️ چارەسەری Activation",
                callback_data="activation_fix"
            )
        ],
        [
            InlineKeyboardButton(
                "💿 دامەزراندنی بەرنامە",
                callback_data="software_install"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 گەڕانەوە",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        "🔐 *سۆفتوێر و Activation*\n\n"
        "• Windows Activation\n"
        "• Microsoft Office Activation\n"
        "• Online Activation\n"
        "• چارەسەرکردنی کێشەی Activation\n"
        "• دامەزراندنی بەرنامە\n\n"
        "⚠️ Activation ـی بەرنامەکان بە شێوەی یاسایی و بە لایسەنس/هەژمارێکی ڕەسمی ئەنجام دەدرێت.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# =========================
# Snapchat
# =========================

async def snapchat_menu(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "👻 Snapchat SS06",
                callback_data="ss06"
            )
        ],
        [
            InlineKeyboardButton(
                "🚫 Snapchat Ban",
                callback_data="snap_ban"
            )
        ],
        [
            InlineKeyboardButton(
                "📩 Appeal / Support",
                callback_data="snap_support"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 گەڕانەوە",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        "👻 *Snapchat Services*\n\n"
        "خزمەتگوزارییەکان:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# =========================
# Callback Handler
# =========================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "home":

        await query.edit_message_text(
            "👋 *Mahabad Computer*\n\n"
            "تکایە خزمەتگوزارییەکەت هەڵبژێرە:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    elif data == "mobile":
        await mobile_menu(query)

    elif data == "computer":
        await computer_menu(query)

    elif data == "software":
        await software_menu(query)

    elif data == "snapchat":
        await snapchat_menu(query)

    elif data == "iphone":

        await query.edit_message_text(
            "🍎 *iPhone / iCloud*\n\n"
            "• iPhone Software\n"
            "• iOS Restore\n"
            "• iCloud Support\n"
            "• Apple ID Support\n"
            "• چارەسەرکردنی کێشەکانی iPhone\n\n"
            "🔙 بۆ گەڕانەوە کرتە لە دوگمەی خوارەوە بکە.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    elif data == "repair":

        await query.edit_message_text(
            "🔧 *Repair / چاککردنەوە*\n\n"
            "📱 مۆبایل\n"
            "💻 لەپتۆپ\n"
            "🖥️ کۆمپیوتەر\n"
            "🔌 کێشەی شارژ\n"
            "🔋 باتری\n"
            "🖥️ شاشە\n"
            "💾 هاردوێر\n"
            "🛠️ سۆفتوێر",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    elif data == "sales":

        await query.edit_message_text(
            "🛒 *فرۆشتن*\n\n"
            "📱 مۆبایل\n"
            "💻 لەپتۆپ\n"
            "🖥️ کۆمپیوتەر\n"
            "🎧 Accessories\n"
            "🔌 کەلوپەلی ئەلیکترۆنی\n"
            "💾 SSD / HDD / RAM\n\n"
            "بۆ نرخ و بەردەستبوون پەیوەندیمان پێوە بکە.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    elif data == "contact":

        await query.edit_message_text(
            "📞 *پەیوەندی بە Mahabad Computer*\n\n"
            "بۆ نرخ، کڕین و خزمەتگوزاری:\n"
            "📱 پەیوەندیمان پێوە بکە.\n\n"
            "🖥️ Mahabad Computer",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    elif data == "location":

        await query.edit_message_text(
            "📍 *شوێنی Mahabad Computer*\n\n"
            "شوێنی دوکان دەتوانین دواتر بە لینکێکی Google Maps زیاد بکەین.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    else:

        messages = {

            "mobile_repair":
                "🔧 چاککردنەوەی مۆبایل\n\n"
                "کێشەی هاردوێر و سۆفتوێری مۆبایل چارەسەر دەکرێت.",

            "mobile_flash":
                "🔄 Flash / Software\n\n"
                "دامەزراندن و نوێکردنەوەی سیستەمی مۆبایل.",

            "frp":
                "🔐 FRP / Google Account\n\n"
                "خزمەتگوزارییەکانی FRP بۆ ئامێرێک کە بە شێوەی یاسایی هی خۆتە.",

            "bootloader":
                "🔓 Bootloader\n\n"
                "ڕێنمایی و خزمەتگوزارییەکانی Unlock ـی Bootloader بەپێی پشتگیریی مۆدێلەکە.",

            "android":
                "📲 Android Problems\n\n"
                "چارەسەرکردنی کێشەکانی Android، Software و System.",

            "windows":
                "🪟 Windows\n\n"
                "دامەزراندن، Update، Driver و چارەسەرکردنی کێشەکانی Windows.",

            "office":
                "📊 Microsoft Office\n\n"
                "دامەزراندن و ڕێکخستنی Word، Excel، PowerPoint و Office.",

            "laptop":
                "💻 Laptop Repair\n\n"
                "چاککردنەوە و پشکنینی هاردوێر و سۆفتوێری لەپتۆپ.",

            "virus":
                "🦠 Virus / Malware\n\n"
                "پشکنین و پاککردنەوەی ڤایرۆس و Malware.",

            "network":
                "🌐 Wi-Fi / Network\n\n"
                "چارەسەرکردنی کێشەکانی Wi-Fi و Network.",

            "hardware":
                "💾 HDD / SSD / RAM\n\n"
                "پشکنین و گۆڕینی HDD، SSD و RAM.",

            "windows_activation":
                "🪟 Windows Activation\n\n"
                "چالاککردنی Windows بە شێوەی یاسایی بە Product Key یان لایسەنسی ڕەسمی.",

            "office_activation":
                "📊 Office Activation\n\n"
                "چالاککردنی Microsoft Office بە لایسەنسی ڕەسمی.",

            "online_activation":
                "🔑 Online Activation\n\n"
                "چالاککردنی بەرنامەکان بە شێوەی Online بە هەژمار یان لایسەنسی ڕەسمی.",

            "activation_fix":
                "🛠️ Activation Fix\n\n"
                "پشکنین و چارەسەرکردنی کێشەکانی Activation.",

            "software_install":
                "💿 Software Installation\n\n"
                "دامەزراندن و ڕێکخستنی بەرنامە پێویستەکان.",

            "ss06":
                "👻 Snapchat SS06\n\n"
                "SS06 پەیوەندی بە سنووردارکردن/باندی Snapchat ـەوە هەیە.\n\n"
                "دەتوانین ڕێنمایی Appeal و پەیوەندی بە Snapchat Support بدەین.\n"
                "هیچ بەڵێنێک بۆ bypass کردنی باند نادرێت.",

            "snap_ban":
                "🚫 Snapchat Ban\n\n"
                "پشکنینی هۆکاری Ban و ڕێنمایی بۆ Appeal و Support.",

            "snap_support":
                "📩 Snapchat Support\n\n"
                "ڕێنمایی بۆ ناردنی Appeal و Recovery بۆ Snapchat Support.",
        }

        text = messages.get(
            data,
            "❌ خزمەتگوزاری نەدۆزرایەوە."
        )

        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 گەڕانەوە",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )


# =========================
# Run Bot
# =========================

def main():

    server_thread = threading.Thread(
        target=start_server,
        daemon=True
    )

    server_thread.start()

    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Mahabad Computer Bot is running...")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
