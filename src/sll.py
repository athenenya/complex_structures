class SLLNODE:
    def __int__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "SLLNode object: data={}" . format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribure with new_data"""
        self.data = new_data

    def get_next(self):
        """Return the self.data attribute"""
        return self.data

    def set_next(self, new_next):
        """Replace the existing value of the self.data attribure with new_next"""
        self.next = new_next

class SLL:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return "SLLNode object: data={}" . format(self.head)
    

    def is_empty(self):
        return self.head is None


    def add_front(self):
        pass


    def size(self, data):
        pass


    def search(self, data):
        pass


    def remove(self, data):
        pass

node = SLLNODE()
print(node.get_data())
node.set_data(7)
print(node.get_data())
node2 = SLLNODE('carrot')
print(node.get_next())