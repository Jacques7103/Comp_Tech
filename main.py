def keyword_count(file):
    keywords = ["int", "float", "while", "main", "const"]
    key_count = {key: 0 for key in keywords}
    
    keyword_buffer = ""
    
    for char in file:
        if char.isalpha():
            keyword_buffer += char
        else:
            if keyword_buffer in keywords:
                key_count[keyword_buffer] += 1
            keyword_buffer = ""
    
    return key_count

file = """int main(){
            const float payment = 384.00
            while (true) {
                int x = 10;
            }
        }"""

keyword_counts = keyword_count(file)

for key, count in keyword_counts.items():
    print(f"'{key}' appears {count} times.")