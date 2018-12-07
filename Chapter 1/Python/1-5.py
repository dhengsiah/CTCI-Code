def OneAway(string1,string2):
        flag = False
        s1_len = len(string1)
        s2_len = len(string2)
        
        if abs(s1_len-s2_len)>1:
            return False
                
        x = 0 #S1 iterator
        y = 0 #S2 iterator
        
        while x<s1_len and y <s2_len:
            if string1[x] != string2[y]:
                if flag:
                    return False
                elif s1_len > s2_len:
                    flag = True
                    x += 1
                elif  s1_len < s2_len:
                    flag = True
                    y += 1
                
                else:
                    x+=1
                    y+=1
            else:        
                x += 1
                y += 1
            
        return True


def OneAway_improved(string1,string2):
        flag = 0
        s1_len = len(string1)
        s2_len = len(string2)
        
        if abs(s1_len-s2_len)>1:
            return False
                
        x = 0 #S1 iterator
        y = 0 #S2 iterator
        
        while x<s1_len and y <s2_len:
            if string1[x] != string2[y]:
                flag += 1
                if flag == 2:
                    return False
                elif s1_len > s2_len:
                    x += 1
                    continue
                elif  s1_len < s2_len:
                    y += 1
                    continue        
            x += 1
            y += 1
            
        return True