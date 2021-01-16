
import java.util.Scanner;

public class Gameplay {
// note for tomorrow: make helper functions to remove redundant codes
// note for tomorrow: use chessboard.checkRank to make sure that the number typed is within the board (done)
// note for tomorrow: Add a feature where only player1 can move White pieces and vice versa (done)
// note for tomorrow: Add a feature that players can say 'continue' after they review their move before changing the board orientation or 'retry' if they did something invalid
    public static void main(String[] args) {
        ChessBoard chessboard = new ChessBoard();
        chessboard.initChessboard();
        /* Checking for accurate board rotation */

        //System.out.println(chessboard.view(1));

        /*
        System.out.println("\n");
        System.out.println(chessboard.view(0));

         */

        System.out.println("Welcome to Chess Tournament PvP!");
        System.out.println("Goal: The first player to checkmate the opponent wins!");
        System.out.println("Player 1 gets to play first using white chess pieces while Player 2 gets to play the black chess pieces");
        System.out.println("Format: *Piece* *Location* *Destination* (File should be capitalized)");
        System.out.println("Type 'Checkmate' if the player thinks the game is over");
        System.out.println("Cheating is prohibited at all times!! \n");

        System.out.print("Are all the chess strategists ready? ");
        Scanner theChoice = new Scanner(System.in);
        if (theChoice.hasNext()){
            String choice = theChoice.next();
            if (choice.equals("Yes") || choice.equals("yes") || choice.equals("YES")) {
                int checkmate = 1;

                // Record the number of moves of each player
                int whiteMove = 0;
                int blackMove = 0;
                chessboard.setMovePieces();
                System.out.println("Initializing Chessboard...\n");
                // White turn if turns == 1 and Black turn if turns == 0
                boolean turns = true;
                while (checkmate == 1){

                    while (true) {
                        //chessboard.setMovePieces();
                        if (whiteMove == 0) {
                            ((King) ChessBoard.getBoard()[7][4].getPiece()).setInitialtoFalse();
                            ((King) ChessBoard.getBoard()[0][4].getPiece()).setInitialtoFalse();
                        }

                        if (turns) {
                            System.out.println("               Player1(White) View");
                            System.out.println(chessboard.debug(1));
                            //System.out.println(chessboard.view(1));
                            System.out.println();
                            System.out.print("Player1(White) Move: ");
                        } else {
                            System.out.println("               Player2(Black) View");
                            System.out.println(chessboard.debug(0));
                            System.out.println();
                            System.out.print("Player2(Black) Move: ");
                        }
                        Scanner input = new Scanner(System.in);
                        String move = input.next();
                        String locate = input.next();
                        String dest = input.next();

                        //System.out.println("row: " + new String(ChessBoard.getRank()).indexOf(locate.charAt(1)));
                        //System.out.println("col: " + new String(ChessBoard.getFile()).indexOf(locate.charAt(0)));
                        //System.out.println("move: " + move + " locate: " + locate + " dest: " + dest);
                        if (chessboard.checkFile(locate.charAt(0)) && chessboard.checkFile(dest.charAt(0)) && chessboard.checkRank(locate.charAt(1)) && chessboard.checkRank(dest.charAt(1))) {
                            //System.out.println("Invalid File. Check the location and the destination of the Piece again. (File: A, B, C, D, E, F, G, H) \n");
                            ChessPiece piece = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(locate.charAt(1))][new String(ChessBoard.getFile()).indexOf(locate.charAt(0))].getPiece();
                            //CheckeredBox locateBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(locate.charAt(1))][new String(ChessBoard.getFile()).indexOf(locate.charAt(0))];
                            CheckeredBox destBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(dest.charAt(1))][new String(ChessBoard.getFile()).indexOf(dest.charAt(0))];
                            if (piece instanceof Pawn) {
                                if (((piece.getColor() == 1 && turns) || (piece.getColor() == 0 && !turns)) && ((Pawn) piece).getName().equals(move)) {
                                    //System.out.println("true");
                                    //System.out.println("Info: " + piece.getBoardRow() + piece.getBoardCol() + piece.getFile() + piece.getRank() + piece.getColor());

                                    //System.out.println("xcoor: " + new String(ChessBoard.getRank()).indexOf(dest.charAt(1)) + " ycoor: " + new String(ChessBoard.getFile()).indexOf(dest.charAt(0)));
                                    //System.out.println("boxRow: " + destBox.getRow() + " boxCol: " + destBox.getCol());

                                    System.out.println(chessboard.showMove(piece));

                                    int result = ((Pawn) piece).move(destBox);
                                    System.out.println("result: " + result);
                                    if (result == 0) {
                                        if (turns) {
                                            System.out.println(chessboard.debug(1));
                                            whiteMove++;
                                            chessboard.checkKing(0);
                                            System.out.println("is BlackKing check: " + chessboard.checkKing(0));
                                            turns = false;
                                            //System.out.println(turns);
                                        } else {
                                            System.out.println(chessboard.debug(0));
                                            blackMove++;
                                            chessboard.checkKing(1);
                                            System.out.println("is whiteKing check: " + chessboard.checkKing(1));
                                            turns = true;
                                        }
                                        // checkKing()????????????????????????????????????????????????????????????????
                                        System.out.println(((Pawn) piece).getName() + " was moved from " + locate + " to " + dest + "");
                                        System.out.print("Press 1 to Continue: ");
                                        while (true) {
                                            Scanner cont = new Scanner(System.in);
                                            String command = cont.next();
                                            if (!command.equals("1")) {
                                                System.out.print("Invalid command. Press 1 to continue: ");
                                            } else break;
                                        }

                                        //System.out.println("Curr Pawn Info: ");
                                        //System.out.println("boardRow: " + piece.getBoardRow());
                                        //System.out.println("boardCol: " + piece.getBoardCol());
                                        //System.out.println(piece.checkEatCoor(destBox));
                                        chessboard.setMovePieces();
                                        chessboard.setPieces();
                                        //chessboard.setMovePieces();
                                        //break;
                                    } else if (result == 1) {
                                        System.out.println("Invalid move. The move is not within the board. Try again.");
                                    } else if (result == 2) {
                                        System.out.println("Invalid move. The move is not available for the current ChessPiece. Try again.");
                                    } else {
                                        System.out.println("Invalid move. The player cannot move to its current location. Try again. \n");
                                    }
                                    //box.setPiece(piece);
                                    //box.setStatus(((Pawn) piece).getStatus());
                                } else {
                                    System.out.println("Not a valid Chessboard Piece (e.g. Pawn, King, Queen, Bishop, Rook, Horse). Try again. \n");
                                }
                            } else if (piece instanceof Queen) {
                                if (((piece.getColor() == 1 && turns) || (piece.getColor() == 0 && !turns)) && ((Queen) piece).getName().equals(move)) {
                                    //System.out.println("true");
                                    //System.out.println("Info: " + piece.getBoardRow() + piece.getBoardCol() + piece.getFile() + piece.getRank() + piece.getColor());
                                    //System.out.println("boxInfo: " + locateBox.getRow() + locateBox.getCol());
                                    //CheckeredBox locateBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(locate.charAt(1))][new String(ChessBoard.getFile()).indexOf(locate.charAt(0))];
                                    //CheckeredBox destBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(dest.charAt(1))][new String(ChessBoard.getFile()).indexOf(dest.charAt(0))];
                                    //System.out.println("xcoor: " + new String(ChessBoard.getRank()).indexOf(dest.charAt(1)) + " ycoor: " + new String(ChessBoard.getFile()).indexOf(dest.charAt(0)));
                                    //System.out.println("boxRow: " + destBox.getRow() + " boxCol: " + destBox.getCol());


                                    System.out.println(chessboard.showMove(piece));

                                    int result = ((Queen) piece).move(destBox);
                                    System.out.println("result: " + result);
                                    if (result == 0) {
                                        if (turns) {
                                            System.out.println(chessboard.debug(1));
                                            whiteMove++;
                                            chessboard.checkKing(0);
                                            System.out.println("is BlackKing check: " + chessboard.checkKing(0));
                                            turns = false;
                                            //System.out.println(turns);
                                        } else {
                                            System.out.println(chessboard.debug(0));
                                            blackMove++;
                                            chessboard.checkKing(1);
                                            System.out.println("is whiteKing check: " + chessboard.checkKing(1));
                                            turns = true;
                                        }
                                        System.out.println( ((Queen) piece).getName() + " was moved from " + locate + " to " + dest + "\n");

                                        System.out.print("Press 1 to Continue: ");
                                        while (true) {
                                            Scanner cont = new Scanner(System.in);
                                            String command = cont.next();
                                            if (!command.equals("1")) {
                                                System.out.print("Invalid command. Press 1 to continue: ");
                                            } else break;
                                        }
                                        //System.out.println("Curr Pawn Info: ");
                                        //System.out.println("boardRow: " + piece.getBoardRow());
                                        //System.out.println("boardCol: " + piece.getBoardCol());
                                        //System.out.println(piece.checkEatCoor(destBox));
                                        chessboard.setMovePieces();
                                        chessboard.setPieces();
                                        //break;
                                    } else if (result == 1) {
                                        System.out.println("Invalid move. The move is not within the board. Try again.");
                                    } else if (result == 2) {
                                        System.out.println("Invalid move. The move is not available for the current ChessPiece. Try again.");
                                    } else {
                                        System.out.println("Invalid move. The player cannot move to its current location. Try again. \n");
                                    }
                                    //box.setPiece(piece);
                                    //box.setStatus(((Pawn) piece).getStatus());
                                } else {
                                    System.out.println("Chessboard Piece access denied or invalid Chessboard Piece (e.g. Pawn, King, Queen, Bishop, Rook, Horse). Try again. \n");
                                }
                            } else if (piece instanceof King) {
                                if (((piece.getColor() == 1 && turns) || (piece.getColor() == 0 && !turns)) && ((King) piece).getName().equals(move)) {
                                    //System.out.println("true");
                                    //System.out.println("Info: " + piece.getBoardRow() + piece.getBoardCol() + piece.getFile() + piece.getRank() + piece.getColor());
                                    //System.out.println("boxInfo: " + locateBox.getRow() + locateBox.getCol());
                                    //CheckeredBox locateBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(locate.charAt(1))][new String(ChessBoard.getFile()).indexOf(locate.charAt(0))];
                                    //CheckeredBox destBox = ChessBoard.getBoard()[new String(ChessBoard.getRank()).indexOf(dest.charAt(1))][new String(ChessBoard.getFile()).indexOf(dest.charAt(0))];
                                    //System.out.println("xcoor: " + new String(ChessBoard.getRank()).indexOf(dest.charAt(1)) + " ycoor: " + new String(ChessBoard.getFile()).indexOf(dest.charAt(0)));
                                    //System.out.println("boxRow: " + destBox.getRow() + " boxCol: " + destBox.getCol());

                                    System.out.println(chessboard.showMove(piece));

                                    int result = ((King) piece).move(destBox);
                                    System.out.println("result: " + result);
                                    if (result == 0) {
                                        if (turns) {
                                            System.out.println(chessboard.debug(1));
                                            whiteMove++;
                                            turns = false;
                                            //System.out.println(turns);
                                        } else {
                                            System.out.println(chessboard.debug(0));
                                            blackMove++;
                                            turns = true;
                                        }
                                        System.out.println( ((King) piece).getName() + " was moved from " + locate + " to " + dest + "\n");

                                        System.out.print("Press 1 to Continue: ");
                                        while (true) {
                                            Scanner cont = new Scanner(System.in);
                                            String command = cont.next();
                                            if (!command.equals("1")) {
                                                System.out.print("Invalid command. Press 1 to continue: ");
                                            } else break;
                                        }
                                        //System.out.println("Curr Pawn Info: ");
                                        //System.out.println("boardRow: " + piece.getBoardRow());
                                        //System.out.println("boardCol: " + piece.getBoardCol());
                                        //System.out.println(piece.checkEatCoor(destBox));
                                        chessboard.setMovePieces();
                                        chessboard.setPieces();
                                        //break;
                                    } else if (result == 1) {
                                        System.out.println("Invalid move. The move is not within the board. Try again.");
                                    } else if (result == 2) {
                                        System.out.println("Invalid move. The move is not available for the current ChessPiece. Try again.");
                                    } else {
                                        System.out.println("Invalid move. The player cannot move to its current location. Try again. \n");
                                    }
                                    //box.setPiece(piece);
                                    //box.setStatus(((Pawn) piece).getStatus());
                                } else {
                                    System.out.println("Chessboard Piece access denied or invalid Chessboard Piece (e.g. Pawn, King, Queen, Bishop, Rook, Horse). Try again. \n");
                                }
                            } else {
                                System.out.println("Invalid Move. Try again. \n");
                            }
                        } else {
                            System.out.println("Invalid input. Check the location and the destination of the Piece again. (File: A, B, C, D, E, F, G, H) (Rank: 1, 2, 3, 4, 5, 6, 7, 8) \n");
                        }
                    }
                    //checkmate = 0;
                }
            }
        }
        


        // chessboard.move(checkboard[][] to , )

    }
}
