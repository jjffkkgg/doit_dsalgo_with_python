#%%
from __future__ import annotations
from typing import Any, Type

#%%
class Node:

    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev or self        # 앞노드 지정
        self.next = next or self       # 뒷노드 지정 

#%%
class DoubleLinkedList:
    """원형 이중 연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.head = self.current = Node()
        self.no = 0

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no
        

    def is_empty(self) -> bool:
        """리스트가 비어 있는가?"""
        return (self.head == self.head.next)
        

# Do it! 실습 8-5 [B]
    def search(self, data: Any) -> Any:
        """data와 값이 같은 노드를 검색"""
        index = 0
        p = self.head.next
        while p != self.head:
            if p.data == data:
                return index
            p = p.next
            self.current = p
            index += 1
        return -1

    def __contains__(self, data: Any) -> bool:
        return (self.search(data) >= 0)

# Do it! 실습 8-5 [C]
    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.is_empty():
            print('리스트가 비어있습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        p = self.head.next
        while p != self.head:
            print(p.data)
            p = p.next

    def print_reverse(self) -> None:
        """모든 노드를 역순으로 출력"""
        p = self.head.prev
        while p != self.head:
            print(p.data)
            p = p.prev

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current.next == self.head or self.is_empty():
            print('배열의 끝이거나 비었습니다.')
            return False
        else:
            self.current = self.current.next
            return True

    def prev(self) -> bool:
        """주목 노드를 한 칸 앞으로 이동"""
        if self.current.prev == self.head or self.is_empty():
            print('배열의 처음이거나 비었습니다.')
            return False
        else:
            self.current = self.current.prev
            return True

# Do it! 실습 8-5[D]
    def add(self, data: Any) -> None:
        """주목 노드의 바로 뒤에 노드를 삽입"""
        p = self.current
        node = Node(data,p,p.next)
        self.current.next.prev = node            # 보충 8-4 참고. 한줄로 써버리면 파이썬에서는 잘못된 해석이 이루어진다
        self.current.next = node                 # next 가 먼저 reference 되지 않도록 주의할 것. 
        self.current = self.current.next
        self.no += 1

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        self.current = self.head
        self.add(data)

    def add_last(self, data: Any) -> None:
        """맨 뒤에 노드를 삽입"""
        self.current = self.head.prev
        self.add(data)

# Do it! 실습 8-5[E]
    def remove_current_node(self) -> None:
        """주목 노드 삭제"""
        if not self.is_empty():
            p = self.current
            self.current.prev.next = p.next
            self.current.next.prev = p.prev
            self.current = p.prev
            self.no -= 1
            if self.current == self.head:           # head 는 더미므로 헤드에 배정되면
                self.current = self.head.next       # 그 다음걸로 current 를 넘겨주기
        else:
            print('배열이 비었습니다.')


    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        pnt = self.head.next
        while pnt != p:
            pnt = pnt.next
            if pnt == self.head:
                return None
        self.current = pnt
        self.print_current_node()



    def remove_first(self) -> None:
        """머리 노드 삭제"""
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        """꼬리 노드 삭제"""
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        """모든 노드를 삭제"""
        self.__init__()
        

# Do it! 실습 8-5[F]
    def __iter__(self) -> DoubleLinkedListIterator:
        """반복자를 반환"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """내림차순 반복자를 반환"""
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList의 반복자용 클래스"""
    
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data