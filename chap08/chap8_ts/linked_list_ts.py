#%%
from __future__ import annotations		# 아직까지 필요함. 3.8 기준
from typing import Any, Type

#%%
class Node:

	def __init__(self, data: Any, next: Node):	# next: Node 에서 Node annotation 은 import 없이는 error 나타남
		self.data = data
		self.next = next

#%%
class LinkedList:

	def __init__(self) -> None:
		self.no = 0
		self.head = None
		self.current = None


	def __len__(self):
		return self.no


	def add_first(self, data: Any) -> None:
		hd = self.head
		self.head = self.current = Node(data,hd)
		self.no += 1


	def add_last(self, data: Any) -> None:
		if self.head == None:
			self.add_first(data)
		else:
			p = self.head
			while p.next is not None:
				p = p.next
			p.next = self.current = Node(data, None)
		

	def search(self, data: Any) -> int:
		index = 0
		p = self.head

		while p is not None:
			if p.data == data:	# 노드가 먼저 생성된 후 call 이기 때문에 Node 의 attribute 사용 가능
				return index
			else:
				p = p.next
				index += 1

		return None


	def remove_first(self) -> None:
		hd = self.head
		if hd is not None:
			self.head = self.current = hd.next
			self.no -= 1		# 놓치지 말것

	def remove_last(self):
		if self.head.next is None:		# 계산 줄여줌
			self.remove_first()			# self.clear() 로도 가능
		else:
			p = self.head
			while p.next.next is not None:
				p = p.next				# while 종료시 p 는 끝에서 두번째 노드
			p.next = None
			self.current = p
			self.no -= 1


	def remove(self, p: Node) -> None:
		hd = self.head
		if hd is not None:
			if p is hd:
				self.remove_first()
		else:
			while hd.next is not p:
				hd = hd.next
			hd.next = p.next
			self.current = hd		# 잊지말것
			self.no -= 1


	def remove_current_node(self) -> None:
		self.remove(self.current)


	def clear(self) -> None:
		self.__init__()


	def next(self) -> bool:
		if self.current.next is None or self.current is None:
			return False
		else:
			self.current = self.current.next
			return True


	def print_current_node(self) -> None:
		if self.current is None:
			print('해당 노드가 비어있습니다.')
		else:
			print(self.current.data)


	def print(self) -> None:
		p = self.head
		while p is not None:
			print(p.data)
			p = p.next

	def __iter__(self) -> LinkedListIterator:
		return LinkedListIterator(self.head)

class LinkedListIterator:

	def __init__(self, head: Node):
		self.current = head

	def __iter__(self) -> LinkedListIterator:
		return self

	def __next__(self) -> Any:
		if self.current is None:
			raise StopIteration
		else:
			data = self.current.data
			self.current = self.current.next
			return data