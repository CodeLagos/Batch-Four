/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jbot;
import java.util.Date;
import javax.swing.JOptionPane;


/**
 *
 * @author Joromi
 */
public class sarah {
    public void dist_sarah(){
        Date todaysDATE = new Date();
        String greet = "";
        if(todaysDATE.getHours() >= 16){
           greet = "Good Evening";
        }else if(todaysDATE.getHours() < 16){
           greet = "Good Afternoon";
        }else if(todaysDATE.getHours() >= 0){
            greet = "Good Morning";
        }else{
            greet = "Hello!";
        }
          
        String q1 , q2 , q3 , q4 , q5 , q6 , q7 , q8 , q9 , q10 , q11 , q12 , q13 , q14 , q15 , q16 , q17 , q18 , q19 , q20 , q21 , q22 , q23 , q24 , q25 , q26 ;
        q1 = greet + " i am Sarah and you are: ";
        
        String colq1 = JOptionPane.showInputDialog(q1);
        if("quit".equalsIgnoreCase(colq1)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
        
            q2 = "How are you "+ colq1 +": ";
        String colq2 = JOptionPane.showInputDialog(q2);
            if("Fine and you".equalsIgnoreCase(colq2) || "sad and you".equalsIgnoreCase(colq2) || "not so good and you".equalsIgnoreCase(colq2) || "bad and you".equalsIgnoreCase(colq2) || "feeling nice and you".equalsIgnoreCase(colq2) || "and you".equalsIgnoreCase(colq2) || "good and you".equalsIgnoreCase(colq2) || "cool and you".equalsIgnoreCase(colq2)){
                JOptionPane.showMessageDialog(null,"Same!");
        
            }else if("quit".equalsIgnoreCase(colq2)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
            JOptionPane.showMessageDialog(null,"Hmmmmmmmm okay!");
            }
        q3 = "Tell me about your self: ";
        String colq3 = JOptionPane.showInputDialog(q3);
        if("quit".equalsIgnoreCase(colq3)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
            JOptionPane.showMessageDialog(null,"Nice!");
                
        q4 = "What do you think about Gender Equality: ";
        String colq4 = JOptionPane.showInputDialog(q4);
        if("quit".equalsIgnoreCase(colq4)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
                
        q5 = "Do you have any plans in entering politics or leading a set of people[yes/no]:  ";
        String colq5 = JOptionPane.showInputDialog(q5);
        if("quit".equalsIgnoreCase(colq5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
            jarvisQ5_cond run = new jarvisQ5_cond();
            run.sarahQ5_cond();
        int score = 0;   
        q6 = "Let me test your knowledge on the 2018 World Cup: ";
        String subQ6_1 = "Who hosted the World Cup: ";
        String subQ6_2 = "Who won the World Cup: ";
        String subQ6_3 = "Who disqualified Nigeria from the World Cup: ";
        String subQ6_4 = "Who did Nigeria lose their first match to: ";
        String subQ6_5 = "Who did Nigeria draw with in the World Cup: ";
        JOptionPane.showMessageDialog(null,q6);
        

            String subcolq6_1 = JOptionPane.showInputDialog(subQ6_1);
            
                if ("russia".equalsIgnoreCase(subcolq6_1)){
                    score = score + 1;
                    JOptionPane.showMessageDialog(null,"Correct!");
                }else if("quit".equalsIgnoreCase(subcolq6_1)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
                    JOptionPane.showMessageDialog(null,"Incorrect!");
                }
            String subcolq6_2 = JOptionPane.showInputDialog(subQ6_2);
             if ("France".equalsIgnoreCase(subcolq6_2)){
                    score = score + 1;
                    JOptionPane.showMessageDialog(null,"Correct!");
                }else if("quit".equalsIgnoreCase(subcolq6_2)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
                    JOptionPane.showMessageDialog(null,"Incorrect!");
                }
                
           String subcolq6_3 = JOptionPane.showInputDialog(subQ6_3);
            
                if ("Argentina".equalsIgnoreCase(subcolq6_3)){
                    score = score + 1;
                    JOptionPane.showMessageDialog(null,"Correct!");
                }else if("quit".equalsIgnoreCase(subcolq6_3)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");
            }else{
                    JOptionPane.showMessageDialog(null,"Incorrect!");
                }
            String subcolq6_4 = JOptionPane.showInputDialog(subQ6_4);
            
                if ("Croatia".equalsIgnoreCase(subcolq6_4)){
                    score = score + 1;
                    JOptionPane.showMessageDialog(null,"Correct!");
                }else if("quit".equalsIgnoreCase(subcolq6_4)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");
            }else{
                    JOptionPane.showMessageDialog(null,"Incorrect!");
                }
            String subcolq6_5 = JOptionPane.showInputDialog(subQ6_5);
            
                if ("Iceland".equalsIgnoreCase(subcolq6_5)){
                    score = score + 1;
                    JOptionPane.showMessageDialog(null,"Correct!");
                }else if("quit".equalsIgnoreCase(subcolq6_5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");
            }else{
                    JOptionPane.showMessageDialog(null,"Incorrect!");
                }   
                    if(score == 1){
                        JOptionPane.showMessageDialog(null,"Hmmmm You answered " + score + " question corectly");
                    }else if(score == 0){
                        JOptionPane.showMessageDialog(null,"You answered NO questions corectly");
                    }else if(score == 5){
                        JOptionPane.showMessageDialog(null,"You answered 5 questions corectly and you won your self a recharge card for any network");
                        JOptionPane.showMessageDialog(null,"14588-57895-51578-799");
                        JOptionPane.showMessageDialog(null,"You can win another soon as the chat goes on");
                    }else{
                    JOptionPane.showMessageDialog(null,"WOW! You answered " + score + " questions corectly");
                    }
                    
        q7 = "Am feeling good today \nso here is the thing\nguess my nickname and i will give you 1000 naira worth of airtime: ";
        String colq7 = JOptionPane.showInputDialog(q7);
        
            if("joromi".equalsIgnoreCase(colq7)){
                JOptionPane.showMessageDialog(null,"You have won your self 1000 naira airtime");
                String airtym = JOptionPane.showInputDialog("Select your network: ");
                if ("airtel".equalsIgnoreCase(airtym) ||"Mtn".equalsIgnoreCase(airtym) ||"9mobile".equalsIgnoreCase(airtym) ||"glo".equalsIgnoreCase(airtym) ||"ntel".equalsIgnoreCase(airtym) || "zain".equalsIgnoreCase(airtym) ||"etisalat".equalsIgnoreCase(airtym)){
                        JOptionPane.showMessageDialog(null,"14588-57895-51578-799");
                    }else if("quit".equalsIgnoreCase(airtym)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
                    JOptionPane.showMessageDialog(null,"I only have for\nAirtel \nGlo \nNtel \nMtn and \n9mobile");
                    }
            }else if("quit".equalsIgnoreCase(colq7)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
                JOptionPane.showMessageDialog(null,"Incorrect sorry maybe next time");
            }
        
       
        
        
        
        
        jarvisQ9_cond runq9 = new jarvisQ9_cond();
        runq9.maincond();
        
        
        JOptionPane.showMessageDialog(null,"\nLet me tell you some facts you proberbly did not know");
        JOptionPane.showMessageDialog(null,"After every fact press enter to go to the next fact"); 
        facts read = new facts();
        read.sFACTS();
        
        JOptionPane.showMessageDialog(null,"For more facts check Gideon facts");
        
        
        games play = new games(); 

        play.sub_games();
}
}
