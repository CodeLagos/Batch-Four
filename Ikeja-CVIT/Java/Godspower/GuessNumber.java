/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Org.School.www;

import java.util.ArrayList;

import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashSet;

import java.util.List;
import java.util.Objects;
import java.util.Random;
import java.util.Set;
import java.util.Scanner;

/**
 *
 * @author God
 */
public class GuessNumber {

    String result;
    int injury;
    int dead;
    List<Integer> r = randomList();

    public static void main(String[] args) {
        GuessNumber sub = new GuessNumber();
        int i;
        for (i = 1; i <= 12; i++) {
            System.out.println("tried " + i + "/" + 12);
            List li = sub.userList();
            sub.elvaluate(sub.r, li);
            if (sub.dead == 3) {
                System.out.println("you have won after " + (i) + " times");
                break;
            } else {
                sub.dead = 0;
                sub.injury = 0;
            }

        }

        System.out.println("you have finished after " + i + " tries " + sub.dead + " dead " + sub.injury + " injury");
        System.out.println();
    }

    public List<Integer> userList() {
        Scanner inp = new Scanner(System.in);
        Set<Integer> set = new LinkedHashSet<>();

        System.out.println("Enter your 3 digit");
        String dig = inp.nextLine();
        for (int i = 0; i <= 2; i++) {
            String d = Character.toString(dig.charAt(i));
            int t = Integer.parseInt(d);
            set.add(t);
        }
        while (set.size() < 3) {
            System.out.println("mutliple values are not allow enter a new one to replace one of them");
            int digg = inp.nextInt();
            set.add(digg);
        }

        List<Integer> li = new ArrayList<>(set);
        System.out.println(li);
        return li;
    }

    public void elvaluate(List list1, List list2) {

        for (int i = 0; i <= 2; i++) {

            if (list1.get(i) == list2.get(i)) {
                dead++;
                // System.out.println(list1.get(i) + " " + list2.get(i));
                //return;
            } else if (list1.contains(list2.get(i))) {
                injury++;

            }

        }
        System.out.println(list1);
        System.out.println(dead+" dead"+ injury+" injury");
        System.out.println();

    }

    public void Elvaluate(List<Integer> list1, List<Integer> list2) {
        list1.forEach((i) -> {
            list2.forEach((j) -> {
                if (Objects.equals(i, j)) {
                    dead++;
                    System.out.println("this is n2 " + i + " " + j);

                } else if (list1.contains(j)) {
                    injury++;
                    System.out.println("this is n3 " + j);

                } else if (list1.equals(list2)) {
                    dead++;
                    System.out.println("this is n1");

                } else {

                }
            });
        });
        System.out.println(list1);
        System.out.println(r);
        System.out.println(dead + " dead " + injury + " injury ");

    }

    public static List<Integer> randomList() {
        Random ran = new Random();
        Set<Integer> se = new HashSet<>();
        while (se.size() < 3) {
            se.add(ran.nextInt(10));
        }
        List<Integer> li = new ArrayList<>(se);
        Collections.shuffle(li);
        return li;
    }

}
