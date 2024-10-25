from aiogram import types

write_message = types.InlineKeyboardButton('Написать сообщение✍️', callback_data='WriteMessage')
send_message = types.InlineKeyboardButton('Отправить сообщение 📩', callback_data='SendMessage')
test_button = types.InlineKeyboardButton('📩', callback_data='SendMessage')

keyboard_menu = {
    "Написать сообщение": [write_message],
    "Отправить сообщение": [send_message],
    "Ля финаль": [test_button]
}
