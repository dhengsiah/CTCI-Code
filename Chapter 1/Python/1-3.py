#INCOMPLETE

def urlify(string):
    
    output = []
    
    for x in string:
        if x == ' ':
            output.append("%")
            output.append("2")
            output.append("0")
            
        else:
            output.append(x)
            
    return ''.join(output)
    
    
def urlify_inplace(string):
    
    