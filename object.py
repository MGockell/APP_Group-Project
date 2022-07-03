import random

class Object():
    '''A class to represent a single object falling down the screen.'''

    def __init__(self, time) -> None:
        '''Initializes an object to fall down the screen
        Parameters:
        time(int): total game time that has been passed'''
        
        self.time = time


    def move(self) -> None:
        ''' Function to move the object one step
        Parameters:
        -> None
        '''
        # Falling speed increases with time 
        if self.coordinates[0] > 1:
            self.coordinates[1] += 1+self.time/50000


    def check_coordinates(self) -> float:
        ''' Function to check the object's coordinates
        Parameters:
        -> None
        '''
        self.x = self.coordinates[0]
        self.y = self.coordinates[1] 

        return self.x, self.y   


