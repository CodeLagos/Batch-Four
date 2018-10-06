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
public class sub_jbot {
    public void sub_chat(){
        String CollectQ3 = JOptionPane.showInputDialog("1. Jarvis[For Males]\n2. Sarah[For Females]\n3. Gideon Games[For Games]\n");
        if ("1".equalsIgnoreCase(CollectQ3)){
            jarvis run_jarvis = new jarvis();
            run_jarvis.dist_jarvis();
        }else if("quit".equalsIgnoreCase(CollectQ3)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else if("2".equalsIgnoreCase(CollectQ3)){
            sarah run_sarah = new sarah();
            run_sarah.dist_sarah();           
        }else if("3".equalsIgnoreCase(CollectQ3)){
            games play = new games(); 

            play.sub_games();
        }else{
            
            sub_jbot run = new sub_jbot();
            run.sub_chat();

            }
}
}
