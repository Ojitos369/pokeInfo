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
        
        print("Agregando tipos...")
        for t in tipos:
            if not conexion.ejecutar(query, (t,)):
                conexion.rollback()
                raise Exception("Error al guardar tipos")
            conexion.commit()
        
        json_data_path = 'media/json/tipos.json'
        
        data = {}
        
        with open(json_data_path, 'r') as f:
            data = json.load(f)
        
        query = "SELECT * FROM tipos WHERE nombre = '{}'"
        for k, v in data.items():
            print(f"Datos de {k}...")
            rs = conexion.consulta_asociativa(query.format(k))
            tipo = rs[0]

            # dad - da_doble - da_a
            print(f"Da Doble de {k}...")
            dad = v["dad"]
            for d in dad:
                rs = conexion.consulta_asociativa(query.format(d))
                tipo_d = rs[0]
                            
                qr = f"""INSERT INTO da_doble
                        (tipo, da_a) VALUES
                        ('{tipo["id"]}', '{tipo_d["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar da_doble")
                conexion.commit()

            # recibed - recibe_doble - recibe_de
            print(f"Recibe Doble de {k}...")
            recibed = v["recibed"]
            for r in recibed:
                rs = conexion.consulta_asociativa(query.format(r))
                tipo_r = rs[0]
                            
                qr = f"""INSERT INTO recibe_doble
                        (tipo, recibe_de) VALUES
                        ('{tipo["id"]}', '{tipo_r["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar recibe_doble")
                conexion.commit()

            # dam - da_mitad - da_a
            print(f"Da Mitad de {k}...")
            dam = v["dam"]
            for d in dam:
                rs = conexion.consulta_asociativa(query.format(d))
                tipo_d = rs[0]
                            
                qr = f"""INSERT INTO da_mitad
                        (tipo, da_a) VALUES
                        ('{tipo["id"]}', '{tipo_d["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar da_mitad")
                conexion.commit()

            # recibem - recibe_mitad - recibe_de
            print(f"Recibe Mitad de {k}...")
            recibem = v["recibem"]
            for r in recibem:
                rs = conexion.consulta_asociativa(query.format(r))
                tipo_r = rs[0]
                            
                qr = f"""INSERT INTO recibe_mitad
                        (tipo, recibe_de) VALUES
                        ('{tipo["id"]}', '{tipo_r["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar recibe_mitad")
                conexion.commit()

            # da0 - da_nada - da_a
            print(f"Da Nada de {k}...")
            da0 = v["da0"]
            for d in da0:
                rs = conexion.consulta_asociativa(query.format(d))
                tipo_d = rs[0]
                            
                qr = f"""INSERT INTO da_nada
                        (tipo, da_a) VALUES
                        ('{tipo["id"]}', '{tipo_d["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar da_nada")
                conexion.commit()

            # recibe0 - recibe_nada - recibe_de
            print(f"Recibe Nada de {k}...")
            recibe0 = v["recibe0"]
            for r in recibe0:
                rs = conexion.consulta_asociativa(query.format(r))
                tipo_r = rs[0]
                            
                qr = f"""INSERT INTO recibe_nada
                        (tipo, recibe_de) VALUES
                        ('{tipo["id"]}', '{tipo_r["id"]}')
                        """
                if not conexion.ejecutar(qr):
                    conexion.rollback()
                    raise Exception("Error al guardar recibe_nada")
                conexion.commit()

            print("Agregado correctamente")


