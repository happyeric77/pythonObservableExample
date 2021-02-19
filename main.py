from part1_basic import observableBasic
from part2_advanced import observableAdvanced
from part3_expert import observableExpert

if __name__ == "__main__":
    
    # Part1 

    print('*'*10, "Part1", '*'*10)
    eric = observableBasic.Observer("Eric")
    yuko = observableBasic.Observer("Yuko")
    pipu = observableBasic.Observer("pipu")

    observable = observableBasic.Observalbe()

    observable.register(eric)
    observable.register(yuko)
    observable.register(pipu)

    observable.dispatch("Time to have lunch")

    observable.unregister(pipu)
    observable.dispatch("Time to have dinner")


    # Part2

    print('*'*10, "Part2", '*'*10)
    eric = observableAdvanced.Observer1("Eric")
    yuko = observableAdvanced.Observer1("Yuko")
    pipu = observableAdvanced.Observer2("pipu")

    observable = observableAdvanced.Observalbe()

    observable.register(eric, eric.update)
    observable.register(yuko, yuko.update)
    observable.register(pipu, pipu.renew)

    observable.dispatch("Time to have lunch")

    observable.unregister(pipu)
    observable.dispatch("Time to have dinner")

    # Part3
    
    print('*'*10, "Part3", '*'*10)
    eric = observableExpert.Observer("Eric")
    yuko = observableExpert.Observer("Yuko")
    pipu = observableExpert.Observer("pipu")

    observable = observableExpert.Observalbe(["Lunch", "Dinner"])

    observable.register(eric, "Lunch")
    observable.register(yuko, "Lunch")
    observable.register(pipu, "Dinner")

    observable.dispatch("Lunch", "Time to have lunch")

    observable.dispatch("Dinner", "Time to have dinner")
