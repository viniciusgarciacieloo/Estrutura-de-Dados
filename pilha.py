# A  avaliação  da expressão deve  utilizar  o tipo  abstrato  de  dados Pilha  (com  implementação  estática 
# em vetor, conforme visto em sala de aula e constante no material de estudo – slides).
TAM_MAX = 99   # constante: o vetor terá TAM_MAX + 1 posições (0..TAM_MAX)

class TpPilha:
    def __init__(self):
        self.elem = [None] * (TAM_MAX + 1)   # vetor de tamanho FIXO
        self.topo = -1                    
    
def inicializaPilha(p: TpPilha):
    p.topo = -1
        
def pilhaVazia(p:TpPilha)-> bool:
    if p.topo == -1:
        return True
    else:
        return False
    
def pilhaCheia(p: TpPilha)-> bool:
    if p.topo == TAM_MAX:
        return True
    else:
        return False

def empilha(p: TpPilha, x: int)-> None:
    if not pilhaCheia(p):
        p.topo = p.topo + 1
        p.elem[p.topo] = x
        
def desempilha(p: TpPilha):
    if not pilhaVazia(p):
        x = p.elem[p.topo]
        p.topo = p.topo - 1
        return x
    
def elementoDoTopo(p: TpPilha):
    if not pilhaVazia(p):
        return p.elem[p.topo]
    else:
        raise IndexError
    
    