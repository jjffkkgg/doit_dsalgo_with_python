#%%
from __future__ import annotations
from typing import Any,Types

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
                    node.right = Node(key,vlaue, None, None)
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
            add_node(node, key, value)

# # Do it! 실습 9-1[D]
    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root
        while True:
            if p is None:
                print('해당 key 가 없습니다.')
                break
            if key == p.key:
                
            elif key > p.key:
                p = p.right
            else:
                p = p.left

# Do it! 실습 9-1[E]
    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""

        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            

# Do it! 실습 9-1[F]
    def min_key(self) -> Any:
        """가장 작은 키"""
        

    def max_key(self) -> Any:
        """가장 큰 키"""
        