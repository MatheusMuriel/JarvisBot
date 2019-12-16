OPCAO_SELECIONADA = "opcao_selecionada"
STATUS_SERVIDOR = "status_servidor"
TRABS_ENTREGAR = "trabs_entregar"
PREV_TEMPO = "prev_temp"
ESTOQ_RACAO = "estoq_racao"

callbacks = [
  OPCAO_SELECIONADA,
  STATUS_SERVIDOR,
  TRABS_ENTREGAR,
  PREV_TEMPO,
  ESTOQ_RACAO,
]

valor_callback = {
  STATUS_SERVIDOR: "status_servidor",
  TRABS_ENTREGAR: "trabs_entregar",
  PREV_TEMPO: "prev_temp",
  ESTOQ_RACAO: "estoq_racao"
}

nomes_bonitos = {
  STATUS_SERVIDOR: "Status do servidor",
  TRABS_ENTREGAR: "Trabalhos para entregar",
  PREV_TEMPO: "Previsão do tempo",
  ESTOQ_RACAO: "Estoque de ração"
}

def get_callback_pelo_valor(_valor):
  for callback, valor in valor_callback.items():
    if valor == _valor:
      return callback