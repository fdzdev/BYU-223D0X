from src.bst import BST


def test_inorder_is_sorted():
    t = BST()
    for k in [5, 3, 8, 1, 4, 7, 9]:
        t.insert(k)
    assert t.inorder() == [1, 3, 4, 5, 7, 8, 9]
