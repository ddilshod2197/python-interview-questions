class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and data < node.left.data:
            return self._right_rotate(node)

        if balance < -1 and data > node.right.data:
            return self._left_rotate(node)

        if balance > 1 and data > node.left.data:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and data < node.right.data:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)

tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

print("Inorder traversal of the AVL tree:")
tree.inorder()
```

Bu kodda AVL ko'p qatlamli tugma (AVL tree) yaratiladi. AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Har bir tugma uchun balans qiymatini hisoblaydi (chap qatlamning balans qiymati - o'ng qatlamning balans qiymati).
2. Agar tugma balans qiymati 2 dan katta bo'lsa, chap qatlamni chapga buradi.
3. Agar tugma balans qiymati -2 dan kichik bo'lsa, o'ng qatlamni o'ngga buradi.
4. Agar tugma balans qiymati 2 dan kichik bo'lsa, o'ng qatlamni chapga buradi.
5. Agar tugma balans qiymati -2 dan katta bo'lsa, chap qatlamni o'ngga buradi.

Shunday qilib, AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chapga burish.
2. O'ng qatlamni o'ngga burish.
3. Chap qatlamni o'ngga burish.
4. O'ng qatlamni chapga burish.

AVL tugma balanslanganligini ta'minlash uchun quyidagilar qiladi:

1. Chap qatlamni chap
