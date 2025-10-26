import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from tools.upload_main import UploadMain


class BlocExporterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ACF Block Exporter")
        self.geometry("700x600")

        # variables
        self.bloc_path = tk.StringVar()
        self.theme_name = tk.StringVar()
        self.global_json = tk.StringVar()
        self.js_dest = tk.StringVar()
        self.scss_dest = tk.StringVar()
        self.php_dest = tk.StringVar()

        entry_width = 40

        # --- bloc ACF ---
        ttk.Label(self, text="Dossier du bloc ACF à exporter", font=("Helvetica", 12, "bold")).pack(pady=5)
        bloc_frame = ttk.Frame(self)
        bloc_frame.pack(pady=5)
        ttk.Entry(bloc_frame, textvariable=self.bloc_path, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(bloc_frame, text="Sélectionner", command=self.select_bloc).pack(side='left')

        # --- thème cible ---
        ttk.Label(self, text="Thème cible du projet", font=("Helvetica", 12, "bold")).pack(pady=5)
        theme_frame = ttk.Frame(self)
        theme_frame.pack(pady=5)
        ttk.Entry(theme_frame, textvariable=self.theme_name, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(theme_frame, text="Sélectionner", command=self.select_theme).pack(side='left')

        # --- JSON ACF ---
        ttk.Label(self, text="Fichier JSON contenant les champs ACF", font=("Helvetica", 12, "bold")).pack(pady=5)
        json_frame = ttk.Frame(self)
        json_frame.pack(pady=5)
        ttk.Entry(json_frame, textvariable=self.global_json, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(json_frame, text="Sélectionner", command=self.select_global_json).pack(side='left')

        # --- dossiers de destination ---
        ttk.Label(self, text="Dossiers de destination :", font=("Helvetica", 12, "bold")).pack(pady=10)

        # JS
        js_frame = ttk.Frame(self)
        js_frame.pack(pady=3)
        ttk.Label(js_frame, text="JavaScript :").pack(side='left', padx=(0, 5))
        ttk.Entry(js_frame, textvariable=self.js_dest, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(js_frame, text="Sélectionner", command=self.select_js_dest).pack(side='left')

        # SCSS
        scss_frame = ttk.Frame(self)
        scss_frame.pack(pady=3)
        ttk.Label(scss_frame, text="SCSS :").pack(side='left', padx=(0, 5))
        ttk.Entry(scss_frame, textvariable=self.scss_dest, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(scss_frame, text="Sélectionner", command=self.select_scss_dest).pack(side='left')

        # PHP
        php_frame = ttk.Frame(self)
        php_frame.pack(pady=3)
        ttk.Label(php_frame, text="PHP / HTML :").pack(side='left', padx=(0, 5))
        ttk.Entry(php_frame, textvariable=self.php_dest, width=entry_width).pack(side='left', padx=(0, 5))
        ttk.Button(php_frame, text="Sélectionner", command=self.select_php_dest).pack(side='left')

        # --- bouton d’export ---
        ttk.Button(self, text="Exporter le bloc", command=self.export_bloc).pack(pady=25)


    # --- sélecteurs de dossier / fichier ---

    def select_bloc(self):
        path = filedialog.askdirectory(title="Sélectionner le dossier du bloc ACF", initialdir=os.getcwd())
        if path:
            self.bloc_path.set(path)

    def select_theme(self):
        path = filedialog.askdirectory(title="Sélectionner le thème")
        if path:
            self.theme_name.set(path)
            theme_path = Path(path)

            # pré-remplir les chemins par défaut
            js_default = theme_path / "resources/js/Components"
            scss_default = theme_path / "resources/scss/templates/content"
            php_default = theme_path / "templates/template-parts/content"

            self.js_dest.set(str(js_default))
            self.scss_dest.set(str(scss_default))
            self.php_dest.set(str(php_default))


    def select_global_json(self):
        theme_path = Path(self.theme_name.get())
        acf_path = theme_path / "acf"
        initial_dir = acf_path if acf_path.exists() else theme_path

        file_path = filedialog.askopenfilename(
            initialdir=initial_dir,
            title="Sélectionner le fichier JSON global ACF",
            filetypes=[("Fichiers JSON", "*.json")]
        )
        if file_path:
            self.global_json.set(file_path)


    def select_js_dest(self):
        theme_path = Path(self.theme_name.get())
        default_path = theme_path / "resources/js/Components"
        initial_dir = default_path if default_path.exists() else theme_path
        path = filedialog.askdirectory(title="Dossier de destination JS", initialdir=initial_dir)
        if path:
            self.js_dest.set(path)


    def select_scss_dest(self):
        theme_path = Path(self.theme_name.get())
        default_path = theme_path / "resources/scss/templates/content"
        initial_dir = default_path if default_path.exists() else theme_path
        path = filedialog.askdirectory(title="Dossier de destination SCSS", initialdir=initial_dir)
        if path:
            self.scss_dest.set(path)


    def select_php_dest(self):
        theme_path = Path(self.theme_name.get())
        default_path = theme_path / "templates/template-parts/content"
        initial_dir = default_path if default_path.exists() else theme_path
        path = filedialog.askdirectory(title="Dossier de destination PHP", initialdir=initial_dir)
        if path:
            self.php_dest.set(path)


    # --- lancement de l’export ---

    def export_bloc(self):
        if not all([self.bloc_path.get(), self.theme_name.get(), self.global_json.get()]):
            messagebox.showerror("Erreur", "Veuillez sélectionner au minimum le bloc, le thème et le JSON global.")
            return

        try:
            uploader = UploadMain()
            uploader.cli.ask_bloc_path = lambda default=None: self.bloc_path.get()
            uploader.cli.ask_theme_name = lambda default=None: self.theme_name.get()
            uploader.cli.ask_global_json_name = lambda: Path(self.global_json.get()).name

            # injection des chemins choisis
            uploader.file_copier.custom_paths = {
                "js": self.js_dest.get(),
                "scss": self.scss_dest.get(),
                "php": self.php_dest.get(),
            }

            uploader.run()
            messagebox.showinfo("Succès", "Le bloc a été exporté avec succès !")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur pendant l’export : {e}")


if __name__ == "__main__":
    app = BlocExporterGUI()
    app.mainloop()
