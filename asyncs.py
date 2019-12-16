import time
import datetime
import requests
import json

""" Metodo que chama agenda funções com tempo determinado """
#@run_async
def cronos():

  while True:
    agr = datetime.now()

  pass

# https://pt.db-city.com/Brasil--Paran%C3%A1--Londrina
# https://imasters.com.br/back-end/criando-um-weather-snapshot-em-python
def verifica_previsao_tempo():
  wth_key = "8728bd7a8d1f574fb07b5e8e96587972"
  wth_loc = "{},{}".format("-23.2927", "-51.1732")

  timestamp = time.strftime("Date: %Y-%m-%d %H:%M", time.localtime())
  msg = []
  msg.append("Stockholm")
  msg.append(timestamp)

  url = "https://api.forecast.io/forecast/{}/{}?lang={}&units={}".format(wth_key, wth_loc, "pt", "auto")
  req = requests.get(url)
  jdata = json.loads(req.text)

  summary = jdata["currently"]["summary"]
  temp = jdata["currently"]["temperature"]
  #temp = Far2Celsius(temp)

  msg.append(u"Temperature: %s°C" % temp)
  msg.append("Summary: %s" %summary)

  return msg