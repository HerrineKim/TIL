rest_li = []

for i in range(10):
    rest_li.append(int(input()) % 42)
    
print(len(set(rest_li)))