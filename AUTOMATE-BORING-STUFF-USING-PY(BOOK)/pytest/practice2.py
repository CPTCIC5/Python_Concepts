from practice import isOdd

def test_odd():
    for i in range(11,3):
        print(i)
        assert isOdd(i) == i
        

test_odd()