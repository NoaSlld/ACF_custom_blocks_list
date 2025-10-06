#!/usr/bin/env node
import chalk from "chalk";
import runUpload from "./upload-main.js";
//import runImport from "./import-main.js";



async function main() {

    const command = process.argv[2] || "upload";
    if (command === "upload") {
        await runUpload();
    //} else if (command === "import") {
        //await runImport();
    } else {
        console.log(chalk.red(`❌ Commande inconnue : ${command}`));
    }
}

main().catch(err => console.error(chalk.red("❌ Erreur globale:", err)));
