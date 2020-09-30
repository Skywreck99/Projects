public class CheckeredBox {

    private final char rank;
    private final char file;
    private ChessPiece piece;
    private char status;
    private final int row;
    private final int col;

    public CheckeredBox(char file, char rank, char status) {
        this.file = file;
        this.rank = rank;
        this.status = status;
        this.row = new String(ChessBoard.getRank()).indexOf(rank);
        this.col = new String(ChessBoard.getFile()).indexOf(file);
    }

    public CheckeredBox(char file, char rank, ChessPiece piece) {
        this.file = file;
        this.rank = rank;
        this.piece = piece;
        this.row = new String(ChessBoard.getRank()).indexOf(rank);
        this.col = new String(ChessBoard.getFile()).indexOf(file);
        //System.out.println("PawnInfo: " + this.file +  this.rank + this.row + this.col);
    }

    public char getRank(){ return this.rank; }
    public char getFile(){ return this.file; }
    public char getStatus(){ return this.status; }
    public ChessPiece getPiece(){ return this.piece; }
    public int getRow() { return row; }
    public int getCol() { return col; }
    public void setStatus(char status) { this.status = status; }
    public void setPiece(ChessPiece piece){ this.piece = piece; }

}
