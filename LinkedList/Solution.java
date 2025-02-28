package LinkedList;

import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode first = dummy;
        
        // Advance first pointer by n steps
        for (int i = 0; i < n; i++) {
            first = first.next;
        }
        
        ListNode second = dummy;
        
        // Move first to the end, maintaining the gap
        while (first.next != null) {
            first = first.next;
            second = second.next;
        }
        
        // Skip the nth node from the end
        second.next = second.next.next;
        
        return dummy.next;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the number of elements in the linked list
        System.out.print("Enter the number of elements in the linked list: ");
        int numElements = scanner.nextInt();

        // Create the linked list
        ListNode head = null;
        ListNode tail = null;
        System.out.println("Enter the elements of the linked list:");
        for (int i = 0; i < numElements; i++) {
            int value = scanner.nextInt();
            ListNode newNode = new ListNode(value);
            if (head == null) {
                head = newNode;
                tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
        }

        // Read the value of n
        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();

        // Remove the nth node from the end
        Solution solution = new Solution();
        head = solution.removeNthFromEnd(head, n);

        // Print the modified linked list
        System.out.println("Modified linked list:");
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();

        scanner.close();
    }
}