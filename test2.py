from csp import *

def quadrado_latino(n, k = [], l = {}):
    """
    Pode receber parametros ou não.
    Deve devolver um CSP, à semelhança dos guiões das aulas PL.
    Comente o código.
    """
    variaveis = [(x,y) for x in range(n) for y in range(n)]


    dominio = {}
    for variavel in variaveis:
        dominio[variavel] = [x for x in range(1,n+1)]
    
    if k != []:
        for x in range(len(k)):
            dominio[k[x][0]] = [k[x][1]]

    vizinho = {}
    for variavel in variaveis:
        vizinho[variavel] = []
        for variavel2 in variaveis:
            if variavel != variavel2 and (variavel[0] == variavel2[0] or variavel[1] == variavel2[1]):
                vizinho[variavel].append(variavel2)
            
    def resticoes_de_maior(posicao, valor):
        O = (-1,0)
        E = (1,0)
        N = (0,-1)
        S = (0,1) 
        if valor == "O":
            return (posicao[0] + O[0], posicao[1] + O[1])
        elif valor == "E":
            return (posicao[0] + E[0], posicao[1] + E[1])
        elif valor == "N":
            return (posicao[0] + N[0], posicao[1] + N[1])
        elif valor == "S":
            return (posicao[0] + S[0], posicao[1] + S[1])

    ll = {}
    for pos in list(l.keys()):
        ll[pos] = resticoes_de_maior(pos, l[pos])
        


    def restricoes_futoshiki(X, a, Y, b):
        if a == b:
            if X[0] == Y[0] or X[1] == Y[1]:
                return False
        else:
            if ll != {}:
                X = (int(X[0]),int(X[1]))
                Y = (int(Y[0]),int(Y[1]))
                if X in list(ll.keys()):
                    if Y == ll[X] and a > b:
                        return True
                if X in list(ll.keys()):
                    if Y != ll[X]:
                        return True
                if Y in list(ll.keys()):
                    if X != ll[Y]:
                        return True
                if Y in list(ll.keys()):
                    if X == ll[X] and b > a:
                        return True
                else:
                    return False
                    
            else:    
                return True
            

    return CSP(variaveis, dominio, vizinho, restricoes_futoshiki), n

w, n = quadrado_latino(3, l = {(1,0): "E"})
print(w.constraints(('1', '0'), 2, ('2', '0'), 3))