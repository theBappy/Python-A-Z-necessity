# def test_distinct(data):
#     if len(data) == len(set(data)):
#         return True
#     else: 
#         return False
# print(test_distinct([1, 5, 7, 9]))
# print(test_distinct([2, 4, 5, 5, 7, 9]))
# def test_distinct(data):
#     if len(data)== len(set(data)):
#         return True
#     return False
# def test_distinct(data):
#     if len(data) == len(set(data)):
#         return True
#     return False
# def test_distinct(data):
#     if len(data)== len(set(data)):
#         return True
#     return False
# print(test_distinct([1,3,5,7]))
# print(test_distinct([2,4,5,5,7,9]))
# import random
# char_list =['a', 'e', 'i', 'u', 'o']
# random.shuffle(char_list)
# print(''.join(char_list))
# import random
# char_list=[ 'a', 'e', 'i', 'o', 'u']
# random.shuffle(char_list)
# print(''.join(char_list))
# def remove_nums(int_list):
#     position = 3 -1
#     idx = 0
#     len_list = len(int_list)
#     while len_list > 0:
#         idx = (position + idx) % len_list
#         print(int_list.pop(idx))
#         len_list = -1
# nums =[10, 20, 30, 40, 50, 60, 70, 80, 90]
# remove_nums(nums)
# def three_sums(nums):
#     result =[]
#     nums.sort()
#     for i in range(len(nums) -2):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         l, r = i + 1, len(nums-1)
# def three_sums(nums):
#     nums.sort()
#     n = len(nums)
#     result
# def three_sum(nums):
#     nums.sort()
#     n = len(nums)
#     result =[]
#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#     left, right = i + 1, n-1
#     while left < right:
#         total = nums[i] + nums[left] + nums[right]
#         if total == 0:
#             result.append(nums[i], nums[left], nums[right])
#             while left < right and nums[left] == nums[left+1]:
#                 left += 1
#             while left < right and nums[left] == nums[right-1]:
#                 right -= 1
#         elif total < 0:
#             left += 1
#         else: 
#             right -=  1
#     return result
# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))
# def three_sum(nums):
#     nums.sort()
#     n = len(nums)
#     result =[]
#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         left, right = i + 1, n - 1
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#             if total == 0:
#                 result.append(nums[i], nums[left], nums[right])

#             while left < right and nums[left] == nums[left+1]:
#                 left += 1
#             while left < right and nums[right] == nums[right-1]:
#                 right -=1
#                 left +=1
#                 right -=1
#             elif total < 0 :
# numbers =[]
# for num in range(1000):
#     num = str(num).zfill(3)
# print(num)
# numbers.append(num)
# numbers =[]
# for num in range(1000):
#     num = str(num).zfill(3)
# print(num)
# numbers.append(num)
# numbers =[]
# for num in range(1000):
#     num = str(num).zfill(3)
# print(num)
# numbers.append(num)
string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
... (omitting the rest for brevity) ... 
... much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''
# words_list = string_words.split()
# word_freq=  [words_list.count(n) for n in words_list]
# print(word_freq)
# print('Pairs (words and frequencies:\n {})'.format(str(list(zip(words_list, word_freq)))))
# import collections
# import pprint
# file_input = input('File name:')
# with open(file_input, 'r') as info:
#     count = collections.Counter(info.read().upper())
#     value = pprint.pformat(count)
# print(value)
# from GoogleNews import GoogleNews

# def get_top_google_news_stories():
#     # Initialize the Google News object
#     googlenews = GoogleNews(period='1d')  # Last 1 day of news
#     googlenews.search('Top Stories')  # Search for "Top Stories"
#     googlenews.getpage(1)  # Get the first page of results
#     results = googlenews.result()
    
#     print("\n📢 Top Stories from Google News 📢\n")
#     for i, story in enumerate(results[:10], start=1):  # Limit to 10 stories
#         print(f"{i}. 📰 Title: {story['title']}")
#         print(f"   📍 Source: {story['media']}")
#         print(f"   🔗 Link: {story['link']}\n")

# if __name__ == "__main__":
#     get_top_google_news_stories()
# from GoogleNews import GoogleNews
# def get_top_news():
#     googleNews = GoogleNews(period='1d')
#     googleNews.search('Top stories')
#     googleNews.getpage(1)
#     result = googleNews.result()

#     print('\n Top stories from Google news are: \n')
#     for i , story in enumerate(result[:5], start=1):
#         print(f"{i} Title: {story['title']}")
#         print(f" Source: {story['media']}")
#         print(f" Link: {story['link']}")
# if __name__ =='__main__':
#     get_top_news()
# from GoogleNews import GoogleNews
# def get_top_news():
#     googlenews = GoogleNews(period='1d')
#     googlenews.search('Top news')
#     googlenews.getpage(1)
#     results = googlenews.result()

#     print('\n google top news: \n')
#     for i, story in enumerate(results[:10], start=1):
#         print(f"{i} title: {story['title']}")
#         print(f" source: {story['media']}")
#         print(f" link: {story['link']}\n")
# # if __name__ == "__main__":
# get_top_news()
# import pkg_resources
# installed_pkg = pkg_resources.working_set
# installed_pkg_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_pkg])
# for m in installed_pkg_list:
#     print(m)
# import platform as pl
# os_profile = [
#     'architecture',
#     'machine',
#     'node',
#     'platform',
#     'processor',
#     'python_build',
#     'python_compiler',
#     'python_version',
#     'release',
#     'uname',
#     'version',
# ]
# for key in os_profile:
#     if hasattr(pl, key):
#         print( key + ": " +str(getattr(pl, key)()))

# for key in os_profile:
#     if hasattr(pl, key):
#         print(key + ': ' + str(getattr(pl, key)()))
# import itertools
# from functools import partial
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# T = 70
# def check_sum_array(N, *nums):
#     if sum(x for x in nums) == N:
#         return (True, nums)
#     return (False, nums)
# pro = itertools.product(X,Y,Z)
# func = partial(check_sum_array, T)
# sums = list(itertools.starmap(func,pro))
# result = set()
# for s in sums:
#     if s[0] == True and s[1] not in result:
#         result.add(s[1])
#         print(result)
# import itertools
# from functools import partial
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# T = 70
# def check_sum_array(N , *nums):
#     if sum(x for x in nums) == N:
#         return (True, nums)
#     return (False, nums)
# pro = itertools.product(X,Y,Z)
# func = partial(check_sum_array, T)
# sums = list(itertools.starmap(func, pro))
# result = set()
# for s in sums:
#     if s[0] == True and s[1] not in result:
#         result.add(s[1])
#         print(result)
# print(pro)
# print(func)
# print(sums)
# def permnumute(nums):
#     result_perms =[]
#     for n in nums:
#         new_perms =[]
#         for perm in result_perms:
#             for i in range(len(perm)+1):
#                 new_perms.append(perm[:i]+[n]+perm[i:])
#         result_perms = new_perms
#     return result_perms
# my_nums = [1, 2, 3]
# print(my_nums)
# print(permnumute(my_nums))
# def letter_combinations(digits):
#     if digits == '':
#         return []
#     string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#     result =['']
#     for num in digits:
#         temp =[]
#         for an in result: 
#             for char in string_maps[num]:
#                 temp.append(an + char)
#             result = temp
#         return result
# digit_string = '47'
# print(letter_combinations(digit_string))
# digit_string = '29'
# print(letter_combinations(digit_string))
# def add_without_using_plus_operator(a, b):
#     while b != 0:
#         data = a & b
#         a = a ^ b
#         b = data << 1
#     return a
# print(add_without_using_plus_operator(2,10))
# print(add_without_using_plus_operator(-20,10))
# def add_without_plus_operator(a,b):
#     while b != 0:
#         data = a & b
#         a = a ^ b
#         b = data << 1
#     return a
from collections import deque
import re
__operators__= "+-/*"
__parenthesis__= "()"
__priority__ = {
    '+':0,
    '-':0,
    '*': 1,
    '/': 1,
}
def higher_priority(opeator1, operator2):
    return __priority__[opeator1] >= __priority__[operator2]
print(higher_priority('*','-'))
print(higher_priority('+','-'))
print(higher_priority('+','*'))
print(higher_priority('+','/'))
print(higher_priority('*','/'))








      


            


