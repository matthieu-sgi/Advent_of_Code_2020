import os



def clear_tab(text):
    clear_tab_result = []
    a_pass = ""
    for line in range (0, len(text)):
        
        if len(text[line]) >1:
            
            a_pass += text[line]
        else:
            clear_tab_result.append(a_pass)
            a_pass = ""
        
    for i in range(0, len(clear_tab_result)):
        clear_tab_result[i]= clear_tab_result[i].split('\n')
        clear_tab_result[i].pop()
    return clear_tab_result


def line_counter(grp):
    temp = str(grp[0])
    temp_2=""
    for i in range(1, len(grp)):
        for j in range(0, len(temp)):
            index = grp[i].find(temp[j])
            if( index != -1 ):
                temp_2+=temp[j]
        temp = temp_2
        temp_2=""
    # print(len(grp))
    # print(temp)
    return len(temp)

if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')


    text = file.readlines()
    # print(clear_tab(text))
    main_counter = 0
    cleared_text = clear_tab(text)
    # print(cleared_text)
    # print(line_counter(cleared_text[len(cleared_text)-1]))

    for i in range(0, len(cleared_text)):
        main_counter += int(line_counter(cleared_text[i]))

    print(main_counter)
