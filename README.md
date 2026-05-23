Editor de Texto

Você foi contratado para desenvolver um editor de texto simples. Esse editor deve manter a posição do cursor e realizar algumas edições básicas. O cursor começa posicionado no início do texto (antes do primeiro caractere) e pode ser posicionado entre quaisquer dois caracteres ou no final do texto (após o último caractere). Você pode assumir que o único caractere em branco utilizado é o espaço.

Os seguintes comandos devem ser implementados:

Mover o cursor para a esquerda: O comando é representado por E N, onde N é um valor inteiro positivo. O cursor deve se mover N posições para a esquerda, a menos que chegue na posição inicial (antes do primeiro caractere). Se ele chegar na posição inicial, ele deve permanecer lá. Mover o cursor para a direita: O comando é representado por D N, onde N é um valor inteiro positivo. O cursor deve se mover N posições para a direita, a menos que chegue na posição final (após o último caractere). Se ele chegar na posição final, ele deve permanecer lá. Apagar um caractere: O comando é representado por x. O caractere logo após o cursor deve ser apagado, e o cursor deve permanecer na mesma posição. Se o cursor estiver na posição final (após o último caractere), o comando x não deve fazer nada. Apagar uma palavra: O comando é representado por X. A palavra na posição atual do cursor deve ser apagada, e o cursor deve ser posicionado antes do caractere seguinte à palavra deletada. O cursor está em uma palavra se ele estiver entre dois caracteres da palavra ou antes do primeiro caractere da palavra. Se o cursor estiver na posição final (após o último caractere) ou antes de um caractere de espaço ou de pontuação (. ou ,), o comando X não deve fazer nada. Você pode assumir que as palavras são precedidas de um espaço, exceto a primeira, e seguidas por um espaço, um ponto ou uma vírgula. Ao deletar uma palavra você deve deletar o espaço que a precede, se ele existir. Inserir um caractere: O comando é representado por i C, onde C é o caractere a ser inserido. O caractere deve ser inserido logo após o cursor, e o cursor deve se mover uma posição para a direita após a inserção. Você pode assumir que não serão inseridos espaços, ou seja, o caractere a ser inserido será sempre um caractere alfanumérico. Inserir uma palavra: O comando é representado por I P, onde P é a palavra a ser inserida. A palavra deve ser inserida na posição atual do cursor, e o cursor deve se mover para a direita após a inserção. Antes da palavra deve ser inserido um espaço, a menos que o cursor esteja na posição inicial (antes do primeiro caractere). Você pode assumir que as palavras a serem inseridas não conterão espaços, ou seja, serão sempre palavras alfanuméricas. A entrada para o programa consistirá de um texto inicial contido em uma única linha seguida por várias linhas, cada uma contendo um comando a ser executado. O último comando será F, indicando que o programa chegou ao fim. O programa deve processar os comandos na ordem em que são recebidos e, ao final, imprimir o texto resultante.

A seguir, exemplos de entradas e saídas esperadas pelo seu programa. Após cada exemplo, há uma representação do resultado da execução de cada comando, onde o caractere | representa a posição do cursor.

Teste 01 Entrada

Oi como vai. D 20 E 1 I panda F Saída

Oi como vai panda. Execução dos comandos: Oi como vai.| Oi como vai|. Oi como vai panda|. Teste 02 Entrada

O lab08 de MC102 e muito dificil. D 27 X I divertido E 29 x F Saída

O lab8 de MC102 e muito divertido. Execução dos comandos: O lab08 de MC102 e muito di|ficil. O lab08 de MC102 e muito|. O lab08 de MC102 e muito divertido|. O lab|08 de MC102 e muito divertido. O lab|8 de MC102 e muito divertido. Teste 03 Entrada

Aguas passadas nao movem moinhos. D 15 x x x x E 2 X I futuras F Saída

Aguas futuras movem moinhos. Execução dos comandos: Aguas passadas |nao movem moinhos. Aguas passadas |ao movem moinhos. Aguas passadas |o movem moinhos. Aguas passadas | movem moinhos. Aguas passadas |movem moinhos. Aguas passada|s movem moinhos. Aguas| movem moinhos. Aguas futuras| movem moinhos. Código Base No arquivo auxiliar lab08.py você irá encontrar um código base para dar início ao processo de elaboração deste laboratório.
