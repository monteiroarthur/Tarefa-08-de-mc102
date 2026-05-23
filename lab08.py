###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Editor de Texto
# Nome: Arthur Miguel Monteiro
# RA: 285519
###################################################

txt_ini = str(input()) #texto inicial
lista_txt = list(txt_ini)
pos_cursor = 0 #posição do cursor setada na posição inicial

while True:
    i = 0
    lista_cmd = input().split() #lista com os comandos do editor

    #====================enterromper operação====================
    if lista_cmd[0] == "F":
        break
    #====================enterromper operação====================
    
    #========================movimentação========================
    if lista_cmd[0] == "D":

        if pos_cursor + int(lista_cmd[1]) > len(lista_txt):
            pos_cursor = len(lista_txt)
        
        elif pos_cursor + int(lista_cmd[1]) <= len(lista_txt):
            pos_cursor += int(lista_cmd[1])

        #print(lista_txt[pos_cursor])
        #print(pos_cursor)

    if lista_cmd[0] == "E":
        if pos_cursor - int(lista_cmd[1]) < 0:
            pos_cursor = 0
        
        elif pos_cursor - int(lista_cmd[1]) >= 0:
            pos_cursor -= int(lista_cmd[1])

        #print(lista_txt[pos_cursor])
        #print(pos_cursor)
    #========================movimentação========================
    
    #=======================del caractere========================
    if lista_cmd[0] == "x":
        if pos_cursor == len(lista_txt):
            continue
        else:
            lista_txt.pop(pos_cursor)

        #print(lista_txt)
    #=======================del caractere========================
    
    #========================del palavra=========================
    if lista_cmd[0] == "X":
        if pos_cursor == len(lista_txt) or lista_txt[pos_cursor] in [" ", ".", ","]:
            continue
            
        else:           
            ini_apag = pos_cursor

            while ini_apag > 0 and lista_txt[ini_apag] not in [" ", ".", ","]:
                ini_apag -= 1

            pos_cursor = ini_apag
            
            while lista_txt[pos_cursor + 1] not in [" ", ".", ","]:
                lista_txt.pop(pos_cursor)
            
            lista_txt.pop(pos_cursor)
            
            #print(lista_txt)
    #========================del palavra=========================
    #=====================inserir caractere======================
    if lista_cmd[0] == "i":
        lista_txt.insert(pos_cursor, lista_cmd[1])
        pos_cursor += 1

        #print(lista_txt)
    #=====================inserir caractere======================

    #======================inserir palavra=======================
    if lista_cmd[0] == "I":
        palavra = list(lista_cmd[1])
        if pos_cursor == 0:

            for i in range(len(palavra)):
                lista_txt.insert(pos_cursor,palavra[i])
                pos_cursor += 1
        else:
            lista_txt.insert(pos_cursor, " ")
            pos_cursor += 1

            for i in range(len(palavra)):
                lista_txt.insert(pos_cursor,palavra[i])
                pos_cursor += 1
            
            #print(lista_txt)
    #======================inserir palavra=======================

saida = "".join(lista_txt)
print(saida)