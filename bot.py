import telebot
import os

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn_vpn = telebot.types.InlineKeyboardButton("🌐 VPN + 5 ប្រទេស", callback_data='vpn_menu')
    btn_proxy = telebot.types.InlineKeyboardButton("🚀 PROXY IPA 2", callback_data='proxy_menu')
    markup.add(btn_vpn, btn_proxy)
    
    bot.send_message(
        message.chat.id, 
        "🙏 សូមស្វាគមន៍មកកាន់ NamGaucho VPN\nសូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'vpn_menu':
        bot.answer_callback_query(call.id)
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        btn1 = telebot.types.InlineKeyboardButton("🔑 ៣ ថ្ងៃ - $1.00", callback_data='buy_3days')
        btn2 = telebot.types.InlineKeyboardButton("🔑 ៧ ថ្ងៃ - $2.00", callback_data='buy_7days')
        btn_back = telebot.types.InlineKeyboardButton("⬅️ ថយក្រោយ", callback_data='back_home')
        markup.add(btn1, btn2, btn_back)
        
        bot.edit_message_text(
            "NamGaucho VPN (VPN + 5 ប្រទេស) - សូមជ្រើសរើសរយៈពេល៖", 
            call.message.chat.id, 
            call.message.message_id, 
            reply_markup=markup
        )
    elif call.data == 'buy_3days':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "✅ លោកអ្នកបានជ្រើសរើសកញ្ចប់ ៣ ថ្ងៃ ($1.00)។ សូមទូទាត់ប្រាក់តាម ABA: 000 123 456 រួចផ្ញើ Slip មកទីនេះ។")
    elif call.data == 'back_home':
        bot.answer_callback_query(call.id)
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        btn_vpn = telebot.types.InlineKeyboardButton("🌐 VPN + 5 ប្រទេស", callback_data='vpn_menu')
        markup.add(btn_vpn)
        bot.edit_message_text(
            "🙏 សូមស្វាគមន៍មកកាន់ NamGaucho VPN\nសូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", 
            call.message.chat.id, 
            call.message.message_id, 
            reply_markup=markup
        )

bot.infinity_polling()
