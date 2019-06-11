class Tree:
    def __init__(self, data):
        self.data = data
        self._left = None
        self._right = None

    def set_left(self, value):
        self._left = value

    def get_left(self):
        return self._left

    left = property(fset=set_left, fget=get_left)

    def set_right(self, value):
        self._right = value

    def get_right(self):
        return self._right
    
    right = property(fset=set_right, fget=get_right)
