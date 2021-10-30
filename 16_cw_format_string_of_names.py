"""
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
Дано: массив, содержащий хеши имен
Возврат: строка, отформатированная как список имен, разделенных запятыми, за исключением последних двух имен,
которые должны быть разделены амперсандом.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]) # returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]) # returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ]) # returns 'Bart'
namelist([]) # returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
Примечание: все хэши предварительно проверены и будут содержать только A-Z, a-z, '-' и '.'.
"""

def namelist(names):
    llen = len(names)
    if (llen == 0):
        return ''
    elif llen == 1:
        return names[0]['name']
    elif llen == 2:
        return names[0]['name']+' & '+names[1]['name']
    else:
        for i in range(llen):
            if i == 0:
                s = names[0]['name']
            elif i < llen-1:
                s = s +', '+names[i]['name']
            else:
                s = s + ' & '+names[i]['name']
        return s



print(namelist([]))  # returns ''
print(namelist([{'name': 'Bart'}]))                                           # returns 'Bart'
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))                         # returns 'Bart & Lisa'
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))     # returns 'Bart, Lisa & Maggie'
