#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "treemap.h"

int main(int argc, char *argv[]){

  int echo = 0;                                // controls echoing, 0: echo off, 1: echo on
  if(argc > 1 && strcmp("-echo",argv[1])==0) { // turn echoing on via -echo command line option
    echo=1;
  }

  printf("TreeMap Editor\n");
  printf("Commands:\n");
  printf("  quit:            exit the program\n");
  printf("  print:           shows contents of the tree in reverse sorted order\n");
  printf("  add <key> <val>: inserts the given key/val into the tree, duplicate keys are ignored\n");
  printf("  get <key>:       prints FOUND if the name is in the tree, NOT FOUND otherwise\n");
  printf("  clear:           eliminates all key/vals from the tree\n");
  printf("  preorder:        prints contents of the tree in pre-order which is how it will be saved\n");
  printf("  save <file>:     writes the contents of the tree in pre-order to the given file\n");
  printf("  load <file>:     clears the current tree and loads the one in the given file\n");

  char cmd[128], key[128], val[128], file[128];
  treemap_t tree;
  int success;
  treemap_init(&tree);
  // char *key = malloc(sizeof(char)*strlen(k));
  // char *val = malloc(sizeof(char)*strlen(v));
  // char *file = malloc(sizeof(char)*strlen(f));

  while(1) {
    printf("TM> ");                 // print prompt
    success = fscanf(stdin,"%s",cmd); // read a command
    if(success == EOF){                 // check for end of input
      printf("\n");                   // found end of input
      break;                          // break from loop
    }
    if(strcmp("quit", cmd) == 0){
      printf("quit\n");

      break;
    } else if (strcmp("print", cmd) == 0){
      printf("print\n");
      treemap_print_revorder(&tree);
    } else if (strcmp("add", cmd) == 0){
      fscanf(stdin,"%s",key);
      fscanf(stdin,"%s",val);
      if (echo) {
        printf("add %s %s\n", key, val);
      }
      success = treemap_add(&tree, key, val);
      if (!success) {
        printf("modified existing key\n");
      }

    } else if (strcmp("get", cmd) == 0){
      fscanf(stdin,"%s",key);
      if (echo) {
        printf("get %s\n", key);
      }
      char *result = treemap_get(&tree, key);
      if (result == NULL) {
        printf("NOT FOUND\n");

      } else {
        printf("FOUND: %s\n", result);
      }
    } else if (strcmp("clear", cmd) == 0){
      printf("clear\n");
      treemap_clear(&tree);

    } else if (strcmp("preorder", cmd) == 0){
      printf("preorder\n");

      treemap_print_preorder(&tree);
    } else if (strcmp("save", cmd) == 0){
      fscanf(stdin,"%s",file);
      if (echo) {
        printf("save %s\n",file);
      }
      treemap_save(&tree, file);
    } else if (strcmp("load", cmd) == 0){
      fscanf(stdin,"%s",file);
      if (echo) {
        printf("load %s\n", file);
      }
      success = treemap_load(&tree, file);
      if (!success) {
        printf("load failed\n");
      }
    } else {
      printf("\n");
    }
  }
  treemap_clear(&tree);
  return 0;
}
