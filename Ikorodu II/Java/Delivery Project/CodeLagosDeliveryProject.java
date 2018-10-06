/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codelagosdeliveryproject;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Oladotun Aboaba
 */
public class CodeLagosDeliveryProject {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // create introductory text for the app
    //create option for location data collection
    Scanner first = new Scanner(System.in);
    int continueRunning = 1;
    while(continueRunning != 0)
    {
        
    try {   
    System.out.println("How many bags of rice would you like to purchase?: ");
    double b =  first.nextDouble();
    int bag = 1200;
    double x = ( b * bag);
    System.out.println( "the cost of " + b + " bags is "+ x + "naira. ");    
       Math.random();
    }catch(InputMismatchException e){
            System.out.println( e + "\n" + "please input a figrue, Eg. 5." + "\n" + "Please restart the operation.");
    //catch error and force app restart
            System.exit(0);
    }
    //request for location input
    System.out.println("Enter your location: ");
     String input_a = first.next();
    //create synch to the helper class
    HelperClassCodeLagosDeliveryProject helper = new HelperClassCodeLagosDeliveryProject(input_a);
    helper.formular(); 
    continueRunning = first.nextInt();
    
    } 
    }
}
