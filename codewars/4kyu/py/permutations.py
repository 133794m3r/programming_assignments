"""
desc:
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Solution.
Create all permutations of the input string of the length of said string. 
Then put them into a set as a set has unique values. Then join all items of each list.
As the permutations are lists, then return a list of those permutated strings.
Thanks to them having itertools this was super easy.
"""
def permutations(string):
    from itertools import permutations
    return [ ''.join(x) for x in set(permutations(string,len(string))) ]
