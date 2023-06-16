class OverloadDemo
{
void area(float x)
{
System.out.println("the area of the square is "+Math.pow(x, 2)+" sq units");
}
void area(float x, float y)
{
System.out.println("the area of the rectangle is "+x*y+" sq units");
}
void area(double x)
{
double z = 3.14 * x * x;
System.out.println("the area of the circle is "+z+" sq units");
}
}
class Overload 
{

public static void main(String args[]) 
{
System.out.println("\nName : Anilmon J");
System.out.println("Reg.No : SJC22MCA-2006");
System.out.println("Course Code : 20MCA132");
System.out.println("Course Name : OOPS LAB");
System.out.println("Date : 05 JUNE 2023");
System.out.println("\n-------------------------------------------------------------\n");
OverloadDemo ob = new OverloadDemo();
ob.area(5);
ob.area(11,12);
ob.area(2.5);
}
}
