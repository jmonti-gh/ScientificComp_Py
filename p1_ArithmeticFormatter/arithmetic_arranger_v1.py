''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger_vX.py:
#   use '{:>n}'.format to aling instead of add spaces
#   using regex, or str.find() & slicing instead of str.split()
#   make to more controls to string text in operations
#   use list to save partials results 
#   other project: permit more problems and arrange in grups by (% -mod)
#   other project: add more operations permited



def aritmetic_arranger(lst, b=False):
    # check number of problems limit restriccions
    limit = 5
    lenght = len(lst)
    if lenght > limit:
        print('Error: Too many problems')
        return (1, 'Too many problems', lenght)
    elif len(lst) < 1:                          #more control example
        print('Error: Very few problems')
        return (2, 'Very few problems', lenght)



# aritmetic_arranger([])
# aritmetic_arranger([i for i in range(10)])
# print(aritmetic_arranger([])[0])
# print(aritmetic_arranger([]))


