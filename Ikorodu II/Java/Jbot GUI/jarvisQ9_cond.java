
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jbot;

import javax.swing.JOptionPane;


/**
 *
 * @author Joromi
 */
public class jarvisQ9_cond {
    public void subcond(){
    String subQ9_1 = JOptionPane.showInputDialog("Have you attened or register[yes/no]");
    if("yes".equalsIgnoreCase(subQ9_1)){
                    String subQ9_2 = JOptionPane.showInputDialog("Which course did you register for");
                    if("quit".equalsIgnoreCase(subQ9_2)){
                        JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
                    }
                    JOptionPane.showMessageDialog(null,"Nice course there bro");
                    String plans = "So what are your plans with the acquired knowledge: ";
                    String colplans = JOptionPane.showInputDialog(plans);
                    if("quit".equalsIgnoreCase(colplans)){
                        JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
                    }
                    
     }else if("quit".equalsIgnoreCase(subQ9_1)){
        JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
    }else if("no".equalsIgnoreCase(subQ9_1)){
            //open code lagos link
            JOptionPane.showMessageDialog(null,"Open this link: www.codelagos.org");
        }else{
            JOptionPane.showMessageDialog(null,"Input yes or no: ");
            jarvisQ9_cond run = new jarvisQ9_cond();
            run.subcond();
        }
    }
    public void maincond(){
        String colq9 =  JOptionPane.showInputDialog("Have you heard about codelagos[yes/no]: ");
        if("yes".equalsIgnoreCase(colq9)){
            jarvisQ9_cond run = new jarvisQ9_cond();
            run.subcond();
                
        }else if("quit".equalsIgnoreCase(colq9)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else if("no".equalsIgnoreCase(colq9)){
                    //open code lagos link
                    JOptionPane.showMessageDialog(null,"Open this link: www.codelagos.org");
        }else{
              JOptionPane.showMessageDialog(null,"Input yes or no: ");
              jarvisQ9_cond run = new jarvisQ9_cond();
              run.maincond();
                    
            }
    }
   
    
}
