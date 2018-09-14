/*
CODE LAGOS PROJECT
**HELPER/SUB CLASS**
AIMAKHEDE DAVID SUNDAY
08166554021
aimakhededavido@gmail.com
*/
package lagosrwtsproject;

import java.util.*;

public class LagosRWTShelper {

 public void Fix(){
    int day, month, year;
    int second, minute, hour;
    GregorianCalendar date = new GregorianCalendar();
    
    day = date.get(Calendar.DAY_OF_MONTH);
    month = date.get(Calendar.MONTH);
    year = date.get(Calendar.YEAR);
    
    second = date.get(Calendar.SECOND);
    minute = date.get(Calendar.MINUTE);
    hour = date.get(Calendar.HOUR);
    
    System.out.println("====================================================");
    System.out.println("Registration Date:  "+day+"/"+(month+1)+"/" +year);
    System.out.println("Registration Time:  "+hour+":"+minute+":"+second);
    System.out.println("====================================================");
    }

}
