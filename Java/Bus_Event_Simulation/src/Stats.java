
// Stat2.java
// Revised March 2017
// Allows for stats for multiple Washer2s, as it is instantiable

// Statistics class for Car Simulation

public class Stats {
	 // private variables

    private String busType;
    private static String longestWaitatStop;
    private int allStops;
    private int totalBusPass;
    private static int totalAveBusPass;
    private int busNum;
    private static double longestWaitingTime = 0;
    private static double totalWaitingTime;
    private static int totalPassServiced;

    // constructors

    public Stats(boolean type, int BusNumber) {
        if (type) {
            busType = "Express Bus";
        } else {
            busType = "Regular Bus";
        }
        busNum = BusNumber;
    }

    public static void setTotalAveBusPass(int pass) { totalAveBusPass += pass;}
    public static void setLongestWaitingTime(String name) { longestWaitatStop = name; }
    public void settotalStops(int stops) {
        allStops += stops;
    }
    public void settotalBusPass(int pass) {
        totalBusPass += pass;
    }
    public static void setTotalPassServiced(int pass) {
        totalPassServiced += pass;
    }
    public static void settotalWaitingTime(double wait) {
        totalWaitingTime += wait;
    }
    public static boolean checkWaitingTime(double time) {
        if (longestWaitingTime == 0 || longestWaitingTime < time) {
            longestWaitingTime = time;
            return true;
        } else {
            return false;
        }
    }

    public void displayStatsEachBus() {
        System.out.println("\n" + busType + ": " + busNum);
        System.out.println("Total Passengers Boarded the Bus: " + totalBusPass);
        System.out.println("Total Stops: " + allStops);
        System.out.println("Average number of Passengers: " + totalBusPass / allStops + "\n");
        setTotalAveBusPass(totalBusPass/allStops);
        /*
        System.out.println("\n** Simulation Results **\n");
        System.out.println(" Calculated Simulation Time: " + totalTime);
        System.out.println(" Idle Time: " + idleTime);
        System.out.println(" Busy Time: " + busyTime);
        System.out.println(" (Busy Time based on service time: " + 
                                               averageServiceTime + ")\n");
        System.out.println(" Maximum Queue Length: " + maxQLength);
        System.out.println(" Avg. Queue Length: " + averageQLength/totalTime);
        System.out.println(" Maximum Waiting Time: " + maxWait);
        System.out.println(" Avg. Waiting Time for cars through the queue: " +
                                                 averageWait/count);
        System.out.println(" Avg. Service Time: " + averageServiceTime/
                                                       count);
        System.out.println(" Number of cars through system: " + count);
        System.out.println("\n");

         */

    }  // displayStats

    public static void displayStats() {
        displayMaxAndAveQLength();
        displayBuses();
        displayWaitingTime();
    }

    public static void displayMaxAndAveQLength() {
        int MaxQLength = 0;
        int AveQLength = 0;
        String busStopName = "";

        for (int i = 0; i < BusSim.stops.length; i++) {
            AveQLength += BusSim.stops[i].getMaxQLength();
            if (BusSim.stops[i].getMaxQLength() > MaxQLength) {
                MaxQLength = BusSim.stops[i].getMaxQLength();
                busStopName = BusSim.stops[i].getName();
            }
        }
        System.out.println("The Maximum Queue Length is " + MaxQLength + " at Bus Stop " + busStopName);
        System.out.println("The Average Queue Length is " + AveQLength/BusSim.stops.length);
    }

    public static void displayBuses() {
        int ExCount = 0;
        int RegCount = 0;
        int TotalBus = 0;

        for (int i = 0; i < BusSim.bus.length; i++) {
            if (BusSim.bus[i].getbusType()) {
                ExCount++;
            } else {
                RegCount++;
            }
        }
        TotalBus += ExCount + RegCount;

        System.out.println("Total Buses in the System: " + TotalBus);
        System.out.println("Number of Express Buses in the System: " + ExCount);
        System.out.println("Number of Regular Buses in the System: " + RegCount);
        System.out.println("Average number of Passengers in all Buses: " + totalAveBusPass/TotalBus);
    }

    public static void displayWaitingTime() {
        System.out.println("Total Passengers Serviced: " + totalPassServiced);
        System.out.println("Longest Waiting TIme: " + longestWaitingTime + " at Stop " + longestWaitatStop);
        System.out.println("Average Waiting Time: " + totalWaitingTime / totalPassServiced);
    }


}  // Stat2 class

