#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "search.h"

int main(int argc, char *argv[]){
  if(argc < 4){                       // validity conditional
    printf("\nusage: ./search_benchmark <minpow> <maxpow> <repeats> [which]\n");
    printf(" which is a combination of:\n"); // Necessary print statements
    printf("  a : Linear Array Search\n");
    printf("  l : Linked List Search\n");
    printf("  b : Binary Array Search\n");
    printf("  t : Binary Tree Search\n");
    printf("  (default all)\n\n");
    return 1;
  }
  int run_linear_array = 0;                  // Given code
  int run_linear_list = 0;                   // basically booleans to determine
  int run_binary_array = 0;                     // whether functions should be
  int run_binary_tree = 0;                      // turned on or off

  char *algs_string = argv[4];           // 4th is string/char array of commands
  int cur_search_size = atoi(argv[1]);   // extract each of the 4 args
  int max = atoi(argv[2]);               // 1st is size, 2nd is max
  int repetitions = atoi(argv[3]);       // 3rd is # of repetitions

  if(algs_string==NULL) {run_linear_array = 1; run_linear_list = 1; run_binary_array = 1; run_binary_tree = 1; printf("       array"); printf("         linear"); printf("          binary"); printf("            tree\n");}
  else {

      for(int i = 0; i < strlen(algs_string); i++){ // for the length of the string...
        if(algs_string[i] == 'a'){           // if string contains a
          run_linear_array = 1;              // iniitiate it to 1/turn it 'on'
          printf("       array");            // printing for formatting
        } else if(algs_string[i] == 'l'){    // Do this process for all elements
          run_linear_list = 1;
          printf("         linear");
        } else if(algs_string[i] == 'b'){
          run_binary_array = 1;
          printf("          binary");
        } else if(algs_string[i] == 't'){
          run_binary_tree = 1;
          printf("            tree\n");
        }
      }
      printf("\n");
    }

    clock_t start, end;                        // start and end variables for the clock
    while(cur_search_size < max+1){              // while size is less than the max
      int i;                                   // will eventually be a counter
      int Exponent = 1;                        // exponent var: alternative to math.pow()
      for(int j=0; j<cur_search_size; j++){
        Exponent *= 2;                         // Exponent = Exponent * 2
      }
      printf("%10d%10d", Exponent, Exponent*2); // you will print this out for formatting

      if(run_linear_array == 1){             // if the run_linear_array function is on
        i = 0;
        int *arr = make_evens_array(Exponent);  // then you will call make_evens_array


        start = clock();                     // iniitialize the clock for the start time
        while(i<repetitions){                // while i < # of repetitions
          for (int j=0; j<2*Exponent; j++){
            linear_array_search(arr, Exponent, j); // do a linear_array_search
          }
          i++;                               // increment the i counter
        }
        end = clock();                       // end the clock
        double cpu_time_used = ((double) (end-start) / CLOCKS_PER_SEC);
        free(arr);                // above functions computes amount of time taken
        printf("%15e", cpu_time_used); // finally free arr and print computed time
      }


      if(run_linear_list == 1){                 // similar to run_linear_array_search
        i = 0;
        list_t *list = make_evens_list(Exponent); // makes use of a list_t struct
        start = clock();
        while(i < repetitions){
          for (int j=0; j<2*Exponent; j++){
            linkedlist_search(list, Exponent, j);
          }
          i++;
        }
        end = clock();
        double cpu_time_used = ((double) (end-start) / CLOCKS_PER_SEC);
        list_free(list);
        printf("%15e", cpu_time_used);      // print and report time
      }

      if(run_binary_array == 1){                // similar to above 2 functions
        i = 0;
        int *arr = make_evens_array(Exponent);
        start = clock();
        while(i < repetitions){
          for (int j=0; j<2*Exponent; j++){
            binary_array_search(arr, Exponent, j);
          }
          i++;
        }
        end = clock();
        double cpu_time_used = ((double) (end-start) / CLOCKS_PER_SEC);
        free(arr);
        printf("%15e", cpu_time_used);
      }

      if(run_binary_tree == 1){                 // similar to above 3 functions
        i = 0;
        bst_t *tree = make_evens_tree(Exponent);      // calls make_evens_tree function
        start = clock();
        while(i < repetitions){
          for (int j=0; j<2*Exponent; j++){
            binary_tree_search(tree, Exponent, j);
          }
          i++;
        }
        end = clock();
        double cpu_time_used = ((double) (end-start) / CLOCKS_PER_SEC);
        bst_free(tree);
        printf("%15e", cpu_time_used);
      }

    // printf("\n");
    // if(cur_search_size < max){                // if the size is less than max
    //   cur_search_size++;                      // then you increment the size
    //   Exponent *= 2;                          // as well as multiply Exp. by 2
    // }

      cur_search_size++;                        // increments size regardless
      printf("\n");
  }
  return 0;                                   // returns success
}
