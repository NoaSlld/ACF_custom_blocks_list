import shutil
from pathlib import Path
import sys

class FileCopier:
    def __init__(self):
        self.custom_paths = {}

    def check_and_copy(self, src: Path, dest: Path, label: str):
        """Copie le contenu du dossier src vers dest
        - recrée les sous-dossiers si présents
        - copie les fichiers
        """
        if not src.exists():
            print(f"⚠️  Aucun dossier source trouvé pour {label} → {src} (ignoré)")
            return 

        if not dest.exists():
            print(f"⚠️  Le dossier de destination pour {label} n'existe pas → création : {dest}")
            dest.mkdir(parents=True, exist_ok=True)

        has_subdirs = any(item.is_dir() for item in src.iterdir())

        if has_subdirs:
            # recréer la hiérarchie complète
            for item in src.iterdir():
                dest_item = dest / item.name
                if item.is_dir():
                    shutil.copytree(item, dest_item, dirs_exist_ok=True)
                else:
                    shutil.copy2(item, dest_item)
        else:
            for item in src.iterdir():
                if item.is_file():
                    shutil.copy2(item, dest / item.name)

        print(f"✅ {label} copié : {src} → {dest}")


    def copy_bloc_files(self, mappings):
        for m in mappings:
            self.check_and_copy(Path(m["src"]), Path(m["dest"]), m["label"])
