#!/bin/bash

set -e

echo "Vérification de l'environnement..."

# --- Aller à la racine du projet ---
cd "$(dirname "$0")/.." || exit 1

# --- Vérification de Python 3.10 ---
if command -v python3.10 &>/dev/null; then
    PYTHON=python3.10
elif command -v python3 &>/dev/null && python3 --version | grep -q "3.10"; then
    PYTHON=python3
else
    echo "❌ Python 3.10 n'est pas installé."
    echo "👉  Pour l’installer sur macOS, exécutez :"
    echo "    brew install python@3.10"
    echo ""
    echo "Une fois installé, relancez ce script."
    exit 1
fi

echo "✅ Python 3.10 trouvé : $($PYTHON --version)"


# --- Création du venv ---
VENV_DIR="venv"
if [ -d "$VENV_DIR" ]; then
    echo "⚠️  Le dossier $VENV_DIR existe déjà. Il sera supprimé et recréé."
    rm -rf "$VENV_DIR"
fi

$PYTHON -m venv "$VENV_DIR"
echo "✅ Virtualenv créé dans $VENV_DIR"


# --- Activation et mise à jour de pip ---
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
echo "✅ pip mis à jour"


# --- Installation des dépendances ---
if [ ! -f requirements.txt ]; then
    echo "❌ Fichier requirements.txt introuvable."
    echo "Assurez-vous qu'il est présent à la racine du projet."
    deactivate
    exit 1
fi

pip install -r requirements.txt
echo "✅ Dépendances installées"


# --- Vérification de Tkinter ---
$PYTHON - <<'END'
try:
    import tkinter
    print(f"✅ Tkinter est disponible : version {tkinter.TkVersion}")
except ImportError:
    print("❌ Tkinter n'est pas disponible.")
    print("👉  Pour l’installer sur macOS, exécutez :")
    print("    brew install python-tk@3.10")
    print("👉  Puis rafraichissez votre terminal avec :")
    print("    'exec zsh -l' ou 'exec bash -l' selon votre shell")
    print("")
    print("Une fois installé, relancez le script setup.sh.")
    exit(1)
END

echo ""
echo "✅ Environnement virtuel prêt !"
echo "👉 Pour l'utiliser (MacOS / Linux), tapez :"
echo "    source $VENV_DIR/bin/activate"