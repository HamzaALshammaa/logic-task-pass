def remove_char(str, char):
    return str.replace(char, '')


def primes(start, end):
    primes_given = []
    for num in range(start, end):
        if num > 1:
            for num2 in range(2, int(num/2)+1):
                if num % num2 == 0:
                    break
                else:
                    primes_given.append(num)
    return primes_given


def repeted(string, character):
    count = 0
    list_string = list(string)
    for i in list_string:
        if i == character:
            count += 1
    print(count)
