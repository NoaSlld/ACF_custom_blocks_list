# Script d’export de blocs ACF vers un projet WordPress

Ce script Node.js permet d'exporter automatiquement les fichiers d’un **bloc ACF flexible** (JSON, SCSS, JS, PHP) dans la structure d’un thème WordPress existant.  


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
- Vérifie la présence de Node.js ≥ 18 et npm
- Vérifie le fichier package.json et le script upload
- Installe automatiquement les dépendances nécessaires (chalk, inquirer, fs-extra, uuid)


## Utilisation

Lancez le script avec :
```bash
npm run upload
```

- Chemin du bloc à exporter → dossier source contenant acf/, js/, scss/, php/
- Chemin du projet WordPress → dossier racine du projet
- Nom du thème WordPress → ex : mon-theme
- Le nom du fichier JSON global ACF → ex : group_67b5e6f413fa6.json