#include <stdio.h>
#include <stdlib.h>

// Prints a graph of the values in data which is an array of integers
// that has len elements. The max_height argument is the height in
// character rows that the maximum number data[] should be
void print_graph(int *data, int len, int max_height) {

  // Initialize variables for graphing
  int min, max, y_coor, *ptr;
  min = max = *data;

  // Finding the max and min in the array
  for (int i = 1; i < len; i++) {
    if (min > data[i]) {
      min = data[i];
    }
    if (max < data[i]) {
      max = data[i];
    }
  }

  // Print the variables needed to make the graph
  printf("length: %d\n", len);
  printf("min: %d\n", min);
  printf("max: %d\n", max);
  printf("range: %d\n", max-min);
  printf("max_height: %d\n", max_height);
  printf("units_per_height: %.2f\n", (double) (max-min)/max_height);

  // Printing the top part of the graph
  printf("     ");
  for (int i = 0; i < len; i++) {
    if (i % 5 == 0) {
      printf("+");
    } else {
      printf("-");
    }
  }
  printf("\n");

  // Printing the range of the graph
  for (int i = max_height; i >= 0; i--) {
    y_coor = (int) min + i * ((double) (max-min)/max_height);
    printf("%3d |", y_coor);

    // Printing the body of the graph
    for(int j = 0; j < len; j++) {
      //printf("%d\n", *data+j);
      ptr = &data[j];
      if (*ptr >= y_coor) {
        printf("X");
      } else {
        printf(" ");
      }
    }
    printf("\n");
  }

  // Printing the bottom part of the graph
  printf("     ");
  for (int i = 0; i < len; i++) {
    if (i % 5 == 0) {
      printf("+");
    } else {
      printf("-");
    }
  }
  printf("\n     ");

  // Printing the domain of the graph
  for (int i = 0; i < len; i++) {
    if (i % 5 == 0) {
      printf("%-5d", i);
    }
  }
  printf("\n");

}
