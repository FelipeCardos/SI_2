# def x(X, a, Y, b, l = {}):
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


#     def restricoes_futoshiki(X, a, Y, b):
#         if a == b:
#             if X[0] == Y[0] or X[1] == Y[1]:
#                 return False
#         else:
#             if l != {}:
#                 posicao_X = (int(X[0]),int(X[1]))
#                 posicao_Y = (int(Y[0]),int(Y[1]))
#                 if posicao_X in list(l.keys()):
#                     valor_X = l[posicao_X]
#                     if posicao_Y == resticoes_de_maior(posicao_X, valor_X) and a > b:
#                         return True
#                     else:
#                         return False
#                 if posicao_Y in list(l.keys()):
#                     valor_Y = l[posicao_Y]
#                     if posicao_X == resticoes_de_maior(posicao_Y, valor_Y) and b > a:
#                         return True
#                     else:
#                         return False
#                 else:
#                         return True
#             else:    
#                 return True
    
#     return restricoes_futoshiki(X, a, Y, b)

# # print(x(('0', '0'), 1, ('0', '1'), 1))
# # print(x(('0', '0'), 1, ('0', '1'), 2))
# # print(x(('0', '0'), 1, ('1', '0'), 1))
# print(x(('1', '0'), 3, ('2', '0'), 2, {(1,0):'E'}))

l = {(1,0):'E', (3,1):'O'}
ll = {}
for pos in list(l.keys()):
    ll[pos] = resticoes_de_maior(pos, l[pos])
    
print(ll)



            # if l != {}:
            #     posicao_X = (int(X[0]),int(X[1]))
            #     posicao_Y = (int(Y[0]),int(Y[1]))
            #     if posicao_X in list(l.keys()):
            #         valor_X = l[posicao_X]
            #         if posicao_Y == resticoes_de_maior(posicao_X, valor_X) and a > b:
            #             return True
            #         else:
            #             return False
            #     if posicao_Y in list(l.keys()):
            #         valor_Y = l[posicao_Y]
            #         if posicao_X == resticoes_de_maior(posicao_Y, valor_Y) and b > a:
            #             return True
            #         else:
            #             return False
            #     else:
            #             return True
            # else:    