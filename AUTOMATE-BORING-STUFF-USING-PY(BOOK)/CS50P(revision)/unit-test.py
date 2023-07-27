from square import square

def main():
    test_square()

#without using assert
"""
def test_square():
    if square(2) != 4:
        print(' 2 square wasnt 4')
    if square(3) != 9:
        print('3 square wasnt 9')
    else:
        print('workin')
"""


"""
def test_square():
    try:
        assert square(2) == 4
        
    except AssertionError:
        print('2 square isnt showing 4')

    try:
        assert square(3) == 9
    except AssertionError:
        print('3 square isnt showing 9')

    try:
        assert square(-2) == 4
    except AssertionError:
        print('-2 squared was not 4')

    try:
        assert square(-3) == 9
    except AssertionError:
        print('-3 squared was not 9')
    
    try:
        assert square(0) == 0
    except AssertionError:
        print('0 squared was not 0')
"""

#with pytest (by writing pytest in terminal and <filename>.py)
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    

if __name__ == "__main__":
    main()