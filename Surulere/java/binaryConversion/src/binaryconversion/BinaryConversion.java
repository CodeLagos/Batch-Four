/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package binaryconversion;
import java.util.ArrayList;
import java.util.Scanner;
/**
 *
 * @author Tundesky
 */
public class BinaryConversion {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input=new Scanner(System.in);
        ArrayList<String>polly=new ArrayList<String>();
        int a;
        int b;
        System.out.println("enter number in base 10");
        a=input.nextInt();
        System.out.println("enter number to convert it to");
        b=input.nextInt();
        int remainder=a%b;
        int quotient=a/b;
        String g=Integer.toString(remainder);
        String sp="";
        String po="";
        sp=sp+g;
        while(quotient!=0){
            a=quotient;
            remainder=a%b;
            quotient=a/b;
            sp=sp+Integer.toString(remainder);
        }
        int k=sp.length();
        
        while(k>0){
             po=po+sp.charAt(k-1);
             k=k-1;
        }
       System.out.println("The Conversion is "+po);    
       
    }
    
}
