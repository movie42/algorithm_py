# 다음은 Tree 자료구조를 순회하는 방법 중, Pre-order 순회 방법을 설명한 것이다. 자료구조의 순회란, 자료구조에 속한 모든 data를 한 번씩 접근하는 것이다. Pre-order 순회를 하면서 순회한 순서대로 Node의 data를 콘솔에 출력하는 `preorder()` 메소드를 완성하시오.

# - Tree 자료구조를 순회할 때에는 반드시 root node부터 순회를 시작한다.
# - Pre-order 순회를 할 때에는 아래와 같은 방법을 재귀적으로 수행한다.
#    - 새로운 node에 접근할 경우, 아래 순서대로 동작한다.
#        1. Node에 있는 data를 출력한다.
#         1. Node에 left child가 있으면, left child node에 접근한다.
#         1. Node에 right child가 있으면, right child node에 접근한다.
#     - root node에서 순회를 시작할 경우, 재귀적 동작으로 인해 모든 node의 data를 출력할 수 있다.


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        node = self.root
        while node:
            if data < node.data:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(data)
                    break
            elif data > node.data:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(data)
                    break

    def search(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
        return False

    def delete(self, data):
        searched = False
        node = self.root
        node_p = self.root
        while node:
            if node.data == data:
                searched = True
                break
            if node.data > data:
                node_p = node
                node = node.left
            elif node.data < data:
                node_p = node
                node = node.right
        if searched:
            # 찾은 노드가 leaf일 때
            if node.left == None and node.right == None:
                if data < node_p.data:
                    node_p.left = None
                elif data > node_p.data:
                    node_p.right = None
            # 찾은 노드가 child를 왼쪽 또는 오른쪽에 가지고 있을 때
            if node.left and node.right == None:
                if data < node_p.data:
                    node_p.left = node.left
                    node = None
                else:
                    node_p.right = node.left
                    node = None
            elif node.right and node.left == None:
                if data < node_p.data:
                    node_p.left = node.right
                    node = None
                else:
                    node_p.right = node.right
                    node = None
            # 찾은 노드가 왼, 오른쪽 노드를 다 가지고 있을 때
            elif node.left and node.right:

                c_node = node.right
                c_p_node = node.right

                while c_node.left:
                    c_p_node = c_node
                    c_node = c_node.left

                if c_node.right:
                    c_p_node.left = c_node.right
                else:
                    c_p_node.left = None

                if data < node_p.data:
                    node_p.left = c_node
                else:
                    node_p.right = c_node

                if c_node.right.data == c_p_node.right.data:
                    c_node.right = None
                else:
                    c_node.right = node.right

                c_node.left = node.left

            return node.data
        else:
            return searched

    # 재귀를 사용하여 순환한다.
    def preorder(self):
        def recursion(node):
            print(
                "node",
                node.data,
                "node.right",
                node.right.data if node.right != None else "None",
                "node.left",
                node.left.data if node.left != None else "None",
            )

            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)

        recursion(self.root)


# Test code

tree = Tree(20)


data_list = [5, 3, 4, 33, 60, 100, 232, 6, 26, 7, 55]
for i in data_list:
    tree.insert(i)

tree.preorder()

print(tree.delete(33))

tree.preorder()
