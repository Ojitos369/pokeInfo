import os
import json
from app.core.bases.apis import get_d, pln, PostApi, GetApi, media_dir
 

class ShowDanio(PostApi):
    def main(self):
        pln("ShowDanio")
        
        tipos = get_d(self.data, "tipos")
        if type(tipos) not in (list, tuple):
            raise self.MYE("tipos debe ser una lista")
        
        query = f"""SELECT * 
                    FROM tipos
                    WHERE nombre = %s
                    """
        # dad - da_doble - da_a
        # recibed - recibe_doble - recibe_de
        # dam - da_mitad - da_a
        # recibem - recibe_mitad - recibe_de
        # da0 - da_nada - da_a
        # recibe0 - recibe_nada - recibe_de

        query_dad = f"""SELECT (select nombre from tipos where id = d.da_a) nombre FROM da_doble d where tipo = %s """
        query_recibed = f"""SELECT (select nombre from tipos where id = d.recibe_de) nombre FROM recibe_doble d where tipo = %s """
        query_dam = f"""SELECT (select nombre from tipos where id = d.da_a) nombre FROM da_mitad d where tipo = %s """
        query_recibem = f"""SELECT (select nombre from tipos where id = d.recibe_de) nombre FROM recibe_mitad d where tipo = %s """
        query_da0 = f"""SELECT (select nombre from tipos where id = d.da_a) nombre FROM da_nada d where tipo = %s """
        query_recibe0 = f"""SELECT (select nombre from tipos where id = d.recibe_de) nombre FROM recibe_nada d where tipo = %s """
        
        data = {
            "dam": [],
            "recibed": [],
            "recibem": [],
            "dad": [],
            "da0": [],
            "recibe0": [],
        }

        for t in tipos:
            ts = self.conexion.consulta_asociativa(query, (t,))
            if not ts:
                raise self.MYE(f"No existe el tipo {t}")
            tipo = ts[0]

            dad = self.conexion.consulta_asociativa(query_dad, (tipo["id"],))
            data["dad"] += dad

            recibed = self.conexion.consulta_asociativa(query_recibed, (tipo["id"],))
            data["recibed"] += recibed

            dam = self.conexion.consulta_asociativa(query_dam, (tipo["id"],))
            data["dam"] += dam

            recibem = self.conexion.consulta_asociativa(query_recibem, (tipo["id"],))
            data["recibem"] += recibem

            da0 = self.conexion.consulta_asociativa(query_da0, (tipo["id"],))
            data["da0"] += da0

            recibe0 = self.conexion.consulta_asociativa(query_recibe0, (tipo["id"],))
            data["recibe0"] += recibe0
    
        danio = {}
        for f in recibed:
            if f["nombre"] not in danio:
                danio[f["nombre"]] = 0
            danio[f["nombre"]] += 2
        for f in recibem:
            if f["nombre"] not in danio:
                danio[f["nombre"]] = 0
            danio[f["nombre"]] -= 2
        for f in recibe0:
            if f["nombre"] not in danio:
                danio[f["nombre"]] = 1
            danio[f["nombre"]] *= 0
    
        danio_fin = {}
        for k, v in danio.items():
            v = int(v)
            if v != 0:
                if v < 0:
                    v = -1/v
                danio_fin[k] = v
        danio_fin = {k: v for k, v in sorted(danio_fin.items(), key=lambda item: item[1], reverse=True)}

        self.response = {
            "tipo": tipos,
            "danio": danio_fin,
        }
            
            
            

"""
"""

