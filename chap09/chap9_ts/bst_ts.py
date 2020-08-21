#%%
from __future__ import annotations
from typing import Any,Type

#%%
class Node:

    def __init__(self, key: Any, value: Any, left: Node, right: Node) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

# Do it! 실습 9-1[B]
    def search(self, key: Any) -> Any:
        """키 key를 갖는 노드를 검색"""
        p = self.root
        while True:
            if p is None:
                break
            if key == p.key:
                return p.value
            elif key > p.key:
                p = p.right
            else:
                p = p.left


# Do it! 실습 9-1[C]
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고, 값이 value인 노드를 삽입"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
            if key == node.key:
                return False
            elif key > node.key:
                if node.right == None:
                    node.right = Node(key,value, None, None)
                else:
                    add_node(node.right, key, value)
            else:
                if node.left == None:
                    node.left = Node(key,value, None, None)
                else:
                    add_node(node.left, key, value)
            return True

        if self.root == None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)                  # 리턴을 안하면 False 처리된다. 잊지말것

# # Do it! 실습 9-1[D]
    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root
        parent = None
        is_left = False
        while True:
            if p is None:
                print('해당 key 가 없습니다.')
                return False
            if key == p.key:                                    # 지울 키 찾음
                if p.left != None and p.right != None:          # 자식 둘다 있는경우
                    new_parent = p
                    p_new = p.left
                    while p_new.right != None:                  # 자식 중 가장 큰 키노드
                        new_parent = p_new
                        p_new = p_new.right
                    
                    #temp = p_new                                # 같은 노드를 지시하기 때문에 같이 바뀌어버리는 문제가 생김.
                    p.key = p_new.key                            # 키와 값만 갖고 온다.
                    p.value = p_new.value
                    """
                    if is_left:                                 # 복사
                        parent.left = temp
                    else:
                        parent.right = temp
                    temp.right, temp.left = p.right, p.left
                    """
                    """ 연결 자체를 재설정하기 보단, key 와 value 만 복사해 오는 것이 더 깔끔"""
                    if p_new.left != None:                      # 끌올한 큰노드에 왼쪽자식존재
                        new_parent.right = p_new.left
                    else:
                        new_parent.right = None


                elif p.left != None and p.right == None:        # 왼쪽 자식 하나
                    if p == self.root:
                        self.root = p.left
                    elif is_left:                                 # 부모-자식(지울) 관계
                        parent.left == p.left
                    else:
                        parent.right == p.left
                elif p.left == None and p.right != None:        # 오른쪽 자식 하나
                    """왼쪽 오른쪽 나누는 대신 왼쪽 판단 -> 오른쪽 판단 으로 둘다 없는 경우까지 커버 가능"""
                    if p == self.root:
                        self.root = p.right
                    elif is_left:
                        parent.left == p.right
                    else:
                        parent.right == p.right
                else:                                           # 둘다 없음
                    if p == self.root:
                        self.__init__()
                    elif is_left:
                        parent.left = None
                    else:
                        parent.right = None

                return True
            elif key > p.key:
                parent = p
                p = p.right
                is_left = False
            else:
                parent = p
                p = p.left
                is_left = True

# Do it! 실습 9-1[E]
    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""

        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}: {node.value}')
                print_subtree(node.right)

        print_subtree(self.root)

# Do it! 실습 9-1[F]
    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root == None:
            return None
        p = self.root
        while p.left != None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root == None:
            return None
        p = self.root
        while p.right != None:
            p = p.right
        return p.key
