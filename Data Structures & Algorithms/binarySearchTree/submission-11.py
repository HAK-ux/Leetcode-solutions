class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None 

class TreeMap:
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        
        def insertion(root, node): 
            if not root:
                return node
            if node.key > root.key:
                root.right = insertion(root.right, node)
            elif node.key < root.key:
                root.left = insertion(root.left, node)
            else:
                root.val = node.val
            
            
            return root

        self.root = insertion(self.root, newNode)
    

    def get(self, key: int) -> int:

        def search(root):
            if not root:
                return -1
            
            if root.key == key:
                return root.val
            elif key > root.key:
                return search(root.right)
            elif key < root.key:
                return search(root.left)

        return search(self.root)


    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left

        return curr.val if curr else -1



    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1



    def remove(self, key: int) -> None:
        def removal(root, key):
            if not root:
                return None
            if key > root.key:
                root.right = removal(root.right, key)
            elif key < root.key:
                root.left = removal(root.left, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minimum = root.right
                    while minimum.left:
                        minimum = minimum.left
                    
                    root.key, root.val = minimum.key, minimum.val
                    root.right = removal(root.right, minimum.key)
                    
            return root
        
        self.root = removal(self.root, key)
                    
                    
                    
    def getInorderKeys(self) -> List[int]:
        results = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            results.append(root.key)
            dfs(root.right)
        
        dfs(self.root)

        return results

