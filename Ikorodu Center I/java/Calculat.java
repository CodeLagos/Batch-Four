// Simple calculation using Java 1.8, NetBeans IDE 8.2 and jdk 8u171 

// By Salau Nurudeen Oladehinbo of Code Lagos Ikorodu Center

// Tel: 08051698765                      

//

public class Calculat
	
{

	public static void main(String[]args)
	
	{

	double num1, num2, num3, num4, num5, nume, denom, total;
	
	num1 = 9.5; num2 = 4.5;	num3 = 2.5; num4 = 45.5;num5 = 3.5;
	
	nume = (num1 * num2) - (num3 * 3);
	
	denom = num4 - num5;

	total = nume/denom;

	//round (total,2);

	{
	
	for (int i = 0; i < 1000; ++i)        /* Clear the screen */
	System.out.println();
	
	}  

	
	System.out.print("\t Calculated Total is: " + total );

	}
}