def  getMinTimeDifference( times):
    for index,time in enumerate(times): #convert times
        hours,minutes = map(int,time.split(":"))
        times[index] = hours*60 + minutes
    times = sorted(times)
    minDiff = float("inf")
    for i in range(-1, len(times)-1):
        diff = timeDiff(times[i], times[i+1])
        if diff < minDiff:
            minDiff = diff
    return minDiff

#A and B are times in minutes
def timeDiff(A,B):
    return min(abs(A-B), 24*60-abs(A-B))

getMinTimeDifference(["10:00", "19:20"])
