''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger_v0.py

def arithmetic_arranger(lst, b=False):
    # check restrictions (number of problems limit restriccions)
    limit, lenght = 5, len(lst)
    if lenght > limit:
        print('Error: Too many problems.')
        return (1, 'Too many problems', lenght)
    elif len(lst) < 1:
        print('Error: Very few problems.')
        return (2, 'Very few problems', lenght)

    # lists were save numbers, signs, and resutls
    topns, signs, bottns, results = [], [], [], []

    cnt, xcod = 0, 0        # problem counter, exit code   
    # parse each problem
    for p in lst:
        cnt += 1
        # check if p is string
        #if type(p) != str :
        if not type(p) is str:
            print("Error: Pobrem must be wirte as strings")
            xcod = (7, 'Invalid problem ', p, ('problem:', cnt))
            print(xcod, '\n')
            continue
        # find invalid signs operations and finish w/error
        for s in ('%', '//', '*', '/', '**'):
            spos = p.find(s)
            if spos != -1:
                print("Error: Operator must be '+' or '-'.")
                xcod = (3, 'Invalid operator ', s, ('problem:', cnt))
                print(xcod, '\n')
                continue  

        # find valid signs positions
        p_pos = p.find('+')
        m_pos = p.find('-')

        # Parse operations & save correct resutls in respective lists
        if p_pos != -1:
            pos = p_pos
            sign = '+'
        elif m_pos != -1:
            pos = m_pos
            sign = '-'
        elif p_pos == -1 and m_pos == -1:   # strings wo/sum or subs
            print("Error: Invalid problem.")
            xcod = (4, 'Invalid problem', "Not '+' or '-' founded",
                        ('problem:', cnt))
            print(xcod, '\n')
            continue
        else:
            print('Siamo Fouri - # Parse operations')
            raise Exception()

        topn = p[:pos].strip()
        bottn = p[(pos+1):].strip()
        # if the operands are not integers
        if not topn.isdigit() or not bottn.isdigit():
            print("Error: Numbers must only contain digits.")
            xcod = (5, 'Not digits ', topn, bottn, ('problem:', cnt))
            print(xcod, '\n')
            continue
        # check operands witth (max 4 digis)
        if len(topn) > 4 or len(bottn) > 4:
            print("Error: Numbers cannot be more than four digits.")
            xcod = (6, 'More than 4 digs ', topn, bottn, ('problem:', cnt))
            print(xcod, '\n')
            continue
        
        # Everything ok, can fill the lists
        # Convert numbers to int
        try:
            topi = int(topn)
            botti = int(bottn)
        except Exception as e:
            print('Siamo Fouri -  # Convert numbers to int ', e)
            raise Exception

        topns.append(topn)
        signs.append(sign)
        bottns.append(bottn)
        # Do operation
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

    # Check really extrange case ...
    if (len(topns) != len(signs) or len(topns) != len(signs) or
        len(topns) != len(bottns)):
        print('Siamo Fouri - # Check really extrange case ...')
        raise Exception()

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


        

        
l = ["32 + 698", {1, 2, 3}, "3801 - 2", 5]
arithmetic_arranger(l, True)

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 19999", "523 - 49"], True)

arithmetic_arranger(["32 + 8", "1 / 3801", "9999 - 9999", "523 - 49"])

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


