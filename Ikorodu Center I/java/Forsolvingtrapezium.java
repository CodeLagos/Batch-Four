/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package newprojectforformula;
/**
 *
 * @author joshua
 */
public class Forsolvingtrapezium {
    double ac;
    double n;
    double b;
    double m;
    double cd;
    double df;
    double heigh;
    
    
      public Forsolvingtrapezium(double ac, double n, double b, double m, double cd, double df, double height){
          this.ac = ac;
        this.b = b;
        this.n = n;
         this.m = m;
          
      }

    Forsolvingtrapezium() { //To change body of generated methods, choose Tools | Templates.
    }

    Forsolvingtrapezium(double c, double d, double heigh) {
      //To change body of generated methods, choose Tools | Templates.
    
    }
      
      public void findArea() {
              
      double area = (1/2*(cd + df)*heigh);
      System.out.print ("Solution for area =" + area );
      

      
           
    }
    
    
}
