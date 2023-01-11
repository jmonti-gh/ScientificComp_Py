''' Scientific Computing with Python - Project 1: Arithmetic Formatter '''

# arithmetic_arranger.py

def arithmetic_arranger(problems, answers=False):
    # check number of problems limit. Max is 5
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # strings (lines) wher save numbers, signs, and resutls
    ln1, ln2, ln3, ln4 = '', '',  '', ''
   
    # parse problems
    for p in problems:                   # for e/problem
        # check wrong operators (only '*' & '/' )
        if '*' in p or '/' in p:
            return "Error: Operator must be '+' or '-'."
       
        # split to obtanin topn, sign, bottn
        topn = p.split()[0]     # other ver: .strip() for wrong spaces
        sign = p.split()[1]
        bottn = p.split()[2]
        # don't check if len(p.split()) > 3 

        # if operands are not integers
        if not topn.isdigit() or not bottn.isdigit():
            return "Error: Numbers must only contain digits."
        
        # check operands witth (max 4 digis)
        if len(topn) > 4 or len(bottn) > 4:
            return "Error: Numbers cannot be more than four digits."

        # calc. answer for future purpose & def problems-separator
        ans =  str(eval(p))
        psep = ' ' * 4

        # now i need to know te relavive witdhs of operands
        ltop, lbott = len(topn), len(bottn)
        diffl = abs(ltop - lbott)
        
        # add necesary spaces to shorter number
        if ltop > lbott:
            bottn = ' ' * diffl + bottn     # add spcs to shoter
            topn = ' ' * 2 + topn           # add 2 spcs to topn (sign+spc)
        else:
            topn = ' ' * (diffl + 2) + topn  # (diffl + 2) for sign + spc
        
        # build the complete strings for every row, r1 = topn
        r2 = sign + ' ' + bottn     
        r3 = '-' * (len(r2))           # Operation ansswer separator
        # for r4 complete w/spcs to have the same width as r3 (right alingn)
        r4 = (len(r3) - len(ans)) * ' ' + ans

        # build the complete lines w/all the prblems
        ln1 += topn + psep
        ln2 += r2 + psep
        ln3 += r3 + psep
        ln4 += r4 + psep

    # buil final result upon second argumnnet (answers) & del final spaces
    layout = ln1.rstrip() + '\n' + ln2.rstrip() + '\n' + ln3.rstrip()
    if answers: layout += '\n' + ln4.rstrip()

    return layout
   
