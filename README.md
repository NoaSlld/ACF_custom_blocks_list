# Script d’export de blocs ACF vers un projet WordPress

Ce script Python permet d'exporter automatiquement les fichiers d’un **bloc ACF flexible** (JSON, SCSS, JS, PHP) dans la structure d’un thème WordPress existant.  


## Structure attendue d’un bloc

Un bloc à exporter doit être organisé ainsi :

blocExemple/  
├── acf/ # Fichier(s) JSON décrivant le bloc ACF  
├── js/ # Fichiers JavaScript associés  
├── scss/ # Fichiers SCSS associés  
└── php/ # Template PHP/HTML du bloc  


## Installation

Préparez votre environnement à la racine du projet avec la commande:
```bash
./setup.sh
```

Ce script :
- Vérifie la présence de Python 3.10
- Crée un environnement virtuel (venv)
- Installe automatiquement les dépendances Python listées dans requirements.txt (tkinter, inquirer, etc.)


## Utilisation

Activez l'environnement virtuel avec:
```source venv/bin/activate```  # macOS / Linux
```venv\Scripts\activate```     # Windows

Lancez le script avec :
```bash
python3 -m tools.gui_upload
```

Désactiver l'environnement virtuel une fois fini avec
```bash
deactivate
```

- Chemin du bloc à exporter → dossier source contenant votre bloc à exporter (comportant: acf/, js/, scss/, php/)
- Thème WordPress → Theme dans lequel il faut exporter le bloc
- Fichier JSON cible contenant tous les champs du ACF du projet → ex : group_67b5e6f413fa6.json





- verif forme json source qui semble avoir une identation de trop

- verif si dans js/scss/php il y a un dossier -> il faut re-créer ces dossier dans le projet cible s'ils n'existent pas, sinon on ajout juste le fichier dedans
