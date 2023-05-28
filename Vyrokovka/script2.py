# write a function that takes input as file name.
# Select only rows that start with three hashtags.
# Remove the hashtags and write the output to a new file.
# .txt file can contain undefined characters that dont map

def remove_hashtags(file_name):
    lines = []
    # open file
    with open(file_name, 'r', encoding="utf-8") as f:
        # read lines
        lines = f.readlines()
        # remove hashtags
        lines = [line.replace('#', '') for line in lines if line.startswith('###')]
    # write to new file
    with open('new_file.txt', 'w', encoding="utf-8") as f:
        f.writelines(lines)
        

remove_hashtags('otazky.txt')