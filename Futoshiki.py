from csp import *
    
def diferentes(x,y):
    return x != y 

def Futoshiki(n):
    variables = [str(x) for x in range(1,n+1)]
    domains = {}
    neighbors = ''
    restricoes = {}
    for variable in variables:
        domains[variable] = [(x, y) for x in range(n) for y in range(n)]
        neighbors+= str(variable) + ' : ' + str(domains[variable])
    neighbors = parse_neighbors(neighbors)

    def restricoes_futoshiki(x, y, a, b):
        if x in variables and y in linha or \
           x in variables and y in coluna:
           restricoes[(x,y)] = diferentes

        if (x,y) in restricoes:
            return restricoes[(x,y)(a,b)]

    return CSP(variables, domains, neighbors, restricoes_futoshiki)