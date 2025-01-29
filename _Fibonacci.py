def max_fibonacciness(t, test_cases):
    results = []
    for a1, a2, a4, a5 in test_cases:
        possible_a3_values = [a4 - a2, a5 - a4, a1 + a2]
        max_fib_count = 0
        
        for a3 in possible_a3_values:
            count = 0
            if a3 == a1 + a2:
                count += 1
            if a4 == a2 + a3:
                count += 1
            if a5 == a3 + a4:
                count += 1
            
            max_fib_count = max(max_fib_count, count)
        
        results.append(max_fib_count)
    
    return results


t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]


for result in max_fibonacciness(t, test_cases):
    print(result)
