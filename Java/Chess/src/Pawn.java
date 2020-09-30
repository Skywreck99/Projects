public class Pawn extends ChessPiece {
    // note for tomorrow: print out the available moves of each pawn because pawns can overlap other pawns for moving... Also check the one for eating
    // note for efficiency: Pawn is the only Piece that uses setPossibleEat()
    // note for tomorrow: Pawn eat moves can be combined with possible moves
    private final char status;
    private final String name;
    public int initial;

    public Pawn(char file, char rank, int color) {
        super(file, rank, color);
        this.status = 'P';
        this.name = "Pawn";
        this.initial = 2;
    }
    public int[][] whiteEat() {
        //System.out.println("getBoardRow: " + getBoardRow() + " getBoardCol: " + getBoardCol());
        int[][] eat;
        if(/* Checks if in-bounds */ inBoard(getBoardRow() - 1, getBoardCol() - 1) && /* Checks if the box is not empty */ ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() - 1].getStatus() != 'e' && /* Checks if the Piece is White */ ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() - 1].getPiece().getColor() == 0) {
            if (inBoard(getBoardRow() - 1, getBoardCol() + 1) && ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() + 1].getStatus() != 'e' && ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() + 1].getPiece().getColor() == 0) {
                eat = new int[][]{{getBoardRow() - 1, getBoardCol() - 1}, {getBoardRow() - 1, getBoardCol() + 1}};
            } else {
                //System.out.println("success");
                eat = new int[][]{{getBoardRow() - 1, getBoardCol() - 1}};
            }
        } else if (inBoard(getBoardRow() - 1, getBoardCol() + 1) && ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() + 1].getStatus() != 'e' && ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() + 1].getPiece().getColor() == 0) {
            eat = new int[][]{{getBoardRow() - 1, getBoardCol() + 1}};
        } else {
            //System.out.println("here");
            eat = new int[][]{{getBoardRow(), getBoardCol()}};
        }
        return eat;
    }
    public int[][] blackEat() {
        /*
        System.out.println("Status: " + ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() - 1].getStatus());
        System.out.println("Inboard: " + inBoard(getBoardRow() + 1, getBoardCol() - 1));
        System.out.println("Empty box: " + (ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() - 1].getStatus() != 'e'));
        System.out.println("Is this piece Black: " + (ChessBoard.getBoard()[getBoardRow() - 1][getBoardCol() - 1].getPiece().getColor() == 1));

         */
        int[][] eat;
        if(/* Checks if in-bounds */ inBoard(getBoardRow() + 1, getBoardCol() - 1) && /* Checks if the box is not empty */ ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() - 1].getStatus() != 'e' && /* Checks if the Piece is white */ ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() - 1].getPiece().getColor() == 1) {
            if (inBoard(getBoardRow() + 1, getBoardCol() + 1) && ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() + 1].getStatus() != 'e' && ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() + 1].getPiece().getColor() == 1) {
                eat = new int[][]{{getBoardRow() + 1, getBoardCol() - 1}, {getBoardRow() + 1, getBoardCol() + 1}};
            } else {
                eat = new int[][]{{getBoardRow() + 1, getBoardCol() - 1}};
            }
        } else if (inBoard(getBoardRow() + 1, getBoardCol() + 1) && ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() + 1].getStatus() != 'e' && ChessBoard.getBoard()[getBoardRow() + 1][getBoardCol() + 1].getPiece().getColor() == 1) {
            eat = new int[][]{{getBoardRow() + 1, getBoardCol() + 1}};
        } else {
            eat = new int[][]{{getBoardRow(), getBoardCol()}};
        }
        return eat;
    }
    public char getStatus() { return this.status; }
    public String getName() { return this.name; }


    // Sets available move (moving forward) **Pawns cannot go backwards or sideways.
    // They can move one checkered box diagonally when they eat other player's pieces
    public void setMove() {
        CheckeredBox[][] board = ChessBoard.getBoard();
        int total = 0, count = 0,  arrIdx = 0;

        /* pos_move holds Pawn possible moves */ int[][][] pos_move = new int[3][][]; /* arr_move holds Pawn available moves*/ int[][] arr_move;
        int row = getBoardRow(), col = getBoardCol();


        int temp;
        if (getColor() == 1) {
            temp = row - 1;
            while (temp > row-3) {
                if (board[temp][col].getStatus() == 'e') {
                    if (this.initial == 1) {
                        count++;
                        temp -= 3;
                    } else {
                        count++;
                        temp--;
                    }
                } else {
                    temp -= 3;
                }
            }

            if (count == 0) {
                pos_move[1] = new int[][]{{row, col}};
            } else {
                pos_move[1] = new int[count][];
                for (int i = row-1; i >= row - count; i--, arrIdx++) {
                    pos_move[1][arrIdx] = new int[]{i, col};
                }
                arrIdx = 0;
            }

            // Setting Possible Eat
            if (inBoard(getBoardRow() - 1, getBoardCol() - 1)) {
                if (inBoard(getBoardRow() - 1, getBoardCol() + 1)) {
                    pos_move[2] = new int[][]{{getBoardRow() - 1, getBoardCol() + 1}};

                } else {
                    pos_move[2] = new int[][]{{getBoardRow(), getBoardCol()}};
                }
                pos_move[0] = new int[][]{{getBoardRow() - 1, getBoardCol() - 1}};

            } else if (inBoard(getBoardRow() - 1, getBoardCol() + 1)) {
                pos_move[0] = new int[][]{{getBoardRow(), getBoardCol()}};
                pos_move[2] = new int[][]{{getBoardRow() - 1, getBoardCol() + 1}};
            } else {
                pos_move[0] = pos_move[2] = new int[][]{{getBoardRow(), getBoardCol()}};
            }

            // Adding the number of Possible Eat to the total (arr_move's size)
            for (int i = 0; i <= 2; i+=2) {
                if ((board[pos_move[i][0][0]][pos_move[i][0][1]].getStatus() != 'e') && board[pos_move[i][0][0]][pos_move[i][0][1]].getPiece().getColor() == 0) {
                    total++;
                }
            }

        } else {
            temp = row + 1;
            while (temp < row+3) {
                if (board[temp][col].getStatus() == 'e') {
                    if (this.initial == 1) {
                        count++;
                        temp += 3;
                    } else {
                        count++;
                        temp++;
                    }
                } else {
                    temp += 3;
                }
            }

            if (count == 0) {
                pos_move[1] = new int[][]{{row, col}};
            } else {
                pos_move[1] = new int[count][];
                for (int i = row+1; i <= row + count; i++, arrIdx++) {
                    pos_move[1][arrIdx] = new int[]{i, col};
                }
                arrIdx = 0;
            }

            // Setting Possible Eat
            if (inBoard(getBoardRow() + 1, getBoardCol() - 1)) {
                if (inBoard(getBoardRow() + 1, getBoardCol() + 1)) {
                    pos_move[2] = new int[][]{{getBoardRow() + 1, getBoardCol() + 1}};
                } else {
                    pos_move[2] = new int[][]{{getBoardRow(), getBoardCol()}};
                }
                pos_move[0] = new int[][]{{getBoardRow() + 1, getBoardCol() - 1}};

            } else if (inBoard(getBoardRow() + 1, getBoardCol() + 1)) {
                pos_move[0] = new int[][]{{getBoardRow(), getBoardCol()}};
                pos_move[2] = new int[][]{{getBoardRow() + 1, getBoardCol() + 1}};
            } else {
                pos_move[0] = pos_move[2] = new int[][]{{getBoardRow(), getBoardCol()}};
            }

            // Adding the number of Possible Eat to the total (arr_move's size)
            for (int i = 0; i <= 2; i+=2) {
                if ((board[pos_move[i][0][0]][pos_move[i][0][1]].getStatus() != 'e') && board[pos_move[i][0][0]][pos_move[i][0][1]].getPiece().getColor() == 1) {
                    total++;
                }
            }
        }
        total += count;
        row = getBoardRow();

        setHRpossMove(pos_move);


        if (total == 0) {
            arr_move = new int[][]{{row, col}};
        } else {
            arr_move = new int[total][2];
            //System.out.println("PAWN MOVES AND POSSIBLE MOVES");
            for (int i = 0; i < pos_move.length; i++) {
                //System.out.print("pos_move at index " + i + ": ");
                for (int j = 0; j < pos_move[i].length; j++) {
                    //System.out.print("(" + pos_move[i][j][0] + "," + pos_move[i][j][1] + ") ");
                    if ((pos_move[i][j][0] == row && pos_move[i][j][1] == col)) { continue; }
                    else if (i % 2 == 0) {
                        if (board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e') {
                            continue;
                        } else if ((getColor() == 1 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 0) || (getColor() == 0 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 1)) {
                            arr_move[arrIdx] = pos_move[i][j];
                            arrIdx++;
                        }
                    } else if (board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e') {
                        arr_move[arrIdx] = pos_move[i][j];
                        arrIdx++;
                    }
                }
                //System.out.println();
            }
        }

        //System.out.println("here");
        /*
        System.out.print("arr_move: ");
        for (int i = 0; i < arr_move.length; i++) {
            System.out.print("(" + arr_move[i][0] + "," + arr_move[i][1] + ") ");
        }
        System.out.println();
        System.out.println();

         */
        setAvailableMove(arr_move);

    }

    public int move(CheckeredBox /* move to this box */ destBox) {
        /*
        Move successfully: Return 0
        Out of Bounds: Return 1
        Invalid Move: Return 2
        Trying to move to its current position: Return 3
        */


        // Checks if the coordinates given are out of bounds
        if (!inBoard(destBox.getRow(), destBox.getCol())) { return 1; }

        // Checks if Pawn can move to the destBox
        if (checkMoveCoor(destBox)) {
            if (this.initial == 2) { this.initial = 1; }
            setRank(destBox.getRank());
            setFile(destBox.getFile());
            System.out.println("boxRow: " + destBox.getRow() + " boxCol: " + destBox.getCol());
            ChessBoard.getBoard()[getBoardRow()][getBoardCol()].setPiece(null);
            ChessBoard.getBoard()[getBoardRow()][getBoardCol()].setStatus('e');
            setBoardRow(destBox.getRow());
            setBoardCol(destBox.getCol());
            destBox.setStatus(this.status);
            destBox.setPiece(this);
            return 0;

        } else {
            if (getBoardRow() == destBox.getRow() && getBoardCol() == destBox.getCol()) return 3;
            else return 2 ;
        }
    }
}
