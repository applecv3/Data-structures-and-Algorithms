'''
Basic binarysearchtree with linked list.
add new values with 'insert' function
find a certain value with 'search' function
delete a certain value with 'delete' function, it can handle all the cases that can happen
when deleting a node
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        #self.parent = None


class NodeManager:

    def __init__(self):
        self.head = None

    def insert(self, data):#insert a value into a tree
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while True:
                if data < current_node.data:#when the value is smaller than the data in the current node
                    if current_node.left is None:#when the left is empty add the value
                        current_node.left = Node(data)
                        #current_node.left.parent = current_node
                        return
                    else:#when the left is not empty go to the left again
                        current_node = current_node.left
                else:#works same above to the right direction
                    if current_node.right is None:
                        current_node.right = Node(data)
                        #current_node.right.parent = current_node
                        return
                    else:
                        current_node = current_node.right

    def search(self, data):#find a certain value and return True otherwise return False
        if self.head is None:
            return False
        else:
            current_node = self.head
            while True:
                if data == current_node.data:#found the value
                    return True
                elif data < current_node.data:
                    if current_node.left is None:#when not finding the value
                        return False
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        return False
                    else:
                        current_node = current_node.right

    def delete(self, data):#find and delete a certain value
        if self.head is None:
            print('No data to delete')
        else:
            current_node = self.head
            searched = False
            while True:#search the data first.
                if data == current_node.data:
                    searched = True
                    break
                elif data < current_node.data:
                    if current_node.left is None:
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        break
                    else:
                        current_node = current_node.right
            if searched == False:#when not finding the data to delete
                print('No such data to delete')
                return
            #no children case
            if current_node.left is None and current_node.right is None:
                if current_node.parent is None:#when it's the head
                    self.head = None
                elif data < current_node.parent.data:#when the current node is left child of its parent
                    current_node.parent.left = None
                else:
                    current_node.parent.right = None
            #single child case
            elif current_node.left and current_node.right is None:#when the node only has a left child
                if current_node.parent is None:#head case
                    current_node.left.parent = None
                    self.head = current_node.left
                elif data < current_node.parent.data:
                    current_node.parent.left = current_node.left
                    current_node.left.parent = current_node.parent
                else:
                    current_node.parent.right = current_node.left
                    current_node.right.parent = current_node.parent
            elif current_node.left is None and current_node.right:#when the node only has a right child
                if current_node.parent is None:#head case
                    current_node.right.parent = None
                    self.head = current_node.right
                elif data < current_node.parent.data:
                    current_node.parent.left = current_node.right
                    current_node.right.parent = current_node.parent
                else:
                    current_node.parent.right = current_node.right
                    current_node.right.parent = current_node.parent
            #two children case
            elif current_node.left and current_node.right:
                if current_node.parent is None:#head case
                    node_to_delete = current_node
                    current_node = current_node.right
                    while current_node.left:#goes all the way down to the left to get at the smallest value
                        current_node = current_node.left
                    if node_to_delete.right.data == current_node.data:#when it's right under parent
                        current_node.left = node_to_delete.left
                        current_node.left.parent = current_node
                        current_node.parent = None
                        self.head = current_node
                    else:
                        if current_node.right is None:#when the smallest value has no child
                            current_node.left = node_to_delete.left
                            current_node.left.parent = current_node
                            current_node.right = node_to_delete.right
                            current_node.right.parent = current_node
                            current_node.parent.left = None
                            current_node.parent = None
                            self.head =current_node
                        else:
                            current_node.right.parent = current_node.parent
                            current_node.parent.left = current_node.right
                            current_node.left = node_to_delete.left
                            current_node.left.parent = current_node
                            current_node.right = node_to_delete.right
                            current_node.right.parent = current_node
                            current_node.parent = None
                            self.head = current_node
                else:
                    if data < current_node.parent.data:#when the node is to the left of its parent
                        node_to_delete = current_node
                        current_node = current_node.right
                        while current_node.left:#goes all the way down to the left to get at the smallest value
                            current_node = current_node.left
                        if node_to_delete.right.data == current_node.data:#when it's right under parent
                            current_node.left = node_to_delete.left
                            current_node.left.parent = current_node
                            current_node.parent = node_to_delete.parent
                            current_node.parent.left = current_node
                        else:
                            if current_node.right is None:#when the smallest value has no child
                                current_node.left = node_to_delete.left
                                current_node.left.parent = current_node
                                current_node.right = node_to_delete.right
                                current_node.right.parent = current_node
                                current_node.parent.left = None
                                current_node.parent = node_to_delete.parent
                                current_node.parent.left = current_node
                            else:
                                current_node.right.parent = current_node.parent
                                current_node.parent.left = current_node.right
                                current_node.left = node_to_delete.left
                                current_node.left.parent = current_node
                                current_node.right = node_to_delete.right
                                current_node.right.parent = current_node
                                current_node.parent = node_to_delete.parent
                                current_node.parent.left = current_node
                    else:#when the node is to the right of its parent
                        node_to_delete = current_node
                        current_node = current_node.right
                        while current_node.left:
                            current_node = current_node.left
                        if node_to_delete.right.data == current_node.data:
                            current_node.left = node_to_delete.left
                            current_node.left.parent = current_node
                            current_node.parent = node_to_delete.parent
                            current_node.parent.right = current_node
                        else:
                            if current_node.right is None:
                                current_node.left = node_to_delete.left
                                current_node.left.parent = current_node
                                current_node.right = node_to_delete.right
                                current_node.right.parent = current_node
                                current_node.parent.left = None
                                current_node.parent = node_to_delete.parent
                                current_node.parent.right = current_node
                            else:
                                current_node.right.parent = current_node.parent
                                current_node.parent.left = current_node.right
                                current_node.left = node_to_delete.left
                                current_node.left.parent = current_node
                                current_node.right = node_to_delete.right
                                current_node.right.parent = current_node
                                current_node.parent = node_to_delete.parent
                                current_node.parent.right = current_node


tree = NodeManager()
