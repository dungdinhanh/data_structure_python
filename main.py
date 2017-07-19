import Word
import bst
import tree_node


def word_compare(word1, word2):
    if word1.eng > word2.eng:
        return 1
    if word1.eng < word2.eng:
        return -1
    else:
        return 0


def read_file(input_file, bst):
    f = open(input_file, "r")
    for line in f:
        str_list = line.split(":")
        str_list[0] = str_list[0].strip()
        str_list[1] = str_list[1].strip()
        word = Word.Word()
        word.input_word(str_list[0], str_list[1])
        bst.insert_node(word)

bst = bst.BST()
read_file("E:\\Python\\DataStructure\\dictionary.txt", bst)
while True:
    print("Menu")
    print("1. Insert word")
    print("2. Delete word")
    print("3. Search")
    print("4. Traversal")

    choice = int(input("Your choice: "))

    if choice == 1:
        new_word = Word.Word()
        new_word.eng = input("Input English word: ")
        new_word.vi = input("Input Vietnamese word: ")
        bst.insert_node(new_word)

    if choice == 2:
        new_word = Word.Word()
        new_word.eng = input("Input key word to delete: ")
        new_word = bst.search_node(new_word)
        if new_word is None:
            print("no data ")
            continue
        print("Delete \"" , new_word.data, "\" going to be done")
        bst.delete_node(new_word.data)

    if choice == 3:
        new_word = Word.Word()
        new_word.eng = input("Input key word to search: ")
        new_word = bst.search_node(new_word)
        if new_word is None:
            print("no data available")
            continue
        print(new_word.data)

    if choice == 4:
        print("Inorder traversal")
        bst.in_order_traversal()
        print("\nPreorder traversal")
        bst.pre_order_traversal()
        print("\nPostorder traversal")
        bst.post_order_traversal()
        print("close")

    if choice == 5:
        print("Thank you see you later ")
        break;

