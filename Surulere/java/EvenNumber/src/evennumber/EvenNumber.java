/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package evennumber;
import java.util.Scanner;

/**
 *
 * @author Abass Damilola
 */
public class EvenNumber {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        int first; 
        int second;
        
        System.out.println("Enter first number");
        first = input.nextInt();
        System.out.println("Enter second number");
        second = input.nextInt();
        int i = first;
        while (i < second){
            if(i%2==0){
                System.out.println(i);
            
            }
            i=i+1;
        }
        
        
        
        
        
        
               
        
    }
    
}
