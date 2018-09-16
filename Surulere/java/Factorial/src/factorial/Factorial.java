/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package factorial;
import java.util.Scanner;
/**
 *
 * @author hp
 */
public class Factorial {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input=new Scanner(System.in);
        int i;
        int fact;
        System.out.println("enter a number");
        i=input.nextInt();
        fact=1;
        while(i!=0){
            fact=fact*i;
            i=i-1;
        }
        System.out.printf("the factorial of the number you entered is %d",fact);
    }
    
}
