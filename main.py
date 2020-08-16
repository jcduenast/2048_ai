import numpy as np
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = np.array([[0 for x in range(width)] for y in range(height)])
        self.add_tile()
        self.add_tile()
        
    def add_tile(self):
        x = random.randrange(0, self.width)
        y = random.randrange(0, self.height)
        while self.matrix[x, y] != 0:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
        
        self.matrix[x, y] = 2
        # TODO add 0.1 chance of adding a 4
    
    def shift_towrads(self, direction):
        if direction == 'left':
            for x in range(self.height):
                for y in range(self.width):
                    if self.matrix[x, y]==0:
                        y2 = y+1  # x2 next position
                        while y2<self.width:
                            if self.matrix[x, y2]!=0:
                                self.matrix[x, y] = self.matrix[x, y2]
                                self.matrix[x, y2] = 0
                                break
                            y2 = y2+1
                    
                    y2 = y+1
                    while y2<self.width:
                        if self.matrix[x, y2]==self.matrix[x, y]:
                            self.matrix[x, y] = self.matrix[x, y]+self.matrix[x, y2]
                            self.matrix[x, y2] = 0
                            # a mergeable tile was found, merging
                        y2 = y2+1
        
        if direction == 'right':
            for x in range(self.height):
                for y in range(1, self.width+1):
                    if self.matrix[x, -y]==0:
                        y2 = -y-1  # x2 next position
                        while y2>=-self.width:
                            if self.matrix[x, y2]!=0:
                                self.matrix[x, -y] = self.matrix[x, y2]
                                self.matrix[x, y2] = 0
                                break
                            y2 = y2-1
                    
                    y2 = -y-1
                    while y2>=-self.width:
                        if self.matrix[x, y2]==self.matrix[x, -y]:
                            self.matrix[x, -y] = self.matrix[x, -y]+self.matrix[x, y2]
                            self.matrix[x, y2] = 0
                            # a mergeable tile was found, merging
                        y2 = y2-1

        if direction == 'up':
            for y in range(self.width):
                for x in range(self.height):
                    if self.matrix[x, y]==0:
                        x2 = x+1  # x2 next position
                        while x2<self.height:
                            if self.matrix[x2, y]!=0:
                                self.matrix[x, y] = self.matrix[x2, y]
                                self.matrix[x2, y] = 0
                                break
                            x2 = x2+1
                    
                    x2 = x+1
                    while x2<self.height:
                        if self.matrix[x2, y]==self.matrix[x, y]:
                            self.matrix[x, y] = self.matrix[x, y]+self.matrix[x2, y]
                            self.matrix[x2, y] = 0
                            # a mergeable tile was found, merging
                        x2 = x2+1

        if direction == 'down':
            for y in range(self.width):
                for x in range(1, self.height+1):
                    if self.matrix[-x, y]==0:
                        x2 = -x-1  # x2 next position
                        while x2>=-self.height:
                            if self.matrix[x2, y]!=0:
                                self.matrix[-x, y] = self.matrix[x2, y]
                                self.matrix[x2, y] = 0
                                break
                            x2 = x2-1
                    
                    x2 = -x-1
                    while x2>=-self.height:
                        if self.matrix[x2, y]==self.matrix[-x, y]:
                            self.matrix[-x, y] = self.matrix[-x, y]+self.matrix[x2, y]
                            self.matrix[x2, y] = 0
                            # a mergeable tile was found, merging
                        x2 = x2-1

        self.add_tile()

if __name__=='__main__':
    map = Board(4, 4)
    print(map.matrix)
    
    map.shift_towrads('down'); print(map.matrix)
    map.shift_towrads('up'); print(map.matrix)
    map.shift_towrads('left'); print(map.matrix)
    map.shift_towrads('right'); print(map.matrix)

