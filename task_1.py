class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Виведення списку
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Реверс списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Сортування злиттям
def merge_sort(head):
    if not head or not head.next:
        return head

    # Пошук середини
    def get_middle(node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    middle = get_middle(head)
    right_head = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(right_head)

    return merge_sorted_lists(left, right)

# Злиття двох відсортованих списків
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# Створення списку з Python-списку
def create_linked_list(data_list):
    if not data_list:
        return None
    head = Node(data_list[0])
    current = head
    for val in data_list[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Тестування
list1 = create_linked_list([4, 2, 1, 3])
list2 = create_linked_list([5, 6, 7])

print("Original list 1:")
print_list(list1)

print("\nReversed list 1:")
reversed_list = reverse_list(list1)
print_list(reversed_list)

print("\nSorted list 1:")
sorted_list = merge_sort(reversed_list)
print_list(sorted_list)

print("\nList 2:")
print_list(list2)

print("\nMerged sorted list:")
merged = merge_sorted_lists(sorted_list, list2)
print_list(merged)
