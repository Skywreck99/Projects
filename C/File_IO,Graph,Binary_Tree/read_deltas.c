#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include "deltas.h"


// Reads integers in text delta format from the file named by fname
// and returns an array of them. The first integer in the file gives
// the starting point and subsequent integers are changes from the
// previous total.
int *read_text_deltas(char *fname, int *len) {

  // Opens the file with fopen()
  FILE *fin = fopen(fname, "r");

  // checks if fin cannot be opened
  if (fin == NULL) {
    *len = -1;
    return NULL;
  }

  int num;
  int first, *last;
  int result;
  int size = 0;

  // Scans through the file's contents using fscanf() and counting how many text integers exist in it
  while(1) {
    result = fscanf(fin, "%d", &num);

    // checks if the loop reached the end of file
    if (result == EOF) {
      break;
    }
    size++;
  }

  // If there are no integers in the file, sets len to -1 and return NULL
  if (size == 0) {
    fclose(fin);
    *len = -1;
    return NULL;
  }

  // Then allocates an array of appropriate size using malloc()
  int *numArray = malloc(size*sizeof(int));

  // Uses rewind() to go back to the beginning of the file then reads integers into the allocated array
  rewind(fin);

  // The argument len is a pointer to an integer which is set to the length of the array that is allocated by the function
  *len = size;

  // Scans the first element and assign it to &numArray[0]
  fscanf(fin, "%d", &numArray[0]);

  // first will be used for calculation
  first = *numArray;
  num = 1;

  // does the calculation until it reaches the end of file
  while(1){
    result = fscanf(fin, "%d", &numArray[num]);
    if (result == EOF) {
      break;
    }
    last = &numArray[num];
    int data = *last + first;
    *last = data;
    first = *last;
    num++;
  }

  // Closes the file after reading all ints
  fclose(fin);

  // Returns a pointer to the allocated array
  return numArray;
}

// Reads integers in binary delta format from the file named by fname
// and returns an array of them.  The first integer in the file gives
// the starting point and subsequent integers are changes from the
// previous total.
//
int *read_int_deltas(char *fname, int *len) {

  // Opens the file with fopen()
  FILE *fin1 = fopen(fname, "r");

  // Checks if the file cannot be opened
  if (fin1 == NULL) {
    *len = -1;
    return NULL;
  }

  // Integers in the file are in binary format so the size of the file
  // in bytes indicates the quantity of integers. Uses the stat() system
  // call to determine the file size in bytes which then allows an array
  // of appropriate size to be allocated. DOES NOT scan through the file
  // to count its size as this is not needed.

  // struct to hold
  struct stat sb;

  // unix system call to determine size of named file
  int out = stat(fname, &sb);

  // if something went wrong or bail if file is too small
  if(out == -1 || sb.st_size < sizeof(int)) {
    *len = -1;
    fclose(fin1);
    return NULL;
  }

  // size of file in bytes
  int total_bytes = sb.st_size;
  int first1;
  int *last1;

  // Each integer is 4 bytes. This will calculate how many elements are inside the file
  // The argument len is a pointer to an integer which is set to the length of the array that is allocated by the function
  *len = total_bytes/4;

  // allocate enough memory for the array
  int *numArray1 = malloc((total_bytes/4)*sizeof(int));

  // read the file using fread() since the file is in int format
  fread(&numArray1[0], sizeof(int), 1, fin1);

  // Does the calculation
  first1 = *numArray1;
  for (int i = 1; i < *len; i++) {
    fread(numArray1+i, sizeof(int), 1, fin1);
    last1 = &numArray1[i];
    int data1 = *last1 + first1;
    *last1 = data1;
    first1 = *last1;
  }

  // closes the file every time when opened
  fclose(fin1);

  // returns a pointer to the allocated array
  return numArray1;

}
