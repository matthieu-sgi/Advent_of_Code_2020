
import os

def clear_tab(text):
    for i in range(0, len(text)):
        text[i] = int(text[i].split('\n')[0])

def res(text):

    for i in range(25, len(text)):
        toggled = False
        for j in range(1,26):
            for k in range(j+1,26):
                
                # print(text[i-j] + text[i-k])
                if text[i-j] + text[i-k] == text[i] :
                    toggled = True
                    break
            if toggled:
                break
        if toggled == False:
            print(i)
            return text[i]
            

if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')

    text = file.readlines()
    clear_tab(text)
    # print(text)
    # print(res(text))
    print(res(text))