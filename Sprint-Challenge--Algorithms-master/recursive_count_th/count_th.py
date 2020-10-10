'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # less than 2 return string
    if len(word) < 2:
        return 0  # f'Please add more characters'
    # if more than 2 do the following
    if len(word) == 2:
        if word == 'th':
            return 1
        else:
            return 0
    # recursion will look at the first two characters + count how many are there
    return count_th(word[0:2]) + count_th(word[1:])

