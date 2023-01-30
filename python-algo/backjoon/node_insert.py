# 노드 생성
class 노드:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 노드 삽입
class 이진탐색트리:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_value(self.root, value)
        return self.root is not None

    def insert_value(self, node, value):
        if node is None:
            node = 노드(value)
        else:
            if value <= node.value:
                node.left = self.insert_value(node.left, value)
            else:
                node.right = self.insert_value(node.right, value)
        return node

        # 노드 탐색
    def search(self, value):    # 입력한 value가 있으면 True를 반환하는 함수
        self.현재노드 = self.root
        while self.현재노드:
            if self.현재노드.value == value:
                return True
            elif self.현재노드.value > value:
                self.현재노드 = self.현재노드.left
            else:
                self.현재노드 = self.현재노드.right
        return False

    # def 삽입(self, value):
    #     self.현재노드 = self.root
    #     while True:
    #         # 입력한 값이 현재 노드보다 작을 경우
    #         if value < self.현재노드.value:
    #             # 왼쪽 노드가 있을 경우 왼쪽노드를 현재 노드로 변경 후 반복문 재수행
    #             if self.현재노드.left != None:
    #                 self.현재노드 = self.현재노드.left
    #             # 왼쪽 노드가 없으면 왼쪽 노드에 입력한 값 입력
    #             else:
    #                 self.현재노드.left = 노드(value)
    #                 break
    #         # 입력한 값이 현재 노드보다 크거나 같을 경우, 위와 같은 패턴 수행
    #         else:
    #             if self.현재노드.right != None:
    #                 self.현재노드 = self.현재노드.right
    #             else:
    #                 self.현재노드.right = 노드(value)
    #                 break

root = 노드(6)
bst = 이진탐색트리(root)
bst.삽입(2)
bst.삽입(7)
bst.삽입(8)
bst.삽입(10)
print(bst.search(1)) 
print(bst.search(2)) 
print(bst.search(5)) 
print(bst.search(7)) 
print(bst.search(8)) 
print(bst.search(15))

# 재귀함수로 이진트리 수정코드 비교해보기
# 지금꺼 수정 해서 


# 노드 생성과 삽입
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(Node):
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 노드 탐색
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)  