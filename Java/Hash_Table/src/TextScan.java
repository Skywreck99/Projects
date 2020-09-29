// TextScan.java
// Opens text file supplied on the command line
// Usage:  java TextScan filename
// Counts all tokens found (a token is anything delimited by a space character)
// Displays each token found to the screen
// Code may be used in part for Project 5 with proper citing. 

import java.util.Scanner;
import java.io.*;

public class TextScan {
    public static int num;

    public static void main(String[] args) {

        Scanner readFile = null;
        String s;
        int count = 0;

        System.out.println();
        System.out.print("Attempting to read from file: ");
        Scanner myScanner = new Scanner(System.in);
        String filename = myScanner.nextLine();
        try {
            readFile = new Scanner(new File("\\Users\\Skylan\\IdeaProjects\\Project5\\src\\" + filename));
        }
        catch (FileNotFoundException e) {
            System.out.println("File: " + filename + " not found");
            System.exit(1);  
        }

        System.out.println("Connection to file: " + filename + " successful");
        System.out.println();
        HashMap<String, String> hashTable = new HashMap<>();
        while (readFile.hasNext()) {
            s = readFile.next();
            System.out.println("Token found: " + s);
            hashTable.put(s,s);
            count++;
        }
        
        System.out.println();
        System.out.println(count + " Tokens found");

        //hashTable.display();
        System.out.println("Total number of elements: " + num);
        hashTable.showHashtable();
    }  // main

}  // TextScan
