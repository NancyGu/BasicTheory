# 2018-05-16
# list reverse we need to consider the length of list:
#  1- recursion
#  2- iteration = non-recursion
from DS_singleList import Node,List

def reverseList( head ):
    # two nodes plus can be reversed
    if head is None or head.next is None:
        #print("It's null list, we can't reverse")
        return head

    #new_head = reverseList(head.next)
    #head.next.next = head
    #head.next = None
    #return new_head

    # It's okey
    newhead = reverseList(head.next)
    newhead.next, head.next = head.next, None
    return newhead


def reverseList_complex( head ):
    pnow , pre, pnext = head, None ,None
    newHead = None
    while pnow:
        pnext = pnow.next
        if pnext is None:
            newHead = pnow
        pnext,pre,pnow = pre,pnow,pnext
    return newHead



if __name__ == '__main__':

    List = List()
    List.add_node(1)
    List.add_node(2)
    List.add_node(3)
    List.add_node(4)
    #List.print_list()

    #List.head = reverseList(List.head)
    List.head = reverseList_complex(List.head)
    List.print_list()