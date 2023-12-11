from io import TextIOWrapper
import os

def main():
    print("Beginning execution...")

    seedRanges = [int(seed) for seed in open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'seeds.txt')), "r").readline().strip().split(' ')]

    minimumLocation = -1
    
    location = 0
    while minimumLocation == -1:
        print("Trying for location ", str(location))

        humidity = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'humidityToLocation.txt')), "r"), location)
        # print("Humidity: ", str(humidity))

        temperature = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'tempToHumidity.txt')), "r"), humidity)
        # print("Temperature: ", str(temperature))

        light = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lightToTemp.txt')), "r"), temperature)
        # print("Light: ", str(light))

        water = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'waterToLight.txt')), "r"), light)
        # print("Water: ", str(water))

        fertalizer = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fertToWater.txt')), "r"), water)
        # print("Fertalizer: ", str(fertalizer))

        soil = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'soilToFert.txt')), "r"), fertalizer)
        # print("Soil: ", str(soil))

        seed = getValueFromFile(open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'seedToSoil.txt')), "r"), soil)
        # print("Seed: ", str(seed))

        for i in range(0, len(seedRanges), 2):
            rangeStart = seedRanges[i]
            rangeEnd = seedRanges[i + 1] + seedRanges[i]

            # print("Seed range start: ", rangeStart)
            # print("Seed range end: ", rangeEnd)
            if seed >= rangeStart and seed <= rangeEnd:
                print("Seed is in range!")
                minimumLocation = location
                break
        else:
            print("Seed not in range, try next location\n\n")

        location += 1

    print("Minimum location: ", str(minimumLocation))

    print("Finished execution.")
                
def getValueFromFile(file: TextIOWrapper, seekForKey: int):
    for line in file:
        lineKey, lineValue, lineRange = [int(x) for x in line.strip().split(' ')]
        if(lineKey == seekForKey):
            return lineValue
        elif(lineKey < seekForKey and seekForKey < lineKey + lineRange):
            return lineValue + (seekForKey - lineKey)

    return seekForKey

if __name__ == "__main__":
    main()