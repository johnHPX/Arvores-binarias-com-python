from binarySearchTree import BinarySearchTree
from avlTree import AVLTree

def test_binarySerachTree():
    t01 = BinarySearchTree()
    t01.insert(5)
    t01.insert(7)
    t01.insert(3)
    t01.insert(2)
    t01.insert(8)
    t01.insert(4)
    t01.insert(9)
    t01.insert(10)
    t01.print_tree()
    print("------------------------------------")

    t01.remove(5)
    t01.remove(4)
    t01.remove(7)
    t01.print_tree()

    print("------------------------------------")
    t01.print_in_order()

    print("------------------------------------")
    t01.print_pre_order()

    print("------------------------------------")
    t01.print_pos_order()

    print("------------------------------------")
    result = t01.search(10)
    if result:
        print(f"Found {result.data} in binary search tree.")
    else:
        print("Value 10 not found in binary search tree.")

    result = t01.search_maximum()
    if result:
        print(f"Max value in binary search tree is {result.data}.")
    else:
        print("Tree is empty.")

    result = t01.search_minimum()
    if result:
        print(f"Min value in binary search tree is {result.data}.")
    else:
        print("Tree is empty.")


def test_avl_tree():
    t01 = AVLTree()
    t01.insert(5)
    t01.insert(7)
    t01.insert(3)
    t01.insert(2)
    t01.insert(8)
    t01.insert(4)
    t01.insert(9)
    t01.insert(10)
    t01.print_tree()
    print("------------------------------------")

    t01.remove(5)
    t01.remove(4)
    t01.remove(7)
    t01.print_tree()

    print("------------------------------------")
    t01.print_in_order()

    print("------------------------------------")
    t01.print_pre_order()

    print("------------------------------------")
    t01.print_pos_order()

    print("------------------------------------")
    result = t01.search(10)
    if result:
        print(f"Found {result.data} in binary search tree.")
    else:
        print("Value 10 not found in binary search tree.")

    result = t01.search_maximum()
    if result:
        print(f"Max value in binary search tree is {result.data}.")
    else:
        print("Tree is empty.")

    result = t01.search_minimum()
    if result:
        print(f"Min value in binary search tree is {result.data}.")
    else:
        print("Tree is empty.")


# main code
if __name__ == "__main__":
    # test_binarySerachTree()
    test_avl_tree()
