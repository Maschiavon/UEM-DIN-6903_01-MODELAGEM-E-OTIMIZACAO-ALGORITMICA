Para o bom funcionamento deste programa é necessario possuir python3
instaladado no computador.

Este programa constrói e melhora grafos atraves dos arquivos da pasta "Arquivos de teste",
que possuem a formatação a seguir:

NAME : Teste 1
COMMENT :
TYPE : TSP
DIMENSION: 4
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
  1 0 0
  2 0 100
  3 100 100
  4 100 0
EOF

Os arquivos são lidos em ordem alfanumerica, os nomes dos arquvos de testes foram alterados
com o intuito da execução ser feita em ordem crescente de acordo com o tamanho do problema

Para executar o arquivo abra um terminal no diretorio do arquivo main.py e digite o
comando "python3 main.py".