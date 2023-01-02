''' https://www.youtube.com/watch?v=il1j4wkte2E '''

# shout.py could be a good name for this program

while True:
    try:
        sfn = input('Enter a file name:  ')
        fh = open(sfn)
        print(fh)
    except IOError as e:
        print(e)
        print('Invalid file name, try again...')
    else:
        count = 0
        for line in fh:
            print(line.rstrip().upper())
            count += 1
            if count == 9:
                break
        fh.close()
        break



