
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = TreeNode(key)
        else:
            self.insert_recursive(self.root, key)
            #recursive comparison to find where this thing goes

    def insert_recursive(self, node, key):

        if key < node.key:
            if node.left == None:
                node.left = TreeNode(key)
            else:
                self.insert_recursive(node.left, key)
        elif key > node.key:
            if node.right == None:
                node.right = TreeNode(key)
            else:
                self.insert_recursive(node.right, key)

    def print_tree(self):
        self.print_tree_recursive(self.root, 0)

    def print_tree_recursive(self, node, depth):
        if node is None:
            return None
        
        self.print_tree_recursive(node.right, depth + 1)
        print("    "* depth + str(node.key))
        self.print_tree_recursive(node.left, depth + 1)

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        #Base case, what we are looking for doesnt exist
        if node is None:
            return False
        #Base case we find what we are looking for
        if key == node.key:
            return True
        elif key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

    def find_smallest(self, node):
        while node.left:
            node = node.left 
        return node

        
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)
    #replace root if needed

    def delete_recursive(self, node, key):
        #base
        if node is None:
            print(f'{key} aint here!')
            return node
        
        #Binary Search to find the Target
        print(f'Is {node.key} == {key}')
        if key < node.key:
            print('recursive left')
            print(f'Node {node.key} left was {node.left.key if node.left else 'None'}')
            node.left = self.delete_recursive(node.left, key)
            print(f'Node {node.key} left is now {node.left.key if node.left else 'None'}')
        elif key > node.key:
            print('recursive right')
            print(f'Node {node.key} right was {node.right.key if node.right else 'None'}')
            node.right = self.delete_recursive(node.right, key)
            print(f'Node {node.key} right is now {node.right.key if node.right else 'None'}')
        #Found the target
        else:
            print(f'Found target {node.key} == {key}')
            if node.left == None: #if left is None, I have single right branch, or I'm dealing with a leaf
                print(f"{f'Returning Right Branch of {key}' if node.right else f'{key} is a leaf, replacing with None'} ")
                return node.right
            elif node.right == None: #Here, im dealing with a single branch to the left
                print(f"Returning left Branch of {key} ")
                return node.left
            
            print("Node to be removed has two branches")
            print(f"Need to find the smallest node to the right of {key}")
            smallest = self.find_smallest(node.right)
            print(f'The smallest node on the right is {smallest.key}, replacing {key} with {smallest.key}')
            node.key = smallest.key
            print(f'Now removing {smallest.key}')
            node.right = self.delete_recursive(node.right, smallest.key)
            print(f"The old {node.key} has been removed!")
        print(f'Returning {node.key}')
        return node
    
    def in_order_traversal(self):
        self.in_order_traversal_recursive(self.root)

    def in_order_traversal_recursive(self, node):
        if node:
            self.in_order_traversal_recursive(node.left)
            print(node.key)
            self.in_order_traversal_recursive(node.right)

            



tree = BinaryTree()

nodes = [50, 30, 40, 20, 70, 60, 80, 90]
for node in nodes:
    tree.insert(node)

print('Printing Tree')
tree.print_tree()

tree.delete(100)

tree.print_tree()

print('In order Traversal')
tree.in_order_traversal()

#Pre-order traversal: tells you the order you added the nodes

#Post-order traversal:





