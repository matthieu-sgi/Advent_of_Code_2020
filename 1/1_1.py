


if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/1/input.txt','r')

    text = file.readlines()
    
    final1 = 0
    final2 = 0
    for i in range(0, len(text)):
        temp = text[i].split('\n')[0]
        for j in range(i+1, len(text)):
            temp_2 = text[j].split('\n')[0]
            if(int(temp) + int(temp_2) == 2020):
                final1 = int(temp)
                final2 = int(temp_2)
                break

    
    print(str(final1) + ' '+ str(final2))
    print(final1 * final2)
