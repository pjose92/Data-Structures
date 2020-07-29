"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create instance of ListNode with value
        new_node = ListNode(value)
        #check if DLL is empty and if it is empty we will
        if self.length == 0:
            #set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        #if DLL is NOT empty
        else:
            #set the node's next to the current head 
            new_node.next = self.head
            self.head.prev = new_node
            #set head to the new node
            self.head = new_node
        #increment the DDL length attribute 
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #store the value of the head
        value = self.value.head
        #decrement the DDL length attibute 
        self.length -= 1
        #delete the head
        # if head.next is not None
        if self.head.next is not Node:
            #set head.next's prev to None
            self.head.next.prev = None
            #set head to head.next
            self.head = self.head.next
        #elif head.next is Noe:
        else: 
            #set the head to None
            self.head = None
            #self tail to None
            self.tail = None
        # return the value
        return value 
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create instance of ListNode with value
        new_node = ListNode(value)
        #check if DLL is empty. if it is:
        if not self.tail and not self.head:
            #set head and tail to the new node instance 
            self.head = new_node
            self.tail = new_node
        #if DLL is NOT empty:
        else:
            #set new node's prev to current tail
            new_node.prev = self.tail
            #set current tail's next to new node
            self.tail.next = new_node
            #set tail to the new node
            self.tail = new_node
        #increment the DLL lenght attribute 
        self.length += 1
                   
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #store the value of the tail
        value = self.tail.value
        #delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            #set tail.prev's next to None
            self.tail.prev.next = None
            #set tail tp tail.prev
            self.tail = tail.prev
        #elif tail,prev is None:
        else:
            #set head to None
            self.head = None
            #set tail to None
            self.tail = None
        #Decrement the DLL length attribute 
        self.length -= 1
        #return the value 
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if node is head already
        if node is self.head:
            #return None
            return
        #if node is tail
        if node is self.tail:
            #set node.prev as tail as the tail is being moved
            self.tail = self.tail.prev
        #connect the nodes in each side of 'node'
        node.prev.next = node.next
        #if node os not tail. if it has a next node
        if node.next is not None:
            #connect the nodes in each side of 'node' 
            node.next.prev = node.prev
        #set node.prev to None because head's prev is always None
        node.prev = None
        #set node.next tp current head
        node.next = self.head
        #set current head's prev to 'node' so it's not head anymore 
        self.head.prev = node
        #set current head to node
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #if node is tail already
        if node is self.tail:
            #return None
            return None
        #if node is head
        if node is self.head:
            #set head.next as head as the head is being moved
            self.head = self.head.next
        #connect the nodes in each side of 'node' backwards
        node.next.prev = node.prev
        #if 'node' is not head, meanign if it has a prev node
        if node.prev is not None:
            #connect the ndoes in each side of 'node'
            node.prev.next = node.next
        #set node.next to None because tail's next is always None
        node.next = None
        #set node.prev to current tail
        node.prev = self.tail
        #set current tail's next to 'node' so it's not tail anymore
        self.tail.next = node
        #set current tail node
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                node.next.prev = node.prev
                self.head = node.next
            elif node is self.tail:
                node.prev.next = node.next
                self.tail = node.prev
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass