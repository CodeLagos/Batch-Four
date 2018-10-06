/*
 * NAME: Michael Sanyaolu.
 * E-MAIL: mexismic@gmail.com
 * PROJECT NAME: SMART STOCK
 * SUPERVISOR: Rex Ben
 * Smart Stock is an application aimed at helping merchants on online stores keep
 * track of their stock and ensuring they never run out of stock by notifying them
 * whenever a treshold is reached or exceeded
 */
package stockcontrol;

import java.util.Scanner;

/**
 *
 * @author Eben
 */
public class StockControl {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
     Scanner input = new Scanner(System.in);
          System.out.print("SMART STOCK" + "\n" + "Tell me your name: ");
        String name = input.next();
         System.out.println(name + "," + " welcome to SMART STOCK");
        System.out.print("PRIMARY ITEMS IN STOCK " + "\n" + "Samsung ");
          int samsung = input.nextInt();
        System.out.print("iPhone ");
          int iphone = input.nextInt();
        System.out.print("LG ");
          int lg =input.nextInt();
          
          StockControlHelper stockcontroller = new StockControlHelper(samsung, iphone, lg);
          stockcontroller.SmartStock();
    }
    
}
