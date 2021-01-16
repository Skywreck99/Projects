#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "deltas.h"


int main(int argc, char *argv[]){
  if(argc < 3){
    printf("usage: %s <format> <filename>\n",argv[0]);
    printf(" <format> is one of\n");
    printf(" text : text ints are in the given filename\n");
    printf(" int  : binary ints are in the given filename\n");
    printf(" 4bit : 4bit binary ints are in the given filename\n");
    return 1;
  }

  // Initialize the arguments needed: the format of the file, the file name, and the length of the graph
  char *format = argv[1];
  char *fname = argv[2];
  char *data_height = argv[3];
  int data_len = -13;

  // Convert the height to an integer
  int height = atoi(data_height);
  int *data_vals = NULL;

  // Reads the text file
  if( strcmp("text", format)==0 ){
    printf("Reading text format\n");
    data_vals = read_text_deltas(fname, &data_len);
  }

  // Reads the int file
  else if( strcmp("int", format)==0 ){
    printf("Reading int format\n");
    data_vals = read_int_deltas(fname, &data_len);
  }
  // else if( strcmp("4bit", format)==0 ){
  //   printf("Reading 4bit binary int format\n");
  //   data_vals = read_4bit_deltas(fname, &data_len);
  // }
  else {
    printf("Unknown format '%s'\n",format);
    return 1;
  }

  // Print the graph using the data that was read from the file
  if (data_vals != NULL){
    print_graph(data_vals, data_len, height);

    // Free the allocated memory of the array
    free(data_vals);

  } else {
    printf("Returned NULL pointer\n");
    printf("Read %d ints\n",data_len);
  }
  
  return 0;

}
