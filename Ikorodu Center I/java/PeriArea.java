// To calculate Area (#RSquare) and Perimeter (2#R) of a Circle 

// By Salau Nurudeen Oladehinbo of Code Lagos Ikorodu Center

// Tel: 08051698765                      

//

import java.text.DecimalFormat;

public class PeriArea
{
	public static void main(String[]args)
	
	{
	int radius=5;
	
	double pi = 3.142, area, perimeter;
		
	area = pi * radius * radius; // To Calculate radius of the Circle

	perimeter = 2 * pi * radius; // To calculate the perimeter of the circle
	
	//DecimalFormat.ft = new DecimalFormat("##,00");
	
	System.out.println("\t The area of the circle of radius "+ radius + " is " + area );

	System.out.print("\n\t The perimeter of the circle of radius " + radius + " is " + Math.round(perimeter));

	}
}