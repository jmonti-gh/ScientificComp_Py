''' https://www.youtube.com/watch?v=-9TfJF2dwHI '''

# dow.py could be a name (date of week)

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
            # better guardian here do not process blanks
            if line == '':
                continue
            wds = line.strip().split()
            if wds == []: # or if len(wds) < 1
                continue
            elif wds[0] != 'From':
                continue
            else:
                cnt_Fromln += 1
                #print(count, wds, wds[2])
                #print(count, '.', wds[2], '- ', line.strip())
                #print('ln:', cnt_ln, '- From apearence:',
                #cnt_Fromln, ' - dow:', wds[2])
                print('ln: {:>5} - From appearance: {:>3}' 
                ' - dow: {}'.format(cnt_ln, cnt_Fromln, 
                wds[2]))
        fh.close()
        break



