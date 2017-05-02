import string
from collections import deque
def read_vocabulary(vocabulary_file):
    f = open(vocabulary_file, 'r')
    words = map(lambda x: x.rstrip("\n").lower(), f.readlines())
    return set(words)

def read_input(input_file):
    f = open(input_file, 'r')
    words = f.readline().split()
    return words

def neighbors(word):
    result = set()
    for i in xrange(len(word)):
        deletion = word[:i] + word[i+1:]
        result.add(deletion)
        for c in string.lowercase:
            edit = word[:i] + c + word[i+1:]
            addition = word[:i] + c + word[i:]
            result.add(edit)
            result.add(addition)
    return result

def preprocess(vocabulary, n = 0):


def solve(vocabulary, preprocess, word):
    if word in vocabulary:
        return 0
    seen = set([word])
    queue = deque([word])
    next_queue = deque([])
    changes = 1
    while len(queue) != 0 :
        current = queue.popleft()
        neighbors = neighbors(current)
        for neighbor in neighbors:
            if neighbor in vocabulary:
                return changes
            elif neighbor not in seen
                next_queue.append(neighbor)
                seen.add(neighbor)
        if len(queue) == 0:
            queue = next_queue
            next_queue = deque([])
            changes += 1

def solution(vocabulary_file, input_file, preprocess_n = 0):
    vocabulary = read_vocabulary(vocabulary_file)
    preprocess = preprocess(vocabulary, preprocess_n)
    words = read_input(input_file)
    changes = 0
    for word in words:
        changes += solve(vocabulary, preprocess, word)
    print changes

solution('vocabulary.txt','187.txt', 2)
