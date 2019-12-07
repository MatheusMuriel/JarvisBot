import os
from telegram.ext import Updater, CommandHandler

# Le as credenciais
c_dir = os.path.dirname(__file__)
with open(os.path.join(c_dir, "config/credenciais.txt")) as key_file:
  api_token, user_id = key_file.read().splitlines()

def start(update, context):
  if update.message.from_user.id == user_id:
    # Valido
    update.message.reply_text('Olá mestre :D \nComo posso te ajudar?')
  else:
    # Não é valido
    update.message.reply_text('Grrrr!\nVocê não é meu mestre')

updater = Updater(api_token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()