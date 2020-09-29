Project: Discrete Event Simulation
Authors: Jordyn Ojeda(ojeda040) and Skylan Recana(recan001)

Instruction:
    Run the simulation by running the main method in the BusSim class
    (The output will show the statistics of the Discrete Event Simulation using 14 buses: 2 Express Buses and 12 Regular Buses)

Overview:
    The project demonstrates a discrete event simulation for a bus company to show that the business proposal will succeed through maximizing the PMPG of each bus within 3 hours of simulation.
    The project is composed of 7 primary classes, 4 implementation/structural classes,and 2 interfaces:
    QGen - An interface that is composed of add(), remove(), and length() abstract methods
    Event - An interface that is composed of run() abstract method
    NGen - A class that creates a linked list node
    Q1Gen - A class that implements methods from the QGen Interface and is a Linked List implementation by using linked list nodes, which is the NGen
    Segment - A class that implements Q1Gen to create a priority queue node based on the given time for events
    PQ - A class that uses segment nodes to create a priority queue for the agenda. It should only contain different events
    Rider - A class that generates a passenger with a given random time
    Rider Event - A class that generates multiple riders and assign to the agenda for future riders
    Bus - A class that generates either a regular or an express bus with 50 seats available for riders, and can board and deboard riders from the bus stops
    Bus Stops - A class that represents bus stops that stores a queue of riders waiting for their corresponding buses
    Bus Event - A class that runs the buses at each bus stops at the scheduled time to board and deboard riders
    BusSim - A class that runs the discrete event simulation where it initializes the bus stops, the generation of riders through rider events, the generation of buses through bus events, and runs the collected data through Stats class
    Stats - A class that holds the data of the simulation at the given amount of time. That includes the queue length, the average and maximum waiting time, and the number of riders that was serviced by the buses


Data Structures:
    Queues with LinkedList implementation - Queues are a great data structure to be used in this simulation since it demonstrates the real rider queues when waiting at the bus stop
                                          - Since it is implemented as a LinkedList, this could make the event more realistic since queue in every bus stop expands depending how long the time runs
                                          - ArrayList Implementation is not recommended since queues in real life do not have limist and need to be resized every time they get full (most of the time)
    ArrayList - ArrayList is a great data structure for fix number of elements. It was used for creating bus stop objects, storing the bus objects, and creating seats for riders

Bugs and Errors:
    Getting a relatively long waiting time than expected around 20 minutes

Resources:
    QGen, Event, NGen, Q1Gen, Segment, PQ classes and interfaces were taken from CSCI 1933 UMN-TC course
