import tkinter as tk
from tkinter import ttk
import requests
import re
#Arquivo de interface do sistema de login
#Estilização e parte de front / estática do site
#Colunas e botões para manuseio do usuário para com o sistema
#Conexão e criação de requests com o banco de dados para autenticação
#Estrutura de View integrada com rotas (requests) e controle dos dados 
API_URL = "http://localhost:8000/login"
WINDOW_WIDTH = 420
WINDOW_HEIGHT = 300


def center_window(root, w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")


class LoginApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        self.parent = parent
        self.parent.title("Sistema de Login - Padrão de Projetos")
        self.parent.resizable(False, False)
        center_window(self.parent, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except:
            pass

        self.style.configure("Card.TFrame", background="#ffffff")
        self.style.configure("Logo.TLabel",
                             font=("Segoe UI Semibold", 18),
                             foreground="#1a73e8",
                             background="#ffffff")
        self.style.configure("Subtitle.TLabel",
                             font=("Segoe UI", 10),
                             foreground="#444444",
                             background="#ffffff")
        self.style.configure("FieldLabel.TLabel",
                             font=("Segoe UI", 9),
                             foreground="#333333",
                             background="#ffffff")
        self.style.configure("Msg.TLabel",
                             font=("Segoe UI", 9),
                             foreground="#d93025",
                             background="#ffffff")

        self.parent.configure(background="#f3f4f6")

        card = ttk.Frame(self, style="Card.TFrame", padding=20)
        card.grid(row=0, column=0)

        ttk.Label(card, text="Erick - CORP", style="Logo.TLabel").grid(row=0, column=0, pady=(0, 10))
        ttk.Label(card, text="Acesso ao sistema", style="Subtitle.TLabel").grid(row=1, column=0, pady=(0, 12))

        ttk.Label(card, text="CPF", style="FieldLabel.TLabel").grid(row=2, column=0, sticky="w")
        self.cpf_var = tk.StringVar()
        self.cpf_entry = ttk.Entry(card, textvariable=self.cpf_var, font=("Segoe UI", 11), width=30)
        self.cpf_entry.grid(row=3, column=0, pady=(2, 8))
        self.cpf_entry.bind("<KeyRelease>", self._on_cpf_change)

        ttk.Label(card, text="Senha", style="FieldLabel.TLabel").grid(row=4, column=0, sticky="w")
        self.pass_var = tk.StringVar()
        self.pass_entry = ttk.Entry(card, textvariable=self.pass_var, font=("Segoe UI", 11),
                                    width=30, show="•")
        self.pass_entry.grid(row=5, column=0, pady=(2, 12))

        btn_frame = ttk.Frame(card)
        btn_frame.grid(row=6, column=0, pady=(0, 4))

        ttk.Button(btn_frame, text="Entrar", command=self.try_login).grid(row=0, column=0, padx=(0, 8))
        ttk.Button(btn_frame, text="Cancelar", command=self.parent.destroy).grid(row=0, column=1)

        self.msg = ttk.Label(card, text="", style="Msg.TLabel")
        self.msg.grid(row=7, column=0, pady=(8, 0))

        self.grid(row=0, column=0)
        self.cpf_entry.focus_set()

    def _on_cpf_change(self, event=None):
        raw = re.sub(r"\D", "", self.cpf_var.get())[:11]

        if len(raw) == 0:
            formatted = ""
        elif len(raw) <= 3:
            formatted = raw
        elif len(raw) <= 6:
            formatted = f"{raw[:3]}.{raw[3:]}"
        elif len(raw) <= 9:
            formatted = f"{raw[:3]}.{raw[3:6]}.{raw[6:]}"
        else:
            formatted = f"{raw[:3]}.{raw[3:6]}.{raw[6:9]}-{raw[9:]}"

        if self.cpf_var.get() != formatted:
            cursor = self.cpf_entry.index("insert")
            self.cpf_var.set(formatted)
            try:
                self.cpf_entry.icursor(cursor)
            except:
                pass

    def try_login(self):
        cpf = re.sub(r"\D", "", self.cpf_var.get())
        password = self.pass_var.get()

        if len(cpf) != 11:
            self.msg.config(text="CPF inválido.")
            return
        if not password:
            self.msg.config(text="Senha obrigatória.")
            return

        self.msg.config(text="Conectando...")

        try:
            resp = requests.post(API_URL, json={"cpf": cpf, "password": password})
            data = resp.json()
        except Exception as e:
            self.msg.config(text=f"Erro: {e}")
            return

        if "error" in data:
            self.msg.config(text=data["error"])
        else:
            self.msg.config(text="Login OK!", foreground="#0f9d58")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
