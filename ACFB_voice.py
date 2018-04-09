from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters

from telegram import ChatAction
from gtts import gTTS


def start(bot,update):
    update.message.reply_text("Hello!")
    print("Hello!")

def echo(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.UPLOAD_AUDIO)
    repeat_text = update.message.text

    #convert the textual message into a mp3 file

    tts = gTTS(text=repeat_text, lang="en")
    tts.save("echo.mp3")

    #send the message back
    bot.sendVoice(update.message.chat_id, voice=open("echo.mp3","rb"))

def help():
    pass


def main():
    """
    My First Bot
    """
    updater=Updater("")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text,echo))
    dp.add_handler(CommandHandler("help", help))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()