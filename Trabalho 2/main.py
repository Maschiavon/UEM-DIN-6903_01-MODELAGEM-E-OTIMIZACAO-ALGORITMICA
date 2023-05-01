import math
from math import *
import random
import sys
import time
import os
import collections
import matplotlib.pyplot as plt

class vertice:
    index: int
    posX: float
    posY: float
    visitado: bool

class conexao:
    v1: vertice
    v2: vertice
    distancia: float

class cromossomo:
    lstConexao: list
    lstConexaoIntAdj: list
    Aptidao: float


# Recebe a cordenada x e y de dois vertices distintos
# e calcula a distãncia euclidiana entre eles
def distancia_euclidiana(v1, v2):
    r = sqrt((v2.posX - v1.posX) ** 2 + (v2.posY - v1.posY) ** 2)
    return r

# Implementação do metodo construtivo do algoritmo de inserção do mais proximo
# (o algoritmo busca o vertice com menos custo para fazer a conexão)
# para o problema do caixeiro viajante, recebe uma lista de vertices printa o resultado
# e devolve as combinações desses vertices de forma a reduzir o custo (não garante a melhor opção).
def Insercao_Mais_Proximo(lista_vert, i):
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
        vert_inicio = i #random.randrange(0, tamanho)  # Faz ele começar em vertice aleatorio

        k = 0
        index = vert_inicio # vert_inicio # Definindo o vertice inicial

        # Lista das melhores conexoes
        #lst_conexoes_melhor = [] #Adjacente
        lst_conexoes_melhor = [0] * tamanho #[0 for r in range(tamanho)] #Ordenado
        lst_conexoes_int_adj = []  # Adjacente Intero

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

            # Pra fazer o cruzamento depois e p index tem q ser -1 pra n dar erro na lista
            lst_conexoes_int_adj.append(v1.index-1)

            # Adicionando a distancia para a variavel final
            distancia_final += menor_distancia

            # Incrementa K
            k += 1

            # Reiniciando variaveis
            menor_distancia = math.inf

            # o ultimo vertice conectado será o proximo a escolher
            index = menor_vertice
        #print(distancia_final)
        return lst_conexoes_melhor, distancia_final, lst_conexoes_int_adj


# Recebe o cromossomo e faz um print das informações
def Printa_informacoes(cromossomos, tempo):
    for cromossomo in cromossomos:
        print("Vertice Inicio (INT_ADJ):", cromossomo.lstConexaoIntAdj[0])
        print("Custo:",cromossomo.Aptidao)
    print("Tempo (milisegundo)):", tempo, "\n")


# Função que recebe uma lista de conexoes e altera o estado visitado de todos
# os vertices de uma  lista de conexoes ordenada para falso, os vertices da lista
# de conexoes devem estar ligados por referencia.
def Reinicia_Vertices(lista_conexoes):
    for conexao in lista_conexoes:
        conexao.v2.visitado = False


def PosicaoAleatoria(Pai):
    # tamanho da lista do vai ser o limite
    tam = len(Pai)
    # precisa escolher um limite minimo e maximo de posições
    num_posicoes = floor(tam/2)#math.floor(sqrt(tam))
    # num_posicoes = random.randrange(limite, tam-limite)
    # As posições escolhidas com execão da 1 e da lista_pos[1]
    pos_escolhidas = random.sample(range(0, tam), num_posicoes)
    pos_escolhidas.sort()
    return pos_escolhidas


# Execução a função do operador de crusamento OX2, os pais
# DEVEM estar ordenados pela ordem de conexao
def Cruzamento_Ox_2(Pais):
    # Cria os filhos vazios
    Filhos = [[], []]
    for i in range(0, 2):
        n = 1 - i
        pos1 = PosicaoAleatoria(Pais[n])
        Filhos[i] = Pais[i].copy()
        pos2 = [-1] * len(pos1)
        j = 0
        while j < len(pos1):
            pos2[j] = Pais[i].index(Pais[n][pos1[j]-1])
            j += 1
        pos2.sort()
        j = 0
        while j < len(pos2):
            Filhos[i][pos2[j]] = Pais[n][pos1[j]-1]
            j += 1

    return Filhos


# Execução a função do operador de crusamento CX, os pais
# DEVEM estar ordenados pela ordem de conexao
def Cruzamento_Cx(Pai):
    Filho = [[], []]
    for i in range(0, 2):
        n = 1 - i
        Filho[i] = Pai[n].copy()
        index = -1
        while index != 0:
            if index == -1:
                index = 0
            Filho[i][index] = Pai[i][index]
            index = Pai[n].index(Filho[i][index])
    return Filho


def Processar_Cruzamento(Pais, Cruzamento):
    Filho = [[], []]
    Filho_int = [[], []]

    # Cruzamento
    if Cruzamento == "CX":
        Filho_int = Cruzamento_Cx([Pais[0].lstConexaoIntAdj, Pais[1].lstConexaoIntAdj])
    elif Cruzamento == "POS":
        Filho_int = Cruzamento_Pos([Pais[0].lstConexaoIntAdj, Pais[1].lstConexaoIntAdj])
    elif Cruzamento == "OX2":
        Filho_int = Cruzamento_Ox_2([Pais[0].lstConexaoIntAdj, Pais[1].lstConexaoIntAdj])
    else:
        print("ERRO no CRUSAMENTO")

    #for i in range(0, 2):
    #    print("Lista repeticao do filho int", i, ":", [item for item, count in collections.Counter(Filho_int[i]).items() if count > 1])

    # if Cruzamento == "POS":
    #     print(Cruzamento,":",Filho_int)
    # Montagem da estrutura complexa
    tamanho = len(Pais[0].lstConexao)
    for i in range(0,2):
        Filho[i] = cromossomo()
        Filho[i].lstConexaoIntAdj = Filho_int[i]
        Filho[i].lstConexao = [0] * tamanho
        Filho[i].Aptidao = 0

        #Verificar a criação do filho
        vert_antes = Filho_int[i][0]
        for vert in Filho_int[i][1:]:
            conx = conexao()
            conx.v1 = Pais[i].lstConexao[vert_antes].v1
            conx.v2 = Pais[i].lstConexao[vert].v1
            conx.distancia = distancia_euclidiana(conx.v1, conx.v2)
            Filho[i].Aptidao += conx.distancia
            Filho[i].lstConexao[vert_antes] = conx

            vert_antes = vert
        # Fazendo o ultimo voltar para o primeiro
        conx = conexao()
        conx.v1 = Pais[i].lstConexao[vert_antes].v1
        conx.v2 = Pais[i].lstConexao[Filho_int[i][0]].v1
        conx.distancia = distancia_euclidiana(conx.v1, conx.v2)
        Filho[i].Aptidao += conx.distancia
        Filho[i].lstConexao[vert_antes] = conx
    return Filho


def Faz_Mutacao(conexao1, conexao2):
    #print("Conx Mutação:",conexao1, conexao2)
    n1 = conexao1.v1.index-1 #conex1 v1
    n2 = conexao1.v2.index-1 #conex1 v2
    n3 = conexao2.v1.index-1 #conex2 v1
    n4 = conexao2.v2.index-1 #conex2 v2

    Resultado = False
    # nova conexão não pode ser com aresta adjcente
    condicao1 = n1 != n3 and n1 != n4
    condicao2 = n2 != n3 and n2 != n4

    if condicao1 and condicao2:
        Resultado = True
        n1_n4 = distancia_euclidiana(conexao1.v1, conexao2.v2)
        n2_n3 = distancia_euclidiana(conexao1.v2, conexao2.v1)

        conexao1.distancia = n1_n4
        conexao2.distancia = n2_n3
        conexao1.v2, conexao2.v2 = conexao2.v2, conexao1.v2
    return Resultado


def Mutacao(Filhos, Taxa):
    f = []
    for filho in Filhos:
        num_aletorio = random.randrange(1, 100)
        if num_aletorio <= Taxa:
            Sucesso = False
            while not Sucesso:
                conex_int = random.sample(range(0,len(filho.lstConexao)), 2)
                #print("Mutação sorteado:",conex_int)
                c1 = filho.lstConexao[conex_int[0]]
                c2 = filho.lstConexao[conex_int[1]]
                #print("C1 v1:", c1.v1, "- v2:", c1.v2)
                #print("C2 v1:", c2.v1, "- v2:", c2.v2)
                Sucesso = Faz_Mutacao(c1, c2)
            f.append(Sucesso)
        else:
            f.append(False)
    #print(f)
    return f


def Att_Populacao(Filhos, lst_cromossomo, lst_restante):
    lst_apt = [apt.Aptidao for apt in lst_cromossomo]
    old = []
    for i in range(0,2):
        maior = max(lst_apt)
        if maior > Filhos[i].Aptidao:
            # Att lst de cromossomos
            maior_index = lst_apt.index(maior)
            old.append([maior, Filhos[i].Aptidao])
            lst_cromossomo[maior_index] = Filhos[i]
            lst_restante[maior_index] = maior_index
    #for elem in old:
    #    print(elem[0],"->",elem[1])


def Verifica_estagnacao(Filhos, lst_estag, k, Estagnado):
    if len(lst_estag) < 10:
        lst_estag.append(Filhos[0].Aptidao)
        lst_estag.append(Filhos[1].Aptidao)
    else:
        total = 0
        for elem in lst_estag:
            total += elem
        if floor(total / 10) == floor(lst_estag[0]):
            Estagnado = True
        else:
            lst_estag[k] = Filhos[0].Aptidao
            lst_estag[k + 1] = Filhos[1].Aptidao
            if k + 1 == 9:
                k = 0
            else:
                k += 1
    return k, lst_estag, Estagnado


# Recebe a matrix de custo e 2 conexoes, e verfica se mudar as
# conexoes melhora o caminho final, se sim troca a conexao
def mudar_custok2(conexao1, conexao2):
    #print("Conx 2-Opt:",conexao1, conexao2)
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
        custo_melhorado = 0
        for conx in melhor_rota:
            #print("v1:", conx.v1.index, " v2:", conx.v2.index, " distancia:", conx.distancia)
            custo_melhorado += conx.distancia
        #print("Custo Final (k =", k,"):",custo_melhorado)
        return custo_melhorado


def Verifica_Erro(Filhos):
    for var in range(0, 2):
        teste = Filhos[var].lstConexaoIntAdj.copy()
        teste.sort()
        if teste != [x for x in range(0, len(Filhos[var].lstConexaoIntAdj))]:
            print("Filho foi gerado com erro")
        for c in Filhos[var].lstConexao:
            if isinstance(c, int):
                print("Conexao Invalida Filhos", var, ": vertice n:", c)
                print("LstInt:", Filhos[var].lstConexaoIntAdj.sort())


# Testa os casos do diretorio pra construção mais proxima, mais longe
# Melhoramento 2-opt, 3-opt.
def main():
    dict_MS = {
        "1att48.tsp": 33522,
        "2kroA100.tsp": 21282,
        "3tsp225.tsp": 3916,
        "4pr1002.tsp": 259045,
        "5fnl4461.tsp": 182566,
        "6pla7397.tsp": 81438,
        "brd14051.tsp": 46985,
        "d15112.tsp": 1573084,
        "d18512.tsp": 645238,
        "pla33810.tsp": 66048945,
        "pla85900.tsp": 142382641
    }

    directory = 'Arquivos de teste'
    # itera sobre os arquivos
    # daquele diretorio
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # verifica se é arquivo
        if os.path.isfile(f):
            # Abre o arquivo e armazena linha por linha em
            # um vetor de strings sem o \n no final
            print(filename)
            with open(f) as arquivo:
                linhas = [linha.rstrip() for linha in arquivo]

            lista_vertices = []  # Criando a lista de vertices
            for linha in linhas[6:]:
                array_linha = linha.split()
                if array_linha[0] != 'EOF':
                    # Criando vertice e adicionando a lista de vertices
                    vert = vertice()
                    vert.index = int(array_linha[0])
                    vert.posX = float(array_linha[1])
                    vert.posY = float(array_linha[2])
                    vert.visitado = False
                    lista_vertices.append(vert)

            n_populacao = 10 #math.ceil(sqrt(len(lista_vertices)))
            print("\n///// Algoritmos geneticos TESTE:", f[18:], "/////")
            print("///Caso", f[18:],"- Inserção mais proximo///")

            # Gerando população de soluções onde as soluções começam de 0
            # até a raiz do numero de vertices. (pq eu quis)
            start = time.time()
            lst_cromossomos = []
            for i in range(0, n_populacao):
                # Já insere o cromossomo e sua aptidão
                crm = cromossomo()
                crm.lstConexao, crm.Aptidao, crm.lstConexaoIntAdj = Insercao_Mais_Proximo(lista_vertices, i)
                lst_cromossomos.append(crm)

                # Reinicia os vertices das conexoes para gerar uma nova solução(cromossomo)
                Reinicia_Vertices(crm.lstConexao)
            duration = time.time() - start
            print("Duração da criação de crm:", duration)

            lst_cromossomos_reserva = lst_cromossomos.copy()
            for Busca_local in [False, True]:
                for op_cruzamento in ["CX","OX2"]:
                    # Cria variaveis para o grafico
                    x = []
                    y = []
                    fig, ax = plt.subplots()

                    # Lista de elementos
                    lst_restante = [j for j in range(0, n_populacao)]

                    # Tempo decorrido em segundos
                    tempo_decorrido = 0

                    iteracoes = 0 # Contador das iterações
                    k = 0 # Contador da lista de estagnação
                    lst_estag = [] # Lista de estagnação
                    Estagnado = False
                    start = time.time() # Tempo de inicio
                    while (not Estagnado) and (iteracoes < 1000) and (tempo_decorrido < 3600): # Criterio parada

                        # Anota a iteração como X
                        x.append(iteracoes)

                        # Seleção(Roleta) e remoção do restante
                        pais_sorteados = random.sample(lst_restante, 2)
                        #print(pais_sorteados)
                        Pais = [lst_cromossomos[pais_sorteados[0]], lst_cromossomos[pais_sorteados[1]]]

                        # Cruzamento
                        Filhos = Processar_Cruzamento(Pais, op_cruzamento)

                        # Verifica se o filho foi gerado com erro
                        Verifica_Erro(Filhos)

                        # Mutação
                        Mutacao(Filhos, Taxa=15)

                        # Busca Local
                        if Busca_local:
                            Filhos[0].Aptidao = Melhoria_K_Opt(Filhos[0].lstConexao, k = 2)
                            Filhos[1].Aptidao = Melhoria_K_Opt(Filhos[1].lstConexao, k = 2)

                        # Att População
                        Att_Populacao(Filhos, lst_cromossomos, lst_restante)

                        # Aumenta o numero da iteracão
                        iteracoes += 1

                        # Verifica estagnação
                        k, lst_estag, Estagnado = Verifica_estagnacao(Filhos, lst_estag, k, Estagnado)

                        # Anota o menor filho como Y
                        if Filhos[0].Aptidao > Filhos[1].Aptidao:
                            y.append(Filhos[1].Aptidao)
                        else:
                            y.append(Filhos[0].Aptidao)

                        # Atualiza o tempo decorrido
                        tempo_decorrido = time.time() - start
                    end = time.time()
                    tempo = end - start
                    custo = min([x.Aptidao for x in lst_cromossomos])
                    Best = dict_MS[filename]
                    GAP = 100*(custo - Best)/Best
                    print("Best:", Best, "\nCusto Obtido:", custo, "\nTempo:", tempo, "\nNumero Interações:", iteracoes,
                          "\nGAP:", GAP, "\nop_cruzamento:", op_cruzamento, "\nBusca_Local:", Busca_local,"\n")
                    ax.scatter(x, y)
                    for i in range(0, iteracoes):
                        ax.annotate("", (x[i], y[i]))

                    str_busca = "BL_False"
                    if Busca_local:
                        str_busca = "BL_True"

                    plt.savefig("img/"+filename+"_"+op_cruzamento+"_"+str_busca+'.png')
                    lst_cromossomos = lst_cromossomos_reserva.copy()
                    plt.close(fig)




if __name__ == '__main__':
    main()