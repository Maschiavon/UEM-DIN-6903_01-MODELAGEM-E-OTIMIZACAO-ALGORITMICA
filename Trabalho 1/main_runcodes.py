import math
from math import *
import random
import sys


class vertice:
    index: int
    posX: float
    posY: float
    visitado: bool

class conexao:
    v1: vertice
    v2: vertice
    distancia: float


# Recebe a cordenada x e y de dois vertices distintos
# e calcula a distãncia euclidiana entre eles
def distancia_euclidiana(v1, v2):
    r = sqrt((v2.posX - v1.posX) ** 2 + (v2.posY - v1.posY) ** 2)
    return r

# Implementação do metodo construtivo do algoritmo de inserção do mais longe
# (o algoritmo busca o vertice com maior custo para fazer a conexão)
# para o problema do caixeiro viajante, recebe uma lista de vertices printa o resultado
# e devolve as combinações desses vertices de forma a reduzir o custo (não garante a melhor opção).
def Insercao_Mais_Longe(lista_vert):
    tamanho = len(lista_vert)

    # Tratando caso base se tiver 2 ou menor vertices
    if tamanho < 2:
        print(0)
    elif tamanho == 2:
        v1 = lista_vert[0]
        v2 = lista_vert[1]
        custo = 2*distancia_euclidiana(v1, v2)
        print(custo)
    else:
        tamanho_indice = len(lista_vert) - 1
        distancia_final = 0
        maior_vertice = 0
        maior_distancia = -math.inf  # Defindo a variavel que conterá o menor vertice
        vert_inicio = 0 #random.randrange(0, tamanho)  # Faz ele começar em vertice aleatorio

        k = 0
        index = vert_inicio # vert_inicio # Definindo o vertice inicial

        # Lista ordenada das melhores conexoes
        #lst_conexoes_melhor = [] #Adjacente
        lst_conexoes_melhor = [0 for r in range(tamanho)] #Ordenado

        # Matrix simetrica e ordenada com o custo de todas as conexoes
        matrix_custo = [0 for row in range(tamanho)]

        while k <= tamanho_indice:
            # A ultima conexão deve ser com o vertice de inicio
            if k == tamanho_indice:
                lista_vert[vert_inicio].visitado = False

            # Obtendo V1
            v1 = lista_vert[index]
            v1.visitado = True

            # Criando lista de custo da linha
            lista_custoV1 = [0 for r in range(tamanho)]

            for v2 in lista_vert:
                # V2 Não pode ser ele mesmo e não pode ter sido visitado previamente
                vert_vist = not v2.visitado

                # Calcula a distancia euclidiana entre v1 e v2
                distancia = distancia_euclidiana(v1, v2)
                lista_custoV1[v2.index - 1] = distancia # Registra a distancia na linha da matrix de custo

                if vert_vist:
                    # Se essa distancia for menor que a ultima distancia calculada
                    # esse vertice será uma opção menos
                    if distancia > maior_distancia:
                        maior_distancia = distancia
                        maior_vertice = v2.index - 1

            # Adicionando lista de custo na matrix
            matrix_custo[v1.index-1] = lista_custoV1

            # Adicionando na lista a melhor conexao de v1 com v2
            nova_conexao = conexao()
            nova_conexao.v1 = v1
            nova_conexao.v2 = lista_vert[maior_vertice]
            nova_conexao.distancia = maior_distancia
            # Inserindo adjacente
            # lst_conexoes_melhor.append(nova_conexao)
            # Inserção ordenada na posição da escolha da conexão v1
            lst_conexoes_melhor[v1.index-1] = nova_conexao

            # Adicionando a distancia para a variavel final
            distancia_final += maior_distancia

            # Incrementa K
            k += 1

            # Reiniciando variaveis
            maior_distancia = -math.inf

            # o ultimo vertice conectado será o proximo a escolher
            index = maior_vertice
        print(distancia_final)
        return lst_conexoes_melhor, matrix_custo


# Implementação do metodo construtivo do algoritmo de inserção do mais proximo
# (o algoritmo busca o vertice com menos custo para fazer a conexão)
# para o problema do caixeiro viajante, recebe uma lista de vertices printa o resultado
# e devolve as combinações desses vertices de forma a reduzir o custo (não garante a melhor opção).
def Insercao_Mais_Proximo(lista_vert):
    tamanho = len(lista_vert)

    # Tratando caso base se tiver 2 ou menor vertices
    if tamanho < 2:
        print(0)
    elif tamanho == 2:
        v1 = lista_vert[0]
        v2 = lista_vert[1]
        custo = 2*distancia_euclidiana(v1, v2)
        print(custo)
    else:
        tamanho_indice = len(lista_vert) - 1
        distancia_final = 0
        menor_vertice = 0
        menor_distancia = math.inf  # Defindo a variavel que conterá o menor vertice
        vert_inicio = 0 #random.randrange(0, tamanho)  # Faz ele começar em vertice aleatorio

        k = 0
        index = vert_inicio # vert_inicio # Definindo o vertice inicial

        # Lista ordenada das melhores conexoes
        #lst_conexoes_melhor = [] #Adjacente
        lst_conexoes_melhor = [0 for r in range(tamanho)] #Ordenado

        # Matrix simetrica e ordenada com o custo de todas as conexoes
        matrix_custo = [0 for row in range(tamanho)]

        while k <= tamanho_indice:
            # A ultima conexão deve ser com o vertice de inicio
            if k == tamanho_indice:
                lista_vert[vert_inicio].visitado = False

            # Obtendo V1
            v1 = lista_vert[index]
            v1.visitado = True

            # Criando lista de custo da linha
            lista_custoV1 = [0 for r in range(tamanho)]

            for v2 in lista_vert:
                # V2 Não pode ser ele mesmo e não pode ter sido visitado previamente
                vert_vist = not v2.visitado

                # Calcula a distancia euclidiana entre v1 e v2
                distancia = distancia_euclidiana(v1, v2)
                lista_custoV1[v2.index - 1] = distancia # Registra a distancia na linha da matrix de custo

                if vert_vist:
                    # Se essa distancia for menor que a ultima distancia calculada
                    # esse vertice será uma opção menos
                    if distancia < menor_distancia:
                        menor_distancia = distancia
                        menor_vertice = v2.index - 1

            # Adicionando lista de custo na matrix
            matrix_custo[v1.index-1] = lista_custoV1

            # Adicionando na lista a melhor conexao de v1 com v2
            nova_conexao = conexao()
            nova_conexao.v1 = v1
            nova_conexao.v2 = lista_vert[menor_vertice]
            nova_conexao.distancia = menor_distancia
            # Inserindo adjacente
            # lst_conexoes_melhor.append(nova_conexao)
            # Inserção ordenada na posição da escolha da conexão v1
            lst_conexoes_melhor[v1.index-1] = nova_conexao

            # Adicionando a distancia para a variavel final
            distancia_final += menor_distancia

            # Incrementa K
            k += 1

            # Reiniciando variaveis
            menor_distancia = math.inf

            # o ultimo vertice conectado será o proximo a escolher
            index = menor_vertice
        #print(distancia_final)
        return lst_conexoes_melhor, matrix_custo


# Recebe a matrix de custo e 2 conexoes, e verfica se mudar as
# conexoes melhora o caminho final, se sim troca a conexao
def mudar_custok3(matrix_custo, conexao1, conexao2, conexao3):
    n1 = conexao1.v1.index-1 #conex1 v1
    n2 = conexao1.v2.index-1 #conex1 v2
    n3 = conexao2.v1.index-1 #conex2 v1
    n4 = conexao2.v2.index-1 #conex2 v2
    n5 = conexao3.v1.index-1 #conex3 v1
    n6 = conexao3.v2.index-1 #conex3 v2
    result = 0

    # nova conexão não pode ser com aresta adjcente
    condicao1 = n1 != n3 and n1 != n4 and n1 != n5 and n1 != n6
    condicao2 = n2 != n3 and n2 != n4 and n2 != n5 and n2 != n6
    condicao3 = n3 != n5 and n3 != n6
    condicao4 = n4 != n5 and n4 != n6

    if condicao1 and condicao2 and condicao3 and condicao4:
        result = matrix_custo[n1][n6] + matrix_custo[n3][n2] + matrix_custo[n5][n4] \
                 - (matrix_custo[n1][n2] + matrix_custo[n3][n4] + matrix_custo[n5][n6])
        if result < 0:
            # muda as coneções, falta impedir de zoar o grafo !!!!
            conexao1.distancia = matrix_custo[n1][n6]
            conexao2.distancia = matrix_custo[n3][n2]
            conexao3.distancia = matrix_custo[n5][n4]
            conexao1.v2, conexao2.v2, conexao3.v2 = conexao3.v2, conexao1.v2, conexao2.v2


# Recebe a matrix de custo e 2 conexoes, e verfica se mudar as
# conexoes melhora o caminho final, se sim troca a conexao
def mudar_custok2(matrix_custo, conexao1, conexao2):
    n1 = conexao1.v1.index-1 #conex1 v1
    n2 = conexao1.v2.index-1 #conex1 v2
    n3 = conexao2.v1.index-1 #conex2 v1
    n4 = conexao2.v2.index-1 #conex2 v2
    result = 0

    # nova conexão não pode ser com aresta adjcente
    condicao1 = n1 != n3 and n1 != n4
    condicao2 = n2 != n3 and n2 != n4

    if condicao1 and condicao2:
        result = matrix_custo[n1][n4] + matrix_custo[n2][n3] - matrix_custo[n1][n2] - matrix_custo[n3][n4]
        if result < 0:
            # muda as coneções, falta impedir de zoar o grafo !!!!
            conexao1.distancia = matrix_custo[n1][n4]
            conexao2.distancia = matrix_custo[n2][n3]
            conexao1.v2, conexao2.v2 = conexao2.v2, conexao1.v2


# Rebece o valor final do metodo de contrução, uma matrix de conexões e um k
# K-Opt é um metodo de melhoria que remove k arestas de k vertices distintos
def Melhoria_K_Opt(lista_conexao, matrix_custo, k):

    # Tratando caso base se tiver 2 ou menor vertices
    tamanho = len(lista_conexao)
    if tamanho < 2:
        print(0)
    elif tamanho == 2:
        conexao = lista_conexao[0]
        custo = 2*conexao.distancia
        print(custo)
    else:
        # K deverá ser pelo menos 2
        if k == 2:
            melhor_rota = lista_conexao
            # Como i e j nunca vão ser iguais ele faz -1 vezes
            # Como ele não precisa fazer a ultima interação -1 vezes
            for i in range(0, tamanho-1):
                for j in range(i + 1, tamanho):
                    conexao1 = melhor_rota[i]
                    conexao2 = melhor_rota[j]
                    mudar_custok2(matrix_custo, conexao1, conexao2)
        if k == 3:
            melhor_rota = lista_conexao
            # Como i e j nunca vão ser iguais ele faz -1 vezes
            # Como ele não precisa fazer a ultima interação -1 vezes
            for i in range(0, tamanho - 2):
                for j in range(i + 1, tamanho - 1):
                    for l in range(j + 1, tamanho):
                        conexao1 = melhor_rota[i]
                        conexao2 = melhor_rota[j]
                        conexao3 = melhor_rota[l]
                        mudar_custok3(matrix_custo, conexao1, conexao2, conexao3)
        custo_melhorado = 0
        for conx in melhor_rota:
            #print("v1:", conx.v1.index, " v2:", conx.v2.index, " distancia:", conx.distancia)
            custo_melhorado += conx.distancia
        print(custo_melhorado)  # "Custo Final:",


def main():

    #User input tudo de uma vez
    Continuar = True
    lista_vertices = []
    count = 0
    entrada = sys.stdin.readlines()
    while Continuar:
        linha = entrada[count]
        if count > 5:
            array_linha = linha.split()
            if array_linha[0] == "EOF":
                Continuar = False
            else:
                vert = vertice()
                vert.index = int(array_linha[0])
                vert.posX = float(array_linha[1])
                vert.posY = float(array_linha[2])
                vert.visitado = False
                lista_vertices.append(vert)
        count += 1


    # lista_vertices_caso1 = [
    #     [1, 6734, 1453],
    #     [2, 2233, 10],
    #     [3, 5530, 1424],
    #     [4, 401, 841],
    #     [5, 3082, 1644],
    #     [6, 7608, 4458],
    #     [7, 7573, 3716],
    #     [8, 7265, 1268],
    #     [9, 6898, 1885],
    #     [10, 1112, 2049],
    #     [11, 5468, 2606],
    #     [12, 5989, 2873],
    #     [13, 4706, 2674],
    #     [14, 4612, 2035],
    #     [15, 6347, 2683],
    #     [16, 6107, 669],
    #     [17, 7611, 5184],
    #     [18, 7462, 3590],
    #     [19, 7732, 4723],
    #     [20, 5900, 3561],
    #     [21, 4483, 3369],
    #     [22, 6101, 1110],
    #     [23, 5199, 2182],
    #     [24, 1633, 2809],
    #     [25, 4307, 2322],
    #     [26, 675, 1006],
    #     [27, 7555, 4819],
    #     [28, 7541, 3981],
    #     [29, 3177, 756],
    #     [30, 7352, 4506],
    #     [31, 7545, 2801],
    #     [32, 3245, 3305],
    #     [33, 6426, 3173],
    #     [34, 4608, 1198],
    #     [35, 23, 2216],
    #     [36, 7248, 3779],
    #     [37, 7762, 4595],
    #     [38, 7392, 2244],
    #     [39, 3484, 2829],
    #     [40, 6271, 2135],
    #     [41, 4985, 140],
    #     [42, 1916, 1569],
    #     [43, 7280, 4899],
    #     [44, 7509, 3239],
    #     [45, 10, 2676],
    #     [46, 6807, 2993],
    #     [47, 5185, 3258],
    #     [48, 3023, 1942]]
    #
    # lista_vertices_caso2 = [
    #     [1, 0, 0],
    #     [2, 0, 100],
    #     [3, 100, 100],
    #     [4, 100, 0]]
    #
    # lista_vertices = []
    # for lst in lista_vertices_caso2:
    #     vert = vertice()
    #     vert.index = int(lst[0])
    #     vert.posX = float(lst[1])
    #     vert.posY = float(lst[2])
    #     vert.visitado = False
    #     lista_vertices.append(vert)

    lst_conexoes_melhor, matrix_custo = Insercao_Mais_Proximo(lista_vertices)
    #lst_conexoes_melhor, matrix_custo = Insercao_Mais_Longe(lista_vertices)

    #Printa matrix_custo
    # for linha in matrix_custo:
    #     print(linha)
    #
    # custo = 0
    # for conx in lst_conexoes_melhor:
    #     print("v1:",conx.v1.index," v2:",conx.v2.index, " distancia:",conx.distancia)
    #     custo += conx.distancia
    # print("Custo:",custo)
    # print("\n////Melhoramento////")

    k = 2
    Melhoria_K_Opt(lst_conexoes_melhor, matrix_custo, k)

if __name__ == '__main__':
    main()