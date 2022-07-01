import requests
import json
import pymongo
from pymongo import MongoClient


class ConsumoHistorialMultas:

  def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['historial_multas']
    
  def __consumo_api__(vigencia, limite):
    if len(vigencia) > 0:
      for item in vigencia:
        #try:
          url = 'https://www.datos.gov.co/resource/x8g3-nn2c.json?vigencia={vigencia}&%24limit={limit}'.format(vigencia = item, limit=limite)
          response = requests.get(url)
          if len(response.json()) > 0:
            print(response.json())
            collection_name = dbname["multas_2000_al_2022"]
            collection_name.insert_many(response.json())
          else:
            print("no existen multas en el año ",item)
    else:
      print("la variable vigencia esta vacía")

  





if __name__ == "__main__":    
    vigencia = list(range(2000,2023,1))
    dbname = ConsumoHistorialMultas.get_database()
    ConsumoHistorialMultas.__consumo_api__(vigencia, 1000000)