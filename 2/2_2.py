
import re

def get_clean_string(input):
    retour =re.split('-|,|: | |\n',input)
    retour.pop()
    return retour




if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/2/input.txt','r')

    text = file.readlines()
    main_counter = 0

    for i in range(0,len(text)):
        temp = get_clean_string(text[i])

        pos_1 = int(temp[0]) -1
        pos_2 = int(temp[1])-1  
        if(temp[3][pos_1] == temp[2] and temp[3][pos_2] != temp[2] or temp[3][pos_1]!=temp[2] and temp[3][pos_2] == temp[2]):
            main_counter+=1
    print(main_counter)
