package com.kyt;
//Name: Alayande Daniel
//Email: alayandedaniel@ymail.com
//Project Name: KYT (Know Your Temperament Application)
//Supervisor's Name: Rex Ben
//About: 
//This short test was designed to help users figure out their classical personality type: 
//Sanguine, Phlegmatic, Choleric or Melancholic. The test consists of only fifteen questions; to avoid errors, 
//user thinks of thier most typical behavior and answer accordingly. 

import java.util.InputMismatchException; 
import java.util.Scanner;

public class Kyt {

  public static void main(String[] args) {
   Scanner input = new Scanner (System.in);
   System.out.print("Enter your name: ");
   String name = input.nextLine();
   System.out.println("Welcome " + name + "!" + "\n" + "To know your temperament, kindly answer the following questions by selecting from option (a - d).");
   while(true){
       try{
       System.out.println("To continue press 1, to exit press 2");
       int collect = input.nextInt();
       if(collect ==1){
   System.out.println("Q1. Someone is about to beat you up. You: " + "\n" + "(a) Fight him and give him a nice beating" + "\t" + "(b) Run, cos you don't wanna get hurt" + "\n" + "(c) Slap him in the face and get the hell out of there" + "\t" + "(d) Get beaten, cos you don't want enemies");
   System.out.print("Ans: ");
   String ans1 = input.nextLine();
   System.out.println("Q2. What would be one reason if you had hundred of friends? " + "\n" + "(a) I can't have hundred of friends!" + "\t" + "(b) I'm not social, so i've got just few friends" + "\n" + "(c) Cos i love being around friends" + "\t" + "(d) Cos i'm usually nice and don't get offended easily");
   System.out.print("Ans: ");
   String ans2 = input.nextLine();
   System.out.println("Q3. You are a chef in a kitchen with 10 other chefs, suddenly there's a fire outbreak. What would be your reaction?" + "\n" + "(a) Calm down. We can't do anything if everyone is freaking out." + "\t" + "(b) Complain about their carelessness but find a solution" + "\n" + "(c) Freak out and try find a safe spot" + "\t" + "(d) OMG! We are dead.");
   System.out.print("Ans: ");
   String ans3 = input.nextLine();
   System.out.println("Q4. In a group, you are most likely to be: " + "\n" + "(a) The leader" + "\t" + "(b) The influential person" + "\n" + "(c) The idea person" + "\t" + "(d) The shy person");
   System.out.print("Ans: ");
   String ans4 = input.nextLine();
   System.out.println("Q5. What is the usual emotion you feel?" + "\n" + "(a) Anger" + "\t" + "(b) Hapiness" + "\n" + "(c) Depends on the situation" + "\t" + "(d) Sadness");
   System.out.print("Ans: ");
   String ans5 = input.nextLine();
   System.out.println("Q6. Are you:" + "\n" + "(a) Extroverted with a degree of ambiversion" + "\t" + "(b) Introverted with a degree of ambiversion" + "\n" + "(c) Introverted" + "\t" + "(d) Extroverted");
   System.out.print("Ans: ");
   String ans6 = input.nextLine();
   System.out.println("Q7. How do you cope with people you don't like?" + "\n" + "(a) To hell with them!" + "\t" + "(b) Open up to them and become friends" + "\n" + "(c) Avoid them" + "(d) Pretend to be friends and be nice to them");
   System.out.print("Ans: ");
   String ans7 = input.nextLine();
   System.out.println("Q8. When meeting someone new, do you trust them immediately?" + "\n" + "(a) No! Why would i?" + "\t" + "(b) I don't know" + "\n" + "(c) Yes, i am making a new friend" + "\t" + "(d) A little bit");
   System.out.print("Ans: ");
   String ans8 = input.nextLine();
   System.out.println("Q9. Are you a/an:" + "\n" + "(a) Optimist? Yeah!" + "\t" + "(b) Realist? Yeah, sure i am." + "\n" + "(c) Pessimist? Sometimes." + "\t" + "(d) Not really sure cos it depends on everyone else? Yes.");
   System.out.print("Ans: ");
   String ans9 = input.nextLine();
   System.out.println("Q10. Do your friends like being around you?" + "\n" + "(a) I don't know. They call me bossy." + "\t" + "(b) Kind of" + "\n" + "(c) Yes, but i'm always stuck between chats" + "\t" + "(d) Not like. They love being around me.");
   System.out.print("Ans: ");
   String ans10 = input.nextLine();
   System.out.println("Q11. When your friend is sad. you:" + "\n" + "(a) Feel sorry, but barely see it just as intensely" + "\t" + "(b) Try to cheer them up" + "\n" + "(c) are moved with so much feeling for them that you end up crying too" + "\t" + "(d) Just listen");
   System.out.print("Ans: ");
   String ans11 = input.nextLine();
   System.out.println("Q12. 3 more questions to go. Are you relieved?" + "\n" + "(a) No. There's still more questions to answer" + "\t" + "(b) Huh, really? I was having so much fun" + "\n" + "(c) I can always go far more if you like" + "\t" + "(d) Finally! We are almost done. This quiz is so long.");
   System.out.print("Ans: ");
   String ans12 = input.nextLine();
   System.out.println("Q13. What element defines you best?" + "\n" + "(a) Fire" + "\t" + "(b) Earth" + "\n" + "(c) Air" + "\t" + "(d) Water");
   System.out.print("Ans: ");
   String ans13 = input.nextLine();
   System.out.println("Q14. What are your virtues?" + "\n" + "(a) Leader, confident" + "\t" + "(b) Analytical, perfectionist" + "\n" + "(c) Enthusiastic, people-person" + "\t" + "(d) calm, inoffensive");
   System.out.print("Ans: ");
   String ans14 = input.nextLine();
   System.out.println("Q15. What are your flaws?" + "\n" + "(a) Quick-tempered, bossy" + "\t" + "(b) Lover, harsh on self" + "\n" + "(c) Talkative, dramatic" + "\t" + "(d) too shy, indecisive");
   System.out.print("Ans: ");
   String ans15 = input.nextLine();
   
   
   System.out.println("Hi " + name + ", " + "Thanks for your time." + "\n" + "Your predominant temperament is the one where you have the highest score; your secondary temperament is where you have your second highest score.");
   
   String arrayOfAnswers[] = {ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15};
		
		String possibleAnswers1[] = {"a"};
		String possibleAnswers2[] = {"b"};
		String possibleAnswers3[] = {"c"};
		String possibleAnswers4[] = {"d"};

		
		for(String answer1 : possibleAnswers1)
		{
			System.out.println("Choleric" + ":" + countOccurrenceOf(answer1, arrayOfAnswers));
		}
		for(String answer2 : possibleAnswers2)
		{
			System.out.println("Melancholic" + ":" + countOccurrenceOf(answer2, arrayOfAnswers));
		}
		for(String answer3 : possibleAnswers3)
		{
			System.out.println("Phlegmatic" + ":" + countOccurrenceOf(answer3, arrayOfAnswers));
		}
		for(String answer4 : possibleAnswers4)
		{
			System.out.println("Sanguine" + ":" + countOccurrenceOf(answer4, arrayOfAnswers));
		}
	}else{
       System.exit(0);}
  }catch(InputMismatchException e){}
   
   }
  }
	private static int countOccurrenceOf(String answer, String arrayOfAnswers[])
	{
		int count = 0;
		
		for(String s : arrayOfAnswers)
		{
			if(answer.equals(s))
			{
				count++;
			}
		}
		return count;
}
}

