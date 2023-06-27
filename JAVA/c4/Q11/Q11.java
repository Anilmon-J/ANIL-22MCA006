import java.util.*;

public class Q11 {
    public static  void main(String[] args){
      System.out.println("\nName : Anilmon J");
System.out.println("Regi.No : SJC22MCA-2006");
System.out.println("Date : 23 JUNE 2023");
System.out.println("Course Code : 20MCA132");
System.out.println("Course Name : OOPS LAB");
System.out.println("\n-------------------------------------------------------------\n");
        LinkedList<String> L=new LinkedList<>();
        L.add("Gold");
        L.add("Silver");
        L.add("Bronze");
        L.add(0,"Olympics Medals");
        System.out.println(L);
        L.remove("Bronze");
        System.out.println(L);
        L.remove(2);
        System.out.println(L);
        L.removeLast();
        System.out.println(L);
        L.removeFirst();
        System.out.println(L);


    }

}
