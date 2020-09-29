#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "search.h"

int main(int argc, char *argv[]){

  if(argc < 4){
    printf("usage: %s <minpow> <maxpow> <repeats> [which]\n",argv[0]);
    printf("which is a combination of:\n");
    printf("a : Linear Array Search\n");
    printf("l : Linked List Search\n");
    printf("b : Binary Array Search\n");
    printf("t : Binary Tree Search\n");
    printf("(default all)\n\n\n");
    return 1;
  }

  int min = atoi(argv[1]); int max = atoi(argv[2]); int rep = atoi(argv[3]); char *command = argv[4];
  int do_linear_array = 0; int do_binary_array = 0; int do_linked_list = 0; int do_binary_tree = 0;

  if(command==NULL) { do_linear_array = 1; do_linked_list = 1; do_binary_array = 1; do_binary_tree = 1;} else {
    for(int i=0; i < strlen(command); i++){
      if(command[i] == 'a'){do_linear_array = 1;}
      else if (command[i] == 'l'){do_linked_list = 1;}
      else if (command[i] == 'b'){do_binary_array = 1;}
      else if (command[i] == 't'){do_binary_tree = 1;}
      else{printf("'%d': invalid command \n", command[i]);}
    }
  }

  for (int len = min; len < max+1; len++) {
    if (len == min){
      printf("%10s", "LENGTH");
      printf("%11s", "SEARCHES");
      if(do_linear_array){printf("%16s"," array");}
      if(do_linked_list){printf("%16s","  list");}
      if(do_binary_array){printf("%16s","binary");}
      if(do_binary_tree){printf("%16s","  tree");}
      printf("\n");
    }

    int curr_size = 1;
    for(int i = 0; i < len; i++){curr_size *= 2;}
    printf("%10d ",curr_size);
    printf("%10d ",curr_size*2);

    if (do_linear_array){
      int *even_array = make_evens_array(curr_size);
      clock_t start_t, end_t;
      start_t = clock();
      for (int loop = 0; loop < rep; loop++) {
        for (int search_int = 0; search_int < curr_size*2; search_int++) {
          linear_array_search(even_array, curr_size, search_int);
        }
      }
      end_t = clock();
      double cpu_time = ((double) (end_t - start_t)) / CLOCKS_PER_SEC;
      printf("%15e ",cpu_time);
      free(even_array);
    }

    if(do_linked_list){
      list_t *even_list = make_evens_list(curr_size);
      clock_t start_t, end_t;
      start_t = clock();
      for (int loop = 0; loop < rep; loop++) {
        for (int search_int = 0; search_int < curr_size*2; search_int++) {
          linkedlist_search(even_list, curr_size, search_int);
        }
      }
      end_t = clock();
      double cpu_time = ((double) (end_t - start_t)) / CLOCKS_PER_SEC;
      printf("%15e ",cpu_time);
      list_free(even_list);
    }

    if (do_binary_array){
      int *even_binary = make_evens_array(curr_size);
      clock_t start_t, end_t;
      start_t = clock();
      for (int loop = 0; loop < rep; loop++) {
        for (int search_int = 0; search_int < curr_size*2; search_int++) {
          binary_array_search(even_binary, curr_size, search_int);
        }
      }
      end_t = clock();
      double cpu_time = ((double) (end_t - start_t)) / CLOCKS_PER_SEC;
      printf("%15e ",cpu_time);
      free(even_binary);
    }

    if (do_binary_tree){
      bst_t *even_tree = make_evens_tree(curr_size);
      clock_t start_t, end_t;
      start_t = clock();
      for (int loop = 0; loop < rep; loop++) {
        for (int search_int = 0; search_int < curr_size*2; search_int++) {
          binary_tree_search(even_tree, curr_size, search_int);
        }
      }
      end_t = clock();
      double cpu_time = ((double) (end_t - start_t)) / CLOCKS_PER_SEC;
      printf("%15e ", cpu_time);
      bst_free(even_tree);
    }
    printf("\n");
  } return 0;
}
