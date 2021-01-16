
public class BusEvent implements Event {

	// What two attributes will we need to keep track of?
	private int curStop;
	private Bus thebus;

	// We should create a constructor that takes in those attributes and sets them.
	public BusEvent(int curStop, Bus thebus) {
		this.curStop = curStop;
		this.thebus = thebus;
	}

	public Bus getThebus() {
		return thebus;
	}

	public void run() {
		// If there aren't any riders to deboard, let's check if we can board
		//   riders. If there's riders who want to board and space on the
		//   bus, then let's board. Keep track of the number of passengers that
		//   board, because we'll once again be adding another BusEvent to allow
		//   for the time that passed, just like for deboarding.

		// If there is no deboarding and no boarding, then it's time for the bus
		//   to move on. We'll add a new BusEvent to the agenda, this time with
		//   the next stop (remember that the bus goes 0->1->2->... <-15), and the
		//   time as the amount of time it takes to travel to the next stop.

		// Check if there are riders is deboarding
		/*
		System.out.println("Current stop at " + this.curStop + ": " + BusSim.stops[this.curStop].getName());
		System.out.println("Bus Type " + this.thebus.getTheNum() + ": " + this.thebus.theCount() + " Currently on board");
		 */
		Rider[] deboard = this.thebus.removeRidersAtStop(this.curStop);
		/*
		if (deboard == null) {
			System.out.println("Deboard: No Riders to deboard");
		} else {
			System.out.println("Deboard: " + deboard.length);
		}

		 */
		int thetime = 0;

		// If they're deboarding create a new BusEvent with the same
		//   stop and bus. The time will be the amount of time it takes to
		//   deboard these riders.
		BusSim.stops[this.curStop].compare(BusSim.stops[this.curStop].getQ().length());

		// tracks the length of he stop and the number of passengers inside the bus
		/*
		System.out.println("Length of the stop: " + BusSim.stops[this.curStop].getQ().length());
		System.out.println("Count of passengers inside the bus: " + this.thebus.theCount());
		 */

		if (!thebus.getbusType()) {
			if (BusSim.stops[this.curStop].getQ().length() != 0 && !this.thebus.isFull()) {
				int count = 0;

				while (BusSim.stops[this.curStop].getQ().length() != 0 && !this.thebus.isFull()) {
					Rider passenger = BusSim.stops[this.curStop].getQ().remove();
					passenger.setPickupTime(BusSim.agenda.getCurrentTime());
					double waitTime = passenger.getPickupTime() - passenger.getStartTime();
					// Gets the total waiting time for calculations later
					Stats.settotalWaitingTime(waitTime);

					// checks if the waittime is the longest waittime ever recorded, if it is, then get the name of the bus stop for statistical purposes
					if(Stats.checkWaitingTime(waitTime)) {
						Stats.setLongestWaitingTime(BusSim.stops[this.curStop].getName());
					}
					this.thebus.addRiders(passenger);

					// counts the total passengers serviced
					Stats.setTotalPassServiced(1);
					count++;
				}

				int deboardtime = 0;
				if (deboard != null) {
					deboardtime = deboard.length * 2;
				}
				thetime += (count * 3) + deboardtime;

				// keeps track of the passengers boarding and deboarding the bus
				/*
				System.out.println("Riders that boarded bus: " + count);
				System.out.println("Total Riders inside the bus: " + this.thebus.theCount());

				for (int i = 0; i < this.thebus.getRiderArray().length; i++) {
					if (this.thebus.getRiderArray()[i] != null) {
						System.out.println("Passenger " + i + ": " + this.thebus.getRiderArray()[i].getDropoffStop());
					}
				}
				System.out.println("\n\n");
				 */

				// Checks to see if the stop is equal to 29 then sets the stop back to one and if the time less than 15.
				if (this.curStop == 29) {
					this.curStop = 0;
				} else {
					this.curStop++;
				}
				if (thetime < 15) {
					thetime = 15;
				}

				// gets the total number of passengers inside the bus for calculations later
				this.thebus.getThestats().settotalBusPass(thebus.theCount());

				// gets the total number of bus stops that the bus went onto
				this.thebus.getThestats().settotalStops(1);

				BusSim.agenda.add(new BusEvent(this.curStop, this.thebus), 240 + thetime);

			} else {
				BusSim.agenda.add(new BusEvent(this.curStop, this.thebus), 255);
			}

		} else {
			if (BusSim.stops[this.curStop].getQ().length() != 0 && !this.thebus.isFull()) {
				int count = 0;
				int skipStop = 1;

				while (BusSim.stops[this.curStop].getQ().length() != 0 && !this.thebus.isFull()) {
					Rider expressRider = BusSim.stops[this.curStop].removeExpressPass();
					if(expressRider == null) {
						break;
					}
					else {
						expressRider.setPickupTime(BusSim.agenda.getCurrentTime());
						double waitTime = expressRider.getPickupTime() - expressRider.getStartTime();

						// Adds all the waiting time for computations later
						Stats.settotalWaitingTime(waitTime);

						// checks if the time is the longest waiting time ever recorded
						Stats.checkWaitingTime(waitTime);

						this.thebus.addRiders(expressRider);
						count++;
						// counts the total passengers serviced
						Stats.setTotalPassServiced(1);
					}

				}
				int deboardtime = 0;
				if (deboard != null) {
					deboardtime = deboard.length * 2;
				}

				thetime += (count * 3) + deboardtime;

				// keeps track of the passengers boarding and deboarding the bus
				/*
				System.out.println("Riders that boarded bus: " + count);
				//System.out.println("Riders that deboarded bus: " + deboardtime/2);
				System.out.println("Total Riders inside the bus: " + this.thebus.theCount());

				for (int i = 0; i < this.thebus.getRiderArray().length; i++) {
					if (this.thebus.getRiderArray()[i] != null) {
						System.out.println("Passenger " + i + ": " + this.thebus.getRiderArray()[i].getDropoffStop());
					}
				}
				System.out.println("\n\n");
				 */

				// Checks to see if the stop is equal to 29 then sets the stop back to one and if the time less than 15.
				if (this.curStop == 29) {
					this.curStop = 0;
				} else if (this.curStop == 0 || this.curStop == 14 || this.curStop == 15 || this.curStop == 28) {
					this.curStop++;

				} else if (this.curStop == 1) {
					skipStop = 3;
					this.curStop += 3;

				} else if (this.curStop == 12) {
					skipStop = 2;
					this.curStop += 2;

				} else {
					skipStop = 4;
					this.curStop += 4;
				}
				// gets the total number of passengers inside the bus for calculations later
				this.thebus.getThestats().settotalBusPass(this.thebus.theCount());

				// gets the total number of bus stops that the bus went onto
				this.thebus.getThestats().settotalStops(1);

				BusSim.agenda.add(new BusEvent(this.curStop, this.thebus), (240 * skipStop) + thetime); // Adds one to the stop each time its looped through

			} else {
				BusSim.agenda.add(new BusEvent(this.curStop, this.thebus), 255);
			}
		}
		// System.out.println("\n\n");




	}


}
