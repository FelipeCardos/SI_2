from csp import *
    
def diferentes(x,y):
    return x != y

def Futoshiki(n):
    variables = [x for x in range(n)]
    domains = {}
    neighbors = ''

    for variable in variables:
        domains[variable] = [(x, y) for x in range(n) for y in range(n)]
        neighbors+= str(variable) + ' : ' + str(domains[variable])
    neighbors = parse_neeighbors(neighbors)

    def restricoes_futoshiki(x, y, linha, coluna):
        if linha:
            