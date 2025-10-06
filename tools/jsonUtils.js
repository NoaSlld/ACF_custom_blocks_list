import fs from "fs-extra";
import { v4 as uuidv4 } from "uuid";
import chalk from "chalk";



export async function readJson(filePath) {
  if (!await fs.pathExists(filePath)) {
    console.error(chalk.red(`❌ Fichier JSON introuvable → ${filePath}`));
    process.exit(1);
  }
  return fs.readJson(filePath);
}


export async function writeJson(filePath, data) {
  await fs.writeJson(filePath, data, { spaces: 2 });
}


export function addBlocToGlobalJson(globalJson, blocJson) {
  if (!globalJson.fields || !globalJson.fields[0] || !globalJson.fields[0].layouts) {
    console.error(chalk.red("❌ Structure JSON globale inattendue, impossible d'ajouter le bloc."));
    process.exit(1);
  }

  let layoutKey = blocJson.key || `layout_${uuidv4()}`;
  while (globalJson.fields[0].layouts[layoutKey]) {
    layoutKey = `layout_${uuidv4()}`; // unicité de l'id
  }

  blocJson.key = layoutKey;
  globalJson.fields[0].layouts[layoutKey] = { ...blocJson };
}

