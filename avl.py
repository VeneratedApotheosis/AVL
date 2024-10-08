class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height is initially 1 when the node is inserted

class AVL:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def left_rotate(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        
        balance = self.get_balance(root)

        
        
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        if root:
            self.pre_order(root.left)
            print(f"{root.key} ", end="")
            self.pre_order(root.right)

    def listify(self, root):
        if not root:
            return []
        a = [root.key]
        a.extend(self.listify(root.left))
        a.extend(self.listify(root.right))
        return a
    
    def autocomplete(self, root, prefix):
        if not root:
            return []

        results = []
        node = root
        while(node and not node.key.startswith(prefix)):
            if(prefix < root.key):
                node = node.left
            else:
                node = node.right
        print(node.key)
        
        results = self.listify(root)
        return results
    def search(self, root, key):
        if not root:
            return None

        if key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)
        else:
            return root

# Example usage
if __name__ == "__main__":
    tree = AVL()
    root = None

    while True:
        print("Choose an option:")
        print("1. Insert a word")
        print("2. Search for a word")
        print("3. Autocomplete a word")
        print("4. Exit")

        choice = int(input())

        if choice == 1:
            word = input("Enter a word to insert: ")
            root = tree.insert(root, word)
            print(f"Word \"{word}\" has been inserted.")
        elif choice == 2:
            word = input("Enter a word to search for: ")
            result = tree.search(root, word)
            if result:
                print(f"Word \"{word}\" found.")
            else:
                print(f"Word \"{word}\" not found.")
        elif choice == 3:
            prefix = input("Enter a prefix: ")
            results = tree.autocomplete(root, prefix)
            if results:
                print("Suggestions:")
                print(results)
            else:
                print("No suggestions found.")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
