

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
    
        temp = line.split(' ')
        new_temp = []
        temp.pop()

        for i in range(0, len(temp)):
            buff = temp[i].split(':')

            
            new_temp.append(buff)
        return verify_case(new_temp)
        

#region for switch cases

def iyr_check(input):
   
    return  True if int(input)>=2010 and int(input)<=2020 else False

def byr_check(input):
    
    return  True if int(input)>=1920 and int(input)<=2002 else False

def eyr_check(input):
    
    return  True if int(input)>=2020 and int(input)<=2030 else False
    
        

def hgt_check(input):
    
    unit = input[len(input)-2] + input[len(input)-1]
    if(unit == 'cm' and len(input)==5):
        temp = input[0] + input[1] + input[2]
        return  True if int(temp)>=150 and int(temp)<=193 else False
    elif(unit == 'in' and len(input)== 4):
        temp = input[0] + input[1]
        return  True if int(temp)>=59 and int(temp)<=76 else False
    else :
        return False

def hcl_check(input):
    if(input[0] !='#' or len(input) != 7):
        return False
    temp = input.replace('#','')

    try:
        temp = int(temp,16)
        return True
    except ValueError:
        return False

def ecl_check(input):
    return True if input == 'amb' or input == 'blu' or input == 'brn' or input == 'gry' or input == 'grn' or input == 'hzl' or input == 'oth' else False

def pid_check(input):
    return True if len(input) == 9  else False
#endregion

def verify_case(cleared):

    res =True
    counter = 0
    for i in range(0,len(cleared)):
        if(cleared[i][0] =='iyr'):
            res =iyr_check(cleared[i][1])
            counter+=1
            # print(res)
        elif(cleared[i][0] == 'ecl'):
            res =ecl_check(cleared[i][1])
            counter+=1
            # print(res)
        elif(cleared[i][0] == 'hgt'):
            counter+=1
            res =hgt_check(cleared[i][1])
            # print(res)
        elif(cleared[i][0] == 'pid'):
            counter+=1
            res =pid_check(cleared[i][1])
            # print(res)
        elif(cleared[i][0] == 'byr'):
            counter+=1
            res =byr_check(cleared[i][1])
            # print(res)
        elif(cleared[i][0]=='hcl'):
            counter+=1
            res= hcl_check(cleared[i][1])
            # print(res)
        elif(cleared[i][0]=='eyr'):
            counter+=1
            res =eyr_check(cleared[i][1])
            # print(res)

        
        if res == False  :
            return False
    return res if counter ==7 else False

   



if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/4/input.txt','r')

    text = file.readlines()
    counter = 0
    cleared = clear_tab(text)
    # print(cleared)
    
    print(id_verify(cleared[0]))
    for i in range (0, len(cleared)):
        if(id_verify(cleared[i]) == True):
            counter += 1
    print(counter)
    