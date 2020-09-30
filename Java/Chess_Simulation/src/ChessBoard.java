public class ChessBoard {
    private static final CheckeredBox[][] board = new CheckeredBox[8][8];
    private static final char[] file = {'A','B','C','D','E','F','G','H'};
    private static final char[] rank = {'8','7','6','5','4','3','2','1'};
    private static ChessPiece[] whitepieces;
    private static ChessPiece[] blackpieces;
    private ChessPiece blackKing;
    private ChessPiece whiteKing;


    public ChessBoard(){
        // Initializes the board to be empty
        for(int num = 0; num < 8; num++) {
            for (int letter = 0; letter < 8; letter++) { board[num][letter] = new CheckeredBox(file[letter], rank[num], 'e'); }
        }
    }

    public void initChessboard(){
        // Initializes the board for the Gameplay
        // Place BW Pawns here
        for (int letter = 0; letter < 8; letter++) {
            board[6][letter] = new CheckeredBox(file[letter], rank[6], new Pawn(file[letter], rank[6], 1));
            board[1][letter] = new CheckeredBox(file[letter], rank[1], new Pawn(file[letter], rank[1], 0));
        }
        // Place BW Queens here
        board[3][7] = new CheckeredBox(file[7], rank[3], new Queen(file[7], rank[3], 1));
        board[0][3] = new CheckeredBox(file[3], rank[0], new Queen(file[3], rank[0], 0));

        // Place BW Kings here
        board[7][4] = new CheckeredBox(file[4], rank[7], new King(file[4], rank[7], 1));
        board[0][4] = new CheckeredBox(file[4], rank[0], new King(file[4], rank[0], 0));

        board[2][4] = new CheckeredBox(file[4], rank[2], new Pawn(file[4], rank[2], 1));
        // Place BW Bishops here
        // Place BW Horses here
        // Place BW Rooks here
        setPieces();
    }

    public static char[] getFile() { return file; }
    public static char[] getRank() { return rank; }
    public static CheckeredBox[][] getBoard() { return board; }

    public String view(int color){
        String result;
        if (color == 1) {
            result = "     ";
            for (int i = 0; i < file.length; i++){
                result += file[i] + "  ";
            }
            result += "\n  ";
            for (int i = 0; i < 8; i++) {
                result += rank[i] + " ";
                for (int j = 0; j < 8; j++) {
                    if (board[i][j].getPiece() instanceof Pawn) {
                        result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + "]";
                    } else {
                        result += "[ ]";
                    }
                }
                result += " " + rank[i] + "\n  ";
            }
            result += "   ";
            for (int i = 0; i < file.length; i++){
                result += file[i] + "  ";
            }

        } else {
            result = "     ";
            for (int i = 7; i >= 0; i--){
                result += file[i] + "  ";
            }
            result += "\n  ";
            for (int i = 7; i >= 0; i--) {
                result += rank[i] + " ";
                for (int j = 7; j >= 0; j--) {
                    if (board[i][j].getPiece() instanceof Pawn) {
                        result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + "]";
                    } else {
                        result += "[ ]";
                    }
                }
                result += " " + rank[i] + "\n  ";
            }
            result += "   ";
            for (int i = 7; i >=0; i--){
                result += file[i] + "  ";
            }
        }
        return result;
    }

    public String debug(int color){
        String result;
        if (color == 1) {
            result = "      ";
            for (int i = 0; i < file.length; i++){
                result += file[i] + "    ";
            }
            result += "\n  ";
            for (int i = 0; i < 8; i++) {
                result += rank[i] + " ";
                for (int j = 0; j < 8; j++) {
                    if (board[i][j].getPiece() instanceof Pawn) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + ".2]";
                        }

                    } else if (board[i][j].getPiece() instanceof Queen) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((Queen) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((Queen) board[i][j].getPiece()).getStatus() + ".2]";
                        }

                    } else if (board[i][j].getPiece() instanceof King) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((King) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((King) board[i][j].getPiece()).getStatus() + ".2]";
                        }
                    }
                    else {
                        result += "[   ]";
                    }
                }
                result += " " + rank[i] + "\n  ";
            }
            result += "    ";
            for (int i = 0; i < file.length; i++){
                result += file[i] + "    ";
            }

        } else {
            result = "      ";
            for (int i = 7; i >= 0; i--){
                result += file[i] + "    ";
            }
            result += "\n  ";
            for (int i = 7; i >= 0; i--) {
                result += rank[i] + " ";
                for (int j = 7; j >= 0; j--) {
                    if (board[i][j].getPiece() instanceof Pawn) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((Pawn) board[i][j].getPiece()).getStatus() + ".2]";
                        }

                    } else if (board[i][j].getPiece() instanceof Queen) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((Queen) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((Queen) board[i][j].getPiece()).getStatus() + ".2]";
                        }

                    } else if (board[i][j].getPiece() instanceof King) {
                        if ((board[i][j].getPiece()).getColor() == 1) {
                            result += "[" + ((King) board[i][j].getPiece()).getStatus() + ".1]";
                        } else {
                            result += "[" + ((King) board[i][j].getPiece()).getStatus() + ".2]";
                        }
                    }
                    else {
                        result += "[   ]";
                    }
                }
                result += " " + rank[i] + "\n  ";
            }
            result += "    ";
            for (int i = 7; i >=0; i--){
                result += file[i] + "    ";
            }
        }
        return result;
    }

    public boolean checkFile(char File) {
        for (char c : file) {
            if (File == c) {
                return true;
            }
        }
        return false;
    }

    public boolean checkRank(char Rank) {
        for (char c : rank) {
            if (Rank == c) {
                return true;
            }
        }
        return false;
    }

    public String showMove(ChessPiece piece) {
        //System.out.println("len: " + piece.getAvailableMove().length);
        String result = "Piece available moves are: ";
        for (int i = 0; i < piece.getAvailableMove().length; i++) {
            result += "(" + piece.getAvailableMove()[i][0] + "," + piece.getAvailableMove()[i][1] + ") ";
        }
        return result;
    }

    public void setMovePieces() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j].getStatus() != 'e') {
                    ChessPiece piece = board[i][j].getPiece();
                    if (piece instanceof Pawn) {
                        ((Pawn) piece).setMove();
                        //showMove(piece);
                        //((Pawn) piece).setEat();
                    } else if (piece instanceof Queen) {
                        ((Queen) piece).setMove();
                    } else if (piece instanceof King) {
                        ((King) piece).setMove();
                    }
                }
            }
        }
    }

    public void setPieces() {
        int countW = 0;
        int countB = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j].getStatus() != 'e') {
                    if (board[i][j].getPiece().getColor() == 1) {
                        countW++;
                    } else {
                        countB++;
                    }
                }
            }
        }
        whitepieces = new ChessPiece[countW];
        blackpieces = new ChessPiece[countB];
        countW = countB = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j].getStatus() != 'e') {
                    if (board[i][j].getPiece().getColor() == 1) {
                        if (board[i][j].getPiece() instanceof King) {
                            whiteKing = board[i][j].getPiece();
                        }
                        whitepieces[countW] = board[i][j].getPiece();
                        countW++;
                    } else {
                        if (board[i][j].getPiece() instanceof King) {
                            blackKing = board[i][j].getPiece();
                        }
                        blackpieces[countB] = board[i][j].getPiece();
                        countB++;
                    }
                }
            }
        }
    }
    public static ChessPiece[] getWhitePieces() { return whitepieces; }
    public static ChessPiece[] getBlackPieces() { return blackpieces; }

    public boolean checkKing(int kingColor) {
        setMovePieces();
        if (kingColor == 1) {
            for (int i = 0; i < blackpieces.length; i++) {
                for (int j = 0; j < blackpieces[i].getHRpossMove().length; j++) {
                    for (int k = 0; k < blackpieces[i].getHRpossMove()[j].length; k++) {
                        if (blackpieces[i].getHRpossMove()[j][k].length == 1 && blackpieces[i].getHRpossMove()[j][k][0] == blackpieces[i].getBoardRow() && blackpieces[i].getHRpossMove()[j][k][1] == blackpieces[i].getBoardCol()) {
                            continue;
                        } else {
                            if (blackpieces[i].getHRpossMove()[j][k][0] == whiteKing.getBoardRow() && blackpieces[i].getHRpossMove()[j][k][1] == whiteKing.getBoardCol()) {
                                return true;
                            }
                        }
                    }
                }
            }
        } else {
            for (int i = 0; i < whitepieces.length; i++) {
                for (int j = 0; j < whitepieces[i].getHRpossMove().length; j++) {
                    for (int k = 0; k < whitepieces[i].getHRpossMove()[j].length; k++) {
                        if (whitepieces[i].getHRpossMove()[j][k].length == 1 && whitepieces[i].getHRpossMove()[j][k][0] == whitepieces[i].getBoardRow() && whitepieces[i].getHRpossMove()[j][k][1] == whitepieces[i].getBoardCol()) {
                            continue;
                        } else {
                            if (whitepieces[i].getHRpossMove()[j][k][0] == blackKing.getBoardRow() && whitepieces[i].getHRpossMove()[j][k][1] == blackKing.getBoardCol()) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        return false;
    }

}
