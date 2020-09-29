
public class LinkedList<T extends Comparable<T>> implements List<T> {

	private NGen<T> head;

	public LinkedList() {
		head = null;
	}

	/*
	 * Add an element to end of the list. If element is null,
	 * it will NOT add it and return false.  Otherwise, it
	 * will add it and return true.
	 */
	public boolean add(T element) {
		NGen<T> thehead = head;

		if(thehead == null) {   //Checks to  see if thehead is null, then creates a new NGen node.
			head = new NGen<T>(element,null);
			return true;
		}
		else {

			while(thehead.getNext() != null) { //Checks to see if thehead.getNext() doesn't equal null.
				//Then sets the node to the element that was passed in.

				thehead = thehead.getNext();

			}
			thehead.setNext(new NGen<T>(element,null));
			return true;
		}

	}


	/*
	 *  Add an element at specific index. This method should
	 * also shift the element currently at that position (if
	 * any) and any subsequent elements to the right (adds
	 * one to their indices). If element is null, or if index
	 * index is out-of-bounds (index < 0 or index >= size_of_list),
	 * it will NOT add it and return false. Otherwise it will
	 * add it and return true. See size() for the definition
	 * of size of list
	 */
	public boolean add(int index, T element) {

		NGen<T> thehead = head;

		if (thehead == null) {   //Checks to  see if thehead is null, then creates a new NGen node.
			head = new NGen<T>(element,null);
			return true;
		}
		else if(index < 0 || index >= size()) {  // Checks to see if the index passed in was out of range.
			return false;
		}

		else {
			NGen<T> runner;
			NGen<T> previous;
			runner = thehead.getNext();
			previous = thehead;
			int currentindex = 0;

			while(runner != null && currentindex < index) { //Checks to see if thehead doesn't equal null.
				//Also checks to see if the index is in range.
				currentindex++;
				previous = runner;
				runner = runner.getNext();
			}
			if(runner == null) {
				return false;
			}
			else {
				previous.setNext(new NGen<T>(element,runner));   //Then sets the node to the element that was passed in at the certain index.
				return true;
			}

		}
	}


	/*
	 * Remove all elements from the list.
	 */
	public void clear() { //Sets the head to null.

		head = null;

	}

	/*
	 * Return true if element is in the list and false
	 * otherwise.
	 */
	public boolean contains(T element) {
		NGen<T> thehead = head;

		if(thehead == null) {
			return false;
		}
		else {

			while(thehead.getNext() != null ) { //Checks to see if thehead doesn't equal null.
				//If it's not null return true because the element is in the list then.
				thehead = thehead.getNext();
				return true;
			}

			return false;
		}

	}

	/*
	 *  Return the element at given index. If index is
	 * out-of-bounds, it will return null.
	 */
	public T get(int index) {
		NGen<T> thehead = head;

		if(index < 0 || index >= size()) {  // Checks to see if the index passed in was out of range.
			return null;
		}
		else {

			int newindex = 0;

			while(thehead != null && newindex < index) {//Checks to see if thehead doesn't equal null.
				//Also checks to see if the index is in range.
				thehead = thehead.getNext();
				newindex++;

			}
			if(index == newindex) { //If index is equal to newindex then it will return the element in that index.
				return thehead.getData();
			}

		}
		return null;

	}





	/*
	 * Return the first index of element in the list. If element
	 * is null or not found in the list, return -1.
	 */
	public int indexOf(T element) {
		NGen<T> thehead = head;

		if(thehead == null) {
			return -1;
		}

		else {
			int newindex = 0;

			while(thehead != null) {
				if(thehead.getData().equals(element)){ //Checks to see if the thehead equals the element passed in.
					return newindex;  //Then returns the first index found for that element.
				}
				thehead = thehead.getNext();
				newindex++;
			}


		}
		return -1;
	}




	/*
	 * Return true if the list is empty and false otherwise.
	 */
	public boolean isEmpty() {


		if(size() == 0) {  // Checks to see if the size is equal to zero which means the list is empty.
			return true;
		}
		else {
			return false;
		}

	}

	/*
	 * Same as indexOf(), except it will return the last index
	 * of element.
	 */
	public int lastIndexOf(T element) {
		NGen<T> thehead = head;
		int sindex = -1;

		if(thehead == null) {
			return -1;
		}

		else {
			int lastindex = 0;

			while(thehead != null) {   //Checks to see if thehead doesn't equal null.
				if(thehead.getData().equals(element)){ //Checks to see if the thehead equals the element passed in.
					sindex = lastindex;  //Sets sindex equal to the last index of the element.
				}

				thehead = thehead.getNext();
				lastindex++;
			}


		}

		return sindex;
	}



	/*
	 * Replace the element at index with element and return the
	 * element that was previously at index. If index is
	 * out-of-bounds or element is null, do nothing with element
	 * and return null.
	 */
	public T set(int index, T element) {
		NGen<T> thehead = head;
		T oldelement;

		if(index < 0 || index >= size()) { // Checks to see if the index passed in was out of range.
			return null;
		}
		else if(thehead == null) {
			return null;
		}
		else {
			int newindex = 0;

			while(thehead!= null && newindex<index) {//Checks to see if thehead doesn't equal null.
				//Also checks to see if the index is in range.
				thehead = thehead.getNext();
				newindex++;
			}
			if(newindex == index) {
				oldelement = thehead.getData(); //Keeps thehead old value before it gets set so it can be returned.
				thehead.setData(element); //Sets thehead to the new element.
				return oldelement;
			}

		} return null;

	}

	/*
	 * Return the number of elements in the list. For example, if
	 * 4 elements added to a list, size will return 4, while the
	 * last index in the list will be 3.
	 */
	public int size() {  //Counts the number of elements in the list by checking to see if they don't null then adding one to the count each time.
		int count = 0;
		NGen<T> thehead = head;

		while(thehead!= null) {

			count++;
			thehead = thehead.getNext();

		}return count;


	}

	/*
	 * Sort the elements of the list. If order is true, sort the
	 * list in increasing (alphabetically) order. If order is
	 * false, sort the list in decreasing (reverse alphabetical)
	 * order.
	 *
	 * Hint: Since T extends Comparable, you will find it useful
	 * to use the public int compareTo(T o) method.
	 */
	public void sort(boolean order) {
		//Sets up all the variables that are used for the sort.
		NGen<T> thehead = head;
		NGen<T> runner,minData;
		runner = thehead.getNext();
		while(thehead.getNext()!=null) {
			runner = thehead.getNext();
			minData = thehead;
			while(runner!=null) {
				if(runner.getData().compareTo(minData.getData()) < 0 && order) { //Sorts from least to greatest because order is true.
					minData = runner;

				}
				else if(runner.getData().compareTo(minData.getData()) > 0 && !order) { //Sorts from biggest to smallest because order is false.
					minData = runner;

				}
				runner = runner.getNext();

			}
			//This is where the swapping takes place.
			T temps = minData.getData(); //Makes temps of type T equal to minData
			minData.setData(thehead.getData());  //MinData gets set to thehead data
			thehead.setData(temps); //thehead gets set to temps of type T

			thehead = thehead.getNext();
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
		if(head == null) { //Checks to see if the first node is null before starting.
			return false;
		}

		NGen<T> thehead = head.getNext();
		NGen<T> previous = head;

		if(head.getData().equals(element)) { //Special case for if the index is equal to zero.
			head = head.getNext(); //Sets thehead to the next node which skips over the very first node.
			return true;

		}

		else {

			while(thehead != null) {
				if(thehead.getData().equals(element)){ //Checks to see if the thehead equals the element passed in.
					previous.setNext(thehead.getNext()); //Sets previous to the next next node which skips over the one that is removed and connects it to the next link.
					return true;
				}

				thehead = thehead.getNext();
				previous = previous.getNext();

			}


		} return false;


	}

	/*
	 * Remove whatever is at index index in the list and return
	 * it. If index is out-of-bounds, return null. Shift the
	 * indices as in the other remove.
	 */
	public T remove(int index) {

		NGen<T> thehead = head.getNext();
		NGen<T> previous = head;
		T oldindex;


		if(index < 0 || index >= size()) { // Checks to see if the index passed in was out of range.
			return null;
		}
		if(index == 0) {  //Special case for if the index is equal to zero.
			oldindex = previous.getData(); //Keeps thehead old value before it gets set so it can be returned.
			head = head.getNext(); //Sets thehead to the next node which skips over the very first node.
			return oldindex;
		}

		else {
			int newindex = 0;

			while(previous != null) {
				if(index == newindex+1){
					oldindex = thehead.getData(); //Keeps thehead old value before it gets set so it can be returned.
					previous.setNext(thehead.getNext()); //Sets previous to the next next node which skips over the one that is removed and connects it to the next link.
					return oldindex;

				}
				previous = previous.getNext();
				thehead = thehead.getNext();
				newindex++;

			}

			return null;
		}

	}

	public String toString() { //toString method for testing
		String result = "";
		NGen<T> thehead = head;

		while(thehead != null){

			result += thehead.getData().toString();

			if(thehead.getNext() != null){
				result += ", ";
			}
			thehead = thehead.getNext();
		}

		return result;
	}

	public static void main(String [] args){ //Main for testing
		LinkedList<Integer> lists = new LinkedList<Integer>();

		lists.add(5);
		lists.add(8);
		lists.add(3);
		lists.add(2);
		lists.add(6);
		lists.add(5);
		lists.add(3);
		System.out.println(lists.add(1,5));
		System.out.println(lists.add(11,5));
		System.out.println(lists.contains(5));
		System.out.println(lists.get(3));
		System.out.println(lists.get(5));
		System.out.println(lists.indexOf(5));
		System.out.println(lists.isEmpty());
		System.out.println(lists.lastIndexOf(5));
		System.out.println(lists.set(1,11));
		System.out.println(lists.size());
		lists.sort(false);
		System.out.println(lists.remove(1));
		System.out.println(lists.remove((Integer)2));
		//lists.clear();

		System.out.println(lists.toString());


	}

}

