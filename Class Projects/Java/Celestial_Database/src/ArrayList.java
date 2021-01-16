
public class ArrayList<T extends Comparable<T>> implements List<T>{
   int len;
   T[] a;

   public ArrayList() {
      len = 2;
      a = (T[]) new Comparable[len];
   }

   /*
    * Add an element to end of the list. If element is null,
    * it will NOT add it and return false.  Otherwise, it
    * will add it and return true.
    */
   public boolean add(T element) {

      // Condition if the element is null
      if (element == null) {
         return false;
      }

      // Condition if the array is full
      else if (size() == a.length) {
         T[] b = (T[]) new Comparable[a.length*2];

         // put everything in array a to array b
         int j = a.length;
         for (int i = 0; i < a.length; i++) {
            b[i] = a[i];
         }
         a = b;

         a[j] = element;
         len = a.length;
         return true;

      // Condition if none of the conditionals above worked
      } else {
         for (int i = 0; i < a.length; i++) {
            if (a[i] == null) {
               a[i] = element;
               break;
            }
         }
         return true;
      }
   }

   /*
    *  Add an element at specific index. This method should
    * also shift the element currently at that position (if
    * any) and any subsequent elements to the right (adds
    * one to their indices). If element is null, or if index
    * index is out-of-bounds (index < 0 or index >= size_of_list), // Why size_of_list instead of the length of the arraylist?
    * it will NOT add it and return false. Otherwise it will
    * add it and return true. See size() for the definition
    * of size of list
    */
   public boolean add(int index, T element) {

      // checks if the index is out of bounds
      if (element == null || index < 0 || index >= size()) {
         return false;

      // shifts the elements to the right first until it reaches the index where the element should be inserted in
      } else {
         for (int i = a.length-1; i > index; i--) {
            a[i] = a[i-1];
         }

         // Once found, then add the element to the specific index
         a[index] = element;
         return true;
      }
   }

   /*
    * Remove all elements from the list.
    */
   public void clear() {
      a = (T[]) new Comparable[2];
   }

   /*
    * Return true if element is in the list and false
    * otherwise.
    */
   public boolean contains(T element) {
      for (int i = 0; i < size(); i++) {
         if (a[i] == element) {
            return true;
         }
      }
      return false;
   }

   /*
    *  Return the element at given index. If index is
    * out-of-bounds, it will return null.
    */
   public T get(int index) {
      if (index < 0 || index >= size()) {
         return null;
      } else {
         return a[index];
      }
   }

   /*
    * Return the first index of element in the list. If element
    * is null or not found in the list, return -1.
    */
   public int indexOf(T element) {

      if (element == null) {
         return -1;
      } else {
         int j = -1;
         int i = 0;
         while (i < size()) {
            if (a[i] == element) {
               j = i;
               break;
            }
            i++;
         }
         return j;
      }
   }

   /*
    * Return true if the list is empty and false otherwise.
    */

   public boolean isEmpty() {
      if (size() == 0) {
         return true;
      } else {
         return false;
      }
   }

   /*
    * Same as indexOf(), except it will return the last index
    * of element.
    */

   public int lastIndexOf(T element) {
      if (element == null) {
         return -1;
      } else {

         // create variable j to track the last index where the final element is located (must initialize -1 because 0 is an index)
         // create variable i to stop the loop
         //int k = -1;
         int j = -1;
         int i = 0;
         while (i < size()) {
            if (a[i] == element) {
               j = i;
            }
            i++;
         }
        return j;
      }

   }

   /*
    * Replace the element at index with element and return the
    * element that was previously at index. If index is
    * out-of-bounds or element is null, do nothing with element
    * and return null.
    */
   public T set(int index, T element) {
      int i = 0;
      if (index < 0 || index >= size() || element == null) {
         return null;
      } else {
         T j;
         j = a[index];
         a[index] = element;
         return j;
      }
   }

   /*
    * Return the number of elements in the list. For example, if
    * 4 elements added to a list, size will return 4, while the
    * last index in the list will be 3.
    */
   public int size() {
      int count = 0;
      for (int i = 0; i < a.length; i++) {
         if (a[i] != null) {
            count++;
         }
      }
      return count;
   }

   /*
    * Sort the elements of the list. If order is true, sort the
    * list in increasing (alphabeticaly) order. If order is
    * false, sort the list in decreasing (reverse alphabetical)
    * order.
    *
    * Hint: Since T extends Comparable, you will find it useful
    * to use the public int compareTo(T o) method.
	*/
   public void sort(boolean order) {
      int i, j, minIndex;
      T temp;

      if (!order) {

         // do this loop if the order is false, which means that the list will be sorted from biggest to smallest
         for (i = 0; i < size() - 1; i++) {
            minIndex = i;
            for (j = i+1; j < size(); j++) {
               if (a[j].compareTo(a[minIndex]) > 0) {
                  minIndex = j;
               }
            }

            // swap the two elements after going through the loop
            temp = a[minIndex];
            a[minIndex] = a[i];
            a[i] = temp;
         }

      // do this loop if the order is true, which means that the list will be sorted from smallest to biggest
      } else {
         for (i = 0; i < size() - 1; i++) {
            minIndex = i;
            for (j = i+1; j < size(); j++) {

               if (a[j].compareTo(a[minIndex]) < 0) {
                  minIndex = j;
               }
            }

            // swap the two elements after going through the loop
            temp = a[minIndex];
            a[minIndex] = a[i];
            a[i] = temp;
         }
      }
   }

   /*
    * Remove the first instance of element from the list. This
    * method should also shifts any subsequent elements to the
    * left (subtracts one from their indices). If successful,
    * return true. If element is not found in the list, return
    * false.
	*/
   public boolean remove(T element) {
      if (element == null) {
         return false;

      } else {
         int index = -1;
         for (int i = 0; i < a.length; i++) {
            if (a[i] == element) {
               index = i;
               a[i] = null;
               break;
            }
         }

         if (index == -1) {
            return false;
         } else {
            for (int i = index; i < a.length; i++) {
               if (i + 1 < a.length) {
                  a[i] = a[i + 1];
               } else {
                   a[i] = null;
               }
            }
            return true;
         }
      }
   }

   /*
    * Remove whatever is at index in the list and return
    * it. If index is out-of-bounds, return null. Shift the
    * indices as in the other remove.
    */
   public T remove(int index) {

      if (index < 0 || index >= size()) {
         return null;

      } else {
         T track = a[index];
         a[index] = null;
         for (int i = index; i < a.length; i++) {
            if (i + 1 < a.length) {
               a[i] = a[i + 1];
            } else {
               a[i] = null;
            }
         }
         return track;
      }
   }
   
   public String toString() {
      String ArrayList = "";
      for (int i = 0; i < size(); i++) {
         ArrayList += a[i].toString() + "\n";
      }
      return ArrayList;
   }

   public static void main(String[] args) {
      ArrayList<String> lists = new ArrayList<>();
/*
      lists.add(5);
      lists.add(8);
      lists.add(2);
      lists.add(2);
      lists.add(6);
      lists.add(5);
      lists.add(3);
      System.out.println("list: " + lists.toString());

      System.out.println("lastIndexOf : " + lists.lastIndexOf(10));
      System.out.println("isEmpty: " + lists.isEmpty());
      System.out.println("indexOf: " + lists.indexOf(2));
      System.out.println("set the list: " + lists.set(6,11));
      System.out.println("current list: " + lists.toString());
      System.out.println("current size: " + lists.size());

      lists.sort(false);
      System.out.println("lists in descending order: " + lists.toString());

      System.out.println("remove T element: " + lists.remove((Integer)6));
      System.out.println("remove element in index: " + lists.remove(5));
      System.out.println("current list: " + lists.toString());
      System.out.println(lists.remove(4));
      System.out.println("current list after removing element from 4: " + lists.toString());

      lists.clear();
      System.out.println("cleared: " + lists.toString());
      System.out.println("isEmpty: " + lists.isEmpty());

 */
      lists.add("me");
      lists.add("jordyn");
      lists.add("carl");
      lists.add("chris");
      lists.add("hi");
      lists.add("jordyn");
      lists.add("skylan");
      lists.add("jordyn");

      System.out.println("list: " + lists.toString());

      System.out.println("lastIndexOf : " + lists.lastIndexOf("jordyn"));
      System.out.println("isEmpty: " + lists.isEmpty());
      System.out.println("indexOf: " + lists.indexOf("jordyn"));
      System.out.println("set the list: " + lists.set(4, "thomas"));
      System.out.println("current list: " + lists.toString());
      System.out.println("current size: " + lists.size());

      lists.sort(true);
      System.out.println("lists in descending order: " + lists.toString());

      System.out.println("remove T element: " + lists.remove("carl"));
      System.out.println("remove element in index: " + lists.remove(5));
      System.out.println("current list: " + lists.toString());


      System.out.println(lists.remove(4));
      System.out.println("current list after removing element from 4: " + lists.toString());

      lists.clear();
      System.out.println("cleared: " + lists.toString());
      System.out.println("isEmpty: " + lists.isEmpty());
   }

}  // End of interface definition.