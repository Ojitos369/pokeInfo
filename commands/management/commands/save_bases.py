import os
import json
from app.core.bases.commands import MyBaseCommand, pj, pln, TF, get_d
from app.core.mysql import ConexionMySQL
from app.settings import DBDATA, BASE_DIR

class Command(MyBaseCommand):
    def main(self, *args, **options):
        
        conexion = ConexionMySQL(DBDATA, raise_error=True)
        
        tipos = [
            "Normal",
            "Pelea",
            "Volador",
            "Veneno",
            "Tierra",
            "Roca",
            "Bicho",
            "Fantasma",
            "Acero",
            "Fuego",
            "Agua",
            "Planta",
            "Electrico",
            "Psiquico",
            "Hielo",
            "Dragon",
            "Siniestro",
            "Hada",
        ]
        query = f"""INSERT INTO tipos
                    (nombre) values (%s)
                    """
        # for t in tipos:
        #     if not conexion.ejecutar(query, (t,)):
        #         conexion.rollback()
        #         raise Exception("Error al guardar tipos")
        # conexion.commit()
        
        json_data_path = 'media/json/tipos.json'
        
        data = {}
        
        with open(json_data_path, 'r') as f:
            data = json.load(f)
        
        for k, v in data.items():
            query = f"SELECT * FROM tipos WHERE nombre = '{k}'"
            
            rs = conexion.consulta_asociativa(query)
            tipo = rs[0]
            print(tipo)
            
            
        
        
        