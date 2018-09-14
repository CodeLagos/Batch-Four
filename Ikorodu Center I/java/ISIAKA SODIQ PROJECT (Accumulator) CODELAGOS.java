
package accumulator;
import java.util.*;
/**
 *ISIAKA SODIQ
 * ISIAKSOSKEY@GMAIL.COM
 * 08142760707
 * @author zeal brown
 */
public class Accumulator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int age;
        String name;
        Scanner s =new Scanner(System.in);
        System.out.println("Please enter your name:");
        name=s.next();
        System.out.println("Please enter your Age:");
        age=s.nextInt();
       
        if (age>=18)
        {
        System.out.println("You are eligible to vote.");
    }
        else {
                System.out.println("You are not eligible to vote.");
                return;
                }
        System.out.println("Choose party you will like to vote for:");
        System.out.println("---------------------------------------------");
        System.out.println("  PARTY   |   CANDIDATE NAME    |  VOTE NO.  ");
        System.out.println("---------------------------------------------");
        System.out.println("  PDP     |       ISIAKA        |     1      ");
        System.out.println("  APC     |       SODIQ         |     2      ");
        System.out.println("  ADC     |       KUNLE         |     3      ");
        System.out.println("---------------------------------------------");
        System.out.println("\n Choose between 1 to 3 to vote: ");
        
        int index = s.nextInt();
        if (index==1){
            System.out.println("You have voted for PDP -->(ISIAKA)");
        }
        else if (index==2){
            System.out.println("You have voted for APC -->(SODIQ)");
        }
        else if (index==3){
            System.out.println("You have voted for ADC -->(KUNLE)");
        }
        else{
            System.out.println("Invalid input");
        }
        
    }
    
}
