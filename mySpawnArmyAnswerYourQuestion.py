"""
mySpawnArmyAnswerYourQuestion is a python script that try to answer the question:
"How many paths do you have from point A to point B in a square of 10 per 10 ?"
With fact that you can just use 2 movings : to the Right and to the Bottom!
This question was asked to Nicolas by Fabrice in 2017 the Wednesday 22th of november.
See below, the square :

A ---------------------------------------------> X
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
  |
  |
  Y

Here we try to answer with an original aproach base on full spawn agents exploration.

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

Note : mySpawnArmyAnswerYourQuestion was righted with EMACS.

"""

# ask user grid size.
print ()
w = int(input('Grid width ? '))
h = int(input('Grid height ? '))
print()


# declare position_x, position_y, generation_z and name of 1st men!
pos_x = 0
pos_y = 0
gen_z = pos_x + pos_y
name = ['']
# print ('1st men pos_x :', pos_x)
# print ('1st men pos_y :', pos_y)
# print ('1st men gen_Z :', gen_z)
# print ('1t men name :', name)

# declare list 1st men features...
first_men = [pos_x,pos_y,gen_z,name]
# print ('first_men :', first_men)

# declare list curent generation.
gen_list = [first_men]
# print ('gen_list : ', gen_list)

# declare list of human kind.
human_kind = [gen_list]
# print ('human_kind :', human_kind)

# declare generation counter.
gen_count = len(human_kind)-1
# print ('gen_count :', gen_count)

# declare last generation size.
gen_size = len(human_kind[gen_count])
# print ('gen_size :', gen_size, 'for gen_count :', gen_count)

# for each generation need to rise B ( = number of steps)
for generation in range(w+h):
         
         # reboot gen_list for next generation.
         gen_list = []

         # for each men in the last generation :
         for men in range(gen_size):
                  # print ('parents :', human_kind[gen_count][men])

                  if human_kind[gen_count][men][0] < w:
                           son_name = list(human_kind[gen_count][men][3])
                           son_name.append('R')
                           son = [human_kind[gen_count][men][0]+1,
                                  human_kind[gen_count][men][1],
                                  human_kind[gen_count][men][2]+1,
                                  son_name]
                           # update list curent generation.
                           gen_list.append(son)
                           # print ('son :', son)

                  if human_kind[gen_count][men][1] < h:
                           daugther_name = list(human_kind[gen_count][men][3])
                           daugther_name.append('D')
                           daugther = [human_kind[gen_count][men][0],
                                       human_kind[gen_count][men][1]+1,
                                       human_kind[gen_count][men][2]+1,
                                       daugther_name]      
                           # update list curent generation.
                           gen_list.append(daugther)
                           # print ('daugther :', daugther)
                  # print()


         # update list current generation.
         # print ('gen_list', gen_list)

         # update list of human kind.
         human_kind.append(gen_list)
         # print ('human_kind :', human_kind)

         # update generation counter.
         gen_count += 1
         # print ('gen_count :', gen_count)

         # update last generation size.
         gen_size = len(human_kind[gen_count])
         # print ('gen_size :', gen_size, 'for gen_count :', gen_count)

         # print()

# result
print ()
print ('Human kind found', gen_size, 'uniques paths in', w, 'x', h, 'grid')
print ('Checking with mathematic permutation solution C(w+h,w) :', C(w+h,w))
print ()
