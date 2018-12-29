#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: Evan Tilley
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, extra = -1):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(extra)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(extra)
    elif algorithm == 'DFS':
        searcher = DFSearcher(extra)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(extra, -1)
    elif algorithm == 'A*':
        searcher = AStarSearcher(extra, -1)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, extra=-1):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, extra)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename,algorithm,extra=-1):
    """Opens the file with the specified filename and processes the file by solving the eight puzzle for the digit string on each line.
       Inputs: filename = a string specifying the name of a text file in which eaach line is a digit string for an eight puzzle
               algorithm - a string that specifies which state-space search algorithm should be used to solve the puzzle
               extra S- an integer that can be used to specify an optional parameter for the algorithm being used - either a depth limit or a choice of heuristic
     """
    f = open(filename,'r') #reads through the file 
    puzzles = 0 #initializing values of variables
    tested = 0
    moves = 0
    for line in f:
        string = str(line[0:9])
        board = Board(string) #board object
        algorithm = str(algorithm)
        state = State(board,None,'init') #state object
        searcher = create_searcher(algorithm,extra)
        soln = None
        try:
            soln = searcher.find_solution(state)
            if soln == None:
                print(string + ': no solution')
                print()
            else:
                #prints solution
                print(string + ':', soln.num_moves,'moves,',searcher.num_tested, 'states tested')
                puzzles += 1
                moves += soln.num_moves
                tested += searcher.num_tested

        except KeyboardInterrupt:
            print(string + ':'  + ' search terminated, no solution')
            soln = None
    if puzzles!=0:
        print()
        print('solved',puzzles,'puzzles')
        print('averages:', moves/puzzles,'moves,',tested/puzzles,'states tested')

    else:
        print('solved: 0 puzzles')

