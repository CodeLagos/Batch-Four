/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
*/

//DETAILS
/**
 * 
 *
*NAME: OLISA JEREMIAH
*EMAIL: JEREMIAHOLISA453@GMAIL.COM
SUPERVISIORS NAME: REX BEN
*
* BRIEF DESCRIPTION
*    JBOT IS A GUI CHAT BOT POWERED BY JAVA AND JAVAX SWING JOPTIONPANE
 *   JBOT IS A CHAT BOT WHICH ENGAGES USER INTRESTING AND EDUCATIONAL CHATS WITH UPDATE ABOUT RECENT EVENTS
  *  JBOT HAS A SYSTEM ENABLES IT TO GREET USER ACCORDING TO THEIR TIME
   * JBOT HAS A FREE GIFT IN SECTION IN TWO OF ITS CHAT
*
* JBOT ALLOWS USER TO PLAY INRESTING GAMES LIKE 
    *1. SCRAMMBLED - WHERE USER RE-ARRANGES WORDS TO THEIR CORRECT FORMS
    *2. MATH QUIZ - WHERE USER AS TO SOLVE SIMPLE MATH QUESTIONS
    *3. JOKES - WHERE USER AS TO PICK FUN JOKES THEY WANT TO READ
    *4. FACTS - WHERE USER READS INTERESTING FACTS ABOUT THE WORLD AND MOSTLY THEIR BODY
 *
**/

package jbot;

import javax.swing.JOptionPane;


/**
 *
 * @author Joromi
 */
public class Jbotgui {

    
    public static void main(String[] args) {
        // TODO code application logic here
        JOptionPane.showMessageDialog(null,"You can type 'quit' at any time to close chat"); 
        JOptionPane.showMessageDialog(null,"Plese do not use any shortcut like fyn,gr8,etc."); 
       sup_jbot run = new sup_jbot();
       run.innerJBOT();
        
    }
    
}
