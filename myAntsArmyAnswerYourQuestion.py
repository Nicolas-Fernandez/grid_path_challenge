"""
myAntsArmyAnswerYourQuestion is a python script that try to answer the question:
"How many paths do you have from point A to point B in a square of 10 per 10 ?"
With fact that you can just use 2 movings : to the Right and to the Bottom!
This question was asked to Nicolas by Fabrice in 2017 the Wednesday 22th of november.
See below, the square :

A -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  -----------------------------------------
  |   |   |   |   |   |   |   |   |   |   |
  ----------------------------------------- B

Here we try to answere with an original aproach base on probabilistic ants exploration.

Yeah ...
Because the first proposition below, with exact mathematic aproach and permutations
was rejected by the Emperor ...

-----------------------------------------------------------------------------
# import math library to use "factorial" function
"""
import math as mp

# definition C function, return number of combinations k among N note C(n,k)

def C(n,k):
         return(mp.factorial(n)/(mp.factorial(n-k)*mp.factorial(k)))
"""
# ask user for grid height h and width w of this dreams
h = int(input("grid height ? "))
w = int(input("grid width ? "))

# combinations calculation with C function
c = C((w+h),h)

# print result
print(c, "ways on a", h, "per", w, "grid")
-----------------------------------------------------------------------------

Note : myAntsArmyAnswerYourQuestion was righted with EMACS.

"""

# import random.py library to generate ants decisions
import random as rd

# ask user for grid height h and width w of this dreams
height = int(input('Grid height ? '))
width = int(input('Grid width ? '))
print()

# ask user how many agents used for aproximation
ants = int(input('How many ants in my army ? '))
print()

# declare list of all paths
all_paths = []

# declare lenght of paths
paths_lenght = width + height

# for each agent
for agent in range (ants):

    # declare initial position of ant
    # x = position in abscisse -
    # y = postion in ordonate |
    # Starting A point is at (0,0)
    # Ending B point is at (width,heigth)
    ant_x = 0
    ant_y = 0

    # declare ant path, note with R for right move and D for down move.
    ant_path = []

    # for each step in the path
    for step in range (paths_lenght):

        # "random" choice to go Down on the grid.
        choice = rd.randint(0,1)

        # if ant reach far right, just go Down and record path
        if ant_x == width:
            ant_y += 1
            ant_path.append('D')
            
        # or if ant reach deep bottom, just go Right and record path
        elif ant_y == height:
            ant_x += 1
            ant_path.append("R")
            
        else:     
            # if 0, ant don't go Down, go Right, and path is recorded
            if choice == 0:
                ant_x += 1
                ant_path.append('R')
            
            # and if 1, ant go Down, don't go Right, and path is recorded
            elif choice == 1:
                ant_y += 1
                ant_path.append('D')

    # final path of ant is recorded in list as string in all_paths
    all_paths.append(''.join(ant_path))

# count how many UNIQUE path (convert list all_paths in a set) recorded and print it
print ('My ants found at least', len(set(all_paths)), 'uniques paths in a', height, 'x', width, 'grid')
print ('If you found a number of unique path equal or to close of the number of ants,')
print ('you should probably increase the number of ants...')
print ('In nature, some species neasts can provide more than billion of ants !!!')
print ('For better estimation and find (maybe) more unique path, increase ants number !')
print ('Advice, at least', C((height+width),height)*10,'for a', height, 'x', width, 'grid')
print ()

# Queen corection !
queen_paths = []
for path in range(len(all_paths)):
    queen_paths.append(all_paths[path])

for path in range(len(queen_paths)):
    queen_paths[path] = queen_paths[path].replace("R", "A")
    queen_paths[path] = queen_paths[path].replace("D", "B")
    queen_paths[path] = queen_paths[path].replace("A", "D")
    queen_paths[path] = queen_paths[path].replace("B", "R")

new_paths = all_paths + queen_paths

print ('The queen found at least', len(set(new_paths)), 'uniques paths in a', height, 'x', width, 'grid')
print ('If you found a number of unique path equal or to close of the number of ants,')
print ('you should probably increase the number of ants...')
print ('The queen is smarter, she take all inverts paths founded by ants and add it to the set')
print ('For better estimation and find (maybe) more unique path, increase ants number !')
print ('For Queen, just', C((height+width),height)*2,'for a', height, 'x', width, 'grid')
print ()
print ('For information, answear is', C((height+width),height), 'uniques paths')
print ('... end of script ...')
