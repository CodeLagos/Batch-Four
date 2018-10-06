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
public class sup_jbot {
    public void innerJBOT(){
        
        String Q1 = "Do you want to chat with me [yes/no]: ";
        
        String CollectQ1 = JOptionPane.showInputDialog(Q1);
        
        
        
        if ("yes".equalsIgnoreCase(CollectQ1)){
            String Q2 = "Hi am Jbot, what is your name: ";
            String CollectQ2 = JOptionPane.showInputDialog(Q2);
            if("quit".equalsIgnoreCase(CollectQ2)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }
            JOptionPane.showMessageDialog(null,"I Officially Welcome You " + CollectQ2 +" To Jbot Environment");
            JOptionPane.showMessageDialog(null,"We Have three main Chat bots");
            sub_jbot run = new sub_jbot();
            run.sub_chat();
        }else if("quit".equalsIgnoreCase(CollectQ1)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else if("no".equalsIgnoreCase(CollectQ1)) {
            JOptionPane.showMessageDialog(null,"Bye!!!, When you are ready do chat restart me B)");
        }
        else{
            JOptionPane.showMessageDialog(null,"Sorry input either yes or no");
            sup_jbot run = new sup_jbot();
            run.innerJBOT();
            
            
        }
        
       
    }
}
