def count_substring(s, sub_s):
        count=0
        for i in range(len(s)):
            k=s[i:]
            for j in range(0,len(k)):
                if k[0:j+1]==sub_s:
                    count+=1
        return count
def minion_game(string):
    count_c=0
    count_v=0
    c=[]
    v=[]
    for i in range(len(string)):
        if string[i].upper() not in (['A','E','I','O','U']):
            k=string[i:]
            for j in range(0,len(k)):
                if k[0:j+1] not in c:
                    c.append(k[0:j+1])
        else:
            k=string[i:]
            for j in range(0,len(k)):
                if k[0:j+1] not in v:
                    v.append(k[0:j+1])                

    for i in c:
        count_c+=count_substring(string,i)    
    for i in v:
        count_v+=count_substring(string,i)
        
    if count_c>count_v:
        print("Player-1",count_c)
    elif count_v>count_c:
        print("Player-2",count_v)    
    else:
        print("Draw")    
        
        
if __name__ == '__main__':
    s = input("Enter the string to play : ")
    minion_game(s)