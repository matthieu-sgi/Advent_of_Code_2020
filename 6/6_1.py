import os


def clear_tab(text):
    clear_tab_result = []
    a_pass = ""
    for line in range (0, len(text)):
        
        if len(text[line]) >1:
            
            a_pass += text[line].split('\n')[0]
        else:
            clear_tab_result.append(a_pass)
            a_pass = ""
    return clear_tab_result


def line_counter(line):
    temp = ""

    for i in range(0, len(line)):
        if(temp.find(line[i]) ==-1 and line[i] != ' ' ):
            temp += line[i]
        
    # print(temp)
    return len(temp)

if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')


    text = file.readlines()
    # print(clear_tab(text))
    main_counter = 0
    cleared_text = clear_tab(text)
    print(cleared_text)
    # print(line_counter(cleared_text[len(cleared_text)-1]))

    for i in range(0, len(cleared_text)):
        main_counter += int(line_counter(cleared_text[i]))

    print(main_counter)
