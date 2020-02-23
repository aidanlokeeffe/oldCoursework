import time

#get current GMT time
currentTime = time.time()

#get seconds since 1.1.1970
totalSeconds = int(currentTime)

#get current seconds 
currentSeconds = totalSeconds % 60

#get total minutes
totalMinutes = totalSeconds // 60

#get current minutes
currentMinutes = totalMinutes % 60

#get total hours
totalHours = totalMinutes // 60

#get current hours
currentHours = totalHours % 24

#output
print("It is currently", currentHours, ":", currentMinutes, ":", currentSeconds, "GMT")
