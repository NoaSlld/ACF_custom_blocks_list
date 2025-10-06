import inquirer from "inquirer";
import chalk from "chalk";



export async function askBlocPath(defaultPath = "./dossier_blocs/type1/blocExemple") {
  const { blocPath } = await inquirer.prompt([
    {
      type: "input",
      name: "blocPath",
      message: chalk.yellow("Chemin du bloc à exporter :"),
      default: defaultPath,
      transformer: input => chalk.white(input)
    }
  ]);
  return blocPath;
}


export async function askTargetDir(defaultDir = "../mon-projet") {
  const { targetDir } = await inquirer.prompt([
    {
      type: "input",
      name: "targetDir",
      message: chalk.yellow("Chemin du projet WordPress :"),
      default: defaultDir,
      transformer: input => chalk.white(input)
    }
  ]);
  return targetDir;
}


export async function askThemeName(defaultName = "mon-theme") {
  const { themeName } = await inquirer.prompt([
    {
      type: "input",
      name: "themeName",
      message: chalk.yellow("Nom du thème WordPress (ex: mon-theme) :"),
      default: defaultName,
      transformer: input => chalk.white(input)
    }
  ]);
  return themeName;
}


export async function askGlobalJsonName() {
  const { globalJsonName } = await inquirer.prompt([
    {
      type: "input",
      name: "globalJsonName",
      message: chalk.yellow("Nom du fichier JSON contenant les informations des blocs ACF (ex: group_67b5e6f413fa6.json):"),
      transformer: input => chalk.white(input)
    }
  ]);
  return globalJsonName;
}
