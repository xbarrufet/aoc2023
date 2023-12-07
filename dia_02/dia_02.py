




import os


MAX_BALL = {"red":12,"blue":14,"green":13}


def get_id_from_line(line):
    line= line.replace("Game ","")
    line= line.replace(" :","")
    return int(line)


def parse_bola(linia):
    color =""
    if linia.find('red')>=0:
        color="red"
    elif linia.find('blue')>=0:
        color="blue"
    else :
        color="green"    
    return [color,int(linia.replace(color,"").strip())]


def parse_tirada(tirada):
    return list(map(parse_bola,tirada.split(",")))
    
       
def parse_game(line):
    resultat = []
    resultat = list(map(parse_tirada,line.split(";")))
    return resultat
    

def parse_line(line): 
    line_content = line.split(":",1)
    id = get_id_from_line(line_content[0])
    result = parse_game(line_content[1].strip())
    return {"id":id, "tirades":result}


def validar_bola(bola): 
    if bola[1] > MAX_BALL[bola[0]]:
        return 1
    else:
        return 0

def validar_tirada(tirada):
    return sum(validar_bola(bola) for bola in tirada)
    
def process_tirades_A(tirades):
    return sum(validar_tirada(tirada) for tirada in tirades)


   
def process_tirades_B(tirades):
    max_tirada = {"red":0,"blue":0,"green":0}
    for tirada in tirades:
        for bola in tirada:
            if bola[1]>max_tirada[bola[0]]:
                max_tirada[bola[0]]=bola[1]
    return max_tirada['red']*max_tirada['green']*max_tirada['blue']


def process_file(filename):
    games = []
    acum =0
    with open(os.path.dirname(__file__) + "/" + filename) as data_file:
        for line in data_file:
            games.append(parse_line(line))
    for game in games:
        res = process_tirades_A(game["tirades"])
        if res==0:
            acum = acum +game["id"]

    print("resultat A:" +  str(acum))
    #part B
    acum = 0
    for game in games:
        res = process_tirades_B(game["tirades"])
        acum = acum +res
    print("resultat B:" +  str(acum))


#process_file("sample.txt")
process_file("input.txt")

