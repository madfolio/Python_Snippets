import time

x = [0, 9, 0, 0, 0]  # Global variable
print("Starting locations are: " + str(x))

class Trains:
    @staticmethod
    def run_train(CV, Speed, Route):
        # Call the route function passed as Route
        print(str(CV) + " is ready to use " + Route.__name__)
        Route(CV)

class Routes:
    @staticmethod
    def route1_4(CV):
        global x
        x[4] = CV
        print("Route 1 - 4 in progress: " + str(x))
        time.sleep(3)
        x[1] = 0
        x[4] = CV       
        print("Route 1 - 4 complete: " + str(x))


    @staticmethod
    def route4_1(CV):
        global x
        x[1] = CV
        print("Route 4 - 1 in progress: " + str(x))
        time.sleep(3)
        x[1] = 0
        x[4] = CV        
        print("Route 4 - 1 complete: " + str(x))


# Example usage
Trains.run_train(9, 0.35, Routes.route1_4)
Trains.run_train(9, 0.35, Routes.route4_1)
print(x)  # Output: [0, 0, 0, 0, 5]
