#!/usr/bin/env node

import path from "path";
import chalk from "chalk";
import { askBlocPath, askTargetDir, askThemeName, askGlobalJsonName } from "./command-line.js";
import { copyBlocFiles } from "./copyFiles.js";
import { readJson, writeJson, addBlocToGlobalJson } from "./jsonUtils.js";
import fs from "fs-extra";



export default async function main() {
    console.log(chalk.blue.bold("\n🚀 Script d’export de bloc ACF\n"));

    // collecte des infos
    const blocPath = await askBlocPath();
    const blocName = path.basename(blocPath);

    if (!await fs.pathExists(blocPath)) {
        console.error(chalk.red(`❌ Dossier source du bloc introuvable → ${blocPath}`));
        process.exit(1);
    }

    const targetDir = await askTargetDir();
    const themeName = await askThemeName();
    const themeBasePath = path.join(targetDir, "wp-content/themes", themeName);

    // vérification du JSON
    const globalJsonName = await askGlobalJsonName();
    const blocJsonPath = path.join(blocPath, "acf", `${blocName}.json`);
    const globalJsonPath = path.join(themeBasePath, "acf", globalJsonName);

    if (!await fs.pathExists(blocJsonPath)) {
        console.error(chalk.red(`❌ JSON du bloc introuvable → ${blocJsonPath}`));
        process.exit(1);
    }

    if (!await fs.pathExists(globalJsonPath)) {
        console.error(chalk.red(`❌ JSON global introuvable → ${globalJsonPath}`));
        process.exit(1);
    }

    const blocJson = await readJson(blocJsonPath);
    const globalJson = await readJson(globalJsonPath);

    console.log(chalk.cyan(`\n Export du bloc "${blocName}" vers le projet ${targetDir} dans le thème ${themeName}\n`));


    // insertion des fichiers
    try {
        // copier les fichiers
        const mappings = [
            { label: "JavaScript", src: path.join(blocPath, "js"), dest: path.join(themeBasePath, "resources/js/Components") },
            { label: "SCSS", src: path.join(blocPath, "scss"), dest: path.join(themeBasePath, "resources/scss/templates/content") },
            { label: "PHP/HTML", src: path.join(blocPath, "php"), dest: path.join(themeBasePath, "templates/template-parts/content") }
        ];
        await copyBlocFiles(mappings);

        // Mettre à jour le JSON du projet
        addBlocToGlobalJson(globalJson, blocJson);
        await writeJson(globalJsonPath, globalJson);

        console.log(chalk.green.bold(`\n ✅ Le bloc "${blocName}" a été ajouté dans ${themeBasePath}`));
    } catch (err) {
        console.error(chalk.red("❌ Erreur pendant l’export, annulation :", err));
        process.exit(1);
    }
}
