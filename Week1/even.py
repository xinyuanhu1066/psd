def sum_of_numbers():
    n = input('Please input the maximum number: ')
    n = int(n)
    if n < 1:
        print('Invalid number, must be larger or equal than 1')
    else:
        i = 1
        even_sum = 0
        odd_sum = 0
        even_nums = []
        odd_nums = []
        while i <= n:
            if i % 2 == 0:
                even_nums.append(i)
                even_sum += i
            else:
                odd_nums.append(i)
                odd_sum += i
            i += 1
        print('even numbers:', even_nums)
        print('sum of even numbers:', even_sum)
        print('odd numbers:', odd_nums)
        print('sum of odd numbers:', odd_sum)
    
if __name__ == '__main__':
    sum_of_numbers()
        