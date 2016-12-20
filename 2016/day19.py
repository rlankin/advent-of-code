ELVES = 3014387

def part_1():
    """Part 1 is just the Josephus Problem:
    https://en.wikipedia.org/wiki/Josephus_problem
    https://www.youtube.com/watch?v=uCsD3ZGzMgE
    """
    l = ELVES - 2 ** (ELVES.bit_length() - 1)
    print('Part 1: {}'.format(l * 2 + 1))

"""
This solution was taken entirely from here: https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/dbdobax/
"""
def f(n,p=1):
  while 3*p<=n: p*=3
  if n==p: return n
  return n-p+max(n-2*p,0)

def part_2():
    print('Part 2: {}'.format(f(ELVES)))

part_1()
part_2()
