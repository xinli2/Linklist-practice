"""
    File: main2.py
    Author: Xin Li
    Purpose: In this program i will write a handful of functions
    that link lists.
"""
from list_node import *

def is_sorted (head):
    '''
        This function takes a single parameter, which is a list,
        and returns True or False, indicating whether or not the
        values in the list are sorted. Note that duplicates may
        exist in the list; these count as being in order.An empty
        list should return True.
    '''
    if head is None :
        return True
    if head.next is None:
        return True
    else:
        cur = head
        while cur.next is not None:
            if cur.val > cur.next.val:
                return False
            cur = cur.next
        return True


def list_sum (head):
    '''This function takes a single parameter, which is a list,
        where all of the values are numeric. It returns the sum of
        all of the values stored in the list. An empty list should
        return zero.
    '''
    sum = 0
    if head is None:
        return 0
    if head.next is None:
        sum = head
        return sum
    else:
        cur = head
    while cur is not None:
        sum += cur.val
        cur = cur.next
    return sum

def pair(list1, list2):
    '''
        This function takes two lists, which may be of different
        lengths (either or both of them might be empty). It builds
        new ListNode objects, where the value of each one is a
        tuple, consisting of one value from the first list, and one
        value from the second list, in the same order as they existed
        in those input lists. If the lists are different lengths,
        then the length of the returned list will be equal to the
        length of the shorter one.
    '''
    if list1 is None or list2 is None:
        return None
    #add new_node
    cur1 = list1
    cur2 = list2
    list3 = ListNode((cur1.val, cur2.val))
    cur3 = list3
    while cur1.next is not None and cur2.next is not None:
        cur1 = cur1.next
        cur2 = cur2.next
        cur3.next = ListNode((cur1.val, cur2.val))
        cur3 = cur3.next
    return list3

def print_pair_partial (list1, list2):
    '''
        This function takes two lists, just like pair(). However
        if they are different lengths, then it keeps on printing
        until the longer one is exhausted - even though it will
        be printing None on one side.
    '''
    cur1 = list1
    cur2 = list2
    while cur1 is not None or cur2 is not None:
        if cur1 is None and cur2 is not None:
            print("1: None","2:", cur2.val)
            cur2 = cur2.next
        elif cur1 is not None and cur2 is None:
            print("1:",cur1.val,"2: None")
            cur1 = cur1.next
        elif cur1 is not None and cur2 is not None:
            print("1:",cur1.val,"2:", cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next


def pair_partial(list1, list2):
    '''
        This function takes two lists, just like pair() and
        print_pair_partial(). Like pair(), it returns a linked list,
        where the values are tuples (one value from each list, in
        each tuple). (It should not print anything out.) Like
        print_pair_partial(), it continues on when it finds the end
        of one of the lists; it returns None as one of the values
        in the tuple when necessary.
    '''
    if list1 is None and list2 is None:
        return None
    #add new_node
    cur1 = list1
    cur2 = list2
    if cur1 is None and cur2 is not None:
        list3 = ListNode((None, cur2.val))
        cur2 = cur2.next
    elif cur1 is not None and cur2 is None:
        list3 = ListNode((cur1.val, None))
        cur1 = cur1.next
    elif cur1 is not None and cur2 is not None:
        list3 = ListNode((cur1.val, cur2.val))
        cur1 = cur1.next
        cur2 = cur2.next
    cur3 = list3
    while cur1 is not None or cur2 is not None:
        if cur1 is None and cur2 is not None:
            cur3.next = ListNode((None, cur2.val))
            cur2 = cur2.next
        elif cur1 is not None and cur2 is None:
            cur3.next = ListNode((cur1.val, None))
            cur1 = cur1.next
        elif cur1 is not None and cur2 is not None:
            cur3.next = ListNode((cur1.val, cur2.val))
            cur1 = cur1.next
            cur2 = cur2.next
        cur3 = cur3.next
    return list3
