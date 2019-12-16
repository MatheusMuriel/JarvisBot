import os
from callbacks import *
import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler

print('Iniciando Jarvis...')

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

  reply_markup = InlineKeyboardMarkup(button_list)

  update.message.reply_text("Como posso te ajudar?", reply_markup=reply_markup)

def button(update, context):
  query = update.callback_query

  query.edit_message_text(text="Selected option: {}".format(query.data))

def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  # Cria o Updater e passa para ele o token do bot
  # O "use_context" é marcado como verdadeiro para
  # usar o callback
  updater = Updater(api_token, use_context=True)

  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CallbackQueryHandler(button))
  updater.dispatcher.add_error_handler(error)

  # inicia o bot
  updater.start_polling()
  print('Jarvis iniciado!')

  # Executa o bot ate que ele receba um sinal de parada
  updater.idle()

if __name__ == '__main__':
  main()