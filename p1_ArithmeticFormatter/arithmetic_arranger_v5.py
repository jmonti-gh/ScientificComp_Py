''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger_v0.py



def aritmetic_arranger(lst, b=False):
    lenght = len(lst)
    if lenght > 5:
        print('Error: Too many problems')
        return (1, 'Too many problems', lenght)
    elif len(lst) < 1:
        print('Error: Very few problems')
        return (2, 'Very few problems', lenght)

    

aritmetic_arranger([])
aritmetic_arranger([i for i in range(10)])
print(aritmetic_arranger([])[0])
print(aritmetic_arranger([]))


