#!/usr/bin/env python
'''
Software Description
=====================

There is a deck of cards, and two piles they can be put in.
Initially all cards are in pile A, and pile B is empty.
A dealer is instructed to shuffle the deck as follows:

1. Pull a card from the top of pile A, and put on pile B
2. Pull a card from the top of pile A, and put it in the bottom of pile A
3. Repeat steps 1 & 2 until pile A is empty.

This counts as one round.

'rounds_till_original(decksize)' computes the number of rounds it takes for the
deck to return to its original order.  The algorithm efficiently computes this
by taking Least Common Multiple of cycles cards take though the deck.


Problem Description
======================

Write a test suite for 'rounds_till_original(decksize)'.

Solution will be evaulated by:

1. How you verify the correcness of the algorithm.
2. How well your suite catches regressions.
3. The maintenance burden of your suite.
4. Code clarity and documentation.

Feel free to use any native python2/3 library.

'''


def shuffle_one_round(deck):
    """Shuffle the deck one round."""
    ret = list()
    while deck:
        ret.append(deck.pop())
        if deck:
            deck.insert(0, deck.pop())
    return ret


def get_length_of_closed_loops_in_graph(deck):
    """Treat deck as a graph:
        - Trace the path each card takes.
        - Return the length of each closed loop.
    """
    closed_loops = []
    # for start in xrange(len(deck)):
    for start in range(len(deck)):
        index, loop = start, 0
        while deck[index] is not None:
            loop = loop + 1
            deck[index], index = (None, deck[index])
        if loop:
            closed_loops.append(loop)
    return closed_loops


def gcd(a, b):
    """Compute the greatest common divisor."""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the least common multiple."""
    return a * b / gcd(a, b)


def lcms(*args):
    """Compute the least common multiple of n numbers."""
    ret = 1
    for arg in args[0]:
        ret = lcm(ret, arg)
    return ret


def rounds_till_original(decksize):
    """Compute the number of rounds it takes to shuffle a
       deck back to original order.
    """
    # deck = range(decksize)
    deck = list(range(decksize))
    shuffled_deck = shuffle_one_round(deck)
    loops = get_length_of_closed_loops_in_graph(shuffled_deck)
    return lcms(loops)


if __name__ == "__main__":
    import sys
    import os
    if len(sys.argv) == 2:
        # Check valid input, non-negative integer only
        try:
            num_cards = int(sys.argv[1])
            assert num_cards >= 0
            # Prevent the calculation exceed the memory size
            limit_num = 10 ** 5
            # Adjust the number (10 ** 5) as you need
            if num_cards > limit_num:
                print('Number of rounds needed is too large. Please input smaller than', limit_num)
            else:
                print('Number of rounds needed to restore: ', rounds_till_original(int(sys.argv[1])))
        except:
            print('Number of cards should be one non-negative integer.')
    else:
        print("Usage: {} <deck size>".format(os.path.basename(__file__)))

