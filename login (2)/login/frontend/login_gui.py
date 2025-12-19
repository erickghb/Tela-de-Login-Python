import tkinter as tk
import requests

class LoginGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")

        tk.Label(text="CPF").pack()
        self.cpf_entry = tk.Entry()
        self.cpf_entry.pack()

        tk.Label(text="Senha").pack()
        self.pass_entry = tk.Entry(show="*")
        self.pass_entry.pack()

        tk.Button(text="Login", command=self.login).pack()

        self.msg = tk.Label(text="")
        self.msg.pack()

        self.window.mainloop()

    def login(self):
        data = {
            "cpf": self.cpf_entry.get(),
            "password": self.pass_entry.get()
        }

        response = requests.post("http://localhost:8000/login", json=data)
        result = response.json()

        if "error" in result:
            self.msg.config(text=result["error"], fg="red")
        else:
            self.msg.config(text="Acesso liberado!", fg="green")

LoginGUI()
