/** TAIWO AMINAT ADESHOLA
* 0703 185 1082, 0815 211 2416
* aminataiwo26@gmail.com
*/

//package practice;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
/**
 *
 * @author DISTINCT
 */
public class Practice {
    int [] myArray = new int [3];
    public Practice(){ }
    public static void main(String[] args) {
        // TODO code application logic hereRandom rn = new Random();
        Scanner input= new Scanner(System.in);
        System.out.println("Hello Children!");
        System.out.println("How are you today?");
        int i=0;
        int rdeadValue =0;
        int rinjuredValue = 0;
        int threeNumbers = 0;
        int count=0;
        while(i<12){
            //int threeNumbers
            
           while(true){
               
                System.out.print("\nPlease enter three digit numbers at random: ");
                threeNumbers = input.nextInt();
                
                String nextvalue= "" + threeNumbers;
               
                if( nextvalue.length()== 3){
                    break;
                }
                else if (nextvalue.length()< 3 || nextvalue.length()> 3) {
                    System.out.print("\nKindly ensure you enter three digit numbers");
                    count++;
                }
                if(count==3){
                    System.exit(0);
                }
                
            }
            int value1= threeNumbers % 10;
            int remainder= threeNumbers /10;
            int value2 = remainder % 10;
            int value3 = remainder /10;

            int [] sArray = new int[3];
            sArray [0] = value3;
            sArray [1] = value2;
            sArray [2] = value1;
            
            Practice rand = new Practice();
            rand.storerandom_array();

            rdeadValue = rand.deadValue(sArray);
            rinjuredValue = rand.injuredValue(sArray);
            System.out.println(" The number of dead is: " + rdeadValue );
            System.out.println(" The number of injured is: " + rinjuredValue );  
            if(rdeadValue == 3 && rinjuredValue == 0){
                break;
            }
            else if (rdeadValue < 3 && rinjuredValue < 3){
                        System.out.println("Try again");
            }               
        }
            
        if(rdeadValue == 3 && rinjuredValue == 0){
                System.out.println("Application accepted");}
         else if (rdeadValue < 3 && rinjuredValue < 3){
                        System.out.println("Try again");
                }
          }      
      
    public int randFirstNumber(){
        int rand = (int)(ThreadLocalRandom.current().nextInt(0, 9));
        return rand;
    }    
    
    public void storerandom_array(){
        int i = 0;     
        while(i<3){
            myArray[i] = this.randFirstNumber();
              i++;
        } 
        System.out.print("The 3 random values compute by the computer are: ");
        for (int value: myArray) {
        	System.out.print(value);
        }
        System.out.println(" ");
    }
    
    public int deadValue(int [] value){
        int count = 0;
        for (int i = 0;i<3;i++){
              if (myArray[i]==value[i]){
                  count++;
              }
           
        }
        return count;
    }
    
    public int injuredValue(int [] value){
        int count = 0;
        for (int i = 0;i<3;i++){
         outer:for (int j = 0;j<3;j++){
                 if (myArray[i]==value[j]){
                     if (i==j){
                         continue outer;
                     }
                     count++;
              }
          }
        }
        return count;
    }
}

  
