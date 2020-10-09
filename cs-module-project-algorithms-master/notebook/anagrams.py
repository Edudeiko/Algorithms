from pprint import pprint
import time

# Couple of hours to run?
# O(n^2)
'''
words = []

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.append(w)

print(words[-10:])

def is_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
    # w1_letters = list(word1)
    # w2_letters = list(word2)

def anagrams():
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                continue

            if is_anagrams(word1, word2):
                print(word1, word2)

print(anagrams())  # [listen, silent, ...]
'''

# we want O(n log n) or better

'''
words = {}

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        l = len(w)

        if l not in words:
            words[l] = []

        words[l].append(w)

# print(words[8])

def is_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

print(sorted(words.keys()))
def anagrams():
    for wordlen in range(10, 21):
        if wordlen == 19: continue
        for word1 in words[wordlen]:
            for word2 in words[wordlen]:
                if word1 == word2:
                    continue

                if is_anagrams(word1, word2):
                    print(word1, word2)

print(anagrams())
'''
start = time.process_time()

words = []

with open("words.txt") as f:

    for w in f:
        w = w.strip()
        words.append(w)
        
def is_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def anagrams():
    result = {}
    results_by_len = {}

    longest_sig = None
    longest_len = -1

    for w in words: # O(n) over the number of words
        signature = "".join(sorted(w))

        if signature not in result:
            result[signature] = []

        result[signature].append(w)

        if len(result[signature]) >= longest_len:
            longest_len = len(result[signature])
            longest_sig = signature
    '''
    for sigs in result:  # O(n) over the number of sigs
        l = len(result[sigs])

        if l not in results_by_len:
            results_by_len[l] = []

        results_by_len[l].append(result[sigs])

    for ii in range(3,7):
        pprint(results_by_len[ii])
    '''
    return result # [longest_sig]  # result

pprint(anagrams())
elapsed = (time.process_time() - start)
print(f'time to process: {elapsed:.3f}')
