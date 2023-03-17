# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Tyler Smedley

# Student UT EID: tws933

# Course Name: CS 313E

# Unique Number: 52020

# Output: True or False
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    word1 = list(str1)
    word2 = list(str2)
    for char in word1:
        if char not in word2:
            return False
        word2.remove(char)
    return True

def family_in_list(lst, strng):
    for word in lst:
        if are_anagrams(word, strng):
            return True
    return False

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    families_list = [lst[0]]
    for word in lst[1:]:
        if not family_in_list(families_list, word):
            families_list += [word]
    return len(families_list)

def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
