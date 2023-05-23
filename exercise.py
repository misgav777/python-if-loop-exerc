######## exercise 1 ######
def wholenumber(num):
    return [i for i in range(1, num + 1) if num % i == 0]


# res = wholenumber(100)
# print(res)

######## exercise 2 ######
def until_negative_num():
    user = 0
    count = 0
    sum = 0
    while user >= 0:
        user = int(input('Enter a number please '))
        sum += user
        count += 1
        print(f'Avarage is {sum // count}')
        print(f'Sum is {sum}')
        # user = int(input('Enter a number please '))


until_negative_num()

######## exercise 3 ######


def say_somthing():
    arr = []
    while True:
        user = input('Say something ').lower()
        arr.append(user)
        if list(set([x for x in arr if arr.count(x) >= 3])):
            return


# say_somthing()

######## exercise 4 ######
def bigger(lst1, lst2):
    lst1_score = 0
    lst2_score = 0
    for i in range(len(lst1)):
        if lst1[i] > lst2[i]:
            lst1_score += 1
        elif lst1[i] == lst2[i]:
            lst1_score += 1
            lst2_score += 1
        else:
            lst2_score += 1
    print(f'Lst 1 is the winner' if lst1_score >
          lst2_score else 'Lst 2 is the winner')


lst1 = [1, 2, 34, 56, 7, 8, 8]
lst2 = [1, -2, -34, 56, -7, 8, 8]
# bigger(lst1, lst2)
