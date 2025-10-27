#!/bin/bash

set -e


# --- Vérification de Python 3.10 ---
if command -v python3.10 &>/dev/null; then
    PYTHON=python3.10
elif command -v python3 &>/dev/null && python3 --version | grep -q "3.10"; then
    PYTHON=python3
else
    echo "❌ Python 3.10 n'est pas installé. Veuillez l'installer d'abord."
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


# --- Activation et upgrade pip ---
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
echo "✅ pip mis à jour"


# --- Installation des dépendances ---
pip install -r requirements.txt
echo "✅ Dépendances installées"


# --- Vérification de Tkinter ---
$PYTHON - <<END
try:
    import tkinter
    print("✅ Tkinter est disponible : TkVersion", tkinter.TkVersion)
except ImportError:
    print("❌ Tkinter n'est pas disponible. Sur macOS, installer avec : brew install python-tk")
END

echo "Environnement virtuel prêt !"
echo "Pour l'utiliser (MacOS / Linux), tapez : source $VENV_DIR/bin/activate"
