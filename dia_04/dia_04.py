import os


filename = 'sample.txt'
filename = 'input.txt'


#BOARD_SIZE=10
NUM_CARDS=10
NUM_CARDS=209


def get_points(values, winings):
    res = sum(map(lambda x: 1 if x in winings else 0,values ))
    if res>0:
        return pow(2,res-1)
    else:
        return 0
def get_points_B(values, winings):
    res = sum(map(lambda x: 1 if x in winings else 0,values ))
    return res


def add_cards_to_tickers(cards, tickers):
    for card in cards:
        tickers[card]=tickers[card]+1
    return tickers

def get_priced_scratchcard(values, prices):
    res=[]
    for value in values:
        res.extend(range(value+1,min(NUM_CARDS,value + prices[value]+1)))
    print("---------------")
    print(values)
    print(res)    
    return res

def parse_input(filename):
    values = []
    winings = []
    with open(os.path.dirname(__file__) + "/" + filename) as data_file:
        for line in data_file:

            lines = line[8:].strip().split("|")
            winings.append(list(map(lambda x: int(x),list(filter(lambda x: x.isnumeric(), list(lines[0].split(" ")))))))
            values.append(list(map(lambda x: int(x),list(filter(lambda x: x.isnumeric(), list(lines[1].split(" ")))))))
    return {"values":values, "winings":winings}

board = parse_input(filename)
points = []
#--- A---------------------
for t in range(0,len(board["values"])):
    points.append(get_points(board["values"][t], board["winings"][t]))
print("resultat A:" +str(sum(points)))

#--- B---------------------
tickers =  [1 for i in range(len(board["winings"]))] 
prices =   [0 for i in range(len(board["winings"]))] 
current_prices = []

for t in range(0,len(board["values"])):
    price = get_points_B(board["values"][t], board["winings"][t])
    prices[t] = price
    if price>0:
        current_prices.append(t)
while len(current_prices)>0:
    current_prices=get_priced_scratchcard(current_prices,prices)
    tickers=add_cards_to_tickers(current_prices,tickers)
print(tickers)
print("resultat B:" +str(sum(tickers)))


