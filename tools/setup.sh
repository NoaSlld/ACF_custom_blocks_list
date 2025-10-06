#!/usr/bin/env bash

echo "🚀 Préparation et vérification de l'environnement pour le script upload.js..."


# -- 1 Vérification Node.js --

REQUIRED_NODE_MAJOR=18
if command -v node >/dev/null 2>&1; then
  NODE_VERSION=$(node -v | sed 's/v\([0-9]*\).*/\1/')
  if [ "$NODE_VERSION" -lt "$REQUIRED_NODE_MAJOR" ]; then
    echo "❌ Node.js version $NODE_VERSION détectée. Version minimale requise : $REQUIRED_NODE_MAJOR"
    exit 1
  else
    echo "✅ Node.js version $NODE_VERSION"
  fi
else
  echo "❌ Node.js n'est pas installé. Installe-le avant de continuer."
  exit 1
fi


# -- 2 Vérification npm --

if command -v npm >/dev/null 2>&1; then
  echo "✅ npm version ($(npm -v))"
else
  echo "❌ npm n'est pas installé. Installe-le avant de continuer."
  exit 1
fi


# -- 3 Vérification package.json --

if [ ! -f package.json ]; then
  if [ -f ../package.json ]; then
    echo "⚠️  Aucun package.json trouvé ici, mais trouvé dans le dossier parent → on remonte"
    cd ..
  else
    echo "❌ Aucun package.json trouvé à la racine du projet."
    exit 1
  fi
fi

if ! grep -q '"type": "module"' package.json; then
  echo "❌ Le package.json n'est pas en mode module (\"type\": \"module\" absent)"
  exit 1
fi

if ! grep -q '"upload"' package.json; then
  echo "❌ Le script npm \"upload\" est manquant dans package.json"
  exit 1
fi

echo "✅ package.json vérifié"


# -- 4 Installation des dépendances --

echo "Installation des dépendances du package.json si nécessaire..."
npm install
npm install uuid

echo ""
echo "✅ Environnement prêt !"
echo "👉 Tu peux maintenant lancer : npm run upload"

