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
public class quiz {
    public void mathQUIZ(){
    int score = 0;
        String quiz1 = "what is the sum of 2+2+6/5";
        String QuizInstruc = "Answer this questions correctly \n give your answers in numbers not words \n e.g '10','7.54' ";
        JOptionPane.showMessageDialog(null,QuizInstruc);
        String Quiz1 = JOptionPane.showInputDialog(quiz1 + ": ");
        
        
        if ("2".equalsIgnoreCase(Quiz1)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz1)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect \nCorrect answer is 2");
        }
        
        String quiz2 = "what is the sum of 2+2+11/5";
        String Quiz2 = JOptionPane.showInputDialog(quiz2 + ": ");
        if ("3".equalsIgnoreCase(Quiz2)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz2)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        
        String quiz3 = "what is the product of 3x5x5/5" + ": ";
        String Quiz3 = JOptionPane.showInputDialog(quiz3 + ": ");
        if ("15".equalsIgnoreCase(Quiz3)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz3)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        String quiz4 = "what is the square root of 9" + ": ";
        String Quiz4 = JOptionPane.showInputDialog(quiz4 + ": ");
        if ("3".equalsIgnoreCase(Quiz4)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz4)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        
        String quiz5 = "what is the area of a circle whose radius is 5\nLeave your answer as an whole number" + ": ";
        String Quiz5 = JOptionPane.showInputDialog(quiz5 + ": ");
        if ("79".equalsIgnoreCase(Quiz5)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz5)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        
        String quiz6 = "what is the sum of 2+2+11/5" + ": ";
        String Quiz6 = JOptionPane.showInputDialog(quiz6 + ": ");
        if ("3".equalsIgnoreCase(Quiz6)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz6)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }

        String quiz7 = "what is the area of square with the length of 7";
        String Quiz7 = JOptionPane.showInputDialog(quiz7 + ": ");
        if ("49".equalsIgnoreCase(Quiz7)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz7)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        String quiz8 = "what is the length of square with the area of 49";
        String Quiz8 = JOptionPane.showInputDialog(quiz8 + ": ");
        if ("7".equalsIgnoreCase(Quiz8)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz8)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        String quiz9 = "what is the area of square with the length of 7*2/7+6";
        String Quiz9 = JOptionPane.showInputDialog(quiz9 + ": ");
        if ("64".equalsIgnoreCase(Quiz9)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz9)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        String quiz10 = "what is the area of square with the length of 7*2/7+6/4";
        String Quiz10 = JOptionPane.showInputDialog(quiz10 + ": ");
        if ("4".equalsIgnoreCase(Quiz10)){
        JOptionPane.showMessageDialog(null,"Correct");
        score = score + 1;
        }else if ("quit".equalsIgnoreCase(Quiz10)){
                JOptionPane.showMessageDialog(null,"Nice chatting with you!");System.exit(0);
        }else{
        JOptionPane.showMessageDialog(null,"Incorrect");
        }
        
        
        
        JOptionPane.showMessageDialog(null,"Your Score: " + score);
        
        scrammbled run = new scrammbled();
        run.playMORE();
 
    }
}
