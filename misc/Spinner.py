from itertools import cycle
import time
import sys

class Spinner():
    'Prints a loading spinner that can also tell how long something took'
    def __init__(self, option='spin', frequ=1):
        
        # create a counter
        def counter(start=0):
            while True: start += 1; yield start

        # store atributes
        self.start = time.time()
        self.frequ = frequ
        self.count = counter()

        # select the generator
        if option=='spin':
            self.g = cycle(['|', '/', '-', '\\'])
        elif option=='dots':
            self.g = cycle(['.', '..', '...', '....'])
        elif option=='Numers':
            self.g = counter()

    def __call__(self):
        if not (next(self.count) % self.frequ):
            sys.stdout.write('\r' + next(self.g))
            sys.stdout.flush()

    def time(self, prefix='\t'):
        print(prefix, ' took %.4f'%(time.time()-self.start), 's')
