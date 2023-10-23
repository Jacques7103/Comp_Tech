file = """int main(){
            const float payment = 384.00
        }"""

def keyword(file):
    key_list = []
    file = file.split()
    for word in file:
        words = ''.join(filter(str.isalpha, word))
        if word[0] == "i":
            if word[1] == "n":
                if word[2] == "t" and words[-1] == "t":
                    key_list.append("int")
        elif word[0] == "f":
            if word[1] == "l":
                if word[2] == "o":
                    if word[3] == "a":
                        if word[4] == "t" and words[-1] == "t":
                            key_list.append("float")
        elif word[0] == "w":
            if word[1] == "h":
                if word[2] == "i":
                    if word[3] == "l":
                        if word[4] == "e" and words[-1] == "e":
                            key_list.append("while")
        elif word[0] == "m":
            if word[1] == "a":
                if word[2] == "i":
                    if word[3] == "n" and words[-1] == "n":
                        key_list.append("main")
        elif word[0] == "c":
            if word[1] == "o":
                if word[2] == "n":
                    if word[3] == "s":
                        if word[4] == "t" and words[-1] == "t":
                            key_list.append("const")
    return key_list

print(keyword(file))