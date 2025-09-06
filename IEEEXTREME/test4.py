def solve():
    import sys
    
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    
    def calculate_sum(k):
        if k <= 0:
            return 0
        
        total_sum = 0
        digits = 1
        start = 1
        
        while k > 0:
            if digits == 1:
                if k >= 9:
                    total_sum += 45  # Sum of 1,2,3,4,5,6,7,8,9
                    k -= 9
                else:
                    total_sum += k * (k + 1) // 2  # Sum of 1 to k
                    k = 0
            else:
                count = 9 * (10 ** (digits - 1))  # Count of d-digit numbers
                total_digits_in_range = count * digits
                
                if k >= total_digits_in_range:
                    # Use mathematical formula for sum
                    # Sum of digits in range [10^(d-1), 10^d - 1]
                    
                    # Each position contributes differently
                    range_sum = 0
                    
                    # For each digit position
                    for pos in range(digits):
                        # Contribution from this position
                        if pos == digits - 1:  # Most significant digit
                            # Digits 1,2,...,9 each appear count/9 times
                            for digit in range(1, 10):
                                range_sum += digit * (count // 9)
                        else:
                            # Digits 0,1,2,...,9 each appear count/10 times
                            for digit in range(10):
                                range_sum += digit * (count // 10)
                    
                    total_sum += range_sum
                    k -= total_digits_in_range
                else:
                    # Partial range - calculate directly for remaining
                    complete_nums = k // digits
                    partial_digits = k % digits
                    
                    # Sum complete numbers
                    for i in range(complete_nums):
                        num = start + i
                        while num > 0:
                            total_sum += num % 10
                            num //= 10
                    
                    # Sum partial number
                    if partial_digits > 0:
                        num_str = str(start + complete_nums)
                        for i in range(partial_digits):
                            total_sum += int(num_str[i])
                    
                    k = 0
            
            start *= 10
            digits += 1
        
        return total_sum
    
    for i in range(1, t + 1):
        k = int(data[i])
        print(calculate_sum(k))

solve()