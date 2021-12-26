
def max(text):
    max = 0
    for line in text:
        upper_r = 127
        lower_r=0
        upper_c=7
        lower_c= 0
        

        for i in range(0, len(line) -4):
            if(line[i] == 'B'):
                lower_r = int((upper_r+lower_r)/2) + (upper_r+lower_r)%2
            elif(line[i] == 'F'):
                upper_r = int((upper_r+lower_r)/2)
        for i in range(len(line) -4,len(line)-1):
            if(line[i] == 'R'):
                lower_c = int((upper_c+lower_c)/2) + (upper_c+lower_c)%2
            elif(line[i] == 'L'):
                upper_c = int((upper_c+lower_c)/2)

        if(upper_r*8 + upper_c > max):
            max =upper_r*8 + upper_c



if __name__ == "__main__":
    file = open('D:/Documents/RTU/Data_Structures/Advent_of_Code_2020/5/input.txt','r')

    text = file.readlines()
    # print(text)
    arr = [None] * 866
    for line in text:
        upper_r = 127
        lower_r=0
        upper_c=7
        lower_c= 0
        

        for i in range(0, len(line) -4):
            if(line[i] == 'B'):
                lower_r = int((upper_r+lower_r)/2) + (upper_r+lower_r)%2
            elif(line[i] == 'F'):
                upper_r = int((upper_r+lower_r)/2)
        for i in range(len(line) -4,len(line)-1):
            if(line[i] == 'R'):
                lower_c = int((upper_c+lower_c)/2) + (upper_c+lower_c)%2
            elif(line[i] == 'L'):
                upper_c = int((upper_c+lower_c)/2)
        arr[upper_r*8 + upper_c -1] = True
    
    w = True
    seat = 0
    for i in range(0,len(arr)):
        if(w==True and arr[i] == True):
            w = False
        if(w==False and arr[i] == None):
            seat = i +1
    print(seat)
                
        
