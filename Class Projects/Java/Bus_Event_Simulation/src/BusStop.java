
public class BusStop {
	
	private String name;
	private int stopNumber;
	private int  maxQLength = 0;
	private Q1Gen<Rider> thestop = new Q1Gen<Rider>();
	
	public BusStop(String name, int stopNumber) { //Makes the parameters for the bus stops
		this.name = name;
		this.stopNumber = stopNumber;
	}

	public Rider remove() {
		return thestop.remove();
	}
	public void add(Rider r) {
		thestop.add(r);
		// add each passenger
	}
	public Q1Gen<Rider> getQ(){
		return thestop;
	}
	public String getName() {
		return this.name;
	}
	public int getStopNumber() {return stopNumber;}
	public int getMaxQLength() {
		return maxQLength;
	}

	// What is the purpose of this?
	public Rider removeExpressPass() {
		Rider rider = null;
		Q1Gen<Rider> temp = new Q1Gen<Rider>();

		while(thestop.length() != 0) {
			rider = thestop.remove();
			if(rider.getDropoffStop() % 4 == 0 || rider.getDropoffStop() == 1 || rider.getDropoffStop() == 29 || rider.getDropoffStop() == 14 || rider.getDropoffStop() == 15) {
				break;
			} else {
				temp.add(rider);
				rider = null;
			}
		}
		while (temp.length() != 0) {
			thestop.add(temp.remove());
		}
		return rider;
	}
	public void compare(int length) {
		if (maxQLength < length) {
			maxQLength = length;
		}

	}

}
