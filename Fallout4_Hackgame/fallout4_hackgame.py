# a function for output possible answers
def print_pool(pool):
    print('Possible answers:')
    print('------------------------------')
    for ans in pool:
        print("\t", ans)
    print('------------------------------')

    return None

def str_matches(str1, str2):
    matches = 0

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            matches = matches + 1

    return matches
# get puzzle
fname = "puzzle.txt"

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

ans_pool = list()
for word in fh:
    ans_pool.append(word.strip())

print_pool(ans_pool)

# try
try_limit = 4
while try_limit > 0:
    input_ans = input('Please enter the word you tried:')
    test_ans = input_ans.upper()

    if len(test_ans) == 0 or test_ans not in ans_pool:
        print('Please enter a word in pool')
        continue

    input_result = input('Please enter the result you got:')
    try:
        test_result = int(input_result)
    except:
        print('Please enter matches')
        continue

    try_limit = try_limit - 1

    # get matches for last pool
    # copy list to prevent from count error
    temp_pool = ans_pool[:]
    for word in temp_pool:
        match_cnt = str_matches(test_ans, word)

        # reduce possible by responce
        if match_cnt != test_result:
            ans_pool.remove(word)

    print_pool(ans_pool)

    # extra end up condition
    pool_cnt = len(ans_pool)
    if pool_cnt <= try_limit or pool_cnt == 1:
        break

