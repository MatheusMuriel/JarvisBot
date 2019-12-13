import os
from callbacks import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler

# Le as credenciais
c_dir = os.path.dirname(__file__)
with open(os.path.join(c_dir, "config/credenciais.txt")) as key_file:
  api_token, user_id = key_file.read().splitlines()

user_id = int(user_id)

def start(update, context):
  
  if update.message.from_user.id == user_id:
    # Valido
    update.message.reply_text('Olá mestre! :D')
    mostrar_opcoes(update)
  else:
    # Não é valido
    update.message.reply_text('Grrrr!\nVocê não é meu mestre')

def mostrar_opcoes(update):
  button_list = [
    [InlineKeyboardButton("Status servidor", callback_data=STATUS_SERVIDOR),
      InlineKeyboardButton("Trabalhos para entregar", callback_data=TRABS_ENTREGAR), ],
    [InlineKeyboardButton("Previsão do tempo", callback_data=PREV_TEMPO),
      InlineKeyboardButton("Estoque de ração", callback_data=ESTOQ_RACAO)],
  ]

  update.message.reply_text("Como posso te ajudar?", reply_markup=InlineKeyboardMarkup(button_list))

updater = Updater(api_token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

print('Iniciando Jarvis...')

updater.start_polling()
updater.idle()