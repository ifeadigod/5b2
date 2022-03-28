# def slugify(word):
#     return word.replace(" ","-").lower()

# print(slugify('How do you cook'))
# def first_last(first, last):
#     a = first[:2]
#     b = last[-2:]

#     return a+b

# print(first_last('Adaobi', 'United'))

# x_mean  = map(lambda x : (x-avr)**2, mapped)
# std = sqrt(sum(x_mean)/len(mapped))
# print(f"Standard deviation: {std}")


# from re import X


# v = lambda x : (15 + x)
# print(v(5))


# life = lambda x,y : x*y
# print(life(10,10))

# from posixpath import split


# def slugify(word):
#     return word.swapcase()

# print(slugify('this life no balance'))
# print(slugify('THIS LIFE NO BALANCE'))

# file_name = input('Write any file name\n')
# print(file_name.split(".")[-1])


# num = [1,2,3,4,5]
# x_num = map(lambda x: x*3, num )
# print(x_num)

# x_tri = map(lambda x: x**2, num)
# print(x_tri)


#list
#The list is a collection of data that is enclosed in square bracket separated with a comma
#properties
#it is mutable;it can be changed
#it is ordered
#set
#turpo
#dictionary

#ways of calling a list
# a = []
# print(type(a))

# b = list()

# a = [1,2,3,4,5,6,7,8,9,10]
# x = [1,2,3,4,5,6,7,8,9,10]
# slice(a[1,4,6])
# print(a[4])
#print(a+x)
# a[4] = 20
# print(a[4])

# a = [2,3,4,2[2,3,4,5, [4,52,2],5],24]
# v = a[4][4][1]  

from audioop import reverse


v = [1,2,3,4,5,6,7]
v.sort()
print(v)
print(v[1],v[5])

print(v[:3])
print(v[-3:])

def largest(arr:list, k:int):
    """"this function returns the highest k value in an array:arr"""
    arr.sort(reverse=True)
    return arr[:k]

def smallest(arr:list, k:int):
    """"This function returns the lowerst k value in an array: arr"""

    arr.sort()
    return arr[:k]

print(largest([1,1,1,0,0,0,2,-2,-2],2))
print(smallest([1,1,1,0,0,0,2,-2,-2],2))


