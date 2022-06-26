medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    output_results = {}

    # Iterate over each sport in the given list
    for sport in results:

      # Iterate over podium list for each sport  
      for podium in sport['podium']:
        
        # Get the counrty name, starting at index 2 -> end of string
        country = podium[2:]

        # Get the char at index 0, using int to convert the string to an integar
        position = int(podium[0])

        # Calculate points - since 1=3, 2=2 and 3=1. We can subtract the position from 4 to get the points value required
        points = 4 - position

        # If results does not yet contain the current country we can use the setdefault method to set the value to 0
        output_results.setdefault(country, 0)

        # Then we can increment the current country total using the current points.
        output_results[country] += points

    return output_results

def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
