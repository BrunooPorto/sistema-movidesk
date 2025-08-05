
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
from sistema import criar_chamado_cliente, visualizar_chamados_cliente


def abrir_janela_cliente(root):
    root.withdraw()
    janela = tk.Toplevel()
    janela.title("Área do Cliente")
    janela.geometry("400x500")

    def voltar():
        janela.destroy()
        root.deiconify()

    janela.protocol("WM_DELETE_WINDOW", lambda: [janela.destroy(), root.deiconify()])

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Assunto:").pack()
    entry_assunto = tk.Entry(janela)
    entry_assunto.pack()

    tk.Label(janela, text="Categoria:").pack()
    combo_categoria = ttk.Combobox(janela, values=["Dúvida", "Problema", "Solicitação", "Sugestão"])
    combo_categoria.pack()

    tk.Label(janela, text="Urgência:").pack()
    combo_urgencia = ttk.Combobox(janela, values=["Urgente", "Alta", "Média", "Baixa"])
    combo_urgencia.pack()

    tk.Label(janela, text="Mensagem:").pack()
    entry_mensagem = tk.Text(janela, height=5)
    entry_mensagem.pack()

    def abrir_chamado():
        nome = entry_nome.get()
        assunto = entry_assunto.get()
        categoria = combo_categoria.get()
        urgencia = combo_urgencia.get()
        mensagem = entry_mensagem.get("1.0", tk.END).strip()
        if not (nome and assunto and categoria and urgencia and mensagem):
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return
        id_gerado = criar_chamado_cliente(nome, assunto, categoria, urgencia, mensagem)
        messagebox.showinfo("Chamado Criado", f"ID do chamado: {id_gerado}")

    def ver_chamados():
        nome = entry_nome.get()
        if not nome:
            messagebox.showwarning("Campo obrigatório", "Digite seu nome para buscar seus chamados.")
            return
        chamados = visualizar_chamados_cliente(nome)
        if chamados:
            messagebox.showinfo("Seus chamados", "\n\n".join(chamados))
        else:
            messagebox.showinfo("Seus chamados", "Nenhum chamado encontrado.")

    tk.Button(janela, text="Abrir Chamado", command=abrir_chamado).pack(pady=5)
    tk.Button(janela, text="Ver Meus Chamados", command=ver_chamados).pack(pady=5)
    tk.Button(janela, text="Voltar", command=voltar).pack(pady=5)
