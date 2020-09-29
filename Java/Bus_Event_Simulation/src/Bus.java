
public class Bus {

	
    // make an array of regular bus
    private Rider[] RiderArray = new Rider[50];
    
    // Made a boolean for express vs. regular bus
    // If true express bus, otherwise regular bus
    private boolean busType;
    private int num;
    private Stats thestats;
    
    public Bus(boolean thebus, int number) {
    	busType = thebus;
        this.num = number;
    	thestats = new Stats(thebus, this.num);
    }
    
    public boolean getbusType() {
    	return busType;
    }
    public Stats getThestats() {
		return thestats;
	}

	public boolean addRiders(Rider r) {
        if (!isFull()) { // Checks to see if the bus is full and if not adds the rider to the array.
            int count = 0;
            while (count < RiderArray.length) {
                if (RiderArray[count] == null) {
                     RiderArray[count] = r;
                     break;
                }
                count++;
            }
            return true;
        } else {
            return false;
        }
    }
 
    public Rider[] removeRidersAtStop(int stop) {
        Q1Gen<Rider> staying = new Q1Gen<>();
        Q1Gen<Rider> leaving = new Q1Gen<>();

        // Loops through the RiderArray, separating people who are leaving and staying in separate queues
        for(int i = 0; i < RiderArray.length; i++){

            // Only goes through the seats filled in
            if(RiderArray[i] != null){

                // Checks if the rider is going to the stop passed in
                // Separates leaving riders from staying riders
                if(RiderArray[i].getDropoffStop() == stop) {
                    leaving.add(RiderArray[i]);
                } else {
                    staying.add(RiderArray[i]);
                }
            }
        }

        // checks if no one leaves the bus
        if(leaving.length() == 0) {
            return null;
        }

        // Puts all riders in an array with the same length as the queue
        Rider[] leave = new Rider[leaving.length()];

        // Modify RiderArray
        Rider[] stay = new Rider[RiderArray.length];

        // Convert queues to arrays
        for (int i = 0; i < stay.length; i++) {
            stay[i] = staying.remove();
        }
        for (int i = 0; i < leave.length; i++) {
            leave[i] = leaving.remove();
        }

        RiderArray = stay;
        return leave;
    }

    public boolean isFull() { //Checks to see if the bus is full.
        int count = 0;
        for (int i = 0; i < RiderArray.length; i++) {
        	if(RiderArray[i] != null) {
        		 count++;
        	}
        }
        if (count < RiderArray.length) {
            return false;
        } else {
            return true;
        }
    }

    public int theCount() {
        int count = 0;
        for (int i = 0; i < RiderArray.length; i++) {
            if(RiderArray[i] != null) {
                count++;
            }
        }
        return count;
    }
}


