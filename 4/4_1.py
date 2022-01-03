import os 

def clear_tab(text):
    clear_tab_result = []
    a_pass = ""
    for line in range (0, len(text)):
        
        if len(text[line]) >1:
            
            a_pass += text[line].split('\n')[0] + ' '
        else:
            clear_tab_result.append(a_pass)
            a_pass = ""
    return clear_tab_result

def id_verify(line):
    
        temp = line.split(':')
        temp.pop()
        if(len(temp) >= 7 and len(temp)<=8):
            for i in range(0, len(temp)):
                buff = temp[i].split(' ')

                temp[i] = buff[len(buff) - 1]

            return verify_case(temp)
        else:
            return False
    # for i in range (0,len(line) ):
        
def verify_case(cleared):

    if('iyr' in cleared  and 'ecl' in cleared and 'hgt' in cleared and 'pid' in cleared and 'byr' in  cleared
        and 'hcl' in cleared and 'eyr' in cleared):
        return True
    else :
        return False
   



if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),'input.txt'),'r')


    text = file.readlines()
    counter = 0
    cleared = clear_tab(text)
    for i in range (0, len(cleared)):
        if(id_verify(cleared[i]) == True):
            counter += 1
    print(counter)
        

   
    
