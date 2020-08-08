# ���� ���� ť Ŭ���� FixedQueue �����ϱ�
# Do it! �ǽ� 4-3 [A]
from typing import Any

class FixedQueue:

    class Empty(Exception):
        """��� �ִ� FixedQueue�� ���� deque �Ǵ� peek�� ȣ���� �� �������� ����ó��"""
        pass

    class Full(Exception):
        """���� �� FixedQueue�� enque�� ȣ���� �� �������� ����ó��"""
        pass

    def __init__(self, capacity: int) -> None:
        """�ʱ�ȭ ����"""
        self.no = 0    # ���� ������ ����
        self.front = 0 # �Ǿ� ���� Ŀ��
        self.rear = 0 # �ǳ� ����  Ŀ��
        self.capacity = cacapacity      # ť�� ũ��
        self.que = [None]*capacity  # ť�� ��ü

    def __len__(self) -> int:
        """ť�� �ִ� ��� ������ ������ ��ȯ"""
        return self.no

    def is_empty(self) -> bool:
        """ť�� ��� �ִ��� �Ǵ�"""
        return self.no <= 0

    def is_full(self) -> bool:
        """ť�� ���� á���� �Ǵ�"""
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
            print('ť�� ����ֽ��ϴ�.')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity 
                print(self.que[idx], end="")
