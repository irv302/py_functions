# Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n

def sum_to(n):
    sum = list(range(n+1))
    i = 0
    for num in sum:
        i = i + num
        print(i)

sum_to(5)
# >15


# Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
    new = 0 
    for num in list:
        if num > new:
            new = num
    print(new)

scroll = [23, 46, 9, 222, 90, 35]
largest(scroll)

# >222

# Write a function named occurancesthat takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string1, string2):
    sum = 0
    for letter in string1:
        if string2 == letter:
            sum = sum + 1
    print(sum)

occurances('petter pipper picked a pack of pickled peppers', 'p')
# > 10

# Write a function named productthat takes an arbitrary number of numbers, multiplies them all together, and returns the product.

def product(*arbitrary):
    prod = list(arbitrary)
    group = 1 
    for num in prod:
        group = group * num 
    print(group)

product(1, 2, 6, 8, 9)
#> 864
