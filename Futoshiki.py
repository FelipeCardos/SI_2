from csp import *
    
def diferentes(x,y):
    return x != y 

def Futoshiki(n):
    variables = [str(x) for x in range(1,n+1)]
    domains = {}
    neighbors = ''
    restricoes = {}
    for variable in variables:
        domains[variable] = [(x, y) for x in range(1,n+1) for y in range(1,n+1)]
        neighbors+= variable + ":" 
        for v in variables:
            if v != variable:
                neighbors+=" "+v
        neighbors+=";"
    neighbors = parse_neighbors(neighbors[:-1])
    print(neighbors)
    print("==============================================================")
    print(domains)
    print("==============================================================")
    # def restricoes_futoshiki(x, y, a, b):
    #     if x in variables and y in linha or \
    #        x in variables and y in coluna:
    #        restricoes[(x,y)] = diferentes

    #     if (x,y) in restricoes:
    #         return restricoes[(x,y)(a,b)]

    # return CSP(variables, domains, neighbors, restricoes_futoshiki)

Futoshiki(3)