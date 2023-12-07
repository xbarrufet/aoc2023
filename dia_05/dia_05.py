import os
import sys

filename = "sample.txt"
filename = "input.txt"


def parse_seeds(line_seeds):
    line = line_seeds[7:].strip()
    return list(map(lambda x: int(x),list(filter(lambda x: x.isnumeric(), list(line.split(" "))))))

def process_bloc(bloc):
    res=[]
    tr_map = {}
    for line in bloc:
        vals = list(map(lambda x: int(x), line.split(" ")))
        tr_map["source"]=vals[1]
        tr_map["destination"]=vals[0]
        tr_map["lenght"]=vals[2]
        res.append(tr_map)
        tr_map = {}
    return res

def map_value(value, bloc):
    for map in bloc:
        if value >= map["source"] and value<= map["source"]+map["lenght"]:
            return map["destination"]+value-map["source"]
            break
    return value   

    

def parse_file(filename):
    board = {"seeds":[],"maps":[]}
    lineas = []
    with open(os.path.dirname(__file__) + "/" + filename) as data_file:
        for line in data_file:
            lineas.append(line)
    seeds = parse_seeds(lineas[0])
    board["seeds"]=seeds
    bloc = []
    for t in range(1,len(lineas)):
        if len(lineas[t].strip())>0 and not ":" in lineas[t]:
            bloc.append(lineas[t].strip())
        if len(lineas[t].strip())==0:
            if len(bloc)>0:
                board["maps"].append(process_bloc(bloc))
                bloc=[]
    if len(bloc)>0:
            board["maps"].append(process_bloc(bloc))
    return board

def process_seed(seed, maps):
    for map in maps:
        seed = map_value(seed,map)
    return seed    


def get_mapped_value(value, origin, destination):
    return destination + (value-origin)


def map_value_range(seed_ini, seed_range,map):
    res={"mapped":[],"to map": []}
    for single_map in map:
        if seed_ini >= map["source"] and seed_ini >map["source"]+map["length"]:
             res["to map"].append([seed_ini,seed_range])
        elif seed_ini >= map["source"] and seed_ini+seed_range <=map["source"]+map["length"]:
            res["mapped"].append([get_mapped_value(seed_ini, seed_range, map["destination"]),seed_range])
        elif seed_ini >= map["source"] and seed_ini+seed_range >map["source"]+map["length"]:
            mapped_seed_range = map["length"]-(seed_ini-map["origin"])
            res["mapped"].append([get_mapped_value(seed_ini, seed_range, map["destination"]),mapped_seed_range])
            res["to map"].append([get_mapped_value(seed_ini, seed_range, map["destination"]),mapped_seed_range])


def process_seed_range(seed_ini, range_seed, maps):
    min_total = sys.maxsize
    for seed in range(seed_ini,seed_ini+range_seed):
        for map in maps:
            seed = map_value_range(seed_ini,seed_range,map)
        print("seed:" + str(seed))
        if seed<min_total:
            min_total=seed
    print("min total:" + str(min_total))
    return min_total



def proces_board(board):
    res = []
    for seed in board["seeds"]:
        res.append(process_seed(seed, board["maps"]))
        print(res)
    return res 


board=parse_file(filename)
res = proces_board(board)    
print("Resultat A :" + str(min(res)))
seeds_orig = board["seeds"]
res=[]

for t in range(int(len(seeds_orig)/2)):
    ini_value = seeds_orig[t*2]
    fin_value = seeds_orig[t*2+1]
    res = process_seed_range(ini_value,fin_value,board["maps"])
    
print("Resultat B :" + str(min_total))