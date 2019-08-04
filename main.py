from DataStructures.AVLTree import AVL

if __name__ == '__main__':
    tree = AVL()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    print(tree.get_inorder())
