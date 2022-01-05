import os

def clear_tab(text):
    for i in range(0, len(text)):
        text[i] = text[i].split('\n')[0]



def counting_trees(text):
    x=3
    tree_counter = 0
    for i in range(1,len(text)):
        if(x >= len(text[i])):
            x = x % len(text[i])
        
        if(text[i][x] == '#') :
            tree_counter += 1
        
        x+=3
        
    return tree_counter



if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')

    text = file.readlines()

    clear_tab(text)

    print(counting_trees(text))
    
