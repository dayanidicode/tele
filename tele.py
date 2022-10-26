from telegram import *
from telegram.ext import *
import requests as r
bot = Bot("5584328065:AAHIM8QNc8cU_0ktfj8li9V6TfPXc6xeEt8")

#{'first_name': 'AFPLUAAS', 'username': 'AFPLUAASbot', 'supports_inline_queries': False, 'id': 5584328065, 'can_read_all_group_messages': False, 'can_join_groups': True, 'is_bot': True}

update = Updater("5584328065:AAHIM8QNc8cU_0ktfj8li9V6TfPXc6xeEt8",use_context=True)
dispatcher = update.dispatcher
def testfunction(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=r"https://www.ksrce.ac.in/"
    )


def test1(update:Update,context:CallbackContext):
    file = "file.jpg"
    path = {"photo":open(file,"rb")}
    resp = r.post(f"https://api.telegram.org/bot5584328065:AAHIM8QNc8cU_0ktfj8li9V6TfPXc6xeEt8/sendPhoto?chat_id=-895245832&caption=",files=path)


def test0(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=r"Wel Come"
    )

start=CommandHandler("start",test0)
dispatcher.add_handler(start)

startvalue=CommandHandler("link",testfunction)
dispatcher.add_handler(startvalue)

startvalue1=CommandHandler("photo",test1)
dispatcher.add_handler(startvalue1)


print("Connected")



update.start_polling()
