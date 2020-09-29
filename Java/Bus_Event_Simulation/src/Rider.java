
/**
 * This class is a representation of a Passenger.
 *
 * Created by nguy2284 on 4/1/2017.
 */
import java.util.Random;
public class Rider {
	// The stop that the rider boards the bus
	private int pickupstop;
	// The stop that the rider gets off the bus
	private int dropoffstop;

	private double starttime;
	private double picktime;
	private int arrivaltime;

	public int getDropoffStop() { return dropoffstop; }
	public void setStartTime(double time) {
		starttime = time;
	}
	public void setPickupTime(double time) {
		picktime = time;
	}
	public void setArrivalTime(int time) { arrivaltime = time; }
	public double getPickupTime() {return picktime; }
	public double getStartTime() {
		return starttime;
	}

	//Stops for the rider to be generated to.
	int[] stopSelect = {0, 0, 1, 1, 29, 29, 14, 14, 15, 15, 16, 16,
			2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
			17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28};

	public Rider(int pickStop) {
		pickupstop = pickStop;
		dropoffstop = stopSelect[(int) (Math.random() * (35))];

		if (pickupstop < 15) { // Makes sure the random int is less than 15 and then sets the direction to true which is east.
			while (!(dropoffstop <= 15 && dropoffstop > pickupstop)) {
				dropoffstop = stopSelect[(int) (Math.random() * (35))];
				//System.out.println("this is the drop off stop random:............................................................... " + dropoffstop);
			}
		} else {
			while ((dropoffstop <= 15 || dropoffstop <= pickupstop)) { // Makes sure the random int is greater than 14 and then sets the direction to  which is west.
				dropoffstop = stopSelect[(int) (Math.random() * (35))];
				if(dropoffstop==0)break;
			}
		}
		// System.out.println("Pickup: "+pickupstop +"\t" + "Drop: "+dropoffstop);

	}
}
