/*s
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
public class games {
    public void sub_games(){
            
            JOptionPane.showMessageDialog(null,"Hi I am Gideon Games");
            JOptionPane.showMessageDialog(null,"Let's play some games");
            JOptionPane.showMessageDialog(null,"We have four different sections you can read or play");      
            JOptionPane.showMessageDialog(null,"1. Scrambled Words\n2. Math Quiz\n3. Riddles,Jokes and Stories\n4. Facts");
            String CollectGames = JOptionPane.showInputDialog("Which do u want to play ro read: ");
            if ("1".equalsIgnoreCase(CollectGames)){
                scrammbled s_play = new scrammbled();
                s_play.scrammbled();
            }else if ("2".equalsIgnoreCase(CollectGames)){
                quiz q_play = new quiz();
                q_play.mathQUIZ();
            }else if ("quit".equalsIgnoreCase(CollectGames)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
            }else if ("3".equalsIgnoreCase(CollectGames)){
                jokes j_play = new jokes();
                j_play.introjokesRS();
                j_play.jokesRS();
            }else if ("4".equalsIgnoreCase(CollectGames)){
                facts read = new facts();
                read.jFACTS();
                read.sFACTS();
                scrammbled run = new scrammbled();
                run.playMORE();
            }else{
                games play = new games(); 
                play.sub_games();
            }
    }

}
