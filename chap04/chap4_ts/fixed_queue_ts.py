# 고정 길이 큐 클래스 FixedQueue 구현하기
# Do it! 실습 4-3 [A]
from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int) -> None:
        """초기화 선언"""
        self.no = 0    # 현재 데이터 개수
        self.front = 0 # 맨앞 원소 커서
        self.rear = 0 # 맨끝 원소  커서
        self.capacity = cacapacity      # 큐의 크기
        self.que = [None]*capacity  # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐가 비어 있는지 판단"""
        return self.no <= 0

    def is_full(self) -> bool:
        """큐가 가득 찼는지 판단"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> int:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity 
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) ->int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity 
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity 
                print(self.que[idx], end="")
