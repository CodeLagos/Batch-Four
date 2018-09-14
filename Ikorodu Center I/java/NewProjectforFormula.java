/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package newprojectforformula;
import java.util.Scanner;
/**
 *
 * @author joshua ikeagu(thebigthinker4sure@gmail.com)08180119995

 */
public class NewProjectforFormula {
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("This project is to help solve mensuration of shapes");
       
     System.out.println("This is for solving square area");
      Scanner input = new Scanner(System.in);
      System.out.print ("Enter L: ");  
      double L = input.nextDouble();
      double area = Math.pow(L,2);
       System.out.println("First solution for area = " + area);
       
       System.out.println("This is for solving perimeter of a square");
       System.out.print ("Enter L: ");
      double Lengthofperimeter = input.nextDouble(); 
      double perimeter = (4 * L);
       System.out.println("First solution for perimeter = " + perimeter);
       
       System.out.println("for solving area of a triangle");
       System.out.println("Enter Length: ");
         double length = input.nextDouble();
         
         System.out.println("Enter base: ");
         
        double base =  input.nextDouble();
        
  
       System.out.println("Enter heigth: ");
        double height =  input.nextDouble();
        double areaoftriangle =  (0.5 * base * height  );
        System.out.println("Solution for area = " + area );
        
        System.out.println("This is for solving area of a trapezium");
        System.out.println ("Enter cd: ");  
      double cd  = input.nextDouble();
      
       System.out.println ("Enter df: ");  
      double df  = input.nextDouble();
      
       System.out.println ("Enter heigth: ");  
      double heigh  = input.nextDouble();

        Forsolvingtrapezium forsolvingtrapezium = new Forsolvingtrapezium(cd, df, heigh);
        forsolvingtrapezium.findArea();
      
        
  
      
     
      
      
            
    
    }   
}
