import java.util.concurrent.ThreadLocalRandom;

class Rannumber{
    //Property of the class
    private int value1;
    private int value2;
    private int value3;
    
    //Constructor
    Rannumber(){}
    
    //Declaration of Array
    private int [] rand = new int [3];
    
    //Accessors
    public int getValue1(){return value1;}
    public int getValue2(){return value2;}
    public int getValue3(){return value3;}
    public int[] getRand(){return rand;}
    
    //this Method generates random number 
    public void random1(){
        value1 = (int)(ThreadLocalRandom.current().nextInt(1, 9));
        value2 = (int)(ThreadLocalRandom.current().nextInt(1, 9));
        value3= (int)(ThreadLocalRandom.current().nextInt(1, 9));
        rand[0]= value1;
        rand[1]= value2;
        rand[2]= value3;
        this.Check();
    }
    
    //this method returns the number(s) of dead
    public int dead(int[] value){
        int count = 0;
        for(int i=0;i<3;i++){
            if(rand[i]==value[i]){
                count++;
            }
        }
        return count;
    }
    
    //this method returns the number(s) of injured
    public int injured(int[] value){
        int count = 0;
        for(int i=0;i<3;i++){
         outer:for(int j=0;j<3;j++){
                  if(rand[i]==value[j]){
                     if (i==j){
                       continue outer;
                     }
                     count++;
                   } 
                              
            }
        }
        return count;
    }
    
    //this method checks for the uniqueness of the generated random number
    public void Check(){
        while(true){
            for(int i = 0;i<2;i++){
              for(int j=i+1;j<3;j++){
                  if(rand[i]==rand[j]){
                     rand[i]=(int)(ThreadLocalRandom.current().nextInt(1, 9));
                  }
              }
            }
            if((rand[1]!=rand[2])&& rand[1]!=rand[0] && rand[2]!=rand[0]){
                break;
            }
        }
        
    }
}