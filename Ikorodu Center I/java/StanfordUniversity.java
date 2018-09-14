/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package stanforduniversity;

import java.util.Scanner;

/**
 *
 * @author Aribido Lamzey, lamzey.m@gmail.com, 08131089608.
 */
public class StanfordUniversity {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        String Country ;
        String totalStanford, FirstName, LastName, DateofBirth, Nationality, HomeAddress, EMail, PreviousDegree, YearofGraduation, PreviousCourseofStudy, NativeEnglishSpeaker, CourseofInterest, Session, StartDate;
        Scanner scan = new Scanner(System.in);
        System.out.println("WELCOME to Stanford University (No. 2 University in World Ranking) \nPlease kindly enter your Country of Residence");
        Country = scan.nextLine();
        System.out.printf("First Name :");
        FirstName = scan.nextLine();
        System.out.printf("Last Name :");
        LastName = scan.nextLine();
        System.out.printf("Date of Birth :");
        DateofBirth = scan.nextLine();
        System.out.printf("Nationality :");
        Nationality = scan.nextLine();
        System.out.printf("Home Address :");
        HomeAddress = scan.nextLine();
        System.out.printf("E-Mail :");
        EMail = scan.nextLine();
        System.out.printf("Previous Degree :");
        PreviousDegree = scan.nextLine();
        System.out.printf("Year of Graduation :");
        YearofGraduation = scan.nextLine();
        System.out.printf("Previous Course Of Study :");
        PreviousCourseofStudy = scan.nextLine();
        System.out.printf("Native English Speaker :");
        NativeEnglishSpeaker = scan.nextLine();
        System.out.printf("Please Enter Your Course of Interest At Stanford University :");
        CourseofInterest = scan.nextLine();
        System.out.printf("Session :");
        Session = scan.nextLine();
        System.out.printf("Start Date :");
        StartDate = scan.nextLine();
        System.out.println("Your Application Has Been Successfully Recieved By Us, Check Your E-Mail For Updates");
       
    }

    }

