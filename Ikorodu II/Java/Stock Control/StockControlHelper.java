/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package stockcontrol;

import java.util.Scanner;

/**
 *
 * @author Eben
 */
public class StockControlHelper {
    Scanner input = new Scanner(System.in);
    int samsung;
    int iphone;
    int lg;
    public StockControlHelper(int S, int I, int L){
        samsung = S;
        iphone = I;
        lg = L;
    }
    public void SmartStock(){
        int tStock = (samsung + iphone + lg);
        System.out.println
           ("TOTAL STOCK = " + tStock);
       int samo = 0; 
       int insSam = (samsung - samo); 
       
       int ipho = 0; 
       int insIps = (iphone - ipho); 
       
       int lgo = 0; 
       int insLg = (lg - lgo);
        
        while (true){ 
       System.out.print("Place an order " + "\n" + "Samsung: ");
      //SAMSUNG
       if (insSam>= (1*samsung)){
                System.out.println("In stock");
        }
        System.out.print("Enter order qty: ");
        samo = input.nextInt(); 
        insSam = (samsung - samo); 
        while(insSam <= (0.1*samsung) && samo > (0.05*insSam) 
                || samo > (0.95*samsung)){
        System.out.println
                 (" sorry, order cannot be processed at this time, try reducing the quantity");
        
    System.out.println("Enter order qty: "); 
         samo = input.nextInt();
         insSam = (samsung - samo);
         if (insSam <= (0.1*samsung) && (samo > (0.05*insSam))){ 
         }
           }
        System.out.println(" CONGRATS! Order for " + samo + " samsung phones completed.");
             
//       IPHONE
        System.out.println("iphone ");
        if (insIps >= (1*iphone)){
                System.out.println("iPhone: In stock");
        }
        System.out.print("Enter order qty: ");
        ipho = input.nextInt(); 
        insIps = (iphone - ipho); 
        while(insIps <= (0.1*iphone) && ipho > (0.05*insIps) 
                || ipho > (0.95*iphone) ){
        System.out.println
                 (" sorry, order cannot be processed at this time, try reducing the quantity");
    System.out.print("Enter order qty: "); 
         ipho = input.nextInt();
         insIps = (iphone - ipho);
         if (insIps <= (0.1*iphone) && ipho > (0.05*insIps) 
                || ipho > (0.95*iphone) || ipho > (0.8*insIps)){
            }
        }
        System.out.println(" CONGRATS! Order for " + ipho + " iphones completed.");
       
        // LG
        System.out.println("LG ");
        if (insLg >= (1*lg)){
                System.out.println("LG: In stock");
       } 
        System.out.println("Enter order qty: ");
        lgo = input.nextInt(); 
        insLg = (lg - lgo);
        while(insLg <= (0.1*lg) && lgo > (0.05*insLg) 
                || lgo > (0.95*lg) ){
        System.out.println
                 (" sorry, order cannot be processed at this time, try reducing the quantity");
    System.out.print("Enter order qty: "); 
         lgo = input.nextInt();
         insLg = (lg - lgo);
         if (insLg <= (0.1*lg) && lgo > (0.05*insLg) 
                || lgo > (0.95*lg) || lgo > (0.8*insLg)){   
            }
         }
        System.out.println(" CONGRATS! Order for " + lgo + " LG phones completed.");
       
        System.out.println("SUCCESSFULL ORDERS SO FAR");
        System.out.println("SAMSUNG = " + samo);
        if (insSam <= (0.3*samsung) )
             {System.out.println("Samsung stock is running low");
        }
        System.out.println("iPhone = " + ipho);
        if (insIps <= (0.3*iphone))
             {System.out.println("iPhone stock is running low");
        }
        System.out.println("LG = " + lgo);
        if (insLg <= (0.3*lg))
             {System.out.println("LG stock is running low");
        }
         int tSold = (samo + ipho + lgo);
           System.out.println("TOTAL SOLD = " + tSold);
    int inStock = (tStock - tSold); System.out.println("TOTAL ITEMS IN STOCK AT THE MOMENT = " + inStock);
                 
            System.out.println("BREAKDOWN OF ITEMS IN STOCK");
            System.out.println("Samsung = " + insSam); // insSam = samsung left in stock 
        
            System.out.println("iPhone = " + insIps);
        
            System.out.println("LG = " + insLg);
            
            System.out.println("Refresh Result?" + "\n" + "Enter 1 to continue or 2 to exit");
            int exit = input.nextInt();
                
                if (exit == 1){continue;}
                if (exit == 2){ 
                     System.out.println("THANK YOU FOR USING SmartStock");
                 System.exit(0); }
                    else {System.out.println("Please enter 1 or 2 ");}
                 exit = input.nextInt();
               samsung = insSam;
               iphone = insIps;
               lg = insLg;
               tStock = (samsung + iphone + lg);
                 
       }
        
 }  
}
    

