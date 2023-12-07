import os
from collections import Counter


filename='sample.txt' #--> 1369
filename='input.txt'


def translate_hand_ranks(hand,hand_counter):
    if hand_counter[0]==5:
        return 7
    elif hand_counter[0]==4:
        return 6
    elif hand_counter[0]==3 and hand_counter[1]==2 :
        return 5
    elif hand_counter[0]==3 and hand_counter[1]!=2 :
        return 4
    elif hand_counter[0]==2 and hand_counter[1]==2:
        return 3
    if hand_counter[0] ==2 and hand_counter[1]!=2:
          return 2
    else:
        return 1
      
    
def counter(hand):
    res={}
    if hand == 'JJJJJ':
        return 7
    else:
        joker_count = Counter(hand)["J"]
        print(hand + " " + str(joker_count))
        hand = hand.replace("J","")
        for letter in hand:
            if letter not in res:
                res[letter] = 0
            res[letter] += 1
        res =  sorted(list(res.values ()   ),reverse=True)   
        res[0]=res[0]+joker_count 
        return translate_hand_ranks(hand,res)




cards = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2,'2':1}


def parse_file(filename):
    board = []
    lineas = []
    with open(os.path.dirname(__file__) + "/" + filename) as data_file:
        for line in data_file:
            board.append([line[:5],line[6:].strip(),counter(line[:5]),line[0],line[1],line[2],line[3],line[4]])
    return board

board = parse_file(filename)
board = sorted(board, key=lambda x: (x[2], cards[x[3]],cards[x[4]],cards[x[5]],cards[x[6]],cards[x[7]]),reverse=True)
board.reverse()

for t in range(len(board)):
    print(board[t][0] + ":" +str(t+ 1 ))

for t in range(len(board)):
    board[t].append(t+1)
res=0
for t in range(len(board)):
   res = res + int(board[t][1])*(t+1) 
print(res)


#1343

#246025229
