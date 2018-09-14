package student;
import java.util.*;
/**
 *
 * @author: ODUKOYA MUYIWA
 * @email:  kayusyiwex@gmail.com
 * @phone:  08149224253
 */

public class Student {


public static void main(String[] args) {
   int i, q, z, c, b;
   int x=0;
   String[] name = new String[30];
   int[] age = new int[30];
   String[] course = new String[30];
   String[] year = new String[30];
   String[] section = new String[30];
   int menuChoice;

   Scanner input = new Scanner (System.in);

   start:
   do{

       System.out.println("\t\t\tStudent Record Menu");
       System.out.println("\t\t1. NAME: ODUKOYA MUYIWA KAYODE\t2. \t3. LEVEL: 300\t4.DEPARTMENT: MECHANICAL ENGINEERING\t5.MATRIC NO. F/HD/11/3430057");
       System.out.println("\t\t1. NAME: NOAH WILLIAM MICHAEL\t2. \t3. LEVEL: 300\t4.DEPARTMENT: MECHANICAL ENGINEERING\t5.MATRIC NO. F/HD/11/3430058");
       System.out.println("\t\t1. NAME: JAMES LOGAN ALEXANDER\t2. \t3. LEVEL: 300\t4.DEPARTMENT: MECHANICAL ENGINEERING\t5.MATRIC NO. F/HD/11/3430059");
       System.out.println("\t\t1. NAME: BENJAMIN MASON ETHAM\t2. \t3. LEVEL: 300\t4.DEPARTMENT: MECHANICAL ENGINEERING\t5.MATRIC NO. F/HD/11/3430060");
       System.out.println("Enter a choice: ");
       menuChoice = input.nextInt();
       
       

       if (menuChoice==1)
       {
           for (z=x; z<=29; z++)
           {
               System.out.println("Full name:");
               name [z] = input.nextLine();
               System.out.println("Age:");
               age [z] = input.nextInt();
               System.out.println("Course:");
               year [z] = input.next();
               System.out.println("Section:");
               section [z] = input.next();
               x++;
               continue start;
           }
       }
               else if (menuChoice==2)
               {
                   for (i=0; i<x; i++)
                   {
                       System.out.println(name[i] + age [i] + course [i] + year [i] + section [i]);
                   }
               }

   } while (menuChoice<4);

}
}


			Student Record Menu
		1. NAME: ODUKOYA MUYIWA KAYODE	2. 	3. LEVEL: 300	4.DEPARTMENT: MECHANICAL ENGINEERING	5.MATRIC NO. F/HD/11/3430057
		1. NAME: NOAH WILLIAM MICHAEL	2. 	3. LEVEL: 300	4.DEPARTMENT: MECHANICAL ENGINEERING	5.MATRIC NO. F/HD/11/3430058
		1. NAME: JAMES LOGAN ALEXANDER	2. 	3. LEVEL: 300	4.DEPARTMENT: MECHANICAL ENGINEERING	5.MATRIC NO. F/HD/11/3430059
		1. NAME: BENJAMIN MASON ETHAM	2. 	3. LEVEL: 300	4.DEPARTMENT: MECHANICAL ENGINEERING	5.MATRIC NO. F/HD/11/3430060
Enter a choice: 
5
BUILD SUCCESSFUL (total time: 5 seconds)
