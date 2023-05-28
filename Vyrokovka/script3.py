# function that takes input as file name.
# read all lines from the file
# wrap every word from provided list in markdown bold tags
# write the output to a new file

import sys

def bold_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("output2.txt", "w", encoding="utf-8") as f:
        for line in lines:
            for word in line.split():
                if word in ["Důsledek"]:
                    f.write("**{}** ".format(word))
                else:
                    f.write("{} ".format(word))
            f.write("\n")

if __name__ == "__main__":
    bold_words("output.txt")