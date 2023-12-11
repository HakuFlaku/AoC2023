from io import TextIOWrapper
import os

def main():
    print("Beginning execution...")
    
    seeds = [int(seed) for seed in open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'seeds.txt')), "r").readline().strip().split(' ')]
    print(seeds)

    minimumLocation = -1
    for seed in seeds:
        print("Seeking soil value for seed ", str(seed))
        soil = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'seedToSoil.txt')), "r"), seed)

        # print("Seeking fertilizer value for soil ", str(soil))
        fert = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'soilToFert.txt')), "r"), soil)

        # print("Seeking water value for fertilizer ", str(fert))
        water = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fertToWater.txt')), "r"), fert)

        # print("Seeking light value for water ", str(water))
        light = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'waterToLight.txt')), "r"), water)

        # print("Seeking temperature value for light ", str(light))
        temperature = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lightToTemp.txt')), "r"), light)

        # print("Seeking humidity value for temperature ", str(temperature))
        humidity = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'tempToHumidity.txt')), "r"), temperature)

        # print("Seeking location value for humidity ", str(humidity))
        location = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'humidityToLocation.txt')), "r"), humidity)

        # print("Seed is for location ", str(location))

        print("Value path: ", str(seed), " -> ", str(soil), " -> ", str(fert), " -> ", str(water), " -> ", str(light), " -> ", str(temperature), " -> ", str(humidity), " -> ", str(location), "\n")

        if(minimumLocation == -1):
            minimumLocation = location
        elif(location < minimumLocation):
            minimumLocation = location
        
    print("Minimum location: ", str(minimumLocation))

    print("Finished execution.")
                
def getValueFromFile(file: TextIOWrapper, seekForKey: int):
    for line in file:
        lineValue, lineKey, lineRange = [int(x) for x in line.strip().split(' ')]
        if(lineKey == seekForKey):
            return lineValue
        elif(lineKey < seekForKey and seekForKey < lineKey + lineRange):
            return lineValue + (seekForKey - lineKey)

    return seekForKey

if __name__ == "__main__":
    main()