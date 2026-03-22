from datetime import datetime, timedelta
def planHeader():
    return(
    """
    +-------|+--------------------------+
    | #    |Task                       |
    +-------+---------------------------+              
    """)

def taskDivider():
    print(
    """
    +-------|+------------------------+ 
    """
    )
def getStartTime():
    startTime = input("Enter your desired plan start time in HH:MM format:")
    return datetime.strptime(startTime, "%H:%M")
    startTime = getStartTime()

    #error catcher to come in future

def createTimesList(startTime, sortedPlans):
    times = []
    current_time = startTime
    for t in range(len(sortedPlans)):
        times += [current_time]
        current_time += timedelta(minutes=30)
    return times


def fillTable(sortedPlans, times):
    print("+-----+------------+----------------------------------------------------+")
    print("| {:<3} | {:<10} | {:<50} |".format("No.", "Time", "Task"))
    print("+-----+------------+----------------------------------------------------+")
    for x in range(len(sortedPlans)):
        print("| {:<3} | {:<10} | {:<50} |".format(sortedPlans[x][0], times[x].strftime("%H:%M"), sortedPlans[x][1]))
        print("+-----+------------+----------------------------------------------------+")

    
      
