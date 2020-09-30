public class King extends ChessPiece {
    // note for tomorrow: Test when King is surrounded by allies and finish King tomorrow
    private final char status;
    private final String name;
    private boolean initial;
    public King(char file, char rank, int color) {
        super(file, rank, color);
        this.status = 'K';
        this.name = "King";
        initial = true;
        //setAvailableMove(new int[][]{{getBoardRow(), getBoardCol()}});
        //setPossibleEat(new int[][]{{getBoardRow(), getBoardCol()}});
        //setMove();
    }

    public char getStatus() { return status; }
    public String getName() { return name; }
    public void setInitialtoFalse() { initial = false; }

    public void setMove() {
        // arr_move will hold all King's positions
        int[][] arr_move;
        // each index represents an array for eight different positions
        int[][][] pos_move = new int[8][][];
        // can use an array for count01 to count08
        //int[] count = new int[8];
        int total = 0; int arrIdx = 0; int count = 0; int traverse = 0;
        //System.out.println("here: " + locateBox.getRow());
        int row = getBoardRow(); int col = getBoardCol();
        CheckeredBox[][] board = ChessBoard.getBoard();
        //int pieceColor = getColor();
        //int xPieceColor = ChessBoard.getBoard()[row][col].getPiece().getColor();
        //int boxStatus = ChessBoard.getBoard()[row][col].getStatus();
        while (traverse < 8) {
            // Conditional statements determine the King's move for 8 different positions
            if (traverse == 0 || traverse == 4) {
                // Conditional statements determine when to stop counting the possible moves for each position

                // North and South
                if (traverse == 0) {
                    row--;
                    if (row > -1) {
                        //row--;
                        //System.out.println(" here!!!!!");

                        // Conditional statements determine if the King's path are blocked by an enemy or if its empty
                        if (board[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }



                            //total++; //count++;
                        }
                        count++;
                        row = -1;
                    } else {
                        //pos_move = new int[traverse][];
                        //System.out.println(" here!!!!!");
                        //System.out.println("North");
                        //System.out.println("count: " + count);
                        //row = locateBox.getRow();
                        row = getBoardRow();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //count = 0;
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row-1, col};

                            //System.out.println("Nrow: " + row);
                            //System.out.println("Ncount: " + count);
                            /*
                            for (int i = row-1; i >= row - count; i--, arrIdx++) {
                                // can use the variable col instead of getBoardCol()
                                //System.out.println("arrIdx: " +arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                            }

                             */
                            // loop prepares for 1st traverse
                            //row = locateBox.getRow();
                            count = 0;
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
                        // Conditional statements determine if the King's path are blocked by either an ally or an enemy
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }
                        }
                        count++;
                        row = 8;
                    } else {
                        //System.out.println("South");
                        row = getBoardRow();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row+1, col};
                            /*
                            row = getBoardRow();
                            for (int i = row+1; i <= row + count; i++, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                            }
                            //row = locateBox.getRow();

                             */
                            count = 0;
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
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }
                        }
                        count++;
                        row = -1; col = 8;
                    } else {
                        //pos_move = new int[traverse][];
                        //System.out.println("Northeast");
                        row = getBoardRow();
                        col = getBoardCol();
                        if (count == 0) {
                            //System.out.println("that's me");

                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow();
                            //col = getBoardCol();
                        } else {

                            //row = getBoardRow();
                            //col = getBoardCol();
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row-1, col+1};
                            /*
                            for (int i = row-1; i >= row - count; i--, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                                col++;
                            }

                             */
                            //row = locateBox.getRow();
                            //col = getBoardCol();
                            count = 0;
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
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {
                            //System.out.println("here");
                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }
                        }
                        count++;
                        row = 8; col = -1;
                    } else {
                        //System.out.println("Southwest");
                        row = getBoardRow();
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row+1, col-1};
                            /*
                            //row = getBoardRow();
                            //col = getBoardCol()-1;
                            for (int i = row+1; i <= row + count; i++, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{i, col};
                                col--;
                            }

                             */
                            //col = getBoardCol();
                            count = 0;
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
                        // Conditional statements determine if the King's path are blocked by either an ally or an enemy
                        //col++;
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {
                            //System.out.println("alert!");

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }
                            //System.out.println("went here");
                        }
                        count++;
                        col = 8;
                    } else {
                        //System.out.println("East");
                        //System.out.println("count " + count);
                        col = getBoardCol();
                        //System.out.println("col: " + col);
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //col = getBoardCol();
                        } else {
                            pos_move[traverse] = new int[count][];
                            //System.out.println("count: " + count);
                            //System.out.println("traverse: " + traverse);
                            //System.out.println("arrIdx: " + arrIdx);
                            //System.out.println("row: " + row + ", col: " + (col+1));
                            pos_move[traverse][arrIdx] = new int[]{row, col+1};
                            //col = getBoardCol();
                            //System.out.println("count: " + count);
                            //System.out.println("col: " + col);
                            /*
                            for (int i = col+1; i <= col + count; i++, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                            }

                             */
                            // col = locateBox.getCol();
                            count = 0;
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
                        // Conditional statements determine if the King's path are blocked by either an ally or an enemy
                        //col--;

                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    //System.out.println("thisssssssssssssssssssssssssss");
                                    total++;
                                    //System.out.println("summmmm: " + total);
                                }
                            } else {
                                total++;
                            }
                        }
                        count++;
                        col = -1;
                    } else {
                        //System.out.println("West");
                        //System.out.println("Wcount: " + count);
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //col = getBoardCol();
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row, col-1};
                            //col = getBoardCol();
                            //System.out.println("count: " + count);
                            //System.out.println("col: " + col);
                            /*
                            for (int i = col-1; i >= col - count; i--, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                            }

                             */
                            // col = locateBox.getCol();
                            count = 0;
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
                    //System.out.println("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW");
                    row++; col++;
                    if (row < 8 && col < 8) {
                        //row++;
                        //col++;
                        //System.out.println("1: " + (ChessBoard.getBoard()[row][col].getStatus() == 'e'));
                        //System.out.println("2: " + (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0));
                        //System.out.println("3: " + (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1));
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {
                            if (!initial) {
                                //System.out.println("row: " + row + ", col: " + col);
                                //System.out.println("can move: " + checkMove(row, col));
                                if (checkMove(row, col)) {
                                    //System.out.println("ALERTTTTTTTT");
                                    total++;
                                    //System.out.println("totallllllllllllll: " + total);
                                }
                            } else {
                                //System.out.println("went here instead");
                                total++;
                            }
                        }
                        count++;
                        row = 8; col = 8;
                    } else {
                        //System.out.println("Southeast");
                        row = getBoardRow();
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row+1, col+1};
                            /*
                            row = getBoardRow()+1;
                            col = getBoardCol();
                            //System.out.println("count:" + count);
                            for (int i = col+1; i <= col + count; i++, arrIdx++) {
                                //System.out.println("arrIdx: " + arrIdx);
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                                row++;
                            }
                            row = getBoardRow();

                             */
                            //col = locateBox.getCol();
                            count = 0;
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
                        if (ChessBoard.getBoard()[row][col].getStatus() == 'e' || (getColor() == 1 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 0) || (getColor() == 0 && ChessBoard.getBoard()[row][col].getPiece().getColor() == 1)) {

                            if (!initial) {
                                if (checkMove(row, col)) {
                                    total++;
                                }
                            } else {
                                total++;
                            }
                        }
                        count++;
                        row = -1; col = -1;
                    } else {
                        //System.out.println("Northwest");
                        row = getBoardRow();
                        col = getBoardCol();
                        if (count == 0) {
                            pos_move[traverse] = new int[][]{{row, col}};
                            //row = getBoardRow();
                            //col = getBoardCol();
                        } else {
                            pos_move[traverse] = new int[count][];
                            pos_move[traverse][arrIdx] = new int[]{row-1, col-1};
                            /*
                            row = getBoardRow()-1;
                            col = getBoardCol();
                            for (int i = col-1; i >= col - count; i--, arrIdx++) {
                                pos_move[traverse][arrIdx] = new int[]{row, i};
                                row--;
                            }
                            row = getBoardRow();

                             */
                            //col = locateBox.getCol();
                            count = 0;
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

        System.out.println("KING MOVES AND POSSIBLE MOVES");
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
        System.out.println();
        //System.out.println("total: " + total);
        //System.out.println("current arrIdx: " + arrIdx);
        // Checks if the King can move freely or not (i.e. The King is surrounded by her allies)
        if (total == 0) {
            //System.out.println("here");
            arr_move = new int[][]{{row, col}};
        } else {

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
                    //System.out.println("initial: " + initial);
                    if ((pos_move[i][j][0] == row && pos_move[i][j][1] == col)) { continue; }

                    else if (initial && (board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e' || (getColor() == 1 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 0) || (getColor() == 0 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 1))) {
                        //System.out.println("here");
                        arr_move[arrIdx] = pos_move[i][j];
                        arrIdx++;

                    } else if (!initial && board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() == 'e') {
                        //System.out.println("Absolutely here");
                        arr_move[arrIdx] = pos_move[i][j];
                        arrIdx++;

                    } else if (!initial && board[pos_move[i][j][0]][pos_move[i][j][1]].getStatus() != 'e' && checkMove(pos_move[i][j][0], pos_move[i][j][1])) {
                        //System.out.println("definitely here");
                        if ((getColor() == 1 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 0) || (getColor() == 0 && board[pos_move[i][j][0]][pos_move[i][j][1]].getPiece().getColor() == 1)) {
                            arr_move[arrIdx] = pos_move[i][j];
                            arrIdx++;
                        }
                    }
                    //System.out.println("probably skipped");
                }

                //idx++;
                //System.out.println();
            }
        }
        System.out.print("arr_move: ");
        for (int i = 0; i < arr_move.length; i++) {
            System.out.print("(" + arr_move[i][0] + "," + arr_move[i][1] + ") ");
        }
        System.out.println();
        System.out.println();

        setAvailableMove(arr_move);
    }/*
    private boolean canEat(CheckeredBox box) {
        CheckeredBox[][] board = ChessBoard.getBoard();
    }
    */

    public int move(CheckeredBox destBox) {
        /*
        Move successfully: Return 0
        Out of Bounds: Return 1
        Invalid Move: Return 2
        Trying to move to its current position: Return 3
        */



        // Checks if the coordinates given are out of bounds
        if (!inBoard(destBox.getRow(), destBox.getCol())) { return 1; }

        if (checkMoveCoor(destBox)) {
            //if (initial) { initial = false; }
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

    private boolean checkMove(int row, int col) {
        // ChessBoard.setMovePieces();
        ChessPiece[] pieces;
        /*
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                //System.out.println("once");
                if (board[i][j].getStatus() != 'e') {
                    if ((board[i][j].getPiece().getColor() == 1 && getColor() == 0) || (board[i][j].getPiece().getColor() == 0 && getColor() == 1)) {
                        System.out.println("i: " + i + ", j: " + j);
                        for (int k = 0; k < board[i][j].getPiece().getHRpossMove().length; k++) {
                            for (int l = 0 ; l < board[i][j].getPiece().getHRpossMove()[k].length; k++) {
                                if ((board[i][j].getPiece().getHRpossMove()[k][l][0] != board[i][j].getPiece().getBoardRow() && board[i][j].getPiece().getHRpossMove()[k][l][1] != board[i][j].getPiece().getBoardCol()) && (board[i][j].getPiece().getHRpossMove()[k][l][0] == row && board[i][j].getPiece().getHRpossMove()[k][l][1] == col)) {
                                    canMove = false;
                                    break;
                                }
                            }
                            if (!canMove) {
                                break;
                            }
                        }
                    }
                }
            }
        }

         */
        if (getColor() == 1) {
            pieces = ChessBoard.getBlackPieces();
            for (int i = 0; i < pieces.length; i++) {
                for (int j = 0; j < pieces[i].getHRpossMove().length; j++) {
                    for (int k = 0; k < pieces[i].getHRpossMove()[j].length; k++) {
                        //System.out.println("Pawn length: " + pieces[i].getHRpossMove()[j].length);
                        //System.out.println("row: " + pieces[i].getHRpossMove()[j][k][0] + ", col: " + pieces[i].getHRpossMove()[j][k][1]);
                        if (pieces[i].getHRpossMove()[j][k].length == 1 && pieces[i].getHRpossMove()[j][k][0] == row && pieces[i].getHRpossMove()[j][k][1] == col) {
                            continue;
                        } else {
                            //System.out.println("Pawn length: " + pieces[i].getHRpossMove()[j][k].length);
                            if (pieces[i].getHRpossMove()[j][k][0] == row && pieces[i].getHRpossMove()[j][k][1] == col) {
                                //System.out.println("went hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeee");
                                //System.out.println("rank: " + pieces[i].getRank());
                                //System.out.println("file: " + pieces[i].getFile());
                                return false;
                            }
                        }
                    }
                }
            }
        } else {
            pieces = ChessBoard.getWhitePieces();
            for (int i = 0; i < pieces.length; i++) {
                //System.out.println("Piece: " + pieces[i].getClass());
                //System.out.println("length: " + pieces[i].getHRpossMove().length);
                for (int j = 0; j < pieces[i].getHRpossMove().length; j++) {
                    for (int k = 0; k < pieces[i].getHRpossMove()[j].length; k++) {
                        if (pieces[i].getHRpossMove()[j].length == 1 && pieces[i].getHRpossMove()[j][k][0] == row && pieces[i].getHRpossMove()[j][k][1] == col) {
                            continue;
                        } else {
                            if (pieces[i].getHRpossMove()[j][k][0] == row && pieces[i].getHRpossMove()[j][k][1] == col) {
                                //System.out.println("went hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeee");
                                //System.out.println("rank: " + pieces[i].getRank());
                                //System.out.println("file: " + pieces[i].getFile());
                                //System.out.println("length: " + pieces[i].getHRpossMove()[j][k].length);
                                for (int l = 0; l < pieces[i].getHRpossMove()[j][k].length; l++) {

                                }
                                return false;
                            }
                        }
                    }
                }
            }
        }


        return true;
    }
}


