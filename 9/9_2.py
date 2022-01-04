import os

def clear_tab(text):
    for i in range(0, len(text)):
        text[i] = int(text[i].split('\n')[0])


def res(text):

    for i in range(0, len(text)):
        while



if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')

    text = file.readlines()
    clear_tab(text)
    # print(text)
    # print(res(text))
    print(res(text))