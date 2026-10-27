"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Append at the top so the newest value is removed first (LIFO).
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Inspect the top without changing the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self._items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add at the back; removal from the front preserves arrival order (FIFO).
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Inspect the oldest value without removing it.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self._items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO: TEXT EDITOR UNDO ===")
    history = Stack()
    actions = ["Type title", "Add paragraph", "Bold heading", "Insert image"]
    for action in actions:
        history.push(action)
        print("Recorded:", action)
    print("Next action to undo (peek):", history.peek())
    while not history.is_empty():
        print("Undo newest action:", history.pop())
    for operation in (history.pop, history.peek):
        try:
            operation()
        except IndexError as error:
            print("Expected empty-stack error:", error)
    history.push("Single edit")
    print("Removed only action:", history.pop())
    print("Single-item stack is now empty:", history.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: SUPPORT DESK TICKETS ===")
    tickets = Queue()
    requests = ["Reset password", "Install printer", "Update software", "Fix Wi-Fi"]
    for request in requests:
        tickets.enqueue(request)
        print("Ticket arrived:", request)
    print("Next ticket (front):", tickets.front())
    while not tickets.is_empty():
        print("Serve oldest ticket:", tickets.dequeue())
    for operation in (tickets.dequeue, tickets.front):
        try:
            operation()
        except IndexError as error:
            print("Expected empty-queue error:", error)
    tickets.enqueue("Single ticket")
    print("Removed only ticket:", tickets.dequeue())
    print("Single-item queue is now empty:", tickets.is_empty())


if __name__ == "__main__":
    main()
