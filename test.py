import sys

def cat():
    print('Miao')
def dog():
    print('Woof')
    print('Hahahhaha')
def default():
    print('Hello')

if __name__ == "__main__":
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()
