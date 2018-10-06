package com.phone;
import java.util.Scanner;

public class Phone {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
   
   System.out.println("Enter the phone's name'");
   String name =input.nextLine();
   System.out.println("Does the phone On? ");
   System.out.println("a. Yes b. No c. Sometimes");
   String ans =input.nextLine();
   System.out.println("Can you see what's on Screen?'");
   System.out.println("a. Yes b. No c. Sometimes");
   String ans1=input.nextLine();
   System.out.println("Are the phone's keypad/ touch pad working well'");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans2=input.nextLine();
    System.out.println("Is touch pad broken? ");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans3 =input.nextLine();
    
    System.out.println("Did the phone fell into water? ");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans4 =input.nextLine();
    System.out.println("Does the phone lag?");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans5=input.nextLine();
    
    System.out.println("Does the phone runs on high temperature");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans6=input.nextLine();
    System.out.println("Does the phone trips Off? ");
    System.out.println("a. Yes b. No c. Sometimes");
    String ans7 =input.nextLine();
    String Answers[] ={ans,ans1,ans2,ans3,ans4,ans5,ans6,ans7};
    
    String Answer1[]= {"a"};
    String Answer2[]= {"b"};
    String Answer3[]= {"c"};
    String Answer4[]= {"d"};
    
    for(String com1 :Answer1){
      System.out.println("The phone needs a new lcd");
      
    }
    for(String com2 : Answer2){
      System.out.println("The phone needs to be serviced");
    }
    for(String com3 :Answer3){
      System.out.println("The phone has virus ");
    }
    
    
  }
}
