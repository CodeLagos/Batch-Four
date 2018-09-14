/*
CODE LAGOS PROJECT
**MAIN CLASS**
AIMAKHEDE DAVID SUNDAY
08166554021
aimakhededavido@gmail.com
*/
package lagosrwtsproject;

import java.util.*;

public class LagosRWTSproject {

    public static void main(String[] args) {
    
    String Name, KinName;
    int TransportFee, x = 1500;
    long Number, KinsNumber;
    
    Scanner input = new Scanner(System.in);
            
    System.out.println("WELCOME TO, \nLAGOS RAILWAY TRANSPORTATION SERVICE (LARWTS)");
    System.out.println("LAGOS TO BENIN TRAIN TERMINAL(ONLINE BOOKING)");
    System.out.println("******************************************************\n");
    System.out.println("TO REGISTER FOR AN ONLINE TICKET FOR LAGOS TO BENIN TRAIN (#1500)"
                       + ", \nPLEASE FILL IN YOUR INFORMATION\n"); 
    System.out.println("ENTER YOUR FULL NAME: ");
    Name = input.nextLine();
    System.out.println("\nENTER YOUR NEXT OF KIN'S NAME: ");
    KinName = input.nextLine();
    System.out.println("\nENTER YOUR TELEPHONE NUMBER: ");
    Number = input.nextLong();   
    System.out.println("\nENTER YOUR NEXT OF KINS'S PHONE NUMBER: ");
    KinsNumber = input.nextLong();
    System.out.print("\nTRANSPORTATION FEE: #");
    TransportFee = input.nextInt();
    
    while(TransportFee != x){
    System.out.print("INACCURATE TransportationFee!, \nTRANSPORTATION FEE: #");
    TransportFee = input.nextInt();
    
    }
    
    System.out.println("Congratulations!, You Have Paid The Accurate Transportation Fee.\n");
    
    
        System.out.printf("====================================================");
        System.out.println("\nLAGOS RAILWAY TRANSPORTATION SERVICE (LARWTS)");
        System.out.printf(Name+"'S TRAIN TICKET INFORMATION");
        
        System.out.printf("\n====================================================");
        System.out.printf("\n****************************************************");
        System.out.printf("\nNAME:          ||  %s", Name);
        System.out.printf("\nPHONE NUMBER:  ||  0%d", Number);
        System.out.printf("\nN.O.K'S NAME:  ||  %s", KinName);
        System.out.printf("\nN.O.K'S NUMBER:||  0%d", KinsNumber);
        System.out.printf("\nAMOUNT PAID:   ||  #%d.00k\n", TransportFee);
        
        LagosRWTShelper Dates = new  LagosRWTShelper();
        Dates.Fix();
                
        System.out.println("\nTHANK YOU!, "+Name+"! FOR CHOOSING OUR TRANSPORTATION SERVICE.");
        System.out.println("");
    
        
    }
    }
    

