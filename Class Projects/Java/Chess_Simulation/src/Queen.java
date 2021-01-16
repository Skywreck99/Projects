public class Queen extends ChessPiece {
    // note for tomorrow: check if locateBox is not needed for all Pieces. Instead use getBoardRow() and getBoardCol() (done)
    // note for tomorrow: Fix setMove() for efficiency (limit to four traverses instead of eight traverses) (done)
    // clean up: This condition '(getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)' can be placed in a function and use the function for cleanliness
    private final char status;
    private final String name;

    public Queen(char file, char rank, int color) {
        super(file, rank, color);
        this.status = 'Q';
        this.name = "Queen";
        //setAvailableMove(new int[][]{{getBoardRow(), getBoardCol()}});
        //setPossibleEat(new int[][]{{getBoardRow(), getBoardCol()}});
        //setMove();
    }

    public char getStatus() { return status; }
    public String getName() { return name; }

    public void setMove() {
        // arr_move will hold all Queen's positions
        int[][] arr_move;
        // each index represents an array for eight different positions
        int[][][] pos_move = new int[8][][];
        // can use an array for count01 to count08
        //int[] count = new int[8];
        int total = 0; int arrIdx = 0; int count = 0; int traverse = 0;
        //System.out.println("here: " + locateBox.getRow());
        int row = getBoardRow(), col = getBoardCol();
        CheckeredBox[][] board = ChessBoard.getBoard();
        //int pieceColor = getColor();
        //int xPieceColor = ChessBoard.getBoard()[row][col].getPiece().getColor();
        //int boxStatus = ChessBoard.getBoard()[row][col].getStatus();
        while (traverse < 8) {
            // Conditional statements determine the Queen's move for 8 different positions
            if (traverse == 0 || traverse == 4) {
                // Conditional statements determine when to stop counting the possible moves for each position

                // North and South
                if (traverse == 0) {
                    row--;
                    if (row > -1) {
                        //row--;
                        //System.out.println(" here!!!!!");
                        // Conditional statements determine if the Queen's path are blocked by either an ally or an enemy
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;

                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = -1;                       // Can extract coordinates here for setPossibleEat, but it is unnecessary

                        } else {
                            //System.out.println(" here!!!!!");
                            count++; row = -1;
                        }
                    } else {
                        //pos_move = new int[traverse][];
                        //System.out.println(" here!!!!!");
                        //System.out.println("North");
                        //System.out.println("count: " + count);
                        //row = locateBox.getRow();
                        row = getBoardRow();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow();
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow();
                            //System.out.println("Nrow: " + row);
                            //System.out.println("Ncount: " + count);
                            for (int i = row-1; i >= row - count; i--, arrIdx++) {
                                // can use the variable col instead of getBoardCol()
                                //System.out.println("arrIdx: " +arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                            }
                            // loop prepares for 1st traverse
                            //row = locateBox.getRow();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;
                    }
                } else {
                    //System.out.println("curRow: " + row);
                    row++;
                    if (row < 8) {
                        //System.out.println("Went over here instead");
                        //row++;
                        //System.out.println(row);
                        // Conditional statements determine if the Queen's path are blocked by either an ally or an enemy
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = 8;
                        } else {
                            count++; row = 8;
                        }
                    } else {
                        //System.out.println("South");
                        row = getBoardRow();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow();
                            for (int i = row+1; i <= row + count; i++, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                            }
                            //row = locateBox.getRow();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;

                    }
                }

            } else if (traverse == 1 || traverse == 5) {

                // Northeast and Southwest
                if (traverse == 1) {
                    row--; col++;
                    if (row > -1 && col < 8) {
                        //row--;
                        //col++;
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = -1; col = 8;
                        } else {
                            count++; row = -1; col = 8;
                        }
                    } else {
                        //pos_move = new int[traverse][];
                        //System.out.println("Northeast");
                        row = getBoardRow(); col = getBoardCol();
                        if (count == 0) {
                            //System.out.println("that's me");
                            pos_move[traverse] = new int[][]{{row, col}};
                            // row = getBoardRow(); col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow(); col = getBoardCol()+1;
                            int j = col+1;
                            for (int i = row-1; i >= row - count; i--, j++, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, j};
                            }
                            //row = locateBox.getRow();
                            //col = getBoardCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;

                    }
                } else {
                    row++; col--;
                    if (row < 8 && col > -1) {
                        //row++;
                        //col--;
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = 8; col = -1;
                        } else {
                            count++; row = 8; col = -1;
                        }
                    } else {
                        //System.out.println("Southwest");
                        row = getBoardRow(); col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow(); col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow(); col = getBoardCol()-1;
                            int j = col-1;
                            for (int i = row+1; i <= row + count; i++, j--, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, j};
                                //col--;
                            }
                            //col = getBoardCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;
                    }
                }

            } else if (traverse == 2 || traverse == 6) {

                // East and West
                if (traverse == 2) {
                    //System.out.println("Ecount: " + count);
                    col++;
                    //System.out.println("Erow: " + row);
                    //System.out.println("Ecol: " + col);
                    if (col < 8) {
                        // Conditional statements determine if the Queen's path are blocked by either an ally or an enemy
                        //col++;
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                            //System.out.println("went here");
                            //col++;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; col = 8;
                            //System.out.println("went here");
                        } else {
                            count++; col = 8;
                        }
                    } else {
                        //System.out.println("East");
                        //System.out.println("count " + count);
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //col = getBoardCol();
                            //System.out.println("count: " + count);
                            //System.out.println("col: " + col);
                            for (int i = col+1; i <= col + count; i++, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                            }
                            // col = locateBox.getCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */


                        traverse++;
                    }
                } else {
                    col--;
                    if (col > -1) {
                        // Conditional statements determine if the Queen's path are blocked by either an ally or an enemy
                        //col--;

                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                            //col--;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; col = -1;
                        } else {
                            count++;
                            col = -1;
                        }
                    } else {
                        //System.out.println("West");
                        //System.out.println("Wcount: " + count);
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //col = getBoardCol();
                            //System.out.println("count: " + count);
                            //System.out.println("col: " + col);
                            for (int i = col-1; i >= col - count; i--, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                            }
                            // col = locateBox.getCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */


                        traverse++;
                    }
                }

            } else if (traverse == 3 || traverse == 7) {

                // Southeast and Northwest
                if (traverse == 3) {
                    row++; col++;
                    if (row < 8 && col < 8) {
                        //row++;
                        //col++;
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = 8; col = 8;
                        } else {
                            count++; row = 8; col = 8;
                        }
                    } else {
                        //System.out.println("Southeast");
                        row = getBoardRow(); col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow(); col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow()+1; col = getBoardCol();
                            int j = row+1;
                            //System.out.println("count:" + count);
                            for (int i = col+1; i <= col + count; i++, j++, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{j, i};
                                //row++;
                            }
                            //row = getBoardRow();
                            //col = locateBox.getCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;
                    }
                } else {
                    row--; col--;
                    if (row > -1 && col > -1) {
                        if (board[row][col].getStatus() == 'e') {
                            total++; count++;
                            //row--;
                            //col--;
                        } else if ((getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                            total++; count++; row = -1; col = -1;
                        } else {
                            count++; row = -1; col = -1;
                        }
                    } else {
                        //System.out.println("Northwest");
                        row = getBoardRow(); col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow(); col = getBoardCol(); arrIdx = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            //row = getBoardRow()-1; col = getBoardCol();
                            int j = row-1;
                            for (int i = col-1; i >= col - count; i--, j--, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{j, i};
                                //row--;
                            }
                            //row = getBoardRow();
                            //col = locateBox.getCol();
                            count = arrIdx = 0;
                        }
                        /*
                        System.out.print("pos_move at index " + traverse + ": ");
                        for (int i = 0; i < pos_move[traverse].length; i++) {
                            System.out.print("(" + pos_move[traverse][i][0] + "," + pos_move[traverse][i][1] + ") ");
                        }
                        System.out.println();

                         */
                        traverse++;
                    }
                }

            } else {
                break;
            }
        }
        setHRpossMove(pos_move);


        System.out.println("QUEEN MOVES AND POSSIBLE MOVES");
        for (int i = 0; i < pos_move.length; i++) {
            //System.out.println("pos_move: " + pos_move[i].length);
            System.out.print("pos_move at index " + i + ": ");

            for (int j = 0; j < pos_move[i].length; j++) {
                System.out.print("(" + pos_move[i][j][0] + "," + pos_move[i][j][1] + ") ");
                //System.out.println("color: " + board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus());
                //System.out.println("CHECKPOINT");
                //System.out.println("arrIdx: " + arrIdx);
                //System.out.println("i: " + i);
                //System.out.println("j: " + j);
                /*
                if ((pos_move[i][j][0] == row && pos_move[i][j][1] == col)) { continue; }
                else if (board[pos_move[i][j][0]][pos_move[i][j][0]].getStatus() == 'e' || (getColor() == 1 && board[row][col].getPiece().getColor() == 0) || (getColor() == 0 && board[row][col].getPiece().getColor() == 1)) {
                    arr_move[arrIdx] = pos_move[i][j];
                    arrIdx++;
                }

                 */


                //System.out.println("CHECKPOINT");

            }


            System.out.println();
        }



        //System.out.println();

        //System.out.println("current arrIdx: " + arrIdx);
        // Checks if the Queen can move freely or not (i.e. The queen is surrounded by her allies)
        if (total == 0) {
            setAvailableMove(new int[][]{{row, col}});
        } else {
            //System.out.println("total: " + total);
            //System.out.println("pos_length: " + pos_move[0][0][0]);
            arr_move = new int[total][2];

            //int idx = 0;

            for (int i = 0; i < pos_move.length; i++) {
                //System.out.println("pos_move: " + pos_move[i].length);
                //System.out.print("pos_move at index " + idx + ": ");

                for (int j = 0; j < pos_move[i].length; j++) {
                    //System.out.println("arrIdx: " + arrIdx);
                    //System.out.println("1: " + (board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e'));
                    //System.out.println("2: " + (getColor() == 1 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 0));
                    //System.out.println("3: " + (getColor() == 0 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 1));
                    //System.out.println("pos_move[i][j]row: " + pos_move[i][j][0] + ", pos_move[i][j]col: " + pos_move[i][j][1]);
                    if ((pos_move[i][j][0] == row && pos_move[i][j][1] == col)) { continue; }

                    else if (board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e' || (getColor() == 1 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 0) || (getColor() == 0 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 1)) {
                        arr_move[arrIdx] = pos_move[i][j];
                        arrIdx++;
                    }
                }

                //idx++;
                //System.out.println();
            }



            System.out.print("arr_move: ");
            for (int i = 0; i < arr_move.length; i++) {
                System.out.print("(" + arr_move[i][0] + "," + arr_move[i][1] + ") ");
            }
            System.out.println();
            System.out.println();






            setAvailableMove(arr_move);
            //System.out.println();
        }
    }


    public int move(CheckeredBox destBox) {
        /*
        Move successfully: Return 0
        Out of Bounds: Return 1
        Invalid Move: Return 2
        Trying to move to its current position: Return 3
        */

        // Checks if the coordinates given are out of bounds
        if (!inBoard(destBox.getRow(), destBox.getCol())) { return 1; }

        // Checks if Queen can move or eat
        if (checkMoveCoor(destBox)) {
            setRank(destBox.getRank());
            setFile(destBox.getFile());
            //System.out.println("boardRow: " + getBoardRow() + " boardCol: " + getBoardCol());
            //System.out.println("boxRow: " + destBox.getRow() + " boxCol: " + destBox.getCol());
            ChessBoard.getBoard()[getBoardRow()][getBoardCol()].setPiece(null);
            ChessBoard.getBoard()[getBoardRow()][getBoardCol()].setStatus('e');
            setBoardRow(destBox.getRow());
            setBoardCol(destBox.getCol());
            destBox.setStatus(this.status);
            destBox.setPiece(this);
            //setMove(box);
            //setEat(box);
            //System.out.println("here");
            return 0;
        } else {
            if (getBoardRow() == destBox.getRow() && getBoardCol() == destBox.getCol()) return 3;
            else return 2;
        }
    }
}
