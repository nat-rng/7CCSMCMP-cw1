# implemntation taken from https://github.com/bfaure/Python3_Data_Structures/blob/master/Linked_List/main.py
class ListNode:
    def __init__(self,data=None):
        self.__data = data
        self.__next = None
    
    def get_data(self):
        return self.__data
    
    def get_next(self):
        return self.__next
    
    def set_data(self, data):
        self.__data = data 
    
    def set_next(self, node):
        self.__next = node
        
    def print_val(self):
        print(self.__data)
        
class LinkedList:
    def __init__(self):
        self.__head = ListNode()
        self.__limit = None

    def get_head(self):
        return self.__head
    
    def set_head(self, value):
        self.__head = ListNode(value)
    
    def get_limit(self):
        return self.__limit
    
    def set_limit(self, limit):
        self.__limit = limit
        
    def is_empty(self):
        if self.__head == None:
            return True
        return False

    def is_full(self):
        if self.__limit == self.length():
            return True
        return False
    # Adds new node containing 'data' to the end of the linked list.
    def insert(self, data):
        new_node = ListNode(data)
        cur = self.__head
        while cur.get_next() != None:
            cur = cur.get_next()
        cur.set_next(new_node)
    # Returns the length (integer) of the linked list.
    def length(self):
        cur = self.__head
        total = 0
        while cur.get_next() != None:
            total += 1
            cur = cur.get_next()
        return total 
    
    # Prints out the linked list in traditional Python list format. 
    def traverse(self):
        elems = []
        cur_node = self.__head
        while cur_node.get_next() != None:
            cur_node=cur_node.get_next()
            elems.append(cur_node.get_data())
        return elems
    
    def __str__(self):
        return str(self.traverse())

    # Returns the value of the node at 'index'. 
    def get(self, index):
        if index >= self.length() or index<0: # added 'index<0' post-video
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.__head
        while True:
            cur_node = cur_node.get_next()
            if cur_idx == index: 
                return cur_node.get_data()
            cur_idx += 1
    
    def search(self, value):
        # Initialize current to head
        current = self.__head
        # loop till current not equal to None
        while current != None:
            if current.get_data() == value:
                return True  # data found
            current = current.get_next()
        return False

    # Deletes the first node with value 'value'.
    def delete(self, value):
        cur_node = self.__head
        while True:
            last_node = cur_node
            cur_node = cur_node.get_next()
            if cur_node.get_data() == value:
                last_node.set_next(cur_node.get_next())
                return
    
    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self, index):
        return self.get(index)

    # Sets the data at index 'index' equal to 'data'.
    # Indices begin at 0. If the 'index' is greater than or equal 
    # to the length of the linked list a warning will be printed 
    # to the user.
    def set(self, index, data):
        if index >= self.length() or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return
        cur_node = self.__head
        cur_idx = 0
        while True:
            cur_node = cur_node.get_next()
            if cur_idx == index: 
                cur_node.set_data(data)
                return
            cur_idx+=1