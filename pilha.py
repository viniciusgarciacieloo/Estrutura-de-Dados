TAM_MAX = 99   

class TpPilha:
    def __init__(self):
        self.elem = [None] * (TAM_MAX + 1)  
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
    
    
def posFixa(lista: list[str]):
    s = ""
    p = TpPilha()
    inicializaPilha(p)
    
    for caracter in lista:
        if caracter in "0123456789":
            s += caracter
        elif caracter == ".":
            empilha(p, int(s))
            s = ""
        elif caracter in "+-*/":
            if not pilhaVazia(p):
                direita = desempilha(p)
            else:
                print("Está faltando um operando")
                return
            
            if not pilhaVazia(p):
                esquerda = desempilha(p)
            else:
                print("Está faltando um operando")
                return
            
            if caracter == "+":
                resp = esquerda +  direita
            elif caracter == "-":
                resp = esquerda - direita    
            elif caracter == "*":
                resp = esquerda * direita   
            else:
                if direita == 0:
                    print("Divisão por zero")
                    return 
                else:
                    resp = esquerda // direita
            empilha(p, resp)
            
    if pilhaVazia(p):   
        print("Está faltando um operando")
        return

    resultado = desempilha(p)
    if pilhaVazia(p):
        print("O Resultado da operação é: ", resultado)
    else:
        print("Esta faltando um operador")

def main(): 
    try:
        arquivo = input("Digite o nome do arquivo que deseja: ")
        with open(arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print()
                linha = linha.strip()         
                print("A linha é:", linha)
                posFixa(linha)                       
    except FileNotFoundError:
        print("O arquivo digitado não existe. ")
    
if __name__ == "__main__":
    main()
