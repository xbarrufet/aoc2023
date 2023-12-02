import re
import os.path


#FILENAME = "/sample.txt"
#FILENAME = "/sample2.txt"
FILENAME = "/input.txt"
acum = 0


digit_map ={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}


def finddigit(linia, digit, current):
    pos = linia.find(digit)
    if(pos>=0 and pos<=current[1]):
        current[0]=digit
        current[1]=pos
    return current

def replace_digits(linia):
    res = finddigit(linia,"zero",["",99])
    res = finddigit(linia,"one",res)
    res = finddigit(linia,"two",res)
    res = finddigit(linia,"three",res)
    res = finddigit(linia,"four",res)
    res = finddigit(linia,"five",res)
    res = finddigit(linia,"six",res)
    res = finddigit(linia,"seven",res)
    res = finddigit(linia,"eight",res)
    res = finddigit(linia,"nine",res)
    if res[1]<99:
        linia = linia.replace(res[0],digit_map[res[0]])
        return replace_digits(linia)
    else:
        return linia
    

def extraurenumeros(linia):
    linia=re.sub("[^0-9]", "", linia)
    num_linia = linia[0] + linia[-1]
    return int(num_linia)

file1 = open(os.path.dirname(__file__) + FILENAME)
data = file1.readlines()

new_data = [[x if (x := "".join([v for k, v in digit_map.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))] for line in data]

acum=0
acum_meu=0
pos_llista =0
for linia in new_data:
   # print(linia)
    digits = [int(i) for i in linia if i.isdigit()]
    dig1=digits[0] * 10 + digits[-1]
    acum += digits[0] * 10 + digits[-1]
    linia_x = replace_digits(data[pos_llista])
    pos_llista+=1
    dig2=extraurenumeros(linia_x)
    acum_meu = acum_meu + extraurenumeros(linia_x)
    if dig1 != dig2:
        print(str(dig1) + " " + str(linia))
        print(str(dig2) + " " + linia_x)
        print(pos_llista)
print("num:" + str(acum))
print("num:" + str(acum_meu))




