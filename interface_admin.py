import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from sistema import *

def abrir_janela_admin(root):
    root.withdraw()
    janela = tk.Toplevel()
    janela.title("Área do Administrador")
    janela.geometry("500x600")

    def voltar():
        janela.destroy()
        root.deiconify()

    def ver_fila(ordenar_por="urgencia"):
        fila = listar_chamados_ordenados(ordenar_por)
        if not fila:
            messagebox.showinfo("Fila de chamados", "Nenhum chamado na fila.")
            return
        info = "\n\n".join(str(c) for c in fila)
        messagebox.showinfo("Fila de chamados", info)

    def atender_chamado():
        chamado = atender_proximo_chamado()
        if not chamado:
            messagebox.showinfo("Atendimento", "Nenhum chamado para atender.")
            return
        atender_especifico(chamado)

    def buscar_id():
        id_str = simpledialog.askstring("Buscar", "Digite o ID do chamado:")
        if id_str and id_str.isdigit():
            chamado = buscar_por_id(int(id_str))
            if chamado:
                atender_especifico(chamado)
            else:
                messagebox.showinfo("Resultado", "Chamado não encontrado.")

    def buscar_por_urgencia():
        urgencia = simpledialog.askstring("Buscar", "Digite a urgência (Urgente, Alta, Média, Baixa):")
        if not urgencia:
            return
        nivel = niveis_prioridade.get(urgencia.lower())
        if nivel is None:
            messagebox.showwarning("Inválido", "Urgência inválida.")
            return

        encontrados = [ch for p, _, ch in fila_prioridade if p == nivel]
        if not encontrados:
            messagebox.showinfo("Resultado", "Nenhum chamado encontrado.")
            return

        for chamado in encontrados:
            atender_especifico(chamado)

    def buscar_por_categoria():
        categoria = simpledialog.askstring("Buscar", "Digite a categoria (Dúvida, Problema, Solicitação, Sugestão):")
        if not categoria:
            return
        encontrados = [ch for _, _, ch in fila_prioridade if ch.categoria.lower() == categoria.lower()]
        if not encontrados:
            messagebox.showinfo("Resultado", "Nenhum chamado encontrado.")
            return
        for chamado in encontrados:
            atender_especifico(chamado)

    def atender_especifico(chamado):
        janela_atendimento = tk.Toplevel()
        janela_atendimento.title(f"Atendimento ID {chamado.id}")
        janela_atendimento.geometry("400x400")

        tk.Label(janela_atendimento, text="Detalhes do chamado:").pack()
        tk.Message(janela_atendimento, text=str(chamado), width=350).pack()

        status_var = tk.StringVar(value="Solucionado")
        ttk.Combobox(janela_atendimento, textvariable=status_var, values=["Solucionado", "Não solucionado"]).pack(pady=10)

        def finalizar():
            resolver_chamado(chamado.id, status_var.get())
            messagebox.showinfo("Atendimento", f"Chamado {chamado.id} marcado como '{status_var.get()}'")
            janela_atendimento.destroy()

        tk.Button(janela_atendimento, text="Finalizar Atendimento", command=finalizar).pack(pady=5)

    tk.Button(janela, text="Ver chamados (por urgência)", command=lambda: ver_fila("urgencia")).pack(pady=5)
    tk.Button(janela, text="Ver chamados (por ID)", command=lambda: ver_fila("id")).pack(pady=5)
    tk.Button(janela, text="Atender próximo chamado", command=atender_chamado).pack(pady=5)
    tk.Button(janela, text="Buscar por ID e atender", command=buscar_id).pack(pady=5)
    tk.Button(janela, text="Buscar por urgência e atender", command=buscar_por_urgencia).pack(pady=5)
    tk.Button(janela, text="Buscar por categoria e atender", command=buscar_por_categoria).pack(pady=5)
    tk.Button(janela, text="Ver histórico", command=lambda: messagebox.showinfo("Histórico", "\n\n".join(str(c) for c in historico))).pack(pady=5)
    tk.Button(janela, text="Voltar", command=voltar).pack(pady=10)
