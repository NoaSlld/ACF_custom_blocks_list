from pathlib import Path
from .command_line import CommandLineInterface
from .copy_files import FileCopier
from .json_utils import JsonManager
import sys


class UploadMain:

    def __init__(self):
        self.cli = CommandLineInterface()
        self.file_copier = FileCopier()
        self.json_manager = JsonManager()

    def run(self):
        print("\n Script d’export de bloc ACF\n")

        # --- sélection du bloc ---
        bloc_path = Path(self.cli.ask_bloc_path())
        bloc_name = bloc_path.name

        if not bloc_path.exists():
            print(f"❌ Dossier source du bloc introuvable → {bloc_path}")
            sys.exit(1)

        # --- sélection du thème WordPress ---
        theme_name = self.cli.ask_theme_name()
        theme_path = Path(theme_name)
        if not theme_path.exists():
            print(f"❌ Dossier du thème introuvable → {theme_path}")
            sys.exit(1)

        # --- sélection du fichier global JSON ---
        global_json_name = self.cli.ask_global_json_name()
        bloc_json_path = bloc_path / "acf" / f"{bloc_name}.json"
        global_json_path = theme_path / "acf" / global_json_name

        if not bloc_json_path.exists():
            print(f"❌ Fichier JSON du bloc introuvable → {bloc_json_path}")
            sys.exit(1)
        if not global_json_path.exists():
            print(f"❌ Fichier JSON global introuvable → {global_json_path}")
            sys.exit(1)

        bloc_json = self.json_manager.read_json(bloc_json_path)
        global_json = self.json_manager.read_json(global_json_path)

        print(f"\n🚀 Export du bloc \"{bloc_name}\" vers le thème \"{theme_path.name}\"\n")

        try:
            # --- copie des fichiers ---
            # dans UploadMain.run()
            mappings = [
                {"label": "JavaScript", "src": bloc_path / "js", "dest": Path(self.file_copier.custom_paths.get("js"))},
                {"label": "SCSS", "src": bloc_path / "scss", "dest": Path(self.file_copier.custom_paths.get("scss"))},
                {"label": "PHP/HTML", "src": bloc_path / "php", "dest": Path(self.file_copier.custom_paths.get("php"))},
            ]

            self.file_copier.copy_bloc_files(mappings)

            # --- ajout du bloc dans le JSON global ---
            self.json_manager.add_bloc_to_global_json(global_json, bloc_json)
            self.json_manager.write_json(global_json_path, global_json)

            print(f"\n✅ Bloc \"{bloc_name}\" ajouté avec succès dans le thème {theme_path}")
        
        except Exception as e:
            print(f"❌ Erreur pendant l’export : {e}")
            sys.exit(1)
