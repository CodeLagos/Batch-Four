package otherbases;
// import java elements
import java.util.Scanner;

public class OtherBases {
    
    public static void main(String[] args) {
        
        // PROJECT WORK OF IKE, GOODNEWS O. AND PENDER, RAYMOND
        // CODE_LAGOS JAVA CLASS AUG/SEPT.
        
        // Declare the Scanner input system
        Scanner sc=new Scanner(System.in);
        
        // Receive the decimal number to be converted
        System.out.print("Enter the decimal number : ");
        int n=sc.nextInt(); // n is the number in base 10
        
        // Receive the base to be converted to
        System.out.print("Enter the base you would like to convert the number to : ");
        int b=sc.nextInt(); // b is the base to be converted to
        
        int q=n,r; // q is the quotient and r is the remainder
        
        String ans="";
        while(q!=0)
        {
            r=q%b;
            ans=r+ans;
            q=q/b;
        }
        // print out the result
        System.out.println("The conversion of "+n+ " in base 10 is " +ans+ " in base "+b);
        
        System.out.println("DONE!");
        
    }
    
}
