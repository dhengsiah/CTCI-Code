from baseclass import *
from collections import Counter

def removeDupeSLL(LL):
    #Singly-Linked List version
    #Buffer allowed to keep track of what has been seen
    
    cnt = Counter()
    x = LL.head
    prev = None
    
    while x != None:
        
        if cnt[x.data] == 0:
            cnt[x.data] += 1
            prev = x
            x = x.nextNode
            
        else:
            temp = x.setNode()
            print 'Deleting ' + str(temp.data)
            x = x.nextNode
            LL.deleteNode(prev,temp)
            
    return
            

def removeDupeDLL(LL):
    #Doubly-Linked List version
    #Buffer allowed
    
    cnt = Counter()
    x = LL.head
    prev = x.prevNode
    
    while x != None:
        
        if cnt[x.data] == 0:
            cnt[x.data] +=1
            x = x.nextNode
            prev = x.prevNode
            
        else:
            node = x
            x = x.nextNode
            print 'Deleting ' + str(node.data)
            LL.deleteNode(node)
        
    return