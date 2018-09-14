/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simpleinterest;
import java.util.Scanner;
/**
 *
 * @author oyekoya
 */
public class SimpleInterest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        double pr,ra;
        int t, n;
        Scanner inp = new Scanner(System.in);
        System.out.println("Enter the principle");
        pr= inp.nextDouble();
        System.out.println("Enter the Rate");
        ra= inp.nextDouble();
        System.out.println("Enter the Time period");
        t= inp.nextInt(); 
        System.out.println("Enter the Time frequency");
        n=inp.nextInt();
        double si=pr*ra*t;
        si /=n*100;
        System.out.println("Calculated S.I. "+si);
    }
    
}
