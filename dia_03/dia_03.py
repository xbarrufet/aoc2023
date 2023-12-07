import os

#sample1: --> 4361

#filename = '/sample.txt'
filename = '/input.txt'


#BOARD_SIZE=10
BOARD_SIZE=140

def parse_taulell(filename):
    board = []
    with open(os.path.dirname(__file__) + "/" + filename) as data_file:
        for line in data_file:
            board.append(line) 
    return board

def get_borders(fila, ini, fin):
    res = []
    #ranges
    
    if ini>0:
        ini=ini-1
        res.append([fila,ini])
    if  fin<BOARD_SIZE-1:
        fin=fin+1
        res.append([fila,fin])
    for t in range(ini,fin+1):
        if fila>0:
                res.append([fila-1,t])
        if fila<BOARD_SIZE-1:
                res.append([fila+1,t])
    return res    

def get_numbers_surronds(board):
    resultat = []
    pos_fila=0
    for fila in board:
        pos_columna = 0
        numero = 0
        ini = -1
        fin = -1
        for cela in fila:
            if cela.isnumeric():
               numero= numero*10 + int(cela)
               if ini<0:
                   ini=pos_columna
               fin = pos_columna    
            else:
                if ini>=0:
                    resultat.append({"numero":int(numero), "borders":get_borders(pos_fila,ini,fin)})
                    numero = 0
                    ini = -1
                    fin = -1
            pos_columna+=1
        if ini>0:
            resultat.append({"numero":int(numero), "borders":get_borders(fila,ini,fin)})
        pos_fila+=1
    return resultat




def count_codes(board,borders):
    resultat = 0
    for border in borders:
        cela = board[border[0]][border[1]]
        if not cela.isnumeric() and not cela=='.':
            resultat +=1
    return resultat           



def locate_codes(board):
    res = []
    for fila in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[fila][col]=='*':
                res.append([fila,col])
    return res
    
def number_of_apperances(cela,numeros):
    res = list(filter(lambda numero: cela in numero["borders"],numeros))
    return res

resultat = 0
board = parse_taulell(filename)
numeros = get_numbers_surronds(board)
for numero in numeros:
    codes = count_codes(board, numero["borders"])
    if codes>0:
        resultat=resultat + numero["numero"]
    else:
        print( numero["numero"])
print("PART A resultat es " + str(resultat))


resultat = 0
codes = locate_codes(board)
for code in codes:
    list_res = number_of_apperances(code,numeros)
    
    if len(list_res)==2:
        gear = list_res[0]["numero"]*list_res[1]["numero"]
        resultat = resultat + gear
        print("gear:" + str(gear)+ "-->" + str(resultat))
print("PART B resultat es " + str(resultat))