''' https://www.youtube.com/watch?v=-9TfJF2dwHI '''

# dow.py could be a name (date of week)

# trin = '  \n \t  From car@mozo.edu sun 5 78'
# print(trin)
# print(len(trin))
# print(trin.strip())
# print(trin.strip().split())
# print(trin.startswith('From'))

while True:
    try:
        sfn = input('Enter a file name:  ')
        fh = open(sfn)
        print(fh)
    except IOError as e:
        print(e)
        print('Invalid file name, try again...')
    else:
        cnt_Fromln = cnt_ln = 0
        for line in fh:
            cnt_ln += 1
            line = line.strip()
            # better guardian here do not process blanks
            if not line.startswith('From'):
                continue
            wds = line.split()
            # another guardian for the lengh of line
            if len(wds) < 3:
                continue
            # guardian in compound as an example
            # if len(wds) < 3 or wds[0] != 'From':
            #   continue
            cnt_Fromln += 1
            print('ln: {:>5} - From appearance: {:>3}' 
                ' - dow: {}'.format(cnt_ln, cnt_Fromln, 
                wds[2]))
        fh.close()
        break



