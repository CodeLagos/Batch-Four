/*Code Lagos
 * Adedeji Damilola Isaiah
 * 08147789079
 * adedeji.adewunmi0970@gmail.com
 */
package performanceappraisal;

import java.util.Scanner;

/**
 *
 * @author ADEDEJI DAMILOLA ISAIAH
 */
public class PerformanceAppraisal {
    
    

    /**
     * @param args the command line arguments
     */
    public static String check (int i) {
        String returnValue = "please check employee's performance";
        if (i == 5)
           
            return "Excellent";
        else if (i == 4)
            return "Very Good";
        else if (i == 3)
            return "Good";
        else if (i == 2)
            return "Fair";
        
        else if (i == 1)
            return "Poor";
        
        return returnValue;
    } 
    
    public static void main(String [] args) {
        // TODO code application logic here
        int empNumber;
        String empName;
        String empDepartment;
        int empLevel;
        String empPosition;
        
        int totalPerformance = 0, DepRate, CooRate, AdapRate, CommRate, ProsolvRate, TeamRate, UseRate;
        Scanner scan = new Scanner (System.in);
        System.out.println ("Overall Rating of Employees for 2018  \nKindly input the Employee's details");
        
        System.out.printf("\nInput Employee's Number: ");
        empNumber = scan.nextInt ();
        System.out.printf("Input Employee's Surname Name and Initial: ");
        empName = scan.next();
        System.out.printf("Input Employee's Department: ");
        empDepartment = scan.next();
        System.out.printf("Input Employee's Level: ");
        empLevel = scan.nextInt ();
        System.out.printf("Input Employee's Position: ");
        empPosition = scan.next();
        System.out.printf("Input Dependability Skill: ");
        DepRate = scan.nextInt ();
        System.out.printf("Input Cooperativeness Skill: ");
        CooRate = scan.nextInt ();
        System.out.printf("Input Adaptability Skill: ");
        AdapRate = scan.nextInt ();
        System.out.printf("Input Problem Solving Skill: ");
        ProsolvRate = scan.nextInt ();
        System.out.printf("Input Team Work Skill: ");
        TeamRate = scan.nextInt ();
        System.out.printf("Input Use of Equipment Skill: ");
        UseRate = scan.nextInt ();
        System.out.printf("Input Communication Skill: ");
        CommRate = scan.nextInt ();
        
        
        System.out.println("empNumber=" +empNumber);
        System.out.println("empName=" +empName);
        System.out.println("empDepartment=" +empDepartment);
        System.out.println("empLevel=" +empLevel);
        System.out.println("empPosition=" +empPosition);
        
        System.out.println("        Skill            |             Rate             |            Comment  ");
        System.out.println("-------------------------+------------------------------+--------------------------");
        System.out.printf("\nDependability Rate       |             %d                |       %s",DepRate, check(DepRate));
        System.out.printf("\nCooperativeness Rate     |             %d                |       %s",CooRate, check(CooRate));
        System.out.printf("\nAdaptability Rate        |             %d                |       %s",AdapRate, check(AdapRate));
        System.out.printf("\nProblem Solving Rate     |             %d                |       %s",ProsolvRate, check(ProsolvRate));
        System.out.printf("\nTeam Work Rate           |             %d                |       %s",TeamRate, check(TeamRate));
        System.out.printf("\nUse of Equipment Rate    |             %d                |       %s",UseRate, check(UseRate));
        System.out.printf("\nCommunication Rate       |             %d                |       %s",CommRate, check(CommRate));
        
        
        totalPerformance =  DepRate + CooRate + AdapRate + ProsolvRate + TeamRate + UseRate + CommRate;
        System.out.println("\ntotalPerformance="+totalPerformance);
        if (totalPerformance >= 25)
            System.out.println("Best Worker of the Year");
        else if (totalPerformance >= 18)
            System.out.println("Average Worker of the Year");
        else if (totalPerformance >= 11)
            System.out.println("Upcoming Worker of the Year");
        else
            System.out.println("Downgrading Worker of the Year");
        
        if (totalPerformance >= 25)
            System.out.println("Promoted to the Next Level with an Increment in your Salary and lots of Benefits");
        else if (totalPerformance >= 18)
            System.out.println("Promoted to the Next Level with just an Increment in your Salary");
        else if (totalPerformance >= 11)
            System.out.println("Promoted untrier");
        else
            System.out.println("Not Promotted,You need to Work Harder in the following Year");
        
            
                
        
    } 
    
}

