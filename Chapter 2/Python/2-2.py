from baseclass import *
from collections import Counter

def removekthfromlast_naive(LL,k):
    
    x = LL.head
    total = 0
    
    while x != None:
        total += 1
        x = x.nextNode
        
    counter = total - k
    x = LL.head
    
    assert counter >= 0
    
    while counter != 0:
        x=x.nextNode
        counter -= 1
        
    return x
    
    
    
def removekthfromlast(LL,k):
    
    forward = LL.head
    back = LL.head

    assert k > 0
    delay = k-1
    
    while forward.nextNode != None:
        
        if delay >0:
            delay -= 1
            forward = forward.nextNode
        else:
            forward = forward.nextNode
            back = back.nextNode
            
    
    
    if delay > 0:
        return None
        
    return back