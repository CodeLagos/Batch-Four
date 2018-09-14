/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculator;

import java.util.Scanner;
import java.util.InputMismatchException;



import	calculator.Calculator;
/**
 *
 * @author oyekoya
 */
public class Calculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        char operator;
                Double number1, number2, result;
                
                Scanner scanner = new Scanner(System.in);
                System.out.print("Enter operator (either +, -, * or /): ");
                operator = scanner.next().charAt(0);
                System.out.print("\nEnter number1: ");
                number1 = scanner.nextDouble();
                System.out.print("Enter number2: ");
              
                       
                number2 = scanner.nextDouble();  
                
                switch (operator) {
                    case '+':
                        result = number1 + number2;
                        System.out.print(number1 + "+" + number2 + " = " + result);
                        break;
                        
                    case '-':
                        result = number1 - number2;
                        System.out.print(number1 + "-" + number2 + " = " + result);
                        break;
                       
                       case '*':
                        result = number1 * number2;
                        System.out.print(number1 + "*" + number2 + " = " + result);
                        break;
                           
                       case '/':
                        result = number1 / number2;
                        System.out.print(number1 + "/" + number2 + " = " + result);
                        break;
                    
                       default:
                       System.out.println("invalid operator");
                       break;
                       
                                
                            
                }
                
    }
    
}
