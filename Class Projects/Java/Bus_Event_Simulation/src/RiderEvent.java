
public class RiderEvent implements Event {
	
	private int stop;
	private double percent;
	private int arrivaltime;
	public RiderEvent(int stop){
		this.stop = stop;
	}
	
	double[] arrivalPercents = {.75, .75, .5, .5, .5, .2, .2, .2, .2, 0, 0,-.2,
			-.2, -.2, -.2, -.5, -.5, -.5, -.75, -.75};
	 
	 
	public void run() { 
		percent = arrivalPercents[(int) (Math.random() * 19.0)];
		
		arrivaltime = (int) (BusSim.averageArrival + (percent *  BusSim.averageArrival));
		
		if(stop == 0 || stop == 1 || stop == 29 || stop == 14 || stop == 15 || stop == 16) {
			Rider passenger = new Rider(stop);

			// Sets the start time of the passenger
			passenger.setStartTime(BusSim.agenda.getCurrentTime());

			// Sets the arrival time of the passenger
			passenger.setArrivalTime(arrivaltime);

			// Adds a passenger to a special stop
			BusSim.stops[stop].add(passenger);
			/*
			System.out.println("Rider Event Stop: " + stop);
			System.out.println("Current Time is: " + BusSim.agenda.getCurrentTime());
			System.out.println("Next Rider in " + arrivaltime/2 + " sec \n");
			 */
			BusSim.agenda.add(new RiderEvent(stop), arrivaltime/2.);

		} else {
			Rider passenger = new Rider(stop);
			passenger.setStartTime(BusSim.agenda.getCurrentTime());
			BusSim.stops[stop].add(passenger);
			/*
			System.out.println("Rider Event Stop: " + stop);
			System.out.println("Current Time is: " + BusSim.agenda.getCurrentTime());
			System.out.println("Next Rider in " + arrivaltime + " sec \n");
			 */
			BusSim.agenda.add(new RiderEvent(stop), arrivaltime);
		}
	}
	
}
