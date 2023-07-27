from calculator import square

def main():
    test_square()


#100% MANUAL
"""
def test_square():
    if square(2) !=4:
        print('dikkat')
    if square(3) !=9:
        print('dikkt')
"""

#ASSERT
"""
def test_square():
    assert square(2) ==4
    assert square(3) ==9
"""

#ASSERT WITH ERROR HANDLING/EXCEPTION/PROPER NOTATIONS
"""
def test_square():
    try:
        assert square(2) ==4
    except AssertionError:
        print('not 4')
    try:
        assert square(3) ==9
    except:
        print('not 9')
"""
#pytest handles try except,also runs all blocks of code even tho it fails at even 1st/2nd (helps to catch errors/check other functions)
if __name__ == "__main__":
    main()
