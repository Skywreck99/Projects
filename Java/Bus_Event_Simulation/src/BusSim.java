import java.util.Scanner;
public class BusSim {

	// Note that this is static. This way, it can be accessed anywhere.
    public static PQ agenda = new PQ();
    // BusStop array of stops
    public static BusStop[] stops = new BusStop[30];
    //Calculates arrival percent
    public static int averageArrival = 120;
    // Boolean for type of bus
    public static Bus[] bus = new Bus[14];

    public static void main(String[] args) {
    	// add RiderEvent to agenda

    	stops[0] = new BusStop("Ramp B" , 0) ;
    	stops[1] = new BusStop("4th & Nicollet" , 1);
    	stops[2] = new BusStop("Anderson Hall" , 2);
    	stops[3] = new BusStop("Jones Hall" , 3);
    	stops[4] = new BusStop("Kasota Circle" , 4);
    	stops[5] = new BusStop("Como & Eustis" , 5);
    	stops[6] = new BusStop("Como & Cleveland" , 6);
    	stops[7] = new BusStop("Como & Snelling" , 7);
    	stops[8] = new BusStop("Como & Hamline" , 8);
    	stops[9] = new BusStop("Maryland & Dale" , 9);
    	stops[10] = new BusStop("Maryland & Rice" , 10);
    	stops[11] = new BusStop("Front & Lexington" , 11);
    	stops[12] = new BusStop("Front and Dale" , 12);
    	stops[13] = new BusStop("Capitol" , 13);
    	stops[14] = new BusStop("Cedar" , 14);
    	stops[15] = new BusStop("Union Depot" , 15);
    	stops[16] = new BusStop("Cedar" , 16);
    	stops[17] = new BusStop("Capitol" , 17);
    	stops[18] = new BusStop("Front and Dale" , 18);
    	stops[19] = new BusStop("Front & Lexington" , 19);
    	stops[20] = new BusStop("Maryland & Rice" , 20);
    	stops[21] = new BusStop("Maryland & Dale" , 21);
    	stops[22] = new BusStop("Como & Hamline" , 22);
    	stops[23] = new BusStop("Como & Snelling" , 23);
    	stops[24] = new BusStop("Como & Cleveland" , 24);
    	stops[25] = new BusStop("Como & Eustis" , 25);
    	stops[26] = new BusStop("Kasota Circle" , 26);
    	stops[27] = new BusStop("Jones Hall" , 27);
    	stops[28] = new BusStop("Anderson Hall" , 28);
    	stops[29] = new BusStop("4th & Nicollet" , 29);
    	
    	for(int index = 0; index < 30; index++) {
    		RiderEvent rider1 = new RiderEvent(index);
    		rider1.run();
    	}

		BusEvent bus1 = new BusEvent(8, new Bus(true, 1000));
		BusEvent bus2 = new BusEvent(1, new Bus(false, 2000));
		BusEvent bus3 = new BusEvent(3, new Bus(false, 3000));
		BusEvent bus4 = new BusEvent(5, new Bus(false, 4000));
		BusEvent bus5 = new BusEvent(7, new Bus(false, 5000));
		BusEvent bus6 = new BusEvent(10, new Bus(false, 6000));
		BusEvent bus7 = new BusEvent(16, new Bus(false, 7000));

		BusEvent bus8 = new BusEvent(13, new Bus(false, 8000));
		BusEvent bus9 = new BusEvent(19, new Bus(false, 9000));
		BusEvent bus10 = new BusEvent(20, new Bus(true, 10000));
		BusEvent bus11 = new BusEvent(22, new Bus(false, 11000));
		BusEvent bus12 = new BusEvent(25, new Bus(false, 12000));
		BusEvent bus13 = new BusEvent(27, new Bus(false, 13000));
		BusEvent bus14 = new BusEvent(29, new Bus(false, 14000));

		bus1.run();
		bus2.run();
		bus3.run();
		bus4.run();
		bus5.run();
		bus6.run();
		bus7.run();
		bus8.run();
		bus9.run();
		bus10.run();
		bus11.run();
		bus12.run();
		bus13.run();
		bus14.run();
        	
    	bus[0] = bus1.getThebus();
    	bus[1] = bus2.getThebus();
    	bus[2] = bus3.getThebus();
    	bus[3] = bus4.getThebus();
    	bus[4] = bus5.getThebus();
    	bus[5] = bus6.getThebus();
    	bus[6] = bus7.getThebus();
		bus[7] = bus8.getThebus();
		bus[8] = bus9.getThebus();
		bus[9] = bus10.getThebus();
		bus[10] = bus11.getThebus();
		bus[11] = bus12.getThebus();
		bus[12] = bus13.getThebus();
		bus[13] = bus14.getThebus();
    	
        // loops through agenda and runs the next iEvent
        // will throw an exception until events are added to the agenda
        while(agenda.getCurrentTime() <= 10800) {
            agenda.remove().run();
        }

        //stops[0].printStats();
        //System.out.println(stops[0].getName());
        System.out.println("Stop 0 at " + stops[0].getName() + ": Number of Riders in line: " + stops[0].getQ().length());
		System.out.println("Stop 1 at " + stops[1].getName() + ": Number of Riders in line: " + stops[1].getQ().length());
		System.out.println("Stop 2 at " + stops[2].getName() + ": Number of Riders in line: " + stops[0].getQ().length());
		System.out.println("Stop 3 at " + stops[3].getName() + ": Number of Riders in line: " + stops[3].getQ().length());
		System.out.println("Stop 4 at " + stops[4].getName() + ": Number of Riders in line: " + stops[4].getQ().length());
		System.out.println("Stop 5 at " + stops[5].getName() + ": Number of Riders in line: " + stops[5].getQ().length());
		System.out.println("Stop 6 at " + stops[6].getName() + ": Number of Riders in line: " + stops[6].getQ().length());
		System.out.println("Stop 7 at " + stops[7].getName() + ": Number of Riders in line: " + stops[7].getQ().length());
		System.out.println("Stop 8 at " + stops[8].getName() + ": Number of Riders in line: " + stops[8].getQ().length());
		System.out.println("Stop 9 at " + stops[9].getName() + ": Number of Riders in line: " + stops[9].getQ().length());
		System.out.println("Stop 10 at " + stops[10].getName() + ": Number of Riders in line: " + stops[10].getQ().length());
		System.out.println("Stop 11 at " + stops[11].getName() + ": Number of Riders in line: " + stops[11].getQ().length());
		System.out.println("Stop 12 at " + stops[12].getName() + ": Number of Riders in line: " + stops[12].getQ().length());
		System.out.println("Stop 13 at " + stops[13].getName() + ": Number of Riders in line: " + stops[13].getQ().length());
		System.out.println("Stop 14 at " + stops[14].getName() + ": Number of Riders in line: " + stops[14].getQ().length());
		System.out.println("Stop 15 at " + stops[15].getName() + ": Number of Riders in line: " + stops[15].getQ().length());
		System.out.println("Stop 16 at " + stops[16].getName() + ": Number of Riders in line: " + stops[16].getQ().length());
		System.out.println("Stop 17 at " + stops[17].getName() + ": Number of Riders in line: " + stops[17].getQ().length());
		System.out.println("Stop 18 at " + stops[18].getName() + ": Number of Riders in line: " + stops[18].getQ().length());
		System.out.println("Stop 19 at " + stops[19].getName() + ": Number of Riders in line: " + stops[19].getQ().length());

        for(int i = 0; i < bus.length; i++) {
			bus[i].getThestats().displayStatsEachBus();
		}
		Stats.displayStats();
    	
    }
    
}
