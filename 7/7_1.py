############################ NOT WORKING #################################
def clear_tab(text):
    clear_tab_result = []
    for line in text:
        clear_tab_result.append(line.split(' contain '))
    return clear_tab_result

def count(line):

    return True if line.find("shiny gold") != -1 else False

if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/7/input.txt','r')

    text = file.readlines()
    clear_tab_result =  clear_tab(text)
    # print(clear_tab_result)
    counter = 0
    for line in clear_tab_result:
        if (count(line[1]) ==True):
            counter += 1 
    print(counter)



