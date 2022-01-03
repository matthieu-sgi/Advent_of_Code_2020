import re, os

def get_clean_string(input):
    retour =re.split('-|,|: | |\n',input)
    retour.pop()
    return retour




if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')


    text = file.readlines()
    main_counter = 0

    for i in range(0,len(text)):
        temp = get_clean_string(text[i])

        letter_counter = 0
        for j in range (0,len(temp[3])):
            if(temp[3][j] == temp[2]):
                letter_counter += 1
        if(letter_counter >= int(temp[0]) and letter_counter <= int(temp[1])):
            main_counter+=1
    print(main_counter)
