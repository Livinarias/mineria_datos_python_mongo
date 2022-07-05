import consumo_api
import pandas as pd


class ProcesamientoData:

    def _update_car_or_motorbike(ciudades):
        dbname = consumo_api.ConsumoHistorialMultas.get_database()
        collection_name = dbname["multas_2000_al_2022"]
        for rec in ciudades:
            data = collection_name.find({"ciudad": rec})
            for x in data:
                if x["placa"] and x["placa"][-1].isnumeric():
                    newdata = {"$set":{"tipo_vehiculo":"Carro"}}
                else:
                    newdata = {"$set":{"tipo_vehiculo":"Moto"}}
                collection_name.update_one(x, newdata)
                print("dato modificado ",x["_id"])

    def open_lat_long():
        df = pd.read_excel('../ciudades.xlsx')
        ciudades = df["ciudades"]
        return ciudades


test = ProcesamientoData.open_lat_long()
ProcesamientoData._update_car_or_motorbike(test)

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