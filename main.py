# -*- coding: utf-8 -*-
import os
import logging
import datetime
import time

from callbacks import *
import skills
import asyncs

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
updater = None
user_id = None
api_token = None

print('Iniciando Jarvis...')

# Le as credenciais
def carrega_credenciais():
  dir_atual = os.path.dirname(__file__)
  caminho_credenciais = os.path.join(dir_atual, "config", "credenciais.txt")
  
  # Verifica se o arquivo existe
  if os.path.isfile(caminho_credenciais):
    with open(caminho_credenciais) as arquivo_ultra_secreto:
      credenciais = arquivo_ultra_secreto.read().splitlines()

    global api_token, user_id
    api_token = credenciais[0]
    user_id = int(credenciais[1])
  else:
    print("Arquivo config/credenciais.txt nao foi encontrado")
    exit()

def start(update, context):
  if update.message.from_user.id == user_id:
    update.message.reply_text('Olá mestre 5.0! :D')
  else:
    update.message.reply_text('Grrrr!\nVocê não é meu mestre')

def opcoes(update, context):
  button_list = [
    [InlineKeyboardButton(nomes_bonitos.get(STATUS_SERVIDOR), callback_data=valor_callback.get(STATUS_SERVIDOR)),
      InlineKeyboardButton(nomes_bonitos.get(TRABS_ENTREGAR), callback_data=valor_callback.get(TRABS_ENTREGAR))],
    [InlineKeyboardButton(nomes_bonitos.get(PREV_TEMPO), callback_data=valor_callback.get(PREV_TEMPO)),
      InlineKeyboardButton(nomes_bonitos.get(ESTOQ_RACAO), callback_data=valor_callback.get(ESTOQ_RACAO))],
  ]

  reply_markup = InlineKeyboardMarkup(button_list)

  update.message.reply_text("Como posso te ajudar?", reply_markup=reply_markup)

def processa_botao(update, context):
  query = update.callback_query

  opcao_escolhida = get_callback_pelo_valor(query.data)

  resposta = ''

  if opcao_escolhida == TRABS_ENTREGAR:
    resposta = skills.trabalhos_a_entregar()
  elif opcao_escolhida == PREV_TEMPO:
    resposta = asyncs.verifica_previsao_tempo()

  #query.edit_message_text(text="{}: \n{}".format(nomes_bonitos.get(opcao_escolhida), resposta))
  resposta_callback = "{}: \n{}".format(nomes_bonitos.get(opcao_escolhida), resposta)
  query.message.reply_text(resposta_callback)

  # Linha abaixo é para evitar o bug do relogio ficar aparecendo em cima do botão
  context.bot.answer_callback_query(query.id, text='')

def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def enviar_mensagem(mensagem):
  global updater
  updater.bot.send_message(user_id, mensagem)

def main():
  # Cria o Updater e passa para ele o token do bot
  # O "use_context" é marcado como verdadeiro para
  # usar o callback
  global updater

  updater = Updater(api_token, use_context=True)

  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CommandHandler('opcoes', opcoes))
  updater.dispatcher.add_handler(CallbackQueryHandler(processa_botao))
  updater.dispatcher.add_error_handler(error)

  # inicia o bot
  updater.start_polling()
  print('Jarvis iniciado!')

  asyncs.verifica_previsao_tempo()

  # Executa o bot ate que ele receba um sinal de parada
  updater.idle()

if __name__ == '__main__':
  carrega_credenciais()
  main()
