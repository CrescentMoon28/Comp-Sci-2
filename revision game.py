import csv, random
cards = []
class Card():
    def __init__(self, keyword, definition):
        self.keyword = keyword
        self.definition = definition
        cards.append(self)

        
def get_data():
    values = []
    with open('word.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
            list_def = []
            for row in column:#extracts the cells that have something in
                if row != '':
                    list_def.append(row)
            values.append(list_def)
    return values

words = get_data()
for item in words:
    Card(item[0], item[1])
print(cards)

def pick_word(module="start"):
    if module == "start":
        num = random.randint(0,len(cards)-1)
        print(cards[num].definition)
        keyword = cards[num].keyword
        keyword_list = [keyword]
        for i in range(3):
            while keyword in keyword_list:
                keyword = cards[random.randint(0,len(cards)-1)].keyword
            keyword_list.append(keyword)
    for word in keyword_list:
        print(word)
    answer = input("Enter what you think: ")
    if answer == keyword_list[0]:
        print("Correct")
    

