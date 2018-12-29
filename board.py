#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Evan Tilley
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                #for each cell in the called object
                self.tiles[r][c] = int(digitstr[3*r + c])
                if self.tiles[r][c] == 0:
                    self.blank_r = r #defining self.blank_r
                if self.tiles[r][c] == 0:
                    self.blank_c =  c #defining self.blank_c
        # Do *NOT* remove our code above.
        
    ### Add your other method definitions below. ###
        
    def __repr__(self):
        """Returns a string representation of a Board object."""
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                #for each cell in the called object:
                if self.tiles[row][col] != 0: #if the cell is not 0
                    s += str(self.tiles[row][col]) + ' ' #add the cell to the string
                else:
                    s += '_ ' #otherwise, add an underscore to the string
            s += '\n' #print a newline character after the characters for each row
        return s #return the string

    def move_blank(self,direction):
        """Attempts to modify the contents of the baord object based on the direction; returns True or False to indicate whether the move in the requested direction was possible.
           input direction: a string that specifies the direction in which the blank should move
        """
    
        if direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right': #if direction is not up down left or right
            return 'unknown direction: ' + str(direction) #return error message
        #return False if the new coordinates would take you off the board
        if direction == 'up':
                new = self.blank_r + 1
                if new == 1:
                    return False
        elif direction == 'down':
                new = self.blank_r - 1
                if new < -1 or new==1:
                    return False
        elif direction == 'left':
                new = self.blank_c - 1
                if new<0 or new>len(self.tiles)-1:
                    return False
        elif direction == 'right':
                new = self.blank_c + 1
                if new<0 or new>len(self.tiles)-1:
                    return False

        #if we get here, the new coordinates did not take us off the board
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                #modify the gameboard's cell based on the direction specifed and return True
                
                if direction == 'up':
                    if self.tiles[r][c] == 0:
                        self.tiles[r][c] = self.tiles[r-1][c]
                        self.tiles[r-1][c] = 0
                        self.blank_r = self.blank_r - 1
                        return True
                elif direction == 'down':
                    if self.tiles[r][c] == 0:
                        self.tiles[r][c] = self.tiles[r+1][c]
                        self.tiles[r+1][c] = 0
                        self.blank_r = self.blank_r + 1
                        return True

                elif direction == 'left':
                    if self.tiles[r][c] == 0:
                        self.tiles[r][c] = self.tiles[r][c-1]
                        self.tiles[r][c-1] = 0
                        self.blank_c = self.blank_c - 1
                        return True
                elif direction == 'right':
                    if self.tiles[r][c] == 0:
                        self.tiles[r][c] = self.tiles[r][c+1]
                        self.tiles[r][c+1] = 0
                        self.blank_c = self.blank_c + 1
                        return True
    def digit_string(self):
        """Creates and returns a string of digits that correspond to the current contents of the called Board object's tiles attribute."""
        newlist = [x for y in self.tiles for x in y] #returns a list of the cells in the 2-D list tiles
        newlist1 = ''.join(map(str,newlist)) #joins the cells together in the list into a string
        return newlist1 #returns the string in which the cells have been joined together

    def copy(self):
        """Returns a newly-constructed Board objet that is a deep copy of the called object."""
        new = Board(self.digit_string()) 
        
        return new #returns a new board with the same digit_string input as the called object
    def num_misplaced(self):
        """Counts and returns the number of tiles in the called Board object that are not where they
           should be in the goal state(blank cell not included in this count).
        """ 
        num_misplaced = 0 #initial value of num_misplaced
        for x in range(9):
            row = (x//3) #row = 0,0,0,1,1,1,2,2
            col = int(x%3)#col = 0,1,2,3,4,5,6,7
            if self.tiles[row][col] != 0 and self.tiles[row][col] != x: #if the cell does not equal 0 and the cell does not equal the desired value
                    num_misplaced += 1 #increase the count of num_misplaced

        return num_misplaced #return num_misplaced

    def __eq__(self,other):
        """Returns True if the called object(self) and the argument(otther) have the same values for the tiles attribute, and False otherwise.
           input other: a Board object
        """
        for row in range(len(self.tiles)):
            for column in range(len(self.tiles)):
                #for each cell in the called object
                if self.tiles != other.tiles: #if the cell does not equal the corresponding cell of the other Board object
                    return False #return False
            return True #otherwise, return True

    def algorithm(self):
        """returns how close each tile on the board is to the goal tiles"""
        distance = 0
        for x in range(9):
            row = (x//3) #row = 0,0,0,1,1,1,2,2
            col = int(x%3)#col = 0,1,2,3,4,5,6,7
            distance += abs(self.tiles[row][col] - x) #absolute value of the tiles minus what the tile should be
        return distance


    
