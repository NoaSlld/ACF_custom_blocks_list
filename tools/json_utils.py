import json
import sys
import uuid
from pathlib import Path

class JsonManager:

    def read_json(self, file_path: Path):
        if not file_path.exists():
            print(f"❌ Fichier JSON introuvable → {file_path}")
            sys.exit(1)
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)


    def write_json(self, file_path: Path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


    def add_bloc_to_global_json(self, global_json, bloc_json):
        try:
            layouts = global_json["fields"][0]["layouts"]
        except (KeyError, IndexError):
            print("❌ Structure JSON globale inattendue, impossible d'ajouter le bloc.")
            sys.exit(1)

        layout_key = bloc_json.get("key") or f"layout_{uuid.uuid4()}"
        while layout_key in layouts:
            layout_key = f"layout_{uuid.uuid4()}"

        bloc_json["key"] = layout_key
        layouts[layout_key] = bloc_json
