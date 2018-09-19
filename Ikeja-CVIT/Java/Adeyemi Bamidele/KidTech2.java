
/* CODELAGOS
*  KIDTECH PROJECT
*  NAME: ADEYEMI BAMIDELE
*  EMAIL: bomiangel@gmail.com
*  MOBILE: 08027240590
*/
//package kidtech2;

import java.util.concurrent.ThreadLocalRandom;
import java.util.*;

class KidTech2 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Hello Applicant, \nWelcome to KidTech Annual Entrance Test");
        System.out.println("This program requires you input three digit value from 1-9... For Example 174 ");
        System.out.println("\n3 Dead Value Qualifies you for this summer KIDTECH BOOTCAMP \nGoodluck");

        int NewValue1;
        int NewValue2;
        int NewValue3;

        int[] valueTech = new int[3];

        Rannumber tech = new Rannumber();
        tech.random1();
        int deadValue = 0;
        int injuredValue = 0;
        int i = 0;
        int counter = 12;
        while (i < 12) {

            String value = "";
            System.out.print("Try "+counter);
            while (true) {
                System.out.println("\nEnter 3 Digit Value: ");
                int valueInt = input.nextInt();

                value = "" + valueInt;

                if (value.length() > 3) {
                    System.out.println("The Value you input is more than 3 digits");
                } else if (value.length() < 3) {
                    System.out.println("The Value you input is less than 3 digits");
                } else if (value.length() == 3) {
                    break;
                }
            }
            --counter;
            char value1 = value.charAt(0);
            char value2 = value.charAt(1);
            char value3 = value.charAt(2);

            int valueInt1 = KidTech2.Convert(value1);
            int valueInt2 = KidTech2.Convert(value2);
            int valueInt3 = KidTech2.Convert(value3);

            valueTech[0] = valueInt1;
            valueTech[1] = valueInt2;
            valueTech[2] = valueInt3;

            deadValue = tech.dead(valueTech);
            injuredValue = tech.injured(valueTech);

            System.out.println("\n number of dead Value: " + deadValue + "\n number of injured Value: " + injuredValue);
            if (deadValue == 3 && injuredValue == 0) {
                break;
            }

            System.out.println("\nTry again");
            i++;
        }
        if (deadValue == 3 && injuredValue == 0) {
            System.out.println("Congratulation, You have Qualified for KidTech BootCamp \n\nCheck your mail box for your Admission Letter");
        } else {
            System.out.println("Sorry, Your Times UP...... Try next session ");
        }

    }

    public static int Convert(char value) {
        String value1 = "" + value;
        int value3 = Integer.parseInt(value1);
        return value3;
    }

}

class Rannumber {

    public int value1;
    public int value2;
    public int value3;

    Rannumber() {
        this.rand = new int[3];
    }
    public final int[] rand;

    public int getValue1() {
        return value1;
    }

    public int getValue2() {
        return value2;
    }

    public int getValue3() {
        return value3;
    }

    public int[] getRand() {
        return rand;
    }

    public void random1() {
        value1 = (int) (ThreadLocalRandom.current().nextInt(1, 9));
        value2 = (int) (ThreadLocalRandom.current().nextInt(1, 9));
        value3 = (int) (ThreadLocalRandom.current().nextInt(1, 9));
        rand[0] = value1;
        rand[1] = value2;
        rand[2] = value3;
        this.Check();
    }

    public int dead(int[] value) {
        int count = 0;
        for (int i = 0; i < 3; i++) {
            if (rand[i] == value[i]) {
                count++;
            }
        }
        return count;
    }

    public int injured(int[] value) {
        int count = 0;
        for (int i = 0; i < 3; i++) {
            outer:
            for (int j = 0; j < 3; j++) {
                if (rand[i] == value[j]) {
                    if (i == j) {
                        continue;
                    }
                    count++;
                }

            }
        }
        return count;
    }

    public void Check() {
        while (true) {
            for (int i = 0; i < 2; i++) {
                for (int j = i + 1; j < 3; j++) {
                    if (rand[i] == rand[j]) {
                        rand[i] = (int) (ThreadLocalRandom.current().nextInt(1, 9));
                    }
                }
            }
            if ((rand[1] != rand[2]) && rand[1] != rand[0] && rand[2] != rand[0]) {
                break;
            }
        }

    }
}
