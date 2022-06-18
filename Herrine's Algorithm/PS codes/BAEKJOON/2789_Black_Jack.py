n, m = map(int, input().split())
numbers = list(map(int, input().split()))
combination = []

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:						
            if num1 + num2 + num3 <= m \
                    and num1 != num2 \
                    and num1 != num3 \
                    and num2 != num3:				
                possible_comb = [num1, num2, num3]	
                combination.append(possible_comb)	

combination_sum = [sum(i) for i in combination]		

print(max(combination_sum))
