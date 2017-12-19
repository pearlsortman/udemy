# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
#
# for item in shopping_list:
#     if item == 'spam':
#         # print('I am ignoring ' + item)
#         # continue
#         break
#
#     print('Buy ' + item)

meal = ['egg', 'bacon', 'toast', 'cheese']
badItem = ''

for item in meal:
    if item == 'bacon':
        badItem = item
        break
else:
    print("I'll have a plate of that, please.")

if badItem:
    print('Can I please have something other than {}?'.format(badItem))
