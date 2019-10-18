condition_ls = [' ', ',', '.', '!', '@', '#', '%', '^', '&', '*', '(', ')', '<', '>', '/', '?', '"', "'", ':', ';', '{', '}','[', ']','-', '_', '+', '=', '|', '\n', '\t']
string = input('> ')
string_fixed = ' ' + string + ' '
word_count = 0
pos = 0
while pos < len(string_fixed):
    if string_fixed[pos] not in condition_ls :
        while True:
            pos += 1 
            if string_fixed[pos] in condition_ls:
                word_count += 1
                break
    pos += 1
print(word_count)
