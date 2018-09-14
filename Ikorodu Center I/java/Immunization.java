/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package immunization;
import java.util.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

/**
 *
 * @author USER
 */
public class Immunization {

    /**
     * @param args the command line arguments
     */
    
   
               
          
        
       
    
    public static void main(String[] args) {
         LocalDate date;
        String name;
        String dateOfBirth;
        Scanner scan = new Scanner(System.in);
       System.out.println("Welcome to Oke-Eletu PHC \nEnter your Child's Name");
        name = scan.nextLine();
       
        System.out.println("\nEnter Date of Birth");
        dateOfBirth = scan.nextLine();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        
        //for first visit
        String firstVisit = dateOfBirth + "     |     " + "(Hep B O, Opv0,BCG)";
        
        
        
        // for Second Visit
         date = LocalDate.parse(dateOfBirth, formatter).plus(6, ChronoUnit.WEEKS);
         String secondVisit = date + "     |      " + "(Opv 1,Penta 1, Pcv1)";
         
         // for third Visit
          date = LocalDate.parse(dateOfBirth, formatter).plus(10, ChronoUnit.WEEKS);
          String thirdVisit = date + "     |      " + "(Opv 2, Penta 2, Pcv 2)";
          
          // for Fourth Visit
           date = LocalDate.parse(dateOfBirth, formatter).plus(14, ChronoUnit.WEEKS);
           String fourthVisit = date + "     |     " + "(Opv 3, Penta 3, Pcv 3, Ipv)";
           
           // for fifth Visit
            date = LocalDate.parse(dateOfBirth, formatter).plus(6, ChronoUnit.MONTHS);
            String fifthVisit = date + "     |     " + "(Vitamin A 1st Dose)";
            
            
            // for Sixth Visit
            date = LocalDate.parse(dateOfBirth, formatter).plus(9, ChronoUnit.MONTHS);
            String sixthVisit = date + "     |     " + "(Measles 1, Yellow Fever)";
            
            
            // for seventh Visit
            date = LocalDate.parse(dateOfBirth, formatter).plus(12, ChronoUnit.MONTHS);
            String seventhVisit = date + "     |    " + "(Vitamin A 2nd Dose)";
            
            System.out.println("    Dates      |      Vaccine     ");
        
        System.out.println("-------------------------------------------------");
        System.out.println(firstVisit);
        System.out.println(secondVisit);
        System.out.println(thirdVisit);
        System.out.println(thirdVisit);
        System.out.println(fourthVisit);
        System.out.println(fifthVisit);
        System.out.println(sixthVisit);
        System.out.println(seventhVisit);







        

        

            



   
        
    }
    
    
}
