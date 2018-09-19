
//package cvitproject;

/**
 *
 * @author senge Samuel  
 */


import java.util.*;

public class newp{
    public static final int NUMBERS = 3;
    public static final int MAX_NUMBER = 10;
  static int dead;
   static int injury;
    public static void main(String[] args) {
        
        
       
      for(int i=0; i<=12; i++){
           evaluate(createWinningNumbers(),getTicket());
           if (dead==3){
               break;
           } else
               dead=0; injury=0;
      }
       
      
    }
    
    // generates a set of the winning  numbers
    public static Set<Integer> createWinningNumbers() {
        Set<Integer> winningNumbers = new TreeSet<Integer>();
        Random r = new Random();
        while (winningNumbers.size() < NUMBERS) {
            int number = r.nextInt(MAX_NUMBER) + 1;
            winningNumbers.add(number);
            
        }
        //System.out.println(winningNumbers);
        return winningNumbers;
    }
    
    // reads the user  number  from the console
    public static Set<Integer> getTicket() {
        Set<Integer> userno = new TreeSet<Integer>();
        Scanner console = new Scanner(System.in);
        System.out.print("Type your " + NUMBERS + 
                         " lucky number: ");
        while (userno.size() < NUMBERS) {
            int number = console.nextInt();
            userno.add(number);
        }
        return userno;
    }
    public static void evaluate(Set<Integer> set1,Set<Integer> set2){
        List<Integer> list1=new ArrayList<>(set1);
        List<Integer> list2=new ArrayList<>(set2);
        for(int i=0; i<3; i++){
            if(list1.get(i)==list2.get(i)){
                dead++;
        }else if(list1.contains(list2.get(i)))
            injury++;
        }
        System.out.println(dead +" dead "+injury+" INJURY");
    }   
   }

