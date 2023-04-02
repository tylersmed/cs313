import sys

def spelling_test(s, l):
    thinned_list = thin_frag_list(s, l)
    all_permutations = spelling_test_helper(s, thinned_list)
    for perm in all_permutations:
        strng = ''
        for fragment in perm:
            strng += str(fragment)
        if s in strng:
            return True
    return False

def spelling_test_helper(s, l):
    if len(l) == 1:
        return [l]
    lst = spelling_test_helper(s, l[1:])
    x = l[0]
    perms = []
    for i in range(len(lst)):
        if type(lst[i]) == str:
            lst[i] = list(lst[i])

    for perm in lst:
        for i in range(len(perm)+1):
            perms.append(perm[:i] + [x] + perm[i:])
    return perms

# this is an attempt to bring down the program run time since my code has the horrendeous time complexity
# of at least O(N!). This should work for everything in theory but the program times out once N gets above 12 or so.
def thin_frag_list(s, l):
    new_list = []
    for frag in l:
        if frag in s:
            new_list += [frag]
    return new_list




def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()
