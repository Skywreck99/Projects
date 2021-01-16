// optimized versions of matrix diagonal summing
#include "matvec.h"

// You can write several different versions of your optimized function
// in this file and call one of them in the last function.


// ODD-EVEN-VECTORS-SPLIT-UP-MATRIX
// Working on two parts simultaneously based on oddness end evenness of the matrix (High: 3/35)
int sumdiag_VER1(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){
    printf("sumdiag_base: bad sizes\n");
    return 1;
  }
  for(int i=0; i<vec.len; i++){                   // initialize vector of diagonal sums
    VSET(vec,i,0);                                // to all 0s
  }

  int e = 2*mat.rows-2;
  for(int d=0; d < mat.rows; d++){
    if (d%2) { int c = 0;
      for(int r=mat.rows-d-1; r<mat.rows; r+=2,c+=2){
        VSET(vec, d, MGET(mat, r, c)+VGET(vec, d)+MGET(mat, r+1, c+1));
        VSET(vec, e, MGET(mat, c, r)+VGET(vec, e)+MGET(mat, c+1, r+1));
      }
    } else { int c = 0;
      for(int r=mat.rows-d-1; r<mat.rows; r++,c++){
        VSET(vec, d, MGET(mat, r, c)+VGET(vec, d));
        if (e != d) {VSET(vec, e, MGET(mat, c, r)+VGET(vec, e));}
      }
    } e--;
  } return 0;
}

// MIRRORED-MATRIX
// Works on Bottom-Left-Top-Right first then Converge into the middle (High: 3/35)
int sumdiag_VER2(matrix_t mat, vector_t vec) {
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*  11 12 13 14 |      11  12 |13||14||
      15 16 17 18 |      15  16  17 |18||
      19 20 21 22 | =>  |19| 20  21  22 |
      23 24 25 26 |     |23||24| 25  26 |
      ____________       _______________
  */

  int e = 2*mat.rows-2;
  for (int d = 0; d < mat.rows; d++){
    int c = 0;
    for(int r=mat.rows-d-1; r<mat.rows; r++,c++){
      VSET(vec, d, MGET(mat, r, c) + VGET(vec, d));
      if (e != mat.rows-1){VSET(vec, e, MGET(mat, c, r) + VGET(vec, e));}
    } e--;
  } return 0;
}

// MAJOR-DIAGONAL-AND-TWO-MIRRORED-TRIANGLE-MATRIX
// Computing the longest Diagonal first, then work on the two triangles left (High: 3/35)
int sumdiag_VER3(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*  11 12 13 14 |         |11|     12  13  14 |
      15 16 17 18 |      15     |16|     17  18 |
      19 20 21 22 | =>   19  20     |21|     22 |
      23 24 25 26 |      23  24  25     |26|    |
      ____________       _______________________
  */

  for(int i = 0; i < mat.rows; i++){VSET(vec, mat.rows-1, MGET(mat, i, i) + VGET(vec, mat.rows-1));}

  int e = 2*mat.rows-2;
  for (int d = 0; d < mat.rows-1; d++){ int c = 0;
    for(int r=mat.rows-d-1; r<mat.rows; r++,c++){
      VSET(vec, d, MGET(mat, r, c) + VGET(vec, d));
      VSET(vec, e, MGET(mat, c, r) + VGET(vec, e));
    }
    e--;
  }
  return 0;
}

// OPT-ROW-MATRIX
// Works on One Row based on Vertices (Max: 41/35)
int sumdiag_VER4(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*                    ____________
      11 12 13 14 |     11 12 13 14 |
      15 16 17 18 |     ____________
      19 20 21 22 | =>  15 16 17 18 |
      23 24 25 26 |     19 20 21 22 |
      ____________      23 24 25 26 |
                        ____________
  */

  for (int i = 0; i < mat.rows; i++) { int d = mat.rows-i-1;
    for (int j = 0; j < mat.cols; j++, d++){VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));}
  } return 0;
}

// OPT-TWO-ROW-MATRIX
// Works on Two rows at the same time based on Vertices (Max: 47/35)
int sumdiag_VER5(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*                    ____________
      11 12 13 14 |     11 12 13 14 |
      15 16 17 18 |     ____________
      19 20 21 22 | =>  15 16 17 18 |
      23 24 25 26 |     ____________
      ____________      19 20 21 22 |
                        23 24 25 26 |
                        ____________
  */
  for (int i = 0; i < mat.rows; i+=2) { int d = mat.rows-i-1;
    for (int j = 0; j < mat.cols; j++, d++){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      if (i+1 != mat.rows){VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));}
    }
  }
  return 0;
}

// TWO-BY-TWO-PARTITION-MATRIX
// 2x2 partitions of the matrix using the hidden blueprint of vertices for more optimization (Max: 56/35)
int sumdiag_VER6(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*  11 12 13 14 |     11 12 | 13 14 |
      15 16 17 18 |     15 16 | 17 18 |
      19 20 21 22 | =>  ______ _______
      23 24 25 26 |     19 20 | 21 22 |
      ____________      23 24 | 25 26 |
                        ______ _______
  */
  for (int i = 0; i < mat.rows; i+=2) {
    int d = mat.rows-i-1;
    for (int j = 0; j < mat.cols; j+=2, d+=2){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      if (j+1 != mat.cols){VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));}
      if (i+1 != mat.rows){
        VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
        if (j+1 != mat.cols){VSET(vec, d, MGET(mat, i+1, j+1) + VGET(vec, d));}
      }
    }
  } return 0;
}

int sumdiag_VER7(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  if(vec.len != (mat.rows + mat.cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*  11 12 13 14 |     11 12 | 13 14 |
      15 16 17 18 |     15 16 | 17 18 |
      19 20 21 22 | =>  ______ _______
      23 24 25 26 |     19 20 | 21 22 |
      ____________      23 24 | 25 26 |
                        ______ _______
  */
  /*
  for (int i = 0; i < mat.rows-4; i+=4) {
    int d = mat.rows-i-1;
    for (int j = 0; j < mat.cols-4; j+=4, d+=4){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      VSET(vec, d, MGET(mat, i+1, j+1) + VGET(vec, d));
      VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));
      VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
    }
  }
  */

  int i;
  for (i = 0; i < mat.rows-2; i+=2) {
    int d = mat.rows-i-1, j;
    for (j = 0; j < mat.cols-2; j+=2, d+=2){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      VSET(vec, d, MGET(mat, i+1, j+1) + VGET(vec, d));
      VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));
      VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
    }
    for (; j < mat.cols; j++, d++) {
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
    }
  }

  for (; i < mat.rows; i++) {
    int d = mat.rows-i-1, j;
    for (j = 0; j < mat.cols-2; j+=2, d+=2){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      //VSET(vec, d, MGET(mat, i+1, j+1) + VGET(vec, d));
      VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));
      //VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
    }
    for (; j < mat.cols; j++, d++) {
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      //VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
    }
  }

  return 0;
}

int sumdiag_VER8(matrix_t mat, vector_t vec) {
  // OPTIMIZED CODE HERE
  int rows = mat.rows;
  int cols = mat.cols;
  if(vec.len != (rows + cols -1)){return 1;}
  for(int i=0; i<vec.len; i++){VSET(vec,i,0);}

  /*  11 12 13 14 |     11 12 | 13 14 |
      15 16 17 18 |     15 16 | 17 18 |
      19 20 21 22 | =>  ______ _______
      23 24 25 26 |     19 20 | 21 22 |
      ____________      23 24 | 25 26 |
                        ______ _______
  */

  int i;

  // Unroll the loop 4 times and access rows then columns for better memory access
  // Iterating as 4 by 4 partition of the matrix
  for (i = 0; i < rows-4; i+=4) {
    int d = rows-i-1, j;
    for (j = 0; j < cols-4; j+=4, d+=4){

      // 1 cell
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));

      // 3 cells
      VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));
      VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
      VSET(vec, d, MGET(mat, i+1, j+1) + VGET(vec, d));

      // 5 cells
      VSET(vec, d+2, MGET(mat, i, j+2) + VGET(vec, d+2));
      VSET(vec, d+1, MGET(mat, i+1, j+2) + VGET(vec, d+1));
      VSET(vec, d, MGET(mat, i+2, j+2) + VGET(vec, d));
      VSET(vec, d-1, MGET(mat, i+2, j+1) + VGET(vec, d-1));
      VSET(vec, d-2, MGET(mat, i+2, j) + VGET(vec, d-2));

      // 7 cells
      VSET(vec, d+3, MGET(mat, i, j+3) + VGET(vec, d+3));
      VSET(vec, d+2, MGET(mat, i+1, j+3) + VGET(vec, d+2));
      VSET(vec, d+1, MGET(mat, i+2, j+3) + VGET(vec, d+1));
      VSET(vec, d, MGET(mat, i+3, j+3) + VGET(vec, d));
      VSET(vec, d-1, MGET(mat, i+3, j+2) + VGET(vec, d-1));
      VSET(vec, d-2, MGET(mat, i+3, j+1) + VGET(vec, d-2));
      VSET(vec, d-3, MGET(mat, i+3, j) + VGET(vec, d-3));}
/*
      // 9 cells
      VSET(vec, d+4, MGET(mat, i, j+4) + VGET(vec, d+4));
      VSET(vec, d+3, MGET(mat, i+1, j+4) + VGET(vec, d+3));
      VSET(vec, d+2, MGET(mat, i+2, j+4) + VGET(vec, d+2));
      VSET(vec, d+1, MGET(mat, i+3, j+4) + VGET(vec, d+1));
      VSET(vec, d, MGET(mat, i+4, j+4) + VGET(vec, d));
      VSET(vec, d-1, MGET(mat, i+4, j+3) + VGET(vec, d-1));
      VSET(vec, d-2, MGET(mat, i+4, j+2) + VGET(vec, d-2));
      VSET(vec, d-3, MGET(mat, i+4, j+1) + VGET(vec, d-3));
      VSET(vec, d-4, MGET(mat, i+4, j) + VGET(vec, d-4));}
*/
      // 1 + 3 + 5 + 7 = 16 cells = 4 by 4 matrix

    // Cleanup loop for columns
    for (; j < cols; j++, d++) {
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      VSET(vec, d-1, MGET(mat, i+1, j) + VGET(vec, d-1));
      VSET(vec, d-2, MGET(mat, i+2, j) + VGET(vec, d-2));
      VSET(vec, d-3, MGET(mat, i+3, j) + VGET(vec, d-3));
      /*
      VSET(vec, d-4, MGET(mat, i+4, j) + VGET(vec, d-4));*/}
  }

  // Cleanup loop for rows
  for (; i < rows; i++) {
    int d = rows-i-1, j;
    for (j = 0; j < cols-4; j+=4, d+=4){
      VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));
      VSET(vec, d+1, MGET(mat, i, j+1) + VGET(vec, d+1));
      VSET(vec, d+2, MGET(mat, i, j+2) + VGET(vec, d+2));
      VSET(vec, d+3, MGET(mat, i, j+3) + VGET(vec, d+3));
      /*VSET(vec, d+4, MGET(mat, i, j+4) + VGET(vec, d+4));*/
    }

    // Cleanup loop for columns
    for (; j < cols; j++, d++) {VSET(vec, d, MGET(mat, i, j) + VGET(vec, d));}
  }
  return 0;
}

int sumdiag_OPTM(matrix_t mat, vector_t vec) {
  // call your preferred version of the function
  return sumdiag_VER8(mat, vec);
}
