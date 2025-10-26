import inquirer

class CommandLineInterface:

    def ask_bloc_path(self, default="./dossier_blocs/type1/blocExemple"):
        question = [inquirer.Text("bloc_path", message="Chemin du bloc à exporter :", default=default)]
        return inquirer.prompt(question)["bloc_path"]


    def ask_theme_name(self, default="mon-theme"):
        question = [inquirer.Text("theme_name", message="Nom du thème WordPress (ex: mon-theme) :", default=default)]
        return inquirer.prompt(question)["theme_name"]


    def ask_global_json_name(self):
        question = [inquirer.Text("global_json_name", message="Nom du fichier JSON global (ex: group_67b5e6f413fa6.json) :")]
        return inquirer.prompt(question)["global_json_name"]
