from __future__ import print_function, division
from pydatastructs.utils.misc_util import _check_type, NoneType

__author__ = 'rohansingh9001'

__all__ = [
    'DoublyLinkedList',
    'LinkedList'
]

# A linked list node 
class Node: 

    '''
    Node class for Linked List and Doubly Linked List [ Intended for internal use and not to be imported]

    Parameters
    ==========
    
    For Doubly Linked List use Default constructor(__init__):

        data: type
            A valid object type.
            Should be convertible to string using str() method to use print() method on instance

    For Single Linked List use Alternative constructor(singleLink):
        data: type
            A valid object type
            Should be convertible to string using str() method to use print() method on instance
    
    Note
    ====

    classmethod singleLink has been used for Node class for Single linked list due to non existence of a 
    previous link between the nodes.
    '''

    __slots__ = ['data', 'next', 'prev']
    
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.next = NoneType
        self.prev = NoneType
    #Alternative constructor for Single Linked List
    @classmethod
    def singleLink(obj, data):
        obj.data = data
        obj.next = NoneType
        return obj
    
    def __str__(self):
        return str(self.data)

'''------------------------Doubly Linked List Class---------------------------'''

# Class to create a Doubly Linked List 
class DoublyLinkedList: 
    

    '''
    A Doubly Linked List Class (abb. DLL)
    
    Parameters
    ==========
    
    None

    Methods
    =======

    1) appendleft: 
        takes parameters - data
            data: type 
                A valid object type
                Should be convertible to string using str() method to use print() method on instance.
        action - Pushes a new node at the start i.e. left of the DLL.

    2) appendright: 
        takes parameters - data
            data: type
                A valid object type.
                Should be convertible to string using str() method to use print() method on instance.
        action - Appends a new node at the end i.e. the right of the DLL.
    
    3) insertAfter:
        takes parameters - prevNode, data
            prevNode: Node type 
                An object of Node class 
            data: type
                A valid object type.
                Should be convertible to string using str() method to use print() method in instance.
        action - Inserts a new node after the prevNode.

    4) insertBefore:
        takes parameters - nextNode, data
            prevNode: Node type
                An object of Node class
            data: type
                A valid object type.
                Should be convertible to string using str() method to use print() method in instance.
        action - Inserts a new node before the newNode.

    5) insertAt:
        takes parameters - index, data
            index: int type
                An integer i such that 0<= i <= length, where length refers to the length of the List.
            data: type
                A valid object type.
                Should be convertible to string using str() method to use print() method in instance.
        action - Inserts a new node at the input index.

    6) popleft: 
        takes parameters - None
        action - Removes the Node from the left i.e. start of the DLL and returns the data from the Node.

    7) popright:
        takes parameters - None
        action - Removes the Node from the right i.e. end of the DLL and returns the data from the Node.

    8) pop:
        takes parameters - index
            index: int type
                An integer i such that 0<= i <= length, where length refers to the length of the List.
        action - Removes the Node at the index of the DLL and returns the data from the Node.
    
    9) __getitem__:
        takes parameters - index
            index: int type
                An integer i such that 0<= i <= length, where length refers to the length of the List.
        action - Returns the data of the Node at index.
            
    10) __setitem__:
        takes parameters - index, data
            index: int type
                An integer i such that 0<= i <= length, where length refers to the length of the List.
            data: type
                A valid object type.
                Should be convertible to string using str() method to use print() method in instance.
        action - Sets the data of the Node at the index to the input data.

    11) __str__:
        takes parameters - None
        action - Prints the DLL in a list from from the start to the end.
    
    12) __len__:
        takes parameters - None
        action - Returns the length of the DLL.

    13) isEmpty:
        takes parameters - None
        action - Return a bool value to check if the DLL is empty or not.

    References
    ==========
    
    https://www.geeksforgeeks.org/doubly-linked-list/

    '''
    __slots__ = ['head','tail','length']

    def __init__(self):
        self.head = NoneType
        self.tail = NoneType
        self.length = 0

    def appendleft(self,data):
        self.length += 1
        newNode = Node(data)
        if self.head is not NoneType:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

        if newNode.next == NoneType:
            self.tail = newNode
        if newNode.prev == NoneType:
            self.head = newNode
    
    def appendright(self, data):
        self.length += 1
        newNode = Node(data)
        if self.tail is not NoneType:
            self.tail.next = newNode
            newNode.prev = self.tail
        self.tail = newNode

        if newNode.next == NoneType:
            self.tail = newNode
        if newNode.prev == NoneType:
            self.head = newNode

    def insertAfter(self, prevNode, data):
        self.length += 1
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if newNode.next == NoneType:
            self.tail = newNode
        if newNode.prev == NoneType:
            self.head = newNode
    
    def insertBefore(self, nextNode, data):
        self.length += 1
        newNode = Node(data)
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        newNode.next = nextNode
        
        if newNode.next == NoneType:
            self.tail = newNode
        if newNode.prev == NoneType:
            self.head = newNode
    
    def insertAt(self, index, data):
        if index > self.length or index < 0 or not (_check_type(index, int)):
            raise ValueError('Index input out of range/Index is expected to be an Integer.')
        else:
            if index == 0:
                self.appendleft(data)
            elif index == self.length:
                self.appendright(data)
            else:  
                self.length += 1
                newNode = Node(data)
                counter = 0
                currentNode = self.head
                while counter != index:
                    currentNode = currentNode.next
                    counter += 1
                currentNode.prev.next = newNode
                newNode.prev = currentNode.prev
                currentNode.prev = newNode
                newNode.next = currentNode
                    
                if newNode.next == NoneType:
                    self.tail = newNode
                if newNode.prev == NoneType:
                    self.head = newNode
    
    def popleft(self):
        self.length -= 1
        oldHead = self.head
        oldHead.next.prev = NoneType
        self.head = oldHead.next
        return oldHead.data 

    def popright(self):
        self.length -= 1
        oldTail = self.tail
        oldTail.prev.next = NoneType
        self.tail = oldTail.prev
        return oldTail.data

    def pop(self, index=0):
        if index > self.length or index < 0 or not (_check_type(index, int)):
            raise ValueError('Index input out of range/Index is expected to be an Integer.') 
        else:  
            if index == 0:
                self.popleft()
            elif index == self.length:
                self.popright()
            else:
                self.length -= 1
                counter = 0
                currentNode = self.head
                while counter != index:
                    currentNode = currentNode.next
                    counter += 1
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                return currentNode.data

    def __getitem__(self, index): 
        if index > self.length or index < 0 or not (_check_type(index, int)):
            raise ValueError('Index input out of range/Index is expected to be an Integer.')
        else:     
            counter = 0
            currentNode = self.head      
            while counter != index:
                currentNode = currentNode.next
                counter += 1
            return currentNode.data

    def __setitem__(self, index, data):
        if index > self.length or index < 0 or not (_check_type(index, int)):
            raise ValueError('Index input out of range/Index is expected to be an Integer.')
        else:  
            counter = 0
            currentNode = self.head    
            while counter != index:
                currentNode = currentNode.next
                counter += 1
            currentNode.data = data

    
    def __str__(self):
        elements = []
        currentNode = self.head
        while currentNode is not NoneType:
            elements.append(currentNode.data)
            currentNode = currentNode.next
        return str(elements)

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.length == 0