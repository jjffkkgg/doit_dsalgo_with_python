from __future__ import annotations		# 아직까지 필요함. 3.8 기준
from typing import Any, Type

Null = -1

class Node:
    
    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data
        self.next = next
        self.dnext = dnext      # 삭제 배열의 뒤인덱스

class ArrayLinkedList:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.max, self.current, self.deleted = Null, Null, Null, Null # deleted ->  free list 의 head
        self.no = 0
        self.n = [Node()] * self.capacity       # 리스트 본체

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 첨자를 구합니다"""
        if self.deleted == Null:
            if self.max < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted is Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec     # 오타? 잘못?

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        index = 0
        p = self.head

        while p != Null:
            if self.n[p].data == data:
                self.current = p
                return index
            index += 1
            p = self.n[p].next
        return Null

    def __contains__(self, data: Any) -> bool:
        """선형 리스트에 data가 포함되어 있는지 확인"""
        return (self.search(data) >= 0)

    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        p = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec              # head를 넣을 공간에 포인팅해주고..
            self.n[rec] = Node(data,p)                  # rec 인덱스에 새 노드를 삽입
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head == Null:                           # head 가 null.혼동하지말것
            self.add_first(data)
        else:
            p = self.head
            while self.n[p].next != Null:               #p 를 어떻게?
                p = self.n[p].next                      # 해당 position 의 next (int) 정보를 업데이트해줌

            rec = self.get_insert_index()               # 꼬리노드지만, 넣는 인덱스는 똑같이 정보를 받아와야함 (인덱스는 상관없으므로).
            
            if rec != Null:                             # rec 갖고온 다음 필수.
                self.n[p].next = self.current = rec     # 노드연결
                self.n[rec] = Node(data,Null)
                self.no += 1


    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head != Null:
            paste = self.n[self.head].next
            self.delete_index(self.head)        # head index 를 free list 등록
            self.head = self.current = paste    # 헤드 다음 인덱스를 헤드에 덮어씌우기
            self.no -= 1


    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                p = self.head
                while self.n[p].next != Null:
                    p_b = p
                    p = self.n[p].next
                self.n[p_b].next = Null
                self.delete_index(p_b)
                self.current = p_b
                self.no -= 1


    def remove(self, p: int) -> None:
        """레코드 p를 삭제"""
        if self.head != Null:                   
            if p == self.head:                  # head 가 p (한개)
                self.remove_first()
            else:
                index = self.head
                while self.n[index].next != p:
                    index = self.n[index].next
                    if index == Null:           # 범위 넘어감(검색 안됨)
                        return void     
                self.delete_index(index)        # p 가 아님. 주의
                self.n[index].next = self.n[p].next
                self.current = index
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """모든 노드를 삭제"""
        self.__init__(self.capacity)

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current == Null or self.n[self.current].next == Null:
            return False
        else:
            self.current = self.n[self.current].next
            return True


    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current == Null:
            print('해당 노드가 비어있습니다.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """모든 노드를 출력"""
        p = self.head
        while p != Null:
            print(self.n[p].data)
            p = self.n[p].next


    def dump(self) -> None:
        """배열을 덤프"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """이터레이터를 반환"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """클래스 ArrayLinkedList의 이터레이터용 클래스"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data