import java.util.PriorityQueue;
import java.util.Scanner;

public class Q13{
    public static void main(String[] args) {
    System.out.println("\nName : Anilmon J");
System.out.println("Regi.No : SJC22MCA-2006");
System.out.println("Date : 26 JUNE 2023");
System.out.println("Course Code : 20MCA132");
System.out.println("Course Name : OOPS LAB");
System.out.println("\n-------------------------------------------------------------\n");
    
        Scanner scanner = new Scanner(System.in);

        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
         

        System.out.print("Enter the number of elements to add: ");
        int numElements = scanner.nextInt();

        
        System.out.println("Enter the elements:");
        for (int i = 0; i < numElements; i++) {
            int element = scanner.nextInt();
            queue.offer(element);
        }

        System.out.println("Queue elements:");
        
        
        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }

        scanner.close();
    }
}

