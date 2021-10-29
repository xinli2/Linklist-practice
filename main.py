"""
    File: main.py
    Author: Xin Li
    Purpose: In this program i will write a handful of functions
    that manipulate lists. I also write one function which
    implements a shape, to match a reference diagram that
    teacher given me.
"""
import list_node

def reverse_list(old_head):
    print("--- BEFORE THE LOOP ---")
    print(f"original list: {old_head}")
    if old_head == None:
        return None
    else:
        new_head = old_head
        old_head = old_head.next
        new_head.next = None
        print(f"old: {old_head}")
        print(f"new: {new_head}\n")
    while old_head is not None:
        temp = old_head
        old_head = old_head.next
        temp.next = new_head
        new_head = temp
        print(f"old: {old_head}")
        print(f"new: {new_head}\n")
    return new_head

def accordion(old_head):
    if old_head == None or old_head.next == None:
        return None
    else:
        new_head = old_head.next
        cur = old_head.next
    while cur is not None and cur.next is not None:
        cur.next = cur.next.next
        cur = cur.next
    return new_head

def insert_at(old_head, new_node, pos):
    cur  = old_head
    count = 0
    while cur is not None:
        count += 1
        cur = cur.next
    assert pos >= 0
    assert pos <= count
    if old_head ==None:
        return new_node
    if pos  == 0:
        new_node.next = old_head
        old_head = new_node
        return old_head
    elif pos == count:
        cur  = old_head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        return old_head
    else:
        cur  = old_head
        count = 0
        while count != pos-1:
            count += 1
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        return old_head


def too_many_aliases():
    lst = ['','','','']
    lst_1 = ['','']
    lst_2 = ['','']
    lst_3 = [11,22]
    lst_4 = [33,44]
    lst[0] = lst_1
    lst[2] = lst_1
    lst[1] = lst_2
    lst[3] = lst_2
    lst_2[0] = lst_3
    lst_2[1] = lst_4
    lst_1[0] = lst_3
    lst_1[1] = lst_4
    return lst
