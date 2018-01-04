"""
gofab est, comme son (nom) / ext l'indique, un programme en python,
qui permet, connaissant la longeur L et la largeur l d'un quadrillage,
de calculer le nombre de chemins possibles,
partants de son coin supérieur gauche et allant à son coin inférieur droit,
en n'utilisant que les déplacements gauche-->droite et haut-->bas.
"""

# import math library to use "factorial" function
import math as mp

# definition C function, return number of combinations k among N note C(n,k)
def C(n,k):
         return(mp.factorial(n)/(mp.factorial(n-k)*mp.factorial(k)))

# ask user for grid height h and width w of this dreams
h = int(input("grid height ? "))
w = int(input("grid width ? "))

# combinations calculation with C function
c = C((w+h),h)

# print result
print(c, "ways on a", h, "per", w, "grid")




