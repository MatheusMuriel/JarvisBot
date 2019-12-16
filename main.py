import os
import logging

from callbacks import *
#from skills import *
import skills

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

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
    #mostrar_opcoes(update)
  else:
    # Não é valido
    update.message.reply_text('Grrrr!\nVocê não é meu mestre')

def opcoes(update, context):
  button_list = [
    [InlineKeyboardButton(nomes_bonitos.get(STATUS_SERVIDOR), callback_data=valor_callback(STATUS_SERVIDOR)),
      InlineKeyboardButton(nomes_bonitos.get(TRABS_ENTREGAR), callback_data=valor_callback(TRABS_ENTREGAR))],
    [InlineKeyboardButton(nomes_bonitos.get(PREV_TEMPO), callback_data=valor_callback(PREV_TEMPO)),
      InlineKeyboardButton(nomes_bonitos.get(ESTOQ_RACAO), callback_data=valor_callback(ESTOQ_RACAO))],
  ]

  reply_markup = InlineKeyboardMarkup(button_list)

  update.message.reply_text("Como posso te ajudar?", reply_markup=reply_markup)

def processa_botao(update, context):
  query = update.callback_query

  opcao_escolhida = get_callback_pelo_valor(query.data)

  resposta = ''

  if opcao_escolhida == TRABS_ENTREGAR:
    resposta = skills.trabalhos_a_entregar()

  query.edit_message_text(text="{}: \n{}".format(nomes_bonitos.get(opcao_escolhida), resposta))

def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  # Cria o Updater e passa para ele o token do bot
  # O "use_context" é marcado como verdadeiro para
  # usar o callback
  updater = Updater(api_token, use_context=True)

  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CommandHandler('opcoes', opcoes))
  updater.dispatcher.add_handler(CallbackQueryHandler(processa_botao))
  updater.dispatcher.add_error_handler(error)

  # inicia o bot
  updater.start_polling()
  print('Jarvis iniciado!')

  # Executa o bot ate que ele receba um sinal de parada
  updater.idle()

if __name__ == '__main__':
  main()