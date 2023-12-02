




def get_id_from_line(line):
    line= line.replace("Game ","")
    line= line.replace(" :","")
    return int(line)


def process_game(line);
    

def process_line(line): 
    line_content = line.split(":",1)
    id = get_id_from_line(line_content[0])
    print(id)

def process_file(filename):
    with open(filename) as data_file:
        n = 1
        for line in data_file:
            process_line(line)
            

process_file("sample.txt")

