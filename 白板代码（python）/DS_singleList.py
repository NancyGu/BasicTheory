class Node():
    def __init__(self,v,p):
        self.var = v
        self.next = p
class List():
    def __init__(self):
        self.head = None
    def add_node(self,v):
        if self.head is None:
            # print("add in head" + str(v))
            self.head = Node(v,None)
        else:
            # print("add in head next" + str(v))
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(v,None)


    def print_list(self):
        temp_point = self.head
        if not temp_point:
            print("the list is None!")
        else:
            # print("the list is:")
            while temp_point:
                print(temp_point.var,temp_point.next)
                temp_point = temp_point.next

if __name__ == '__main__':
    list_ins = List()


    list_ins.add_node(1)
    list_ins.add_node(2)
    list_ins.add_node(3)
    list_ins.print_list()