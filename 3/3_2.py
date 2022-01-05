import os

def clear_tab(text):
    for i in range(0, len(text)):
        text[i] = text[i].split('\n')[0]



def counting_trees_slope1(text):
    x=1
    tree_counter = 0
    for i in range(1,len(text)):
        if(x >= len(text[i])):
            x = x % len(text[i])
        
        if(text[i][x] == '#') :
            tree_counter += 1
       
        x+=1
        
    return tree_counter

def counting_trees_slope2(text):
    x=3
    tree_counter = 0
    for i in range(1,len(text)):
        if(x >= len(text[i])):
            x = x % len(text[i])

        
        if(text[i][x] == '#') :
            tree_counter += 1

        x+=3
        
    return tree_counter

def counting_trees_slope3(text):
    x=5
    tree_counter = 0

    for i in range(1,len(text)):
        if(x >= len(text[i])):
            x = x % len(text[i])

        
        if(text[i][x] == '#') :
            tree_counter += 1
        
        x+=5
        
    return tree_counter


def counting_trees_slope4(text):
    x=7
    tree_counter = 0
    for i in range(1,len(text)):
        if(x >= len(text[i])):
            x = x % len(text[i])
        
        if(text[i][x] == '#') :
            tree_counter += 1
        
        x+=7
        
    return tree_counter

def counting_trees_slope5(text):
    x=1
    tree_counter = 0
    for i in range(2,len(text),2):
        if(x >= len(text[i])):
            x = x % len(text[i])
        
        if(text[i][x] == '#') :
            tree_counter += 1
        
        x+=1
        
    return tree_counter



if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')

    text = file.readlines()

    clear_tab(text)

   


    print(counting_trees_slope1(text) * counting_trees_slope2(text) * counting_trees_slope3(text) * counting_trees_slope4(text) * counting_trees_slope5(text))
    
