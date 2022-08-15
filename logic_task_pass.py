def remove_character(string, character):
    return string.replace(character, " ")


string1 = "hi i am hamza"
character = 'a'
new_string = remove_character(string1, character)
print(new_string)

start = int(input("enter the first number in the range: "))
end = int(input("enter the last number in the range: "))
primes_given = []
for num in range(start, end):
    if num > 1:
        for num2 in range(2, num):
            if num % num2 == 0:
                break
            else:
                primes_given.append(num)
print(primes_given)


def repeted(string, character):
    count = 0
    list_string = list(string)
    for i in list_string:
        if i == character:
            count += 1
    print(count)


string = repeted("hi i am hamza", 'a')
