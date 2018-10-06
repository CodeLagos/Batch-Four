/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codelagosdeliveryproject;

/**
 *
 * @author Oladotun Aboaba
 */
public class HelperClassCodeLagosDeliveryProject {
    String a;
        String falomo;
        
        public HelperClassCodeLagosDeliveryProject(String a){
            this.a= a;
             }
        public HelperClassCodeLagosDeliveryProject (String a, double b, double c, double d,double e, double f, double g,double h,double i,double j,double k,double l,double m,double n,
                double o,double p,double q,double r,double s,double t,double u,double v,double w,double x,double y,double z){
        }
    public void formular(){
        //calculate the cost for each location input 
        int cost = 500;
        //lagos island calculations
        if("falomo".equals(a)){ 
        double a = (cost + 100);
        System.out.println("The cost of delivery to falomo is: " + a + "naira");
        
        }else if("bourdillon".equals(a)){
        double b = cost + 200;
        System.out.println("The cost of delivery to bourdillon is: " + b + "naira");
       
        }else if("osborne".equals(a)){
        double c = cost + 200;
        System.out.println("The cost of delivery to osborne is: " + c + "naira");
        
        
        }else if("onikan".equals(a)){
        double d = cost + 300;
        System.out.println("The cost of delivery to onikan is: " + d + "naira");
       
        }
        else if("bananaisland".equals(a)){
        double e = cost + 500;
        System.out.println("The cost of delivery to bananaisland is: " + e + "naira");
       
        }
        else if("victoriaisland".equals(a)){
        double f = cost + 500;
        System.out.println("The cost of delivery to victoriaisland is: " + f + "naira");
       
        }
        else if("marina".equals(a)){
        double g = cost + 500;
        System.out.println("The cost of delivery to marina is: " + g + "naira");
       
        }
        //lekki areas calculations
        else if("admiralty".equals(a)){
        double h = cost + 500;
        System.out.println("The cost of delivery to admiralty is: " + h + "naira");
       
        }
        else if("lekki".equals(a)){
        double i = cost + 500;
        System.out.println("The cost of delivery to lekki is: " + i + "naira");
       
        }
        else if("ikate".equals(a)){
        double j = cost + 500;
        System.out.println("The cost of delivery to ikate is: " + j + "naira");
       
        }
        else if("oniru".equals(a)){
        double k = cost + 500;
        System.out.println("The cost of delivery to oniru is: " + k + "naira");
       
        }
        else if("jakande".equals(a)){
        double l = cost + 500;
        System.out.println("The cost of delivery to jakande is: " + l + "naira");
       
        }
        else if("chevron".equals(a)){
        double m = cost + 500;
        System.out.println("The cost of delivery to chevron is: " + m + "naira");
            
        }
        else if("vgc".equals(a)){
        double n = cost + 500;
        System.out.println("The cost of delivery to vgc is: " + n + "naira");
       
        }
        //lagos mainland claculations
        else if("opebi".equals(a)){
        double o = cost + 200;
        System.out.println("The cost of delivery to opebi is: " + o + "naira");
       
        }
        else if("allen".equals(a)){
        double p = cost + 200;
        System.out.println("The cost of delivery to allen is: " + p + "naira");
       
        }
        else if("oregun".equals(a)){
        double q = cost + 200;
        System.out.println("The cost of delivery to oregun is: " + q + "naira");
       
        }
        else if("ikeja".equals(a)){
        double r = cost + 200;
        System.out.println("The cost of delivery to ikeja is: " + r + "naira");
        //System.out.println("Would you like to rerun this program? 1=yes, 0=no");
    
        }
        else if("alausa".equals(a)){
        double s = cost + 200;
        System.out.println("The cost of delivery to alausa is: " + s + "naira");
       
        }
        else if("maryland".equals(a)){
        double t = cost + 200;
        System.out.println("The cost of delivery is to maryland: " + t + "naira");
       
        }
        else if("agidingbi".equals(a)){
        double u = cost + 200;
        System.out.println("The cost of delivery to agidingbi is: " + u + "naira");
       
        }
        else if("obaakran".equals(a)){
        double v = cost + 200;
        System.out.println("The cost of delivery to obaakran is: " + v + "naira");
       
        }
        else if("anthony".equals(a)){
        double w = cost + 200;
        System.out.println("The cost of delivery to anthony is: " + w + "naira");
       
        }
        else if("magodo".equals(a)){
        double x = cost + 200;
        System.out.println("The cost of delivery to magodo is: " + x + "naira");
       
        }
        else if("shangisha".equals(a)){
        double y = cost + 200;
        System.out.println("The cost of delivery to shangisha is: " + y + "naira");
            
        }
        else if("omole".equals(a)){
        double z = cost + 200;
        System.out.println("The cost of delivery to omole is: " + z + "naira");
        
        }
        
        // Print the cost to the user
        else 
        System.out.println ( "please input a region out of the following" + "\n" + "Our lagos island delivery regions." + "\n" +
 "Falomo, Bourdillon, Osborne, Onikan, Bananaisland, Victoriaisland, Marina." + "\n"+ "Our lekki delivery regions." + "\n" + 
                "Admiralty, Lekki, Ikate, Oniru, Jakande, Chevron, Vgc." + "\n" + "Our lagos mainland delivery regions." + "\n" + "opebi, "
                + "Allen, Oregun, Ikeja, Alausa, Maryland, Agidingbi, Obaakran, Anthony, Magodo, Shangisha, Omole." );
       
        System.out.println("Would you like to make another choice?" + "\n" + "enter 1 to continue,or 0 to end.");
    
           }
    
}

