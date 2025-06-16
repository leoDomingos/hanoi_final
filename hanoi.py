# Aluno: Leonardo Domingos
# DRE: 120168324







class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, item):
        self.itens.append(item)
    
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    
    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)


def torre_de_hanoi(n, origem, destino, auxiliar, movimentos):
    # recursão: é bom começar a função que vai recursionar com
    # o stopping point (no caso, n==1)
    # depois especificar quando a função vai continuar com else
    
    if n == 1:
        disco = origem.desempilhar()
        destino.empilhar(disco)
        movimentos.append(f"Mover disco {disco} de {origem} para {destino}")
    else:
        # print(torre_de_hanoi(1, origem, destino, auxiliar, movimentos))
        # print(torre_de_hanoi(n-1, origem, auxiliar, destino, movimentos))
        # print(torre_de_hanoi(n-1, auxiliar, destino, origem, movimentos))
        torre_de_hanoi(n-1, origem, auxiliar, destino, movimentos)
        torre_de_hanoi(1, origem, destino, auxiliar, movimentos)
        torre_de_hanoi(n-1, auxiliar, destino, origem, movimentos)


def resolver_hanoi(n_discos):
    torre_A = Pilha()
    torre_B = Pilha()
    torre_C = Pilha()
    torre_A.nome = "Torre A"
    torre_B.nome = "Torre B"
    torre_C.nome = "Torre C"



    # empilhando
    for disco in range(n_discos, 0, -1):
        torre_A.empilhar(disco)
        # print(disco)
        # print(torre_A)
    
    movimentos = []
    
    print("Configuração inicial:")
    print(f"{torre_A.nome}: {torre_A}")
    print(f"{torre_B.nome}: {torre_B}")
    print(f"{torre_C.nome}: {torre_C}")
    print()
    
    # Resolve o problema
    torre_de_hanoi(n_discos, torre_A, torre_C, torre_B, movimentos)
    
    # Print sequencia
    print("Sequência de movimentos:")
    for i, movimento in enumerate(movimentos, 1):
        print(f"{i}. {movimento}")
    

    print("\nConfiguração final:")
    print(f"{torre_A.nome}: {torre_A}")
    print(f"{torre_B.nome}: {torre_B}")
    print(f"{torre_C.nome}: {torre_C}")
    print(f"\nTotal de movimentos: {len(movimentos)} (esperado: {2**n_discos - 1})")


# Testando com 3 discos
resolver_hanoi(5)