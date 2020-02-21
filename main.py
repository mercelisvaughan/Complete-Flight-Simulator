import random  # import random and time modules
import time


class American:
    def __init__(self):
        self.queue = ['127 DCA #10', '332 BUF #11', '233 FLL #12', '741 LAX #13', '112 CAE #14', '437 LGA #15', ]

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(Usa.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Cannot remove flight because American is empty")

    def AmericanLength(self):
        return len(American.queue)


Usa = American()
# printing the flights currently in the American queue
for elem in list(Usa.queue):
    print("Flight " + elem + " is in American")


class Delta:
    def __init__(self):
        self.queue = ['221 SFO #20', '348 DET #21', '765 CVG #22', '612 SAN #23', '148 FLL #24']

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(Del.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Cannot remove flight because Delta is empty")

    def DeltaLength(self):
        return len(Delta.queue)


Del = Delta()
# printing the flights currently in the Delta queue
for element in list(Del.queue):
    print("Flight " + element + " is in Delta")


class Southwest:
    def __init__(self):
        self.queue = ['345 LGA #40', '657 PHL #41', '211 BOS #42', '324 SFO #43', '367 SAN #44', '311 LAX #45',
                      '375 FLL #46']

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(South.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Cannot remove flight because South is empty")

    def SouthwestLength(self):
        return len(Southwest.queue)


South = Southwest()
# printing the flights currently in the Southwest queue.
for flights in list(South.queue):
    print("Flight " + flights + " is in Southwest")

print("--------------")

# We initialize the queue to an empty list to add flights from the other airlines.
class Runway:
    def __init__(self):
        self.queue = []

    def enqueue(self, flight):
        self.queue.append(flight)

    def dequeue(self):
        if len(Run.queue) > 0:
            return self.queue.pop(0)
        else:
            return "The runway cannot remove because it is empty."


Run = Runway()


# The add to runway function will be picking the random number for x and adding all t
def addToRunway():
    x = random.random()
    if 0 <= x and x <= 0.33:
        if len(Usa.queue) == 0: # If the lengtgh of a Queue is zero it will move to the next queues.
            if x >= 0 and x <= .5:
                print("The following has been removed from Delta for the runway:", Del.queue[0])
                Run.enqueue(Del.queue[0])

                print("Run.queue has flights: ", Run.queue)
            elif x >= 0.50 and x <= 1:
                print("The following has been removed from South for the runway:", South.queue[0])
                Run.enqueue(South.queue[0])
                print("Run.queue has flights: ", Run.queue)
        else:
            print("The following has been removed from American for the runway:", Usa.queue[0])
            Run.enqueue(Usa.queue[0])
            print("Run.queue has flights: ", Run.queue)

    if 0.33 >= x and x <= 0.67:
        if len(Del.queue) == 0:
            if x >= 0 and x <= 0.50:
                print("The following has been removed from American for the runway:", Usa.queue[0])
                Run.enqueue(Usa.queue[0])
                print("Run.queue has flights: ", Run.queue)
            elif x >= 0.50 and x <= 1:
                print("The following has been removed from South for the runway:", South.queue[0])
                Run.enqueue(South.queue[0])
                print("Run.queue has flights: ", Run.queue)
        else:
            print("The following has been removed from Delta for the runway:", Del.queue[0])
            Run.enqueue(Del.queue[0])
            print("Runway has flights: ", Run.queue)
    if 0.67 <= x and x <= 1:
        if len(South.queue) == 0:
            if x >= 0 and x <= 0.50:
                print("The following has been removed from American for the runway:", Usa.queue[0])
                Run.enqueue(Usa.dequeue)
                print("Run.queue has flights: ", Run.queue)
            elif x >= 0.50 and x <= 1:
                print("The following has been removed from Delta for the runway:", Del.queue[0])
                Run.enqueue(Del.dequeue())
                print("Runway has flights: ", Run.queue)
        else:
            print("The following has been removed from South for the runway:", South.queue[0])
            Run.enqueue(South.dequeue())
            print("Runway has flights: ", Run.queue)


# The runwayTakeoff function determines if a flight is able to take off or if the flights in the runway must wait.
def runwayTakeoff():
    y = random.random()
    if 0 <= y and y <= 0.50:
        print(Run.dequeue(), "will now take off")
        print("The runway currently has flights: ", Run.queue)
        if len(Usa.queue) == 0:
            print("No remaining flights in American.")
        else:
            for elem in list(Usa.queue): # Printing the remaining flights in the runways.
                print("Flight(s) " + elem + " is currently in American")
        print("---------------------------------------")
        if len(Usa.queue) == 0:
            print("No remaining flights in American.")
        else:
            for element in list(Del.queue): # Printing the remaining flights in the runways.
                print("Flight(s) " + element + " is currently in Delta.")
        print("---------------------------------------")
        if len(South.queue) == 0:
            print("No remaining South.")
        else:
            for flights in list(South.queue): # Printing the remaining flights in the runways.
                print("Flight(s) " + flights + " is currently in Southwest.")
    if 0.50 <= y and y <= 1:
        print("An arriving flight is landing.")
        print("The remaining flights: ", Run.queue, " must wait.")
        time.sleep(4)
    if len(Run.queue) == 0:
        print("The runway is currently empty.")

# The cancel flight function generates number z randomly to determine if a flight will be cancelled.
def cancelFlight():
    z = random.random()
    if 0 <= z and z <= 0.10:
        if len(Usa.queue) == 0: # A case to stop a pop from empty Queues
            print("No cancels, American Airlines is empty.")
        else:
            Usa.dequeue()
            print(Usa.dequeue(), " has been removed due to cancellation.")
    if 0.50 <= z and z <= 0.60:
        if len(Del.queue) == 0:
            print("No cancels, Delta airlines is empty.")
        else:
            Del.dequeue()
            print(Del.dequeue(), " has been removed due to cancellation.")
    if .80 <= z and z <= 0.90:
        if len(South.queue) == 0:
            print("No cancels, South airline is empty.")
        else:
            South.dequeue()
            print(South.dequeue(), " has been removed due to cancellation.")


# this while loop will repeatedly call the functions forever until the airports and runway is empty.
while time.time():
    time.sleep(2)
    addToRunway()
    time.sleep(4)
    runwayTakeoff()
    cancelFlight()