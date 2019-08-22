
# Counting occurence of word in a document
import glob

files = glob.glob('*.txt')
print(files)
file_count = len(files)
for fname in files:
# word = input("Enter word to be searched:")
    k = 0

    with open(fname, 'r') as f:
        for line in f:
            words = line.split()

            for i in words:
                # rem = re.sub['a-zA-Z'], ' ', words[i])
                '''count occurence of particular word
                # if (i == word):
                #     k = k + 1
                '''
                k+=1
    print("Occurrences of the word in {} document is:".format(fname))
    print(k)

# Renaming the files in a directory using pyton
import os
path =  os.getcwd()
# listing the content of directory (path) in a list form. Includes subfolders as well
filenames = os.listdir(path)


# Keeping only filenames with particular extention because we dont need subfolders

new_filenames = [x for x in filenames if x.lower().find(".txt") != -1]

# Renaming files in directory with uppercase and replacing space with _
for filename in new_filenames:
    # os.rename(filename, filename.replace(" ", "-").lower())
    os.rename(filename, filename.lower())


'''
Program for natural sorting order
'''

import re


def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s


def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    # return [ tryint(c) for c in re.split('([0-9]+)', s) ]
    return [tryint(c) for c in re.split('r[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', s)]


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)
    return l


l = ["Something22", "something10", "something7", "something1", "something3"]
# lowering the case so that unicode values of strings are on same scale
l1 = [x.upper() for x in l]

sort_nicely(l1)
print(l1)