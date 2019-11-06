from RBTree import RBTreeNode
from RBTree import RBTree
from AVLTree import AVLTree
from AVLTree import Node
from BTree import BTree
from BTree import BTreeNode


def set_avl(words):
    # create an avl tree
    avl_tree = AVLTree()
    # read the file
    file2 = open(words, "r")
    line = file2.readline()
    # while loop to read all lines in file
    while line:
        # each word is added to the tree
        new_word = Node(line.rstrip().lower())
        avl_tree.AVL_Tree_Insert(new_word)
        line = file2.readline()
    # return the tree
    return avl_tree

def create_btree(words):
    # create an btree
    btree = BTree(max_num_keys=6)
    # read the file
    file2 = open(words, "r")
    line = file2.readline()
    # while loop to read all lines in file
    while line:
        # each word is added to the btree
        new_word = line.rstrip().lower()
        btree.insert(new_word)
        line = file2.readline()
    # return the tree
    return btree

def print_tree(tree_node):
    if tree_node is None:
        print("Your tree is empty.")
        return
    # Print left sub-tree
    if tree_node.left is not None:
        print_tree(tree_node.left)
    print(tree_node.key)
    # Print right sub-tree
    if tree_node.right is not None:
        print_tree(tree_node.right)


def count_anagrams(word, tree):
    counter = 0
    anagrams = count_anagrams_helper(word)
    for i in range(len(anagrams)):
        # search for all anagrams within the list of all permutations
        if tree.search(anagrams[i]):
            counter += 1
    return counter


def count_anagrams_helper(word):
    if len(word) <= 1:
        return word
    else:
        # create list to store all possible permutations
        anagrams = []
        for anagram in count_anagrams_helper(word[1:]):
            for i in range(len(word)):
                anagrams.append(anagram[:i] + word[0:1] + anagram[i:])
        return anagrams


def greatest_number_of_anagrams(words, tree):
    file_reader = open(words, "r")
    each_line = file_reader.readline()

    largest = each_line.rstrip().lower()  # word that has the most anagrams
    biggest_number = count_anagrams(largest, tree)

    # loop to access all lines in the file
    while each_line:
        new_word = each_line.rstrip().lower()
        current = count_anagrams(new_word, tree)
        if current > biggest_number:
            largest = new_word
            biggest_number = current
        each_line = file_reader.readline()

    # Returns word with the most anagrams
    return largest


def set_rb(words):
    # create an rb tree
    rb_tree = RBTree()
    # read the file
    file2 = open(words, "r")
    line = file2.readline()
    # while loop to read all lines in file
    while line:
        # each word is added to the tree
        new_word = line.rstrip().lower()
        rb_tree.insert(new_word)
        line = file2.readline()
    # return the tree
    return rb_tree


def main():
    print("What kind of tree do you want?")
    print("Type the number.")
    kind_of_tree = input("1. Red Black Tree\n2. AVL Tree\n3. BTree\n")
    if kind_of_tree == '1':
        rb_tree = set_rb("words.txt")
        print("Red Black Tree:")
        print_tree(rb_tree.root)
        print()
        print("Anagrams in the word file for spot:")
        rb_tree.print_anagrams("spot")
        print()
        print("Number of anagrams for spot: " + str(count_anagrams("spot", rb_tree)))
        print(greatest_number_of_anagrams("words2.txt", rb_tree))
    elif kind_of_tree == '2':
        AVL_Tree = set_avl("words3.txt")
        print()
        print("AVL Tree:")
        print_tree(AVL_Tree.root)
        print()
        print("Anagrams in the word file for abort:")
        AVL_Tree.print_anagrams("abort")
        print()
        print("Number of anagrams for team: " + str(count_anagrams("team", AVL_Tree)))
    elif kind_of_tree == '3':
        BTree = create_btree("words.txt")
        print("BTree: ")
        BTree.print()
        print()
        BTree.print_anagrams("spot")
        print()
        print("Number of anagrams for spot: " + str(count_anagrams("spot", BTree)))
        print(greatest_number_of_anagrams("words2.txt", BTree))



if __name__ == "__main__":
    main()
