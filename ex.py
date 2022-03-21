# Implenmatatian of inverse_cascade
from asyncio.windows_events import NULL
from copy import copy


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

def combo(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a//10, b//10) * 10 + a % 10
    return min(combo(a//10, b) * 10 + a % 10, \
                combo(a, b//10) * 10 + b % 10)

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def finder(t,phrase):
    if is_leaf(t):
      return phrase in label(t)
    return phrase in label(t) or bool(sum(finder(b, phrase) for b in branches(t)))

def filter_tree(t, phrase):
    """
    >>>t = tree('abc', [tree('def',[tree('qwe'), tree('ppp')]), tree('deg', [tree('xyy', [tree('l', [tree('o')])]),tree('y')])])
    >>>filter_tree(t)
    """
    if is_leaf(t):
        if phrase in label(t):
            return copy_tree(t)
    # return tree(label(t), [filter_tree(b, phrase) for b in branches(t) if finder(b, phrase)])
    bran = []
    for b in branches(t):
        tmp = filter_tree(b, phrase)
        if tmp != NULL:
            bran = bran + [tmp]
    if bran == []:
        if phrase in label(t):
            return tree(label(t))
        else:
            return NULL
    return tree(label(t), bran)


# t = tree('abc', [tree('def',[tree('qwe'), tree('ppp')]), tree('deg', [tree('xyy'), tree('y')]), tree('xyz', [tree('deg', [tree('o'), tree('pde')])])])
# f = filter_tree(t,'de')
# print_tree(t)
# print_tree(f)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    cache = {}
    def memoried(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoried