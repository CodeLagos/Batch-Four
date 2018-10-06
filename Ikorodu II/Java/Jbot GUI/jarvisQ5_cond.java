
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
public class jarvisQ5_cond {
    public void q5cond(){
   String subQ5 = "Why: ";
    String colq5 = JOptionPane.showInputDialog("Do you think Nigeria can qualify and win the next World cup[yes/no]");
    if ("yes".equalsIgnoreCase(colq5) || "no".equalsIgnoreCase(colq5)){
                String sub_colq5 = JOptionPane.showInputDialog(subQ5);
                if("quit".equalsIgnoreCase(sub_colq5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
            }else if("quit".equalsIgnoreCase(colq5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
            JOptionPane.showMessageDialog(null,"Input either yes or no: ");
            jarvisQ5_cond run = new jarvisQ5_cond();
            run.q5cond();
            }
    }
    public void sarahQ5_cond(){
        String subQ5 = "Why: ";
    String colq5 = JOptionPane.showInputDialog("Do you think Women should participate in politics[yes/no]");
    if ("yes".equalsIgnoreCase(colq5) || "no".equalsIgnoreCase(colq5)){
                String sub_colq5 = JOptionPane.showInputDialog(subQ5);
                if("quit".equalsIgnoreCase(sub_colq5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
            }else if("quit".equalsIgnoreCase(colq5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else{
            JOptionPane.showMessageDialog(null,"Input either yes or no: ");
            jarvisQ5_cond run = new jarvisQ5_cond();
            run.q5cond();
            }
    }
}




