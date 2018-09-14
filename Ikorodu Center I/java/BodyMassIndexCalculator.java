/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bodymassindexcalculator;

/**
 *
 * @author James Damilola Obadara
 * damiobadara@yahoo.com
 * 08086705784
 */

import java.util.Scanner;

public class BodyMassIndexCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        int w, h, BMI;
        
        System.out.print ("Enter weight:");
        w = input.nextInt();
        // weight is in kg
        
        System.out.print("Enter height:");
        h = input.nextInt();
        // height is in m
        
        BMI = w/(h * h);
        System.out.printf("BMI is %d\n", BMI);
        BMI = w/(h * h);
                
        
        System.out.println("BMI VALUES");
        System.out.println("Underweight: less than 18.5");
        System.out.println("Normal: between 18.5 and 24.9");
        System.out.println("Overweight: between 25 and 29.9");
        System.out.println("Obese: 30 or greater");
    }
    
}
