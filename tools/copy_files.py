import shutil
from pathlib import Path
import sys

class FileCopier:

    def check_and_copy(self, src: Path, dest: Path, label: str):
        if not src.exists():
            print(f"❌ Dossier source absent pour {label} → {src}")
            sys.exit(1)

        if not dest.exists():
            print(f"❌ Dossier de destination absent pour {label} → {dest}")
            sys.exit(1)

        for item in src.iterdir():
            dest_item = dest / item.name
            if item.is_dir():
                shutil.copytree(item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest_item)
                
        print(f"✅ {label} copié : {src} → {dest}")


    def copy_bloc_files(self, mappings):
        for m in mappings:
            self.check_and_copy(Path(m["src"]), Path(m["dest"]), m["label"])
