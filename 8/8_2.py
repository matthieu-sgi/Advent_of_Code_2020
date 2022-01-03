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
    old_inst =""
    old_counter = 0
    while not exit:
        if counter != len(text) - 1:
            inst = text[counter][0]
            amount = int(text[counter][1])
            if(inst == 'acc' and text[counter][2] !=True ):
                old_inst = inst
                old_counter = counter
                acc += amount
                text[counter][2] = True
                counter +=1
            elif(inst == 'nop' and text[counter][2] !=True):
                old_inst = inst
                old_counter = counter
                text[counter][2] = True
                counter +=1
            elif(inst == 'jmp' and text[counter][2] !=True):
                old_inst = inst
                old_counter = counter
                text[counter][2] = True
                counter += amount
            elif(text[counter][2] == True):
                text[old_counter][0] = 'jmp' if old_inst == 'nop' else 'nop'

                exit = True
        else :
            exit = True
    acc = 0
    exit = False
    counter =0
    while not exit:
        if counter != len(text) - 1:
            inst = text[counter][0]
            amount = int(text[counter][1])
            if(inst == 'acc' and text[counter][2] !=True ):
                old_inst = inst
                old_counter = counter
                acc += amount
                text[counter][2] = True
                counter +=1
            elif(inst == 'nop' and text[counter][2] !=True):
                old_inst = inst
                old_counter = counter
                text[counter][2] = True
                counter +=1
            elif(inst == 'jmp' and text[counter][2] !=True):
                old_inst = inst
                old_counter = counter
                text[counter][2] = True
                counter += amount
            elif(text[counter][2] == True):

                exit = True
        else :
            exit = True

    # print(old_inst)
    return acc


if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/8/input.txt','r')

    text = file.readlines()
    text = clear_tab(text)
    print(sum_acc(text))
    # print(text)
    # print(text)
