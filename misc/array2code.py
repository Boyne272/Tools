import numpy as np

class array2code():
    
    def __init__(self, arr):
        self.s = ''
        self._recursive(arr)
        print('np.array(' + self.s + ')')
        

    def _recursive(self, arr):
        if arr.ndim > 1:
            self.s += '['
            for a in arr:
                self._recursive(a)
                self.s += ',\n'
            self.s = self.s[:-2]
            self.s += ']'
        else:
            self._arr_to_lst(arr)
        
    def _arr_to_lst(self, arr):
        assert arr.ndim == 1, 'must be a 1d array'
        
        self.s += '['
        for el in arr:
            self.s += str(el) + ', '
        self.s = self.s[:-2]
        self.s += ']'
        
    def get_string(self):
        return 'np.array(' + self.s + ')'
