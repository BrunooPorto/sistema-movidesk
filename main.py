#bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from interface_cliente import abrir_janela_cliente
from interface_admin import abrir_janela_admin

def main():
    root = tk.Tk()
    root.title("Trabalho seminário A3- Login")
    root.geometry("400x220")
    
#tentaiva style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 10), padding=6)
    style.configure("TLabel", font=("Arial", 11))

    

    def sair():
        root.destroy()

    ttk.Label(root, text="Sistema de Fila Chamados A3", font=("Arial", 14)).pack(pady=10)
    ttk.Button(root, text="Entrar como Cliente", width=25, command=lambda: abrir_janela_cliente(root)).pack(pady=5)
    ttk.Button(root, text="Entrar como Administrador", width=25, command=lambda: abrir_janela_admin(root)).pack(pady=5)
    ttk.Button(root, text="Sair", width=25, command=sair).pack(pady=5)
    ttk.Label(root, text="Trabalho por: Bruno Porto, Hugo Carvalho, Marcelo Carvalho", font=("Arial", 9), foreground="gray").pack(side="bottom", pady=5)


    root.mainloop()

if __name__ == "__main__":
    main()
