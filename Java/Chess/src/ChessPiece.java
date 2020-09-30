public class ChessPiece {

    private char file;
    private char rank;
    private final int color;
    private int boardRow;
    private int boardCol;
    private int[][] availableMove;
    //private int[][] possibleEat;
    private int[][][] HRpossMove;


    public ChessPiece(char file, char rank, int color) {
        /* 0: Black    1: White */

        this.file = file;
        this.rank = rank;
        this.color = color;
        this.boardRow = new String(ChessBoard.getRank()).indexOf(rank);
        this.boardCol = new String(ChessBoard.getFile()).indexOf(file);
    }

    public char getRank() { return this.rank; }
    public char getFile() { return this.file; }
    public int getColor() { return this.color; }
    public int getBoardRow() { return boardRow; }
    public int getBoardCol() { return boardCol; }

    public void setRank(char rank) { this.rank = rank; }
    public void setFile(char file) { this.file = file; }

    public void setBoardRow(int boardRow) { this.boardRow = boardRow; }
    public void setBoardCol(int boardCol) { this.boardCol = boardCol; }

    public void setAvailableMove(int[][] arrMove) { this.availableMove = arrMove; }
    public void setHRpossMove(int[][][] HRpossMove) { this.HRpossMove = HRpossMove; }
    public int[][] getAvailableMove() { return availableMove; }
    public int[][][] getHRpossMove() {
        /*
        Queen and King (White):
            North: HRpossMove[0];
            Northeast: HRpossMove[1];
            East: HRpossMove[2];
            Southeast: HRpossMove[3];
            South: HRpossMove[4];
            Southwest: HRpossMove[5];
            West: HRpossMove[6];
            Northwest: HRpossMove[7];

        Queen and King (Black):
            North: HRpossMove[4];
            Northeast: HRpossMove[5];
            East: HRpossMove[6];
            Southeast: HRpossMove[7];
            South: HRpossMove[0];
            Southwest: HRpossMove[1];
            West: HRpossMove[2];
            Northwest: HRpossMove[3];

        Bishop (White):
            Northeast: HRpossMove[0];
            Southeast: HRpossMove[1];
            Southwest: HRpossMove[2];
            Northwest: HRpossMove[3];

        Bishop (Black):
            Northeast: HRpossMove[2];
            Southeast: HRpossMove[3];
            Southwest: HRpossMove[0];
            Northwest: HRpossMove[1];

        Rook (White):
            North: HRpossMove[0];
            East: HRpossMove[1];
            South: HRpossMove[2];
            West: HRpossMove[3];

        Rook (White):
            North: HRpossMove[2];
            East: HRpossMove[3];
            South: HRpossMove[0];
            West: HRpossMove[1];

        Horse (White):
            Far Northeast: HRpossMove[0];
            Near Northeast: HRpossMove[1];
            Near Southeast: HRpossMove[2];
            Far Southeast: HRpossMove[3];
            Far Southwest: HRpossMove[4];
            Near Southwest: HRpossMove[5];
            Near Northwest: HRpossMove[6];
            Far Northwest: HRpossMove[7];

         Horse (Black):
            Far Northeast: HRpossMove[4];
            Near Northeast: HRpossMove[5];
            Near Southeast: HRpossMove[6];
            Far Southeast: HRpossMove[7];
            Far Southwest: HRpossMove[0];
            Near Southwest: HRpossMove[1];
            Near Northwest: HRpossMove[2];
            Far Northwest: HRpossMove[3];
        */
        return HRpossMove;
    }

    // checks if possible moves are inside the board
    public boolean inBoard(int row, int col) { return row > -1 && row < 8 && col > -1 && col < 8; }
    public boolean checkMoveCoor(CheckeredBox box) {
        if (getBoardRow() == box.getRow() && getBoardCol() == box.getCol()) return false;
        for (int[] ints : availableMove) if (ints[0] == box.getRow() && ints[1] == box.getCol()) return true;
        return false;
    }
    /*
    public boolean checkEatCoor(CheckeredBox box){
        if (getBoardRow() == box.getRow() && getBoardCol() == box.getCol()) return false;
        //System.out.println("eatRow: " + ints[0] + " eatCol: " + ints[1]);
        for (int[] ints : possibleEat) if (ints[0] == box.getRow() && ints[1] == box.getCol()) return true;
        return false;
    }

     */
}
