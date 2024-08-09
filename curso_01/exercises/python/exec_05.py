linguagens = ['python', 'java', 'c++', 'javascript', 'c#', 'go', 'r', 'cobol', 'ruby', 'lisp']
print(linguagens[:4])

maiores4 = []
for item in linguagens:
    if len(item) >= 4:
        maiores4.append(item)
print(maiores4)

j_ou_c = []
for item in linguagens:
    if item[0] == 'c' or item[0] == 'j':
        j_ou_c.append(item)
print(j_ou_c)