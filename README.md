# Script d’export de blocs ACF vers un projet WordPress

Ce script Node.js permet de copier automatiquement les fichiers d’un **bloc ACF** (JSON, SCSS, JS, PHP) dans la structure d’un thème WordPress existant.  


## Structure attendue d’un bloc

Un bloc doit être organisé ainsi :

blocExemple/
├── acf/ # Fichier(s) JSON décrivant le bloc ACF
├── js/ # Fichiers JavaScript associés
├── scss/ # Fichiers SCSS associés
└── php/ # Template PHP/HTML du bloc


## Installation

Préparez votre environnement avec la commande:
```bash
./setup.sh
```

Ce script verifiera la présence de:
- Node.js
- npm
- du package.json correct 
- des dépendnaces fs-extra, chalk et inquirer  


Puis une fois que tout est bon, depuis le dossier du projet contenant le script :
```bash
npm install
```


## Utilisation

Lancez le script avec :
```bash
npm run upload
```

- Chemin du bloc à exporter → dossier source contenant acf/, js/, scss/, php/
- Chemin du projet WordPress → dossier racine du projet
- Nom du thème WordPress → ex : mon-theme


## Règles

Le script vérifie que :
- le dossier du bloc existe
- le dossier du projet existe
- les sous-dossiers de destination existent

En cas d’erreur → le script s’arrête immédiatement sans rien copier.