Time =[7,  15,   30]
Distance =[ 9,  40,  200]
 

TimeB = 59688274
DistanceB = 543102016641022


def calculate_possible_distances(milliseconds,distance ):
    res = []
    res_p = 1
    for t in range(milliseconds):
        _distance  =( milliseconds-t)*t
        if _distance>distance:
            res.append(t)
    return res


def calculate_possible_distances_B(milliseconds,distance ):
    
    res=0
    fora = 0
    for t in range(milliseconds):
        _distance  =( milliseconds-t)*t
        if _distance>distance:
            res=res+1
            if res==1:
                print("primer:" +str(t) + "-->" + str(_distance) + "/" +  str(_distance))
        else:
            if res>0 and fora==0:
                print("fotra:" +str(t) + "-->" + str(_distance) + "/" +  str(_distance))
                fora=1
    return res


prod=1
for t in range(len(Time)):
    res = calculate_possible_distances(Time[t],Distance[t])
    print(str(len(res)) + ":" + str(res))
    prod=prod*len(res)
print(prod)

prod=1

res = calculate_possible_distances_B(TimeB,DistanceB)
print(res)

#36642753 too low
