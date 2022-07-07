import consumo_api
import pandas as pd


class EliminarData:

    def _eliminar_data():
        dbname = consumo_api.ConsumoHistorialMultas.get_database()
        collection_name = dbname["multas_2000_al_2022"]
        data = collection_name.delete_many({"tipo_vehiculo" : {"$exists" : False}})
        print(data.deleted_count,"Archivos borrados.")
        

EliminarData._eliminar_data()