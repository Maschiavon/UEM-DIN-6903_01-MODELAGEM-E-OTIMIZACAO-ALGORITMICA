import math
from math import *
import random
import sys
import time
import os

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
        #matrix_custo = [0 for row in range(tamanho)]

        while k <= tamanho_indice:
            # A ultima conexão deve ser com o vertice de inicio
            if k == tamanho_indice:
                lista_vert[vert_inicio].visitado = False

            # Obtendo V1
            v1 = lista_vert[index]
            v1.visitado = True

            # Criando lista de custo da linha
            #lista_custoV1 = [0 for r in range(tamanho)]

            for v2 in lista_vert:
                # V2 Não pode ser ele mesmo e não pode ter sido visitado previamente
                vert_vist = not v2.visitado

                # Calcula a distancia euclidiana entre v1 e v2
                distancia = distancia_euclidiana(v1, v2)
                #lista_custoV1[v2.index - 1] = distancia # Registra a distancia na linha da matrix de custo

                if vert_vist:
                    # Se essa distancia for menor que a ultima distancia calculada
                    # esse vertice será uma opção menos
                    if distancia > maior_distancia:
                        maior_distancia = distancia
                        maior_vertice = v2.index - 1

            # Adicionando lista de custo na matrix
            #matrix_custo[v1.index-1] = lista_custoV1

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
        #print(distancia_final)
        return lst_conexoes_melhor#, matrix_custo


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
        #matrix_custo = [0 for row in range(tamanho)]

        while k <= tamanho_indice:
            # A ultima conexão deve ser com o vertice de inicio
            if k == tamanho_indice:
                lista_vert[vert_inicio].visitado = False

            # Obtendo V1
            v1 = lista_vert[index]
            v1.visitado = True

            # Criando lista de custo da linha
            #lista_custoV1 = [0 for r in range(tamanho)]

            for v2 in lista_vert:
                # V2 Não pode ser ele mesmo e não pode ter sido visitado previamente
                vert_vist = not v2.visitado

                # Calcula a distancia euclidiana entre v1 e v2
                distancia = distancia_euclidiana(v1, v2)
                #lista_custoV1[v2.index - 1] = distancia # Registra a distancia na linha da matrix de custo

                if vert_vist:
                    # Se essa distancia for menor que a ultima distancia calculada
                    # esse vertice será uma opção menos
                    if distancia < menor_distancia:
                        menor_distancia = distancia
                        menor_vertice = v2.index - 1

            # Adicionando lista de custo na matrix
            #matrix_custo[v1.index-1] = lista_custoV1

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
        return lst_conexoes_melhor#, matrix_custo


# Recebe a matrix de custo e 2 conexoes, e verfica se mudar as
# conexoes melhora o caminho final, se sim troca a conexao
def mudar_custok3(conexao1, conexao2, conexao3):
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
        n1_n6 = distancia_euclidiana(conexao1.v1, conexao3.v2)
        n3_n2 = distancia_euclidiana(conexao2.v1, conexao1.v2)
        n5_n4 = distancia_euclidiana(conexao3.v1, conexao2.v2)

        result = n1_n6 + n3_n2 + n5_n4 \
                 - (conexao1.distancia + conexao2.distancia + conexao3.distancia)
        if result < 0:
            # muda as coneções, falta impedir de zoar o grafo !!!!
            conexao1.distancia = n1_n6
            conexao2.distancia = n3_n2
            conexao3.distancia = n5_n4
            conexao1.v2, conexao2.v2, conexao3.v2 = conexao3.v2, conexao1.v2, conexao2.v2


# Recebe a matrix de custo e 2 conexoes, e verfica se mudar as
# conexoes melhora o caminho final, se sim troca a conexao
def mudar_custok2(conexao1, conexao2):
    n1 = conexao1.v1.index-1 #conex1 v1
    n2 = conexao1.v2.index-1 #conex1 v2
    n3 = conexao2.v1.index-1 #conex2 v1
    n4 = conexao2.v2.index-1 #conex2 v2
    result = 0

    # nova conexão não pode ser com aresta adjcente
    condicao1 = n1 != n3 and n1 != n4
    condicao2 = n2 != n3 and n2 != n4

    if condicao1 and condicao2:
        n1_n4 = distancia_euclidiana(conexao1.v1, conexao2.v2)
        n2_n3 = distancia_euclidiana(conexao1.v2, conexao2.v1)

        result = n1_n4 + n2_n3 - conexao1.distancia - conexao2.distancia
        if result < 0:
            # muda as coneções, falta impedir de zoar o grafo !!!!
            conexao1.distancia = n1_n4
            conexao2.distancia = n2_n3
            conexao1.v2, conexao2.v2 = conexao2.v2, conexao1.v2


# Rebece o valor final do metodo de contrução, uma matrix de conexões e um k
# K-Opt é um metodo de melhoria que remove k arestas de k vertices distintos
def Melhoria_K_Opt(lista_conexao, k):

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
                    mudar_custok2(conexao1, conexao2)
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
                        mudar_custok3(conexao1, conexao2, conexao3)
        custo_melhorado = 0
        for conx in melhor_rota:
            #print("v1:", conx.v1.index, " v2:", conx.v2.index, " distancia:", conx.distancia)
            custo_melhorado += conx.distancia
        print("Custo Final (k =", k,"):",custo_melhorado)
        #print(custo_melhorado)


# Recebe e faz um print da matrix de custo e
# e da lista das mehlores conexoes
def Printa_informacoes(lst_conexoes_melhor, tempo):
    # for linha in matrix_custo:
    #     print(linha)

    custo = 0
    for conx in lst_conexoes_melhor:
        #print("v1:",conx.v1.index," v2:",conx.v2.index, " distancia:",conx.distancia)
        custo += conx.distancia
    print("Custo:",custo)
    print("Tempo (milisegundo)):", tempo)


# Função que recebe uma lista de conexoes e altera o estado visitado de todos
# os vertices de uma  lista de conexoes ordenada para falso, os vertices da lista
# de conexoes devem estar ligados por referencia.
def Reinicia_Vertices(lista_conexoes):
    for conexao in lista_conexoes:
        conexao.v2.visitado = False

# Testa os casos do diretorio pra construção mais proxima, mais longe
# Melhoramento 2-opt, 3-opt.
def TestarCasos():
    directory = 'Arquivos de teste'
    # itera sobre os arquivos
    # daquele diretorio
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # Abre o arquivo e armazena linha por linha em
            # um vetor de strings sem o \n no final
            with open(f) as arquivo:
                linhas = [linha.rstrip() for linha in arquivo]

            lista_vertices = []  # Criando a lista de vertices
            for linha in linhas[6:]:
                array_linha = linha.split()
                if array_linha[0] != 'EOF':
                    # Criando vertice e  adicionando a lista de vertices
                    vert = vertice()
                    vert.index = int(array_linha[0])
                    vert.posX = float(array_linha[1])
                    vert.posY = float(array_linha[2])
                    vert.visitado = False
                    lista_vertices.append(vert)
                # print(array_linha)

            print("\n/////TESTE:", f[18:], "/////")
            print("///Caso", f[18:],"- Inserção mais proximo///")
            start = time.time()
            lst_conexoes_melhor = Insercao_Mais_Proximo(lista_vertices)
            end = time.time()

            # Pega e calcula o tempo decorrido
            tempo = (end - start) * 1000
            Printa_informacoes(lst_conexoes_melhor, tempo)

            k = 2
            print("\n////Caso", f[18:],"- Inserção mais proximo - Melhoramento", k, "- opt////")
            start = time.time()
            Melhoria_K_Opt(lst_conexoes_melhor, k)
            end = time.time()
            tempo = (end - start) * 1000
            print("Tempo (milisegundos):", tempo)

            k = 3
            print("\n////Caso", f[18:],"- Inserção mais proximo - Melhoramento", k, "- opt////")
            start = time.time()
            Melhoria_K_Opt(lst_conexoes_melhor, k)
            end = time.time()
            tempo = (end - start) * 1000
            print("Tempo (milisegundos):", tempo)

            # Reinicia os vertices para fazer a operação com o algoritmo mais longe
            Reinicia_Vertices(lst_conexoes_melhor)

            print("\n///Caso", f[18:],"- Inserção mais Longe///")
            start = time.time()
            lst_conexoes_melhor1 = Insercao_Mais_Longe(lista_vertices)
            end = time.time()

            # Pega e calcula o tempo decorrido
            tempo = (end - start) * 1000
            Printa_informacoes(lst_conexoes_melhor1, tempo)

            k = 2
            print("\n////Caso", f[18:],"- Inserção mais Longe - Melhoramento", k, "- opt////")
            start = time.time()
            Melhoria_K_Opt(lst_conexoes_melhor1, k)
            end = time.time()
            tempo = (end - start) * 1000
            print("Tempo (milisegundos):", tempo)

            k = 3
            print("\n////Caso", f[18:],"- Inserção mais Longe - Melhoramento", k, "- opt////")
            start = time.time()
            Melhoria_K_Opt(lst_conexoes_melhor1, k)
            end = time.time()
            tempo = (end - start) * 1000
            print("Tempo (milisegundos):", tempo)


def main():
    TestarCasos()

if __name__ == '__main__':
    main()