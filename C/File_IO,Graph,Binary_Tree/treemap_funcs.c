#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "treemap.h"

// treemap_funcs.c: Provides a small library of functions that operate on
// binary search trees mapping strings keys to string values.

// Initialize the given tree to have a null root and have size 0.
void treemap_init(treemap_t *tree) {
  tree->root = NULL;
  tree->size = 0;
  return;
}

// Inserts given key/value into a binary search tree. Uses an
// ITERATIVE (loopy) approach to insertion which starts a pointer at
// the root of the tree and changes its location until the correct
// insertion point is located. If the key given already exists in the
// tree, no new node is created; the existing value is changed to the
// parameter 'val' and 0 is returned.  If no node with the given key
// is found, a new node is created and with the given key/val, added
// to the tree, and 1 is returned. Makes use of strcpy() to ease
// copying characters between memory locations.
int treemap_add(treemap_t *tree, char key[], char val[]) {

  // Initialize a pointer to the tree
  node_t *temp_tree =  tree->root;

  // Checks if the root is NULL, if it is, then add a node with the given key and value using the struct node_t then allocate a memory for the node
  if (temp_tree == NULL) {
    node_t *new_node = malloc(sizeof(node_t));

    // Copy the given key and value to the key and value slots of the node
    strcpy(new_node->key, key);
    strcpy(new_node->val, val);

    // Set the left and right part of the node to NULL
    new_node->left = NULL;
    new_node->right = NULL;

    // Make the first node to be the root of the tree
    tree->root = new_node;

    // increase the size fo the tree
    tree->size++;
    
    return 1;

  } else {

    while(1) {

      // When the key already existed, then modify the value of the current key in the tree using the value passed in
      if (strcmp(key, temp_tree->key) == 0) {
        strcpy(temp_tree->val, val);
        return 0;

      // When the key is less than the current key in the tree, make a new node to the left side of the current node by allocating a memory if the left side is NULL
      } else if (strcmp(key, temp_tree->key) < 0) {
        if (temp_tree->left == NULL) {
          node_t *new_node = (node_t *) malloc(sizeof(node_t));

          // Copy the given key and value to the key and value slots of the node
          strcpy(new_node->key, key);
          strcpy(new_node->val, val);

          // Set the left and right part of the node to NULL
          new_node->left = NULL;
          new_node->right = NULL;

          // Set the new node and the left part of the current node
          temp_tree->left = new_node;

          // increase the size fo the tree
          tree->size++;
          return 1;

        // if the left side is not NULL, then go to the left side of the current node
        } else {
          temp_tree = temp_tree->left;
        }

      // Since the left side of the node has already been checked, then go to the right node if it is not NULL. If it is NULL, then create a new node with allocated memory
      } else if (temp_tree->right == NULL) {
        node_t *new_node = (node_t *) malloc(sizeof(node_t));

        // Copy the given key and value to the key and value slots of the node
        strcpy(new_node->key, key);
        strcpy(new_node->val, val);

        // Set the left and right part of the node to NULL
        new_node->left = NULL;
        new_node->right = NULL;

        // Set the new node ad the left part of the current node
        temp_tree->right = new_node;

        // increase the size fo the tree
        tree->size++;
        return 1;

      // if the right side is not NULL, then go to the right side of the current node
      } else {
        temp_tree = temp_tree->right;
      }
    }
  }
  return 0;
}

// Searches the tree for given 'key' and returns its associated
// value. Uses an ITERATIVE (loopy) search approach which starts a
// pointer at the root of the tree and changes it until the search key
// is found or determined not to be in the tree. If a matching key is
// found, returns a pointer to its value. If no matching key is found,
// returns NULL.
char *treemap_get(treemap_t *tree, char key[]) {

  // Initialize a pointer to the tree
  node_t *temp_tree = tree->root;

  // Checks if the root is NULL
  if (temp_tree == NULL) {
    return NULL;
  }

  // Use a loop to find the key in the entire tree using a pointer
  while(1) {

    // When the key is the same as the key of the current node, then return the value of that node
    if (strcmp(temp_tree->key, key) == 0) {
      return temp_tree->val;

    // If the current key is smallee than the key, then go to the right side of the node if it is not NULL, if it is, then return NULL
    } else if (strcmp(temp_tree->key, key) < 0) {
      if (temp_tree->right == NULL) {
        return NULL;

      // Go to the right side of the node if it is not NULL
      } else {
        temp_tree = temp_tree->right;
      }

    // Since the left side of the node has already been checked, then go to the right node if it is not NULL. If it is NULL, then return NULL
    } else if (temp_tree->left == NULL) {
      return NULL;

    // Go to the right node if it is not NULL
    } else {
      temp_tree = temp_tree->left;
    }
  }
}

// Eliminate all nodes in the tree setting its contents empty. Uses recursive node_remove_all() function to free memory for all nodes
void treemap_clear(treemap_t *tree) {

  node_t *temp_tree = tree->root;

  // if the current node of the pointer is NULL, return
  if (temp_tree == NULL) {
    return;
  }

  // Use the recursive node_remove_all() function to free the allocated memory of the nodes
  node_remove_all(temp_tree);

  // set the size to 0 and thre root of the tree to NULL
  tree->size = 0;
  tree->root = NULL;
}

// Recursive helper function which visits all nodes in a tree and
// frees the memory associated with them. This requires a post-order
// traversal: visit left tree, visit right tree, then free the cur
// node
void node_remove_all(node_t *cur) {

  // If the left of the current node is not NULL, then call the node_remove_all() function and pass the left node of the current node to the function
  if (cur->left != NULL) {
    node_remove_all(cur->left);
  }
  // If the right of the current node is not NULL, then call the node_remove_all() function and pass the right node of the current node to the function
  if (cur->right != NULL) {
    node_remove_all(cur->right);
  }

  // Free the current node
  free(cur);
}

// Prints the key/val pairs of the tree in reverse order at differing
// levels of indentation which shows all elements and their structure
// in the tree. Visually the tree can be rotated clockwise to see its
// structure
void treemap_print_revorder(treemap_t *tree) {

    node_t *temp_tree = tree->root;

    // If the root of the tree is NULL, return
    if (temp_tree == NULL) {
      return;
    }

    // Use the node_print_revorder() function to print the tree in reverse order
    node_print_revorder(temp_tree, 0);
}

// Recursive helper function which prints all key/val pairs in the
// tree rooted at node 'cur' in reverse order. Traverses right
// subtree, prints cur node's key/val, then traverses left tree.
// Parameter 'indent' indicates how far to indent (2 spaces per indent
// level)
void node_print_revorder(node_t *cur, int indent) {

  // If the current node is NULL, return
  if (cur == NULL) {
    return;
  }

  // Using the node_print_revorder() fucntion, use the right node of the current node as the first parameter of the function to go to the right node of the current node,
  // then add the indent by 1 since the right node is on the next level
  node_print_revorder(cur->right, indent+1);

  // Print the key and value of the current node with its corresponding indention
  for (int i = 0; i < indent; i++){
    printf("  ");
  }
  printf("%s -> %s\n",cur->key,cur->val);

  // Using the node_print_revorder() function, use the left node of the current node as the first parameter of the function to go to the left node of the current node,
  // then add the indent by 1 since the left node is on the next level
  node_print_revorder(cur->left, indent+1);

}

// Print all the data in the tree in pre-order with indentation
// corresponding to the depth of the tree. Makes use of
// node_write_preorder() for this
void treemap_print_preorder(treemap_t *tree) {

  // If the root of the tree is Null, return
  if (tree->root == NULL) {
    return;
  }

  // set a pointer to the root of the tree
  node_t *temp_tree = tree->root;

  // Use the node_print_revorder() function, print the tree in preorder with their corresponding indentation
  node_write_preorder(temp_tree, NULL, 0);
}

// Saves the tree by opening the named file, writing the tree to it in
// pre-order with node_write_preorder(), then closing the file
void treemap_save(treemap_t *tree, char *fname) {

  // Create a pointere to the root of the tree
  node_t *temp_tree = tree->root;

  // if the root of the tree is NULL, then return;
  if (temp_tree == NULL) {
    return;
  }

  // Open a file to be written
  FILE *out = fopen(fname, "w");

  // Use the node_print_revorder() function to print the tree in the given file in preorder with the corresponding indentation
  node_write_preorder(temp_tree, out, 0);

  // Close the file when done writing
  fclose(out);

}

// Recursive helper function which writes/prints the tree in pre-order
// to the given open file handle. The parameter depth gives how far to
// indent node data, 2 spaces per unit depth. Depth increases by 1 on
// each recursive call. The function prints the cur node data,
// traverses the left tree, then traverses the right tree
void node_write_preorder(node_t *cur, FILE *out, int depth) {

  // If the cureent node is NULL, then return
  if (cur == NULL) {
    return;

  // If the file is not passed in, then print the tree in Preorder with the corresponding indentation
  } else if (out == NULL) {

    // Prints out the indentation per level (two spaces per level)
    for (int i = 0; i < depth; i++){
      printf("  ");
    }

    // Print the keys with their respective values
    printf("%s %s\n",cur->key,cur->val);

    // Go to the left node of the current node using the node_write_preorder() function and add the depth by 1
    node_write_preorder(cur->left, out, depth+1);

    // Go to the right node of the current node using the node_write_preorder() function and add the depth by 1
    node_write_preorder(cur->right, out, depth+1);

  // If file can be opened, write the tree in that file in Preorder
  } else {

    // Initialize the number of spaces needed per tree level
    int space = depth*2;

    // Prints out the spaces on the file
    for (int i = 0; i < space; i++) {
      fprintf(out, "%s", " ");
    }

    // Prints out the key and the value on the file
    fprintf(out, "%s", cur->key);
    fprintf(out, " %s\n", cur->val);

    // Go to the left node of the current node if it is not NULL using the node_write_preorder() function
    if (cur->left != NULL) {
      node_write_preorder(cur->left, out, depth+1);
    }
    // Go to the right node of the current node if it is not NULL using the node_write_preorder() function
    if (cur->right != NULL) {
      node_write_preorder(cur->right, out, depth+1);
    }
  }
}

// Clears the given tree then loads new elements to it from the
// named. Repeated calls to treemap_insert() are used to add strings read
// from the file.  If the tree is stored in pre-order in the file, its
// exact structure will be restored.  Returns 1 if the tree is loaded
// successfully and 0 if opening the named file fails in which case no
// changes are made to the tree.
int treemap_load(treemap_t *tree, char *fname) {

  // Opens the file using fopen()
  FILE *fin = fopen(fname, "r");

  // If the file cannot be opened, then print the error message
  if (fin == NULL){
    printf("ERROR: could not open file '%s'\n", fname);
    return 0;
  }

  // If the file can be opened, then clear the map using treemap_clear() function
  treemap_clear(tree);

  char key[128], val[128];

  // Scan all the elements in the file per line using the fscanf() function to get the key and the value
  while (fscanf(fin, "%s %s", key, val) != EOF) {

    // Add the key and the value to the tree using treemap_add() function
    treemap_add(tree, key, val);
  }

  // Close the file after reading the file
  fclose(fin);
  return 1;
}
