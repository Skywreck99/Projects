
public class HashMap<K,V> implements Map<K,V> {
    private Entry<K,V>[] strTable;
    private int size = 0;

    public HashMap(int buckets) {
        try {
            if (buckets < 1) {
                throw new IllegalArgumentException("Size must be greater than 0");
            } else {
                strTable = new Entry[buckets];
            }
        } catch (Exception e) {
            e.toString();
        }
    }
    public HashMap() {
        strTable = new Entry[64];
    }
    // This method removes all mappings from the Map.
    // Should be more efficient that calling remove() on every element.
    public void clear() {
        strTable = new Entry[64];
        size = 0;
    }

    // This method returns true if the Map contains a mapping for the specified key,
    // and false otherwise.
    public boolean containsKey(K key) {
        Entry<K,V> temp = strTable[hash(key)];
        if (temp == null) return false;

        while (temp != null) {
            if (temp.getKey() == null || temp.getKey().equals(key)) return true; else temp = temp.getNext();
        }
        return false;
    }

    // This method returns true if the Map contains a mapping for the specified value,
    // and false otherwise.
    public boolean containsValue(V value) {
        for (int i = 0; i < strTable.length; i++) {
            Entry<K, V> temp = strTable[i];

            while (temp != null) {
                if (temp.getValue() == value) return true; else temp = temp.getNext();
            }
        }
        return false;
    }

    // This method returns the value to which the specified key is mapped.
    // If the Map does not contain the specified key, the method instead returns null.
    public V get(K key) {
        Entry<K,V> temp = strTable[hash(key)];
        while (temp != null) {
            if (key == temp.getKey()) return temp.getValue(); else temp = temp.getNext();
        }
        return null;
    }

    // This method returns true if the Map contains no key-value mappings,
    //and false otherwise.
    public boolean isEmpty() {
        if (size() == 0) return true; else return false;
    }

    // This method associates the specified key with the specified value in the Map
    // and returns the newly associated value,
    // if the specified key is not already associated with a non-null value.
    // If the specified key is already associated with a non-null value,
    // the association is left unchanged, and the current value is returned instead.
    public V put(K key, V value) {
        // goes to the index of the key based on the output of its hash function
        Entry<K,V> temp = strTable[hash(key)];

        while (temp != null) {
            if ((temp.getKey() == null && key == null) || (temp.getKey() != null && temp.getKey().equals(key))) {
                // returns the new value if added successfully
                if (temp.getValue() == null) {
                    temp.setValue(value);
                    return value;
                // otherwise return the current value instead
                } else {
                    return temp.getValue();
                }
            } else {
                temp = temp.getNext();
            }
        }
        strTable[hash(key)] = new Entry(key, value, strTable[hash(key)]);
        // counts the size of the hashtable
        size++;
        return value;
    }

    // This method removes and returns the mapping for the specified key in the Map
    // if it is present, and returns null otherwise.
    public V remove(K key) {

        Entry<K,V> prev = strTable[hash(key)];

        // when the given key is not on the map
        if (prev == null) return null;

        Entry<K, V> temp = prev.getNext();
        V val;

        // When removing at the very front of the strTable[hash(key)]
        if (prev.getKey() == null || prev.getKey().equals(key)) {
            // checks is there are no entries connected to it, if there aren't, then set the slot to null
            if (temp == null) {
                val = prev.getValue();
                strTable[hash(key)] = null;
                size--;
                return val;
            // If there are entries connected to it, then connect the remaining entries to the slot
            } else {
                val = prev.getValue();
                strTable[hash(key)] = prev.getNext();
                size--;
                return val;
            }
        }

        // When removing at the middle or at the end of the connected entries
        while (temp != null) {
            if (temp.getKey() == null || temp.getKey().equals(key)) {
                // checks if the current entry is the last entry, if it is, then set the previous entry to null
                if (temp.getNext() == null) {
                    val = temp.getValue();
                    prev.setNext(null);
                    size--;
                    return val;
                // if the current entry is at the middle of the connected entries, then set the previous entry to be the rest of the connected entries of the current entry
                } else {
                    val = temp.getValue();
                    prev.setNext(temp.getNext());
                    size--;
                    return val;
                }
            }
            prev = temp;
            temp = temp.getNext();
        }
        return null;
    }

    // This method replaces and returns the mapping for the specified key only if it is currently mapped to some value, and returns null otherwise.
    public V replace(K key, V value) {
        Entry<K,V> temp = strTable[hash(key)];
        V val = null;
        while (temp != null) {
            if (temp.getKey() == null || temp.getKey().equals(key)) {
                val = temp.getValue();
                temp.setValue(value);
                break;
            } else {
                temp = temp.getNext();
            }
        }
        return val;
    }

    // This method returns the number of key-value mappings in the Map.
    public int size() {
        return size;
    }

    // displays the hashtable
    public void display() {
        int j = size();

        System.out.print("{");
        if (isEmpty()) System.out.println("}");

        for (int i = 0; i < strTable.length; i++) {
            Entry temp = strTable[i];

            // Prevents the display to have a trailing comma
            while (temp != null) {
                if (j == 1) {
                    System.out.println(temp.getKey() + ": " + temp.getValue() + "}");
                    TextScan.num++;
                    break;
                } else {
                    System.out.print(temp.getKey() + ": " + temp.getValue() + ", ");
                    TextScan.num++;
                    j--;
                }
                temp = temp.getNext();
            }
        }
    }

    // This method returns an int, determining which “bucket” (index in the array) an Entry should be placed into
    private int hash(K key) {

        // .chars() converts a string to be a stream of ints then reduce it manually
        // .reduce(i, a) reduces the elements inside the stream
        // i is the Identity, where it stores the initial value and the default result when the stream is empty
        // a is the accumulator, where it stores the partial sum and the next element in the stream
        if (key == null) return 0; else return Math.abs(key.toString().chars().reduce(0, Integer::sum)) % strTable.length;
    }
    public void showHashtable() {
        for (int i = 0; i < strTable.length; i++) {
            Entry temp = strTable[i];
            System.out.print(i + "[]" + " {");
            while (temp != null) {
                if (temp.getNext() != null) {
                    System.out.print(temp.getKey() + ": " + temp.getValue() + ", ");
                } else {
                    System.out.print(temp.getKey() + ": " + temp.getValue());
                }
                temp = temp.getNext();
            }
            System.out.println("}");
        }
    }
/*
    public boolean checkDuplicates() {
        for(int i = 0; i < strTable.length; i++) {
            Entry temp = strTable[i];
            while (temp != null) {
                if (temp.)
            }
        }
    }

 */

    public static void main (String[] args) {
        HashMap<String, Integer> ht = new HashMap<>();
        ht.put("one", 1);
        ht.put("two", 2);
        ht.put("three", 3);
        ht.put("four", 4);
        ht.put("five", 5);
        ht.put(null, 8);

        //System.out.println(ht.put(null, 3));
        //System.out.println(ht.put("one", 3));
        ht.display();
        ht.replace(null, 0);

        // System.out.println(ht.containsKey("noe"));
        System.out.println(ht.containsKey(null));     //  true
        System.out.println(ht.containsKey("one"));    //  true
        System.out.println(ht.containsKey("two"));    //  true
        System.out.println(ht.containsKey("three"));  //  true
        System.out.println(ht.containsKey("four"));   //  true
        System.out.println(ht.containsKey("five"));   //  true
        System.out.println(ht.containsKey("zilch"));  //  false

        //System.out.println(ht.containsValue(10));
        System.out.println(ht.remove(null));
        //System.out.println(ht.hash("five"));
        //ht.clear();
        //ht.display();


        System.out.println("hashkey of jordyn: " + "jordyn".chars().reduce(0, Integer::sum));

        ht.showHashtable();
    }
}