class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is Node:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        tmp = self.head

        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                tmp = None
                return

        while tmp is not None:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp is None:
            return

        prev.next = tmp.next

        tmp = None

    def get_count(self):
        count = 0
        tmp = self.head
        while tmp:
            tmp = tmp.next
            count += 1
        return count

    def get_count_recursive(self):
        return self.get_count_helper(self.head)

    def get_count_helper(self, head):
        if head is None:
            return 0
        return 1 + self.get_count_recursive(head.next)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_k(self, head, k):
        current = head
        next = prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse_k(next, k)

        return prev

    def merge_lists(self, head1, head2):
        tmp = None

        if not head1:
            return head2
        if not head2:
            return head1

        if head1.data <= head2.data:
            tmp = head1
            tmp.next = self.merge_lists(head1.next, head2)
        else:
            tmp = head2
            tmp.next = self.merge_lists(head1, head2.next)

        return tmp

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge_lists(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        fast_pointer = head.next
        slow_pointer = head

        while fast_pointer:
            fast_pointer = fast_pointer.next
            if fast_pointer:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
        return slow_pointer

    def rotate(self, k):
        if k == 0:
            return

        current = self.head
        count = 0

        while count < k and current:
            current = current.next
            count += 1

        kth_node = current

        while current.next:
            current = current.next

        current.next = self.head
        self.head = kth_node.next
        kth_node.next = None

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' ')
            tmp = tmp.next


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second

    second.next = third

    linked_list.print_list()

    print()

    linked_list.push(0)
    linked_list.insert_after(linked_list.head.next.next.next, 4)
    linked_list.append(5)

    linked_list.delete_node(4)

    linked_list.print_list()

    print('\nCount:', linked_list.get_count())

    linked_list.reverse()
    linked_list.print_list()

    print()
    linked_list.head = linked_list.merge_sort(linked_list.head)
    linked_list.print_list()

    print()
    linked_list.head = linked_list.reverse_k(linked_list.head, 2)
    linked_list.print_list()

    print()
    linked_list.rotate(2)
    linked_list.print_list()
