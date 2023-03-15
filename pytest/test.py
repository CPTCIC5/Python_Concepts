"""from tryy import square

def test_square():
    assert square(2) ==4"""

"""
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
"""

from tryy import greet


def main():
    test_greet()
def test_greet():
    assert greet() == 'Hello, world'
    #lets test multiple names
    x1=['aryan','nayan','sarthak']
    for i in x1:
        assert greet(i) != f'Hello, {i}'

if __name__ == "__main__":
    main()

