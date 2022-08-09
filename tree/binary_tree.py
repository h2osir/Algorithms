# coding = utf-8

"""
二叉树遍历：
    1. 前序遍历： 根-左-右
    2. 中序遍历： 左-根-右
    3. 后续遍历： 左-右-根
示例：
          a(1)
         /    \
        /      \
      b(2)     c(3)
     /   \     /   \
    /     \   /     \
 d(4)    e(5)f(6)   g(7)
"""


class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Traversal(object):

    result = []

    @staticmethod
    def preorder(root):
        """前序遍历： 根-左-右"""

        if root is None:
            return
        Traversal.result.append(root.value)
        Traversal.preorder(root.left)
        Traversal.preorder(root.right)

        return Traversal.result


    @staticmethod
    def mid_order(root):
        """中序遍历： 左-根-右"""

        if root is None:
            return
        Traversal.mid_order(root.left)  # 一直往左边判断直到 root.left = None.
        Traversal.result.append(root.value)
        Traversal.mid_order(root.right)

        return Traversal.result

    @staticmethod
    def post_order(root):
        """后序遍历： 左-右-根"""
        if root is None:
            return
        Traversal.post_order(root.left)
        Traversal.post_order(root.right)
        Traversal.result.append(root.value)

        return Traversal.result


if __name__ == '__main__':
    a = TreeNode()
    b = TreeNode()
    c = TreeNode()
    d = TreeNode()
    e = TreeNode()
    f = TreeNode()
    g = TreeNode()

    a.value = 1
    b.value = 2
    c.value = 3
    d.value = 4
    e.value = 5
    f.value = 6
    g.value = 7

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    # pre_order_result = Traversal.preorder(root=a)
    # mid_order_result = Traversal.mid_order(root=a)
    post_order_result = Traversal.post_order(root=a)

    # print(pre_order_result)
    # print(mid_order_result)
    print(post_order_result)
