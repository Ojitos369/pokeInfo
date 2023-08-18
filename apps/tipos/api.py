import os
import json
from app.core.bases.apis import get_d, pln, PostApi, GetApi, media_dir


class GetTipos(GetApi):
    def main(self):
        pln("GetTipos")

        filename = "tipos.json"
        filepath = "json/tipos.json"

        file = os.path.join(media_dir, filepath)
        
        tipos = []
        with open(file, "r") as f:
            tipos = json.loads(f.read())
            tipos = tipos["tipos"]
        
        self.response = {
            "tipos": tipos,
        }

