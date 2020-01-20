import tty,sys,termios

class _inputtake:
    '''class to take input'''
    def __init__(self):
        '''init def to take input'''
        self.__a = 4 # random
 
    def __call__(self):
        '''def to call function'''
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar
