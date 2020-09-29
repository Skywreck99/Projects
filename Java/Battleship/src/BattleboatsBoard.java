
public class BattleboatsBoard {
    private int x;
    private int y;
    int count;
    int[] VarrayX;
    int[] VarrayY;
    int[] arrayX;
    int[] arrayY;
    private char[][] array;
    private char[][] player;

    // BattleboatsBoard constructor
    public BattleboatsBoard(int y, int x){
        this.x = x;
        this.y = y;
        array = new char[y][x];
        player = new char[y][x];
        count = count;
    }
    // Accessors
    public int getHeight(){
        return this.y ;
    }
    public int getWidth(){
        return this.x;
    }
    public char[][] getArray() {
        return array;
    }

    public char[][] getPlayer() {
        return player;
    }
    // Setters
    public void setArray(int x, int y, char z) {
        array[y][x] = z;
    }
    public void setPlayer(int x, int y, char z) {
        player[y][x] = z;
    }
    public void MakeBoard(int row, int column){
        for (int i = 0; i < array.length; i++) {
            for(int j = 0; j < array[i].length; j++) {
                array[i][j] = 'O';
            }
        }
    }

    // addBoats adds the boats in the board
    public void addBoat(int n) {
        count = 0;
        arrayY = new int[n];
        arrayX = new int[n];
        VarrayX = new int[n];
        VarrayY = new int[n];
        int indexH = 0;
        int indexV = 0;

        // Creates the number of Boats
        for (int k = 0; k < n; k++) {
            int stop = 0;
            while(stop == 0) {

                // Creates the random position of the Boats
                int x1 = (int) (Math.random() * (this.getWidth() + 1));
                int y1 =  (int) (Math.random() * (this.getHeight() + 1));
                boolean xdirection = (int)(10 * Math.random()) % 2 == 0;
                if (xdirection) {
                    if (x1 + 1 < this.getWidth() && y1 + 1 < this.getHeight() && x1 + 2 < this.getWidth()) {
                        if (array[y1][x1] != '-' && array[y1][x1 + 1] != '-' && array[y1][x1 + 2] != '-') {

                            // Sets up the location of the Boats to be tracked later
                            arrayY[indexH] = y1;
                            arrayX[indexH] = x1;
                            indexH++;

                            // Creates the Horizontal Boats
                            for(int i = 0; i < 3; i++) {
                                array[y1][x1 + i] = '-';
                                count++;
                            }
                            stop = 1;
                        }
                    }
                } else {
                    if (y1 + 1 < this.getHeight() && x1 + 1 < this.getWidth() && y1 + 2 < this.getHeight()) {
                        if (array[y1][x1] != '-' && array[y1 + 1][x1] != '-' && array[y1 + 2][x1] != '-') {

                            // Sets up the location of the Boats to be tracked later
                            VarrayY[indexV] = y1;
                            VarrayX[indexV] = x1;
                            indexV++;

                            // Creates the Horizontal Boats
                            for(int i = 0; i < 3; i++) {
                                array[y1 + i][x1] = '-';
                                count++;
                            }
                            stop = 1;
                        }
                    }
                }
            }
        }
    }
    // Setting up the Drone to see the Board within the Plus (+) Scope
    public String Drone(int y, int x) {
        String drone = "";
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (i == y) {
                    // Prints out everything within the vertical zone of a particular location
                    if (j != array[i].length - 1) {
                        drone += " | " + array[i][j];
                    } else {
                        drone += " | " + array[i][j] + " |";
                    }
                }
                else if (j == x) {
                    // Prints out everything within the horizontal zone of a particular location
                    if (j != array[i].length - 1) {
                        drone += " | " + array[i][j];
                    } else {
                        drone += " | " + array[i][j] + " |";
                    }
                } else {
                    // Prints out 'O' if not in the Plus Scope
                    if (j != array[i].length - 1) {
                        drone += " | |";
                    } else {
                        drone += " | | |";
                    }
                }
            }
            drone += "\n";
        }
        return drone;
    }

    // Prints out the Board with the Boats
    public String toString() {
        String newBoard = "";
        // Debugging Mode
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (j != array[i].length - 1) {
                    newBoard += " | " + array[i][j];
                } else {
                    newBoard += " | " + array[i][j] + " |";
                }
            }
            newBoard += "\n";
        }
        return newBoard;
    }

    // Prints out the Board without the Boats
    public String PlayertoString() {
        String newBoard = "";
        // Debugging Mode
        for (int i = 0; i < player.length; i++) {
            for (int j = 0; j < player[i].length; j++) {
                if (j != player[i].length - 1) {
                    newBoard += " | " + player[i][j];
                } else {
                    newBoard += " | " + player[i][j] + " |";
                }
            }
            newBoard += "\n";
        }
        return newBoard;
    }
}







