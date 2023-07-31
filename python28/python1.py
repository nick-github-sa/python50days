
example = 'LovEisEvil'

def index_position(text):
    list = []
    for place, letter in enumerate(text):
        if letter.isupper() == False:
            list.append(place)
    print(list)


index_position(example)