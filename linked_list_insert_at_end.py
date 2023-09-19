'''
head -> node1 - > node2 -> null
						-> node3 -> null
'''
class NewNode():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while True:
                if node.next is None:
                    node.next = new_node
                    break
                else:
                    node = node.next

    # Todo Insert node at the beginning
    # Todo Insert node bw 2 nodes
    # Todo Delete node from the end
    # Todo Delete node from the beginning
    # Todo Delete node bw 2 nodes

    def print_list(self):
        node = self.head
        if node is None:
            print("Linked List is empty!")
        else:
            print("HEAD")
            print("|")
            print("|")
            while node is not None:
                print(node.data)
                print("|")
                print("|")
                node = node.next
            print("NULL")

# Todo Merge 2 sorted linked lists
# 1-2-30
# 4-5-60
def merge_lists(list1,list2):
        





list1 = LinkedList()
list1.insert_at_end(NewNode(1))
list1.insert_at_end(NewNode(2))
list1.insert_at_end(NewNode(4))

list2 = LinkedList()
list2.insert_at_end(NewNode(1))
list2.insert_at_end(NewNode(3))
list2.insert_at_end(NewNode(4))

merged_sorted_list = merge_lists(list1,list2)
# list1.print_list()
# list2.print_list()
# merged_sorted_list.print_list()


# num = int(input("Enter Node Count: "))
# for x in range(1,num+1):
#     node = NewNode(f"Node{x}")
#     linked_list.insert_at_end(node)
# linked_list.print_list()

