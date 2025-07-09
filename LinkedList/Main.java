package LinkedList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class LRUCache {

    private int capacity;
    private Map<Integer, Node> cache;
    private Node head, tail;

    class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head; 
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        Node node = cache.get(key);
        remove(node);
        add(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.value = value;
            remove(node);
            add(node);
        } else {
            if (cache.size() == capacity) {
                cache.remove(tail.prev.key);
                remove(tail.prev);
            }
            Node newNode = new Node(key, value);
            cache.put(key, newNode);
            add(newNode);
        }
    }

    private void add(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the capacity of the LRU Cache:");
        int capacity = scanner.nextInt();
        LRUCache lruCache = new LRUCache(capacity);

        System.out.println("Enter the number of operations:");
        int numOperations = scanner.nextInt();

        for (int i = 0; i < numOperations; i++) {
            System.out.println("Enter operation type (1 for put, 2 for get):");
            int operationType = scanner.nextInt();

            if (operationType == 1) {
                System.out.println("Enter key and value:");
                int key = scanner.nextInt();
                int value = scanner.nextInt();
                lruCache.put(key, value);
            } else if (operationType == 2) {
                System.out.println("Enter key:");
                int key = scanner.nextInt();
                int result = lruCache.get(key);
                System.out.println("Result of get(" + key + "): " + result);
            } else {
                System.out.println("Invalid operation type. Please enter 1 for put or 2 for get.");
            }
        }

        scanner.close();
    }
}