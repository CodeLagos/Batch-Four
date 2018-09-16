
//program to print decimal equivalent of a Binary Number
//Written by Kanu Chidiebere Augustine, Ayoade Daud, Akomolafe Samson

package Exercise1;
import java.util.Scanner;

public class Exercise1 {
 public static void main(String[] args)
 {
  Scanner sc = new Scanner(System.in);
  long binaryNumber; 
  long decimalNumber = 0; 
  long j = 1; 
  long remainder;
  
  System.out.print("Please enter a binary number of your choice: ");
  binaryNumber = sc.nextLong();

  while (binaryNumber != 0)
  {
   remainder = binaryNumber % 10;
   decimalNumber = decimalNumber + remainder * j;
   j = j * 2;
   binaryNumber = binaryNumber / 10;
  }
  System.out.println("The Decimal Equivalent Number is: " + decimalNumber);
 }
}