"""
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each other and
preserving the original order of elements.

Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и
возвращает список элементов без каких-либо элементов с одинаковым значением рядом друг с другом и
сохранение первоначального порядка элементов.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""

def unique_in_order(iterable):
    iterator = iter(iterable)
    # print(iterator)
    next_element_exist = True
    first_el = True
    llist = []
    prevel = None
    while next_element_exist:
        try:
            element_from_iterator = next(iterator)
            # print(type(element_from_iterator))
        except StopIteration:
            next_element_exist = False
        else:
            if first_el:
                llist.append(element_from_iterator)
                first_el = False
            else:
                if prevel != element_from_iterator:
                    llist.append(element_from_iterator)
            prevel = element_from_iterator
    # print(llist)
    return llist



# unique_in_order('AAAABBBCCDAABBB')
# unique_in_order('ABBCcAD')
unique_in_order([1,2,2,3,3])
