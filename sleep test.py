import time

def sleeper():
    while True:
        # Get user input
        num = input('How long to wait: ')
 
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
 
        # Run our time.sleep() command,
        # and show the before and after time
        print('Before: %s' % time.ctime())
        time.sleep(num)
        print('After: %s\n' % time.ctime())
 
 
#try:
#    sleeper()
#except KeyboardInterrupt:
#    print('\n\nKeyboard exception received. Exiting.')
#    exit()

def test():
    try:
        time.sleep(5)
    except Exception:
        message()
    else:
        print('This didn\'t work')

def message():
    print('This worked!')
    test()

test()
