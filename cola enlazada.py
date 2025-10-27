class Node:
    def __init__(self, info=None, next_node=None):
        self.info = info
        self.next = next_node


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def enqueue(self, info):
        new_node = Node(info)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.head is None:
            return None
        info = self.head.info
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        return info

    def front(self):
        return None if self.head is None else self.head.info

    def __str__(self):
        elems = []
        current = self.head
        while current is not None:
            elems.append(str(current.info))
            current = current.next
        return " <- ".join(elems) if elems else "[Cola vacía]"


if __name__ == "__main__":
    q = LinkedQueue()
    print("=== Simulación de Cola Enlazada ===\n")

    print(f"¿Cola vacía? {q.is_empty()}")
    print(f"Tamaño actual: {q.size()}\n")

    print("Encolando elementos...")
    for n in [10, 20, 30]:
        q.enqueue(n)
        print(f"Encolado: {n} | Cola actual → {q}")
    print(f"\nTamaño: {q.size()}")
    print(f"Elemento al frente: {q.front()}\n")

    print("Desencolando elementos...")
    while not q.is_empty():
        valor = q.dequeue()
        print(f"Desencolado: {valor} | Cola actual → {q}")

    print(f"\n¿Cola vacía? {q.is_empty()}")
    print("\n=== Fin de la simulación ===")
