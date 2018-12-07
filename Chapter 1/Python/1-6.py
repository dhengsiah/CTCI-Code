
def stringCompress(s):
    #For loop version
    current = 'unset'
    counter = 0
        
    compressed = ''
    score = 0
        
    for x in s:
        if current == 'unset':
            current = x
            counter = 1
                
        elif current == x:
            counter += 1
            
        else:
            compressed += current
            compressed += str(counter)
            score -= counter-2
            current = x
            counter = 1
                
    #For the last element
    compressed += current
    compressed += str(counter)
    score -= counter-2            
                
    if score < 0:
        return compressed
        
    else:
        return s


def stringCompress2(s):
    #While loop version
    current = 'unset'
    counter = 0
    
    compressed = ''
    score = 0
    
    length = len(s)
    i = 0
    
    while i < length:
        if current == 'unset':
            current = s[i]
            counter = 1
        
        elif current == s[i]:
            counter += 1
            
        else:
            compressed += current
            compressed += str(counter)
            score -= counter-2
            current = s[i]
            counter = 1
            
        if i == length-1:
            compressed += current
            compressed += str(counter)
            score -= counter-2
            
        i += 1
    
    
    if score < 0:
        return compressed
    else:
        return s