import java.lang.reflect.Array;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("Welcome to Battleboats!");
        String play = "Play";

        // Does the loop until the player wants to stop the Game
        while (true) {
            if (play.equals("Quit")) {
                break;
            }
            else if (play.equals("Restart")) {
                play = "Play";
            }
            System.out.print("Do you want to play (Yes or No)? ");
            Scanner theChoice = new Scanner(System.in);
            String Choice = theChoice.nextLine();
            if (Choice.equals("Yes") || Choice.equals("yes")) {
                int inputX;
                int inputY;
                while (true) {
                    System.out.print("Choose the dimensions of your board ranging from 3 by 3 to 12 by 12: ");
                    Scanner myScanner = new Scanner(System.in);
                    if (!myScanner.hasNextInt()) {
                        System.out.println("Not a Dimension. Please try again.");
                    } else {
                        inputX = myScanner.nextInt();
                        if (inputX < 3 || inputX > 12) {
                            System.out.println("Out of range. Please try again.");
                        } else {
                            inputY = myScanner.nextInt();
                            if (inputY < 3 || inputY > 12) {
                                System.out.println("Out of Range. Please try again.");
                            } else {
                                break;
                            }
                        }
                    }
                }
                BattleboatsBoard theBoard = new BattleboatsBoard(inputY, inputX);

                // Setting the Board as all 'O' to represent water
                for (int i = 0; i < theBoard.getArray().length; i++) {
                    for (int j = 0; j < theBoard.getArray()[i].length; j++) {
                        theBoard.setArray(j, i, 'O');
                        theBoard.setPlayer(j, i, 'O');
                    }
                }
                System.out.println(theBoard.toString());

                // Setting the board with boats in it based on the following restrictions
                if (theBoard.getWidth() == 3 || theBoard.getHeight() == 3) {
                    System.out.println("Boats generated: 1");
                    theBoard.addBoat(1);
                }
                else if((theBoard.getWidth() <= 6 && theBoard.getWidth() > 3) || (theBoard.getHeight() <= 6 && theBoard.getHeight() > 3)) {
                    System.out.println("Boats generated: 2");
                    theBoard.addBoat(2);
                }
                else if((theBoard.getWidth() <= 8 && theBoard.getWidth() > 6) || (theBoard.getHeight() <= 8 && theBoard.getHeight() > 6)) {
                    System.out.println("Boats generated: 3");
                    theBoard.addBoat(3);
                }
                else if((theBoard.getWidth() <= 10 && theBoard.getWidth() > 8) || (theBoard.getHeight() <= 10 && theBoard.getHeight() > 8)) {
                    System.out.println("Boats generated: 4");
                    theBoard.addBoat(4);
                }
                else if((theBoard.getWidth() <= 12 && theBoard.getWidth() > 10) || (theBoard.getHeight() <= 12 && theBoard.getHeight() > 10)) {
                    System.out.println("Boats generated: 6");
                    theBoard.addBoat(6);
                }

                int count = theBoard.count;
                int[] arrayY = theBoard.arrayY;
                int[] arrayX = theBoard.arrayX;
                int[] VarrayX = theBoard.VarrayX;
                int[] VarrayY = theBoard.VarrayY;

                // Does the loop until the player decides to quit the game or if the Game is Over
                while (true) {
                    if (play.equals("Quit")) {
                        break;
                    }
                    else if (play.equals("Restart")) {
                        break;
                    }
                    else if (count == 0) {
                        System.out.println("You Won the Battle Boats!");
                        System.out.println("Game Over");
                        break;
                    }
                    int locationX;
                    int locationY;

                    // Does the loop until the player picks a valid location (not out of bounds)
                    while (true) {
                        int locX;
                        int locY;

                        while (true) {
                            System.out.print("Pick coordinates: ");
                            Scanner theScanner = new Scanner(System.in);
                            if (!theScanner.hasNextInt()) {
                                System.out.println("Invalid Coordinates");
                            } else {
                                locX = theScanner.nextInt();
                                if (!theScanner.hasNextLine()) {
                                    System.out.println("Invalid Coordinates");
                                } else {
                                    if (!theScanner.hasNextInt()) {
                                        System.out.println("Invalid Coordinates");
                                    } else {
                                        locY = theScanner.nextInt();
                                        break;
                                    }
                                }
                            }
                        }

                        // Checks of the coordinates are Out of Bounds
                        if (locX >= theBoard.getWidth() || locX < 0 || locY >= theBoard.getHeight() || locY < 0) {
                            System.out.println("Penalty: Lost one Turn");
                        } else {
                            locationY = locY;
                            locationX = locX;
                            break;
                        }
                    }

                    // Checks if the chosen location of the player hits or miss a boat
                    if (theBoard.getArray()[locationY][locationX] == '-') {
                        System.out.println("Hit");
                        theBoard.setArray(locationX, locationY, 'X');
                        theBoard.setPlayer(locationX, locationY, 'X');
                        count --;
                        System.out.println(theBoard.PlayertoString());

                        // Checks if the chosen location is within the range of the boat
                        for (int l = 0; l < arrayX.length; l++) {
                            if ((locationX == arrayX[l] && locationY == arrayY[l]) || (locationX - 1 == arrayX[l] && locationY == arrayY[l]) || (locationX - 2 == arrayX[l] && locationY == arrayY[l])) {
                                int X = arrayX[l];
                                int Y = arrayY[l];
                                if (theBoard.getArray()[Y][X] == 'X' && theBoard.getArray()[Y][X + 1] == 'X' && theBoard.getArray()[Y][X + 2] == 'X') {
                                    System.out.println("The Boat has Sunk");
                                }
                            }
                        }
                        for (int m = 0; m < VarrayX.length; m++) {
                            if ((locationX == VarrayX[m] && locationY == VarrayY[m]) || (locationX == VarrayX[m] && locationY - 1 == VarrayY[m]) || (locationX == VarrayX[m] && locationY - 2 == VarrayY[m])) {
                                int X = VarrayX[m];
                                int Y = VarrayY[m];
                                if (theBoard.getArray()[Y][X] == 'X' && theBoard.getArray()[Y + 1][X] == 'X' && theBoard.getArray()[Y + 2][X] == 'X') {
                                    System.out.println("The Boat has Sunk");
                                }
                            }
                        }
                    }
                    else if (theBoard.getArray()[locationY][locationX] == 'O') {
                        System.out.println("Miss");
                        theBoard.setArray(locationX, locationY, 'M');
                        theBoard.setPlayer(locationX, locationY, 'M');
                        System.out.print(theBoard.PlayertoString());
                    } else {
                        System.out.println("Penalty: Lost one Turn");

                    }
                    // Does the loop until the player wants to end the Game
                    boolean reference = true;
                    boolean compare = true;
                    int droneX = 0;
                    int droneY = 0;

                    // "!" and "@" are hacking character accessors (Spectator mode)
                    while(true) {
                        if (count == 0) {
                            break;
                        }
                        System.out.print("Choose from Drone, Debugging Mode, Continue, Restart, or Quit: ");
                        Scanner theScanner = new Scanner(System.in);

                        String choice = theScanner.nextLine();
                        if (choice.equals("Drone") || choice.equals("drone") || choice.equals(" drone")) {
                            // The drone is being sent to the board to check any existence on the board in the Plus Scope
                            int locateX;
                            int locateY;

                            while (true) {
                                System.out.print("Locate the coordinates: ");
                                Scanner thisScanner = new Scanner(System.in);
                                if (!thisScanner.hasNextInt()) {
                                    System.out.println("This is not a valid location.");
                                } else {
                                    locateX = thisScanner.nextInt();
                                    if (!thisScanner.hasNextLine()) {
                                        System.out.println("This is not a valid location.");
                                    } else {
                                        if (!thisScanner.hasNextInt()) {
                                            System.out.println("This is not a valid location.");
                                        } else {
                                            locateY = thisScanner.nextInt();
                                            break;
                                        }
                                    }
                                }
                            }
                            if (locateX >= theBoard.getWidth() || locateX < 0 || locateY >= theBoard.getHeight() || locateY < 0) {
                                System.out.println("Penalty: Lost 5 Turns for using the Drone and Being out of Bounds");
                            } else {
                                droneX = locateX;
                                droneY = locateY;
                                System.out.println(theBoard.Drone(locateY, locateX));
                                System.out.println("Penalty: Lost 4 Turns for using the Drone");
                            }
                        } else if (choice.equals("Debugging Mode") || choice.equals("debugging mode") || choice.equals(" debugging mode")) {

                            // Prints out the current board with boats and additional characters
                            System.out.println(theBoard.toString());
                        } else if (choice.equals("Continue") || choice.equals("continue") || choice.equals(" continue")) {
                            break;
                        }
                        else if (choice.equals("Quit") || choice.equals("quit") || choice.equals(" quit")) {
                            play = "Quit";
                            break;
                        }
                        else if (choice.equals("Restart") || choice.equals("restart") || choice.equals(" restart")) {
                            play = "Restart";
                            break;
                        } else if (choice.equals("!")) {
                            if (reference) {
                                System.out.println(theBoard.PlayertoString());
                                reference = false;
                            } else {
                                System.out.println(theBoard.toString());
                                reference = true;
                            }
                        } else if (choice.equals("@")) {
                            if (compare) {
                                System.out.println(theBoard.toString());
                                compare = false;
                            } else {
                                System.out.println(theBoard.Drone(droneY, droneX));
                                compare = true;
                            }
                            System.out.println("Not an Option");
                        }
                    }
                }
            }
            else if (Choice.equals("No") || Choice.equals("no")) {
                System.out.println("You are not Brave Enough to Play It");
                break;
            }
        }
    }
}
