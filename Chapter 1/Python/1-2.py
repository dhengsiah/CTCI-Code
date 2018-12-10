from collections import Counter

def isPerm(string1,string2):
    
    S1_C = Counter()
    S2_C = Counter()
    
    if len(string1) != len(string2):
        return False
        
    for x in range(len(string1)):
        S1_C[string1[x]] += 1
        S2_C[string2[x]] += 1
        
    if S1_C == S2_C:
        return True
        
        
def isPerm_sorting(string1,string2):
    
    S1_S = sorted(string1)
    S2_S = sorted(string2)
    
    if S1_S == S2_S:
        return True
    else:
        return False
        
    