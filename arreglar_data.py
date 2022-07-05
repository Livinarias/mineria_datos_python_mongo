import consumo_api

class ModificarCiudad:

    def _buscar_data():
        dbname = consumo_api.ConsumoHistorialMultas.get_database()
        collection_name = dbname["multas_2000_al_2022"]
        data = collection_name.find({"ciudad": "Guarne(Dptal)"})
        return data

    def modificar_ciudad(data):
        dbname = consumo_api.ConsumoHistorialMultas.get_database()
        collection_name = dbname["multas_2000_al_2022"]
        new_data = {"$set":{"ciudad":"Guarne"}}
        for d in data:
            collection_name.update_many(d,new_data)
        print("Tarea culminada")


datos = ModificarCiudad._buscar_data()
ModificarCiudad.modificar_ciudad(datos)