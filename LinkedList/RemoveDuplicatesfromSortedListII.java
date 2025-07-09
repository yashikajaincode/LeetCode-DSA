package LinkedList;

import java.util.Scanner;

/**
 * Problem Statement:
 * Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list. Return the linked list sorted as well.
 */

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class RemoveDuplicatesfromSortedListII {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode current = head;

        while (current != null) {
            // Skip all duplicates
            while (current.next != null && current.val == current.next.val) {
                current = current.next;
            }

            // If no duplicates were found, move prev to current
            if (prev.next == current) {
                prev = current;
            } else {
                // Otherwise, skip the duplicates
                prev.next = current.next;
            }

            // Move current to the next node
            current = current.next;
        }

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

        // Remove duplicates
        RemoveDuplicatesfromSortedListII solution = new RemoveDuplicatesfromSortedListII();
        head = solution.deleteDuplicates(head);

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