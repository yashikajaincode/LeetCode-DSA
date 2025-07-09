package LinkedList;


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Partitionlist {
    public ListNode partition(ListNode head, int x) {
        if (head == null) {
            return null;
        }

        // Initialize two dummy nodes
        ListNode dummy1 = new ListNode(0);
        ListNode dummy2 = new ListNode(0);

        // Pointers to the current ends of the two partitions
        ListNode tail1 = dummy1;
        ListNode tail2 = dummy2;

        // Traverse the list and partition the nodes
        ListNode current = head;
        while (current != null) {
            if (current.val < x) {
                tail1.next = current;
                tail1 = tail1.next;
            } else {
                tail2.next = current;
                tail2 = tail2.next;
            }
            current = current.next;
        }

        // Concatenate the two partitions
        tail1.next = dummy2.next;
        tail2.next = null;

        // Return the head of the new list
        return dummy1.next;
    }

    // Helper function to print the linked list
    public void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        Partitionlist solution = new Partitionlist();

        // Example 1
        ListNode head1 = new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(5, new ListNode(2))))));
        int x1 = 3;
        ListNode partitionedHead1 = solution.partition(head1, x1);
        solution.printList(partitionedHead1);  // Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> null

        // Example 2
        ListNode head2 = new ListNode(2, new ListNode(1));
        int x2 = 2;
        ListNode partitionedHead2 = solution.partition(head2, x2);
        solution.printList(partitionedHead2);  // Output: 1 -> 2 -> null
    }
}
