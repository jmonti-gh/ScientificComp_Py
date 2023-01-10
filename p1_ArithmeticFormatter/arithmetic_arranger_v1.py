''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger_v1.py: using regex



def aritmetic_arranger(lst, b=False):
    # check number of problems limit restriccions
    limit = 5
    lenght = len(lst)
    if lenght > limit:
        print('Error: Too many problems')
        return (1, 'Too many problems', lenght)
    elif len(lst) < 1:
        print('Error: Very few problems')
        return (2, 'Very few problems', lenght)



    

    

# aritmetic_arranger([])
# aritmetic_arranger([i for i in range(10)])
# print(aritmetic_arranger([])[0])
# print(aritmetic_arranger([]))


