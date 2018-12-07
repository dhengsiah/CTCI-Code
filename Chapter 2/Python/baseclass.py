import random

#Basic Linked list structure

class Node:
    
    def __init__(self,d):
        self.data = d
        self.nextNode = None
        self.prevNode = None
        
    def __repr__(self):
        return str(self.data)
        
    def append_SLL(self,node):
        self.nextNode = node
        return
        
    def append_DLL(self,node):
        self.nextNode = node
        node.prevNode = self
        return
    
    def setNode(self):
        return self
        
class singlyLL:
    #Wrapper for a singly linked list
    def __init__(self):
        self.head = None
        
    
    def appendtoTail(self,node):
        if self.head == None:
            self.head = node
        
        else:
            x = self.head
            while x.nextNode != None:
                x = x.nextNode
                
            x.append_SLL(node)
            
    def deleteNodewithData(self,d):
        #Deleting a single node with data d
        #2 Cases:
        #If d is at head, move head, else just change pointers
        
        if self.head.data == d:
            self.head = self.head.nextNode
            return
            
        else:
            x = self.head
            while x.nextNode != None:
                if x.nextNode.data == d:
                    x.nextNode = x.nextNode.nextNode
                    
                    print 'Node with data ' + str(d) +' has been deleted.'
                    return
            
            print 'No Node with data ' + str(d) + ' has been found.'
            return
            
    def deleteNode(self,prev,node):
        
        if self.head == node:
            self.head = self.head.nextNode
            return
            
        else:
            prev.nextNode = node.nextNode
            return
    
    def insertNode(self,node,prev = None):
        #Insert a node before an element 'prev'
        
        if prev == self.head:
            node.nextNode = self.head
            self.head = node
            return
            
        else:
            node.nextNode = prev.nextNode
            prev.nextNode = node
            return
        
    
    
    def generateRandomLL(self,size,N):
        self.head = None
        
        for x in range(size):
            node = Node(random.randint(0,N))
            self.appendtoTail(node)
            
        return
        
    def printLL(self):
        x = self.head
        
        while x != None:
            print x.data
            x = x.nextNode
            
        return
            
class doublyLL:
    #Wrapper for a doubly linked list
    
    def _init_(self):
        head = None

    def appendtoTail(self,node):
        if self.head == None:
            self.head = node
        
        else:
            x = self.head
            while x.nextNode != None:
                x = x.nextNode
                
            x.append_DLL(node)
    
    def printLL(self):
        x = self.head
        
        while x != None:
            print x.data
            x = x.nextNode
            
        return
    
    def deleteNode(self,node):
        #LOGIC:
        #Check whether head
        #If head, update head
        #Else, remove node and update next/prev pointers
        
        if node == self.head:
            self.head = self.head.nextNode
            return
            
        else:
            node.prevNode.nextNode = node.nextNode
            
            if node.nextNode!= None:
                node.nextNode.prevNode = node.prevNode
            
            return
        
    def insertNode(self,node,prev):
        #Insert a node before a 'prev' node
        
        if node == self.head:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = node
        
        else:
            node.prevNode = prev.prevNode
            node.nextNode = prev
            
            prev.prevNode.nextNode = node
            prev.prevNode = node
            
    def generateRandomLL(self,size,N):
        self.head = None
        
        for x in range(size):
            node = Node(random.randint(0,N))
            self.appendtoTail(node)
            
        return            