import java.util.Scanner;

class authException extends Exception
{

public authException(String s) {
super(s);
}

}
public class Q3
{
public static void main(String[] args) {
System.out.println("\nName : Anilmon J");
System.out.println("Regi.No : SJC22MCA-2006");
System.out.println("Date : 22 JUNE 2023");
System.out.println("Course Code : 20MCA132");
System.out.println("Course Name : OOPS LAB");
System.out.println("\n-------------------------------------------------------------\n");
String username = "student";
String passcode = "student123";
String user_name,password;
Scanner sc = new Scanner(System.in);
try
{
System.out.println("Enter the username:");
user_name = sc.nextLine();

System.out.println("Enter the password:");
password = sc.nextLine();
if(username.equals(user_name) && passcode.equals(password))
{
System.out.println("Authentication successful...");
}
else
throw new authException("Invalid user credentials");

}
catch(authException e)
{
System.out.println("Exception caught "+e);
}
}

}
