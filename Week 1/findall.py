import re
NAME = 'Daniel Smyth'
user_input = input('Please enter the name you want to search with: ')
print(f'The name entered is: {user_input}')
result_findall_1 = re.findall('Da', NAME)
# print('result_findall_1' + result_findall_1)
result_findall_2 = re.findall('Ma', NAME)
# print('result_findall_2' + result_findall_2)
# SEARCH
result_search_1 = re.search('Da', NAME)
print(f'result_search_1: {result_search_1}')
# SUB
result_search_1 = re.sub('Da', 'Ma', NAME)
print(result_search_1)
result_search_2 = re.sub('Ad', 'Me', user_input)
print(result_search_2)
Name_1 = 'Samuel'
print(f'My name is {Name_1}')