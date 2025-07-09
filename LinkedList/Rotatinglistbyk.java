package LinkedList;

import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Rotatinglistbyk {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head; // Return the head itself if the list is empty or has only one node
        }

        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        k %= length;
        if (k == 0) {
            return head;
        }

        int stepsToNewHead = length - k;
        ListNode newTail = head;
        for (int i = 0; i < stepsToNewHead - 1; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;
        tail.next = head;

        return newHead;
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

    // Helper function to create a linked list from an array of values
    public ListNode createList(int[] values) {
        if (values == null || values.length == 0) {
            return null;
        }
        ListNode head = new ListNode(values[0]);
        ListNode current = head;
        for (int i = 1; i < values.length; i++) {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Rotatinglistbyk solution = new Rotatinglistbyk();

        // Read the number of elements in the list
        System.out.print("Enter the number of elements in the linked list: ");
        int numElements = scanner.nextInt();

        // Read the elements of the list
        int[] values = new int[numElements];
        System.out.print("Enter the elements of the linked list: ");
        for (int i = 0; i < numElements; i++) {
            values[i] = scanner.nextInt();
        }

        // Read the rotation count k
        System.out.print("Enter the rotation count k: ");
        int k = scanner.nextInt();

        // Create the linked list from the input values
        ListNode head = solution.createList(values);

        // Rotate the linked list
        ListNode rotatedHead = solution.rotateRight(head, k);

        // Print the rotated linked list
        System.out.println("Rotated Linked List:");
        solution.printList(rotatedHead);

        scanner.close();
    }
}