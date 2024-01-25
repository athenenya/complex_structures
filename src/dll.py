class DLLNODE:
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

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previoys attribure with new_next"""
        self.next = new_previous