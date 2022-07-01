import consumo_api
from pandas import DataFrame as pd

dbname = consumo_api.ConsumoHistorialMultas.get_database()
collection_name = dbname["multas_2000_al_2022"]
item_details = collection_name.find({"vigencia" : "2006"})
items_df = pd(item_details)
print(items_df)

"""
Consumo con power bi

import pymongo
from pymongo import MongoClient
from pandas import DataFrame as pd

CONNECTION_STRING = "mongodb://localhost:27017"
client = MongoClient(CONNECTION_STRING)
dbname = client['historial_multas']
collection_name = dbname["multas_2000_al_2022"]
item_details = collection_name.find({"vigencia" : "2006"})
items_df = pd(item_details)

"""