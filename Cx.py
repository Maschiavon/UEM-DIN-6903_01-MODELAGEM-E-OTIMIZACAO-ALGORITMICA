import random


def PosicaoAleatoria(Pai):
    # tamanho da lista do vai ser o limite
    tam = len(Pai)
    # precisa escolher no minimo 3 posições e no maximo tam
    num_posicoes = random.randrange(3, tam)
    # As posições escolhidas
    pos_escolhidas = random.sample(range(0, tam), num_posicoes)
    pos_escolhidas.sort()
    return pos_escolhidas


def Pos(Pai):
    Filho = [[], []]
    Filho[0] = Pai[0].copy()
    Filho[1] = Pai[1].copy()

    posicoes = [1, 2, 6] #PosicaoAleatoria(Pai[0])
    for pos in posicoes:
        Filho[0][pos] = Pai[1][pos]
        Filho[0][Pai[0].index(Filho[0][pos])] = Pai[0][pos]
        Filho[1][pos] = Pai[0][pos]
        Filho[1][Pai[1].index(Filho[1][pos])] = Pai[1][pos]

    return Filho


def Cx(Pai):
    Filho = [[], []]
    for i in range(0, 2):
        print("i:", i)
        n = 1 - i
        print("n:", n)
        Filho[i] = Pai[n].copy()
        index = -1

        while index != 0:
            if index == -1:
                index = 0

            Filho[i][index] = Pai[i][index]
            index = Pai[n].index(Filho[i][index])
    return Filho


# Função que executa o operador de crusamento OX2
def Ox_2(Pais):
    # Cria os filhos vazios
    Filhos = [[], []]

    # Pega as posições aleatorias
    # os exemplos são pos_p1 = [2, 5, 7] e pos_p2 = [1, 3, 8]
    posP1 = [1, 4, 6] #PosicaoAleatoria(Pais[0])
    posP2 = [0, 2, 7] #PosicaoAleatoria(Pais[1])
    print("posP1:", posP1, "e posP2:", posP2)

    # Pegando os numeros que estão nas respectivas posições
    numP1 = []
    numP2 = []
    for i in posP1:
        numP1.append(Pais[0][i])
    for j in posP2:
        numP2.append(Pais[1][j])
    print("numP1:", numP1, "e numP2:", numP2)

    # Achando esses numeros nas posições do outro pai
    numP1_noP2 = []
    numP2_noP1 = []
    for n in numP1:
        numP1_noP2.append(Pais[1].index(n))
    for m in numP2:
        numP2_noP1.append(Pais[0].index(m))
    numP1_noP2.sort()
    numP2_noP1.sort()

    print("numP1_noP2:", numP1_noP2, "e numP2_noP1:", numP2_noP1)

    #Preenchendo solução
    Filhos[0] = Pais[0].copy()
    Filhos[1] = Pais[1].copy()

    # Remove do Filho 1 as posições dos elementos escolhidos do pai 2 que estão no pai 1
    for pos in numP2_noP1:
        Filhos[0][pos] = -1
    print("f1:", Filhos[0])
    for pos1 in numP2_noP1:
        for num in Pais[1]:
            if num not in Filhos[0]:
                Filhos[0][pos1] = num
                break

    # Remove do Filho 2 as posições dos elementos escolhidos do pai 1 que estão no pai 2
    for pos2 in numP1_noP2:
        Filhos[1][pos2] = -1
    print("f2:", Filhos[1])
    for pos3 in numP1_noP2:
        for num1 in Pais[0]:
            if num1 not in Filhos[1]:
                Filhos[1][pos3] = num1
                break
    return Filhos


def Ox_2v2(Pais):
    # Cria os filhos vazios
    Filhos = [[], []]

    for i in range(0, 2):
        n = 1 - i

        if n == 1:
            pos1 = [1, 3, 8]
        else:
            pos1 = [2, 5, 7]
        #pos1 = PosicaoAleatoria(Pais[n])

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



def main():
    # Ex CX
    # p1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # p2 = [2, 4, 6, 8, 7, 5, 3, 1]
    # print("///CX///\np1:", p1, "\np2:", p2)
    # Filhos = Cx([p1, p2])
    # print("f1:", Filhos[0])
    # print("f2:", Filhos[1])
    #
    # # Ex POS
    # pai2 = [3, 6, 1, 4, 2, 8, 7, 5]
    # pai3 = [1, 2, 4, 5, 3]
    # pai4 = [5, 3, 4, 1, 2]
    # print("///POS///\np1:", p1, "\np2:", pai2)
    # Filhos1 = Pos([p1, pai2])
    # print("f1:", Filhos1[0])
    # print("f2:", Filhos1[1])

    # Ex Ox2
    p3 = [6, 3, 5, 1, 2, 4, 8, 7]
    p4 = [8, 5, 2, 4, 3, 1, 7, 6]
    print("\n///Ox_2///")
    Filhos2 = Ox_2v2([p3, p4])
    print("f1:", Filhos2[0])
    print("f2:", Filhos2[1])


if __name__ == '__main__':
    main()
