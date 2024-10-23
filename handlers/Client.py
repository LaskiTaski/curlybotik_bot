import asyncio

from bot_telegram import bot, TARGET_CHAT_ID
from aiogram import Dispatcher, types

from asyncio import sleep

from utils.state import FSMClient, State, StatesGroup
from keyboards.kb_client import keyboard_menu

messages_dict = {}


# @dp.message_handler(commands=['start'], state= ['*', FSMClient.Start])
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Написать сообщение"])

    await FSMClient.Start.set()

    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет, теперь ты можешь прислать мне своё сообщение, '
                                'для того, чтобы перенаправить его в чат учителей,'
                                'просто напиши своё сообщение ниже.',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='SendMessage', state=FSMClient.Start)
async def cb_Start(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Написать сообщение"])
    await callback.message.edit_text('Привет, теперь ты можешь прислать мне своё сообщение, '
                                     'для того, чтобы перенаправить его в чат учителей, '
                                     'просто напиши своё сообщение ниже.',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='WriteMessage', state=FSMClient.Start)
async def cb_WaitMessage(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Отправить сообщение"])

    await FSMClient.Wait.set()

    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text='Теперь ты можешь прислать мне своё сообщение ниже! '
                                         'Не забудь представиться 🙌',
                                    show_alert=True)

    await callback.message.edit_text('Нажмите на кнопку отправки когда будете готовы',
                                     reply_markup=kb)


# @dp.message_handler(content_types=['any'], state=FSMClient.Wait)
async def cmd_SaveMessage(message: types.Message):
    if message.content_type == 'text':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('text', None):
            messages_dict[message.from_user.id]['text'].append([message.text, message.message_id])

        elif message.from_user.id in messages_dict and 'text' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['text'] = [[message.text, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['text'] = [[message.text, message.message_id]]

    elif message.content_type == 'photo':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('photo', None):
            messages_dict[message.from_user.id]['photo'].append([message.photo[-1].file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'photo' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['photo'] = [[message.photo[-1].file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['photo'] = [[message.photo[-1].file_id, message.message_id]]

    elif message.content_type == 'video':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('video', None):
            messages_dict[message.from_user.id]['video'].append([message.video.file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'video' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['video'] = [[message.video.file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['video'] = [[message.video.file_id, message.message_id]]

    elif message.content_type == 'voice':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('voice', None):
            messages_dict[message.from_user.id]['voice'].append([message.voice.file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'voice' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['voice'] = [[message.voice.file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['voice'] = [[message.voice.file_id, message.message_id]]

    elif message.content_type == 'document':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('document', None):
            messages_dict[message.from_user.id]['document'].append([message.document.file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'document' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['document'] = [[message.document.file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['document'] = [[message.document.file_id, message.message_id]]

    elif message.content_type == 'audio':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('document', None):
            messages_dict[message.from_user.id]['audio'].append([message.audio.file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'audio' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['audio'] = [[message.audio.file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['audio'] = [[message.audio.file_id, message.message_id]]

    elif message.content_type == 'sticker':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('sticker', None):
            messages_dict[message.from_user.id]['sticker'].append([message.sticker.file_id, message.message_id])

        elif message.from_user.id in messages_dict and 'sticker' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['sticker'] = [[message.sticker.file_id, message.message_id]]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['sticker'] = [[message.sticker.file_id, message.message_id]]

    elif message.content_type == 'location':
        if message.from_user.id in messages_dict and messages_dict[message.from_user.id].get('sticker', None):
            messages_dict[message.from_user.id]['location'].append([[message.location.latitude,
                                                                     message.location.longitude], message.message_id])

        elif message.from_user.id in messages_dict and 'location' not in messages_dict[message.from_user.id]:
            messages_dict[message.from_user.id]['location'] = [[message.location.latitude, message.location.longitude],
                                                               message.message_id]

        elif message.from_user.id not in messages_dict:
            messages_dict[message.from_user.id] = {'': ''}
            messages_dict[message.from_user.id]['location'] = [[message.location.latitude, message.location.longitude],
                                                               message.message_id]


# @dp.callback_query_handlers(text='SendMessage', state=FSMClient.SendMessage)
async def cb_SendMessage(callback: types.CallbackQuery):
    if callback.from_user.id in messages_dict:
        user_messages = messages_dict[callback.from_user.id]

        if 'text' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('text', None)):
            full_message = ''
            for message, message_id in user_messages['text']:
                full_message += f'{message} \n'
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=message_id)
            await bot.send_message(chat_id=TARGET_CHAT_ID, text=full_message)

        if 'photo' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('photo', None)):
            for photo, photo_id in user_messages['photo']:
                await bot.send_photo(chat_id=TARGET_CHAT_ID, photo=photo)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=photo_id)

        if 'video' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('video', None)):
            for video, video_id in user_messages['video']:
                await bot.send_video(chat_id=TARGET_CHAT_ID, video=video)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=video_id)

        if 'voice' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('voice', None)):
            for voice, voice_id in user_messages['voice']:
                await bot.send_voice(chat_id=TARGET_CHAT_ID, voice=voice)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=voice_id)

        if 'document' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('document', None)):
            for document, document_id in user_messages['document']:
                await bot.send_document(chat_id=TARGET_CHAT_ID, document=document)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=document_id)

        if 'audio' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('audio', None)):
            for audio, audio_id in user_messages['audio']:
                await bot.send_audio(chat_id=TARGET_CHAT_ID, audio=audio)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=audio_id)

        if 'sticker' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('sticker', None)):
            for sticker, sticker_id in user_messages['sticker']:
                await bot.send_sticker(chat_id=TARGET_CHAT_ID, sticker=sticker)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=sticker_id)

        if 'location' in messages_dict[callback.from_user.id] and 0 < len(user_messages.get('location', None)):
            for latitude, longitude, location_id in user_messages['location']:
                await bot.send_location(chat_id=TARGET_CHAT_ID, latitude=latitude,
                                        longitude=longitude)
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=location_id)

        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Все сообщения отправлены',
                                        show_alert=True)
        messages_dict[callback.from_user.id] = {'': ''}
        await FSMClient.Start.set()
        await cb_Start(callback)

    else:

        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению сообщения для отправки отсутствуют',
                                        show_alert=True)


# @dp.message_handler(content_types=['any'], state='*')
async def cmd_DeleteMessage(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    ALARMMessage = await bot.send_message(chat_id=message.from_user.id,
                                          text='Для того, чтобы написать сообщение нажмите на кнопку!!!')

    await asyncio.sleep(3)
    await bot.delete_message(chat_id=message.chat.id, message_id=ALARMMessage.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=["start"], state=["*"])

    dp.register_callback_query_handler(cb_WaitMessage, text="WriteMessage", state=FSMClient.Start)
    dp.register_message_handler(cmd_DeleteMessage, content_types=["any"], state=FSMClient.Start)

    dp.register_callback_query_handler(cb_SendMessage, text="SendMessage", state=FSMClient.Wait)
    dp.register_callback_query_handler(cmd_Start, text="SendMessage", state=FSMClient.Start)

    dp.register_message_handler(cmd_SaveMessage, content_types=["any"], state=FSMClient.Wait)
