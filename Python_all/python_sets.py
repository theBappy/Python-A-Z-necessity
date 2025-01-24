employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

result  = set(gym_members).intersection(developers)
print(list(result))

result1 = set(employees).difference(gym_members, developers)
print(result1)

if 'Corey' in developers:
    print('Found!')

# Time complexity
# O(n) for list
# O(1) for a set


# # l1 = [1, 2, 3, 1, 2, 3]
# l2 =list(set(l1))
# print(l2)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = {3, 4, 5}

# s4 = s1.intersection(s2 , s3)
# s5 = s3.difference(s1, s2)
# s6 = s2.symmetric_difference(s1)
# print(s6)
# print(s5)
# print(s4)

# s1 = set([1, 2, 3, 4, 5])
# s1.remove(6)
# s1.discard(7)
# print(s1)
# s2 = { 11, 12, 13, 14, 15,11, 12}
# s2.add(7)
# s2.update([8,9,9], s1)