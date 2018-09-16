/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package largestofthreenumbers;
import java.util.Scanner;
/**
 *
 * @author nonnychris
 */
public class LargestofThreeNumbers {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner (System.in);
        int x;
        int y;
        int z;
        System.out.println("Enter value x");
        x = input.nextInt();
        System.out.println("Enter value y");
        y = input.nextInt();
        System.out.println("Enter value z");
        z = input.nextInt();
        
        if (x > y && x > z ){
           System.out.println("largest value is "+x);
        }
        else if (y > x && y > z){
            System.out.println("largest value is "+y);
        }
        else if (z > x && z > y){
            System.out.println("largest value is "+z);
        }
        else{
            System.out.println("Entered value are not distinct");
        }
        
    }
    
}
