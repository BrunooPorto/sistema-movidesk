
import heapq
import itertools

class Chamado:
    novo_id = itertools.count()
    def __init__(self, nome_cliente, assunto, categoria, urgencia, mensagem):
        self.id = next(Chamado.novo_id)
        self.nome_cliente = nome_cliente
        self.assunto = assunto
        self.categoria = categoria
        self.urgencia = urgencia
        self.mensagem = mensagem
        self.status = "Aberto"

    def __str__(self):
        return f"ID: {self.id} | Cliente: {self.nome_cliente}\nAssunto: {self.assunto} | Categoria: {self.categoria} | Urgência: {self.urgencia}\nMensagem: {self.mensagem}\nStatus: {self.status}"

# Dicionário que define o nível de prioridade
niveis_prioridade = {
    "urgente": 0,
    "alta": 1,
    "média": 2,
    "baixa": 3
}

#prioridade para os chamados
fila_prioridade = []

# Lista de chamados resolvidos (histórico)
historico = []

# resgistar todos os chamados por ID (inclusive resolvidos)
registro_geral = {}
# função para gerar chamados automáticos para testes/apresentação
def gerar_chamados_fake():
    exemplos = [
        ("Problema de login", "Problema", "Alta"),
        ("Erro no sistema", "Problema", "Urgente"),
        ("Solicitação de melhoria", "Sugestão", "Média"),
        ("Dúvida sobre plano", "Dúvida", "Baixa")
    ]
    for assunto, categoria, urgencia in exemplos:
        chamado = Chamado("AutoCliente", assunto, categoria, urgencia, "Gerado automaticamente.")
        prioridade = niveis_prioridade.get(urgencia.lower(), 2)
        heapq.heappush(fila_prioridade, (prioridade, chamado.id, chamado))
        registro_geral[chamado.id] = chamado

# Chamada automática para gerar dados fake
gerar_chamados_fake()

#criar chamado "cliente"
def criar_chamado_cliente(nome, assunto, categoria, urgencia, mensagem):
    chamado = Chamado(nome, assunto, categoria, urgencia, mensagem)
    prioridade = niveis_prioridade.get(urgencia.lower(), 2)
    heapq.heappush(fila_prioridade, (prioridade, chamado.id, chamado))
    registro_geral[chamado.id] = chamado
    return chamado.id

def visualizar_chamados_cliente(nome):
    return [str(ch) for ch in registro_geral.values() if ch.nome_cliente.lower() == nome.lower()]

#area adm de lista
def listar_chamados_ordenados(ordenar_por="urgencia"):
    if ordenar_por == "urgencia":
        return [ch for _, _, ch in sorted(fila_prioridade)]
    else:
        return [ch for _, _, ch in sorted(fila_prioridade, key=lambda x: x[1])]

def atender_proximo_chamado():
    if fila_prioridade:
        _, _, chamado = heapq.heappop(fila_prioridade)
        return chamado
    return None

def resolver_chamado(id_chamado, status="Solucionado"):
    chamado = registro_geral.get(id_chamado)
    if chamado:
        chamado.status = status
        historico.append(chamado)

def buscar_por_id(id_):
    return registro_geral.get(id_)
