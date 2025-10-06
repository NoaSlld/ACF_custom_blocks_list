import fs from "fs-extra";
import chalk from "chalk";


export async function checkAndCopy(src, dest, label) {
  if (!await fs.pathExists(src)) {
    console.error(chalk.red(`❌ Dossier source absent pour ${label} → ${src}`));
    process.exit(1);
  }

  if (!await fs.pathExists(dest)) {
    console.error(chalk.red(`❌ Dossier de destination absent pour ${label} → ${dest}`));
    process.exit(1);
  }

  await fs.copy(src, dest, { overwrite: true });
  console.log(chalk.green(`${label} copié : ${src} → ${dest}`));
}


export async function copyBlocFiles(mappings) {
  for (const { src, dest, label } of mappings) {
    await checkAndCopy(src, dest, label);
  }
}
