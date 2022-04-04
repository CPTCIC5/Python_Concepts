def solve(s):
    for x in s.split():
        s.replace(x,s.capitalize())
    return s
