
public class CelestialDatabase {
    private List<Star> list;

    public CelestialDatabase(String type) {

        // Implement list as type ArrayList
        if (type.equals("array")) {
            list = new ArrayList<>();

        // Implement list as type LinkedList
        } else if (type.equals("linked")) {
            list = new LinkedList<>();
        }
    }

    public boolean add(Star s) {

        // returns true if added successful; else, return false
        return list.add(s);
    }


    public Star find(String name) {

        // finds the star with teh same name that was passed in
        Star thestar = null;
        for(int i = 0; i < list.size(); i++) {

            // list.get(i) is the star,
            // then we get the name of the star using .getName(),
            // then we use .equals(name) to verify if the star has the same name as the one passed in
            if(list.get(i).getName().equals(name)) {

                // return that star along with its properties if true
                thestar = list.get(i);
                break;
            }
        }
        return thestar;
    }

    public Star findSun() {

        // loop through the list to get the star objects
        for (int i = 0; i < list.size(); i++) {

            // checks if the star is a Sequence
            if (list.get(i) instanceof Sequence) {

                // make the star as a Sequence object to access the methods inside it
                Sequence this_elem = (Sequence) list.get(i);

                // Check if the Sequence Star is a Sun or not
                if (this_elem.isSun()) {

                    // return the first instance of the Sequence Star
                    return list.get(i);
                }
            }
        }

        // return null when no star is a sun
        return null;
    }

    public Star remove(int index) {

        // remove the star from the index that was passed in then return it
        return list.remove(index);
    }

    public Star get(int index) {

        // get the star from the index of the list that was passed in
        return list.get(index);
    }

    public void sort() {

        // sorts from lightest star to heaviest star
        list.sort(true);
    }

    public Star[] getStarsByType(String type) {

        // thesize will be used as the index for Star[] stars
        int thesize = 0;

        // create a new Star[] stars for stars with one type with length list.size() that corresponds to the type that was passed in
        Star[] stars = new Star[list.size()];

        // loop through the list to access star objects
        for (int i = 0; i < list.size(); i++) {

            // if-else block checks the type of the star that corresponds to the type that was passed in
            // use .set() to set the corresponding index of stars (use thesize as the star's index) with the element of the list in current position i
            if (type.equals("sequence")) {
                if (list.get(i) instanceof Sequence) {
                        stars[thesize] = list.set(i, list.get(i));
                        thesize++;
                }
            } else if (type.equals("whitedwarf")) {
                if (list.get(i) instanceof WhiteDwarf) {
                        stars[thesize] = list.set(i, list.get(i));
                        thesize++;
                }
            } else if (type.equals("redgiant")) {
                if (list.get(i) instanceof RedGiant) {
                        stars[thesize] = list.set(i, list.get(i));
                        thesize++;
                }
            }
        }

        // make another Star[] thestars to create a new Star[] with the same elements, but without null
        Star[] thestars = new Star[thesize];
        for (int i = 0; i < thesize; i++) {
            thestars[i] = stars[i];
            System.out.print(thestars[i] + ", ");
        }

        return thestars;

    }

    public Star[] listBlackHoles() {

        // count will be used as the index for Star[] stars
        int count = 0;

        // create a new Star[] stars with length list.size()
        Star[] stars = new Star[list.size()];

        // go through the list using a loop to get the star objects
        for(int i = 0; i < list.size(); i++) {

            // if-else block checks the star object weather is it a Sequence, a RedGiant, and a WhiteDwarf
            // Cast a star object to any type of the Star to access the methods inside it
            // Check if the star object is a black hole or not
            // use .set() to set the corresponding index of stars (use thesize as the star's index) with the element of the list in current position i
            if(list.get(i) instanceof Sequence) {
                Sequence this_elem = (Sequence) list.get(i);
                if(this_elem.isBlackHole()) {
                    stars[count] = list.get(i);
                    count += 1;
                }
            }
            else if(list.get(i) instanceof RedGiant) {
                RedGiant this_elem = (RedGiant) list.get(i);
                if(this_elem.isBlackHole()) {
                    stars[count] = list.get(i);
                    count += 1;
                }
            }

        // checks if count is equal to zero. That means that no star was counted during the proess
        } if (count == 0) {
            return null;

        // make another Star[] thestars to create a new Star[] with the same elements, but without null
        } else {
            Star[] thestars = new Star[count];

            for(int i = 0; i < count; i++) {
                thestars[i] = stars[i];
                System.out.print(thestars[i] + ", ");
            }
            return thestars;
        }
    }

    public Star[] getTopKHeaviestStar(int k) {

        // change the order of the list from heaviest to smallest using the star's masses
        list.sort(false);
        Star[] stars = new Star[k];

        // returns null if there are no stars inside the list
        if (list.size() == 0) {
            return null;

        // returns Star[] stars with length the same as the number of elements inside the list, thus,
        // disregarding the length k when the size of the list is less than k
        } else if (list.size() < k) {
            stars = new Star[list.size()];
            for (int i = 0; i < list.size(); i++) {
                stars[i] = list.get(i);
            }

        // Since the list is already sorted from heaviest to smallest, we can then get star objects from the very front of the list to the index [k - 1]
        } else {
            for (int i = 0; i < k; i++) {
                stars[i] = list.get(i);
            }
        }

        // loop through stars to print the star objects inside it
        for (int j = 0; j < stars.length; j++) {
            System.out.print(stars[j] + ", ");
        }

        return stars;
    }

    public int[] countStars(){

        // make int[] countlist with length 3
        // (index 0 for the number of Sequence Star, index 1 for the number of Red Giant stars, and index 2 for the number of the White Dwarf Stars)
        int[] countlist = new int[3];

        // loop through the list, then count the number of star objects based on their types to their corresponding indices
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) instanceof Sequence) {
                countlist[0] += 1;
            } else if (list.get(i) instanceof RedGiant) {
                countlist[1] += 1;
            } else if (list.get(i) instanceof WhiteDwarf) {
                countlist[2] += 1;
            }
        }

        // loop through stars to print the star objects inside it
        for(int j = 0; j < countlist.length; j++) {
            System.out.print(countlist[j] + ", ");
        }
        return countlist;
    }

    // returns the reference of the list
    public List<Star> getList() {
        return list;
    }

    // make a new oString() intended for the list itself
    public String toString() {
        return list.toString();
    }

    public static void main(String[] args) {
        CelestialDatabase lists = new CelestialDatabase("linked");
        RedGiant red1 = new RedGiant("Sky", 160, 1111);
        Sequence seq1 = new Sequence("Me", 2, 430);
        WhiteDwarf white1 = new WhiteDwarf("Hi", 100, 100);
        RedGiant red2 = new RedGiant("Sky", 16, 24);
        //Sequence seq2 = new Sequence("Me", 2, 430);
        WhiteDwarf white2 = new WhiteDwarf("Hi", 100, 100);
        RedGiant red3 = new RedGiant("Sky", 160, 24);
        Sequence seq3 = new Sequence("Me", 2, 430);
        //WhiteDwarf white3 = new WhiteDwarf("Hi", 100, 100);
        RedGiant red4 = new RedGiant("Sky", 50, 24);
        Sequence seq4 = new Sequence("Me", 2, 430);
        WhiteDwarf white4 = new WhiteDwarf("Hi", 100, 100);

        lists.add(red1);
        lists.add(seq1);
        lists.add(white1);
        lists.add(red2);
        //lists.add(seq2);
        lists.add(white2);
        lists.add(red3);
        lists.add(seq3);
        //lists.add(white3);
        lists.add(red4);
        lists.add(seq4);
        lists.add(white4);

        System.out.println(lists.toString());
        System.out.println();
        //System.out.println(lists.find("Me"));
        System.out.println(lists.findSun());
        System.out.println();
        //System.out.println(lists.listBlackHoles());
        System.out.println(lists.countStars());
        System.out.println();
        System.out.println(lists.getTopKHeaviestStar(13));
        lists.sort();
        System.out.println();
        System.out.println(lists.toString());
        System.out.println();
        System.out.println(lists.listBlackHoles());
        System.out.println();
        System.out.println(lists.getStarsByType("redgiant"));
        System.out.println();
    }
}
