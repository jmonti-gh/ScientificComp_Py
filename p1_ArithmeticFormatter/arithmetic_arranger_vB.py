''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger_v0.py

def arithmetic_arranger(problems, b=False):
    # check number of problems limit is 5
    limit, lenght = 5, len(problems)
    if lenght > limit:
        return 'Error: Too many problems.'

    # lists were save numbers, signs, and resutls
    topns, signs, bottns, results = [], [], [], []
   
    # parse problems
    for p in problems:                   # for e/problem
        # check apropiate operators
        if '*' in p or '/' in p:
            return "Error: Operator must be '+' or '-'."

        # find valid signs positions
        p_pos = p.find('+')
        m_pos = p.find('-')

        # get sign
        if p_pos != -1:
            pos = p_pos
            sign = '+'
        elif m_pos != -1:
            pos = m_pos
            sign = '-'

        # get top and botton numbers
        topn = p[:pos].strip()
        bottn = p[(pos+1):].strip()

        # if operands are not integers
        if not topn.isdigit() or not bottn.isdigit():
            return "Error: Numbers must only contain digits."
        
        # check operands witth (max 4 digis)
        if len(topn) > 4 or len(bottn) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Everything ok, can fill the lists
        topns.append(topn)      # save top number in topns[]
        signs.append(sign)      # save sign in signs[]
        bottns.append(bottn)

        # Convert numbers to int
        try:
            topi = int(topn)
            botti = int(bottn)
        except Exception as e:
            print('Siamo Fouri -  # Convert numbers to int ', e)
            raise Exception

        # Do operation & save the result
        if sign == '+':
            result = topi + botti
        elif sign == '-':
            result = topi - botti
        else:
            print('Siamo Fouri - # Do operation')
            raise Exception()
        results.append(str(result))
    
    # print(topns)
    # print(signs)
    # print(bottns)
    # print(results)
    # print()

    # No es necesario salvarlos en lists, si vamos 'retunr' un GRAN str con varias 
    # líneas vamos comppletando las líneas y despues las contactenemos y
    # los espacios delante de los nros, justamante los llenamos con ' ' para que nos
    # quede alineado a la derecha siempre tomando como nro de ref el max. width, o
    # se el sign + esp + max(len) - todo strings solo pasan a int. cuando se sum o rest

    # vamos a trabajerlos a partir de las listas ya que est 
    print()
    # Print the top numbers (first line)
    for i in range(len(topns)):
        print('{:>6}'.format(topns[i]), end='    ')
    print()

    # Print the sign + botton numbers (second line)
    for i in range(len(bottns)):
        # Construct the second line w/ sign and bottn
        if len(topns[i]) > len(bottns[i]):
            diffdig = len(topns[i]) - len(bottns[i]) + 1
            secln = signs[i] + ' ' * diffdig + bottns[i]
        else:
            secln = signs[i] + ' ' + bottns[i]
        print('{:>6}'.format(secln), end='    ')
    print()

    # print dashes
    for i in range(len(signs)):
        maxn = max((len(topns[i]), len(bottns[i])))
        print('{:>6}'.format(('-' * (maxn + 2))), end='    ')
    print()

    # print results if b = True
    if b:
        for i in range(len(results)):
            print('{:>6}'.format(results[i]), end='    ')
    print()


        

        
#l = ["32 + 698", {1, 2, 3}, "3801 - 2", 5]
l = ["32 + 698", "3801 - 2"]
#arithmetic_arranger(l, True)

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 19999", "523 - 49"], True))

print(arithmetic_arranger(["32 + 8", "1 / 3801", "9999 - 9999", "523 - 49"]))

# p = '32 + 8'   
# p_pos = p.find('+')
# m_pos = p.find('-')
# x_pos = p.find('*')
# d_pos = p.find('/')
# print(p_pos, m_pos, x_pos, d_pos)

# print()
# tn = '32.5 '.strip()
# bn = '   80'.strip()
# if not tn.isdigit() or not bn.isdigit:
#     print('NOT INTEGERS')
# else:
#     print(tn, bn, int(tn) - int(bn), tn + bn)






    

    

# aritmetic_arranger([])
# aritmetic_arranger([i for i in range(10)])
# print(aritmetic_arranger([])[0])
# print(aritmetic_arranger([]))


