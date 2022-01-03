def clear_tab(text):
    return_tab = []

    for line in text:
        temp = line.split(' ')
        temp[1] = temp[1].split('\n')[0]
        temp.append(False)
        return_tab.append(temp)
        
    return return_tab

def sum_acc(text):
    exit =False
    
    counter = 0
    acc = 0
    while not exit:
        if counter != len(text) - 1:
            inst = text[counter][0]
            amount = int(text[counter][1])
            if(inst == 'acc' and text[counter][2] !=True ):
                
                acc += amount
                text[counter][2] = True
                counter +=1
            elif(inst == 'nop' and text[counter][2] !=True):
                text[counter][2] = True
                counter +=1
            elif(inst == 'jmp' and text[counter][2] !=True):
                text[counter][2] = True
                counter += amount
            elif(text[counter][2] == True):
                exit = True
        else :
            exit = True
    return acc


if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/8/input.txt','r')

    text = file.readlines()
    text = clear_tab(text)
    # sum_acc(text)
    # print(text)
    print(sum_acc(text))
