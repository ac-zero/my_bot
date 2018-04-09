from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters

from telegram import ChatAction

def start(bot,update):
    update.message.reply_text("Hello!")
    print("Hello!")

def echo(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    repeat_text = update.message.text
    print(repeat_text)
    update.message.reply_text(repeat_text)

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