import math

def add_time(start, duration, day = None ):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  finalString = ""
  startTime = start.split(" ")[0]
  startHour = startTime.split(":")[0]
  startMin = startTime.split(":")[1]
  startInMins = (int(startHour) * 60) + int(startMin)

  amOrPmInput = startTime = start.split(" ")[1]
  
  durationHour = duration.split(":")[0]
  durationMin = duration.split(":")[1]
  durationInMins = int(durationHour)*60 + int(durationMin)

  if amOrPmInput == "PM":
    startInMins = startInMins + 60*12

  endTime = startInMins + durationInMins
  
  midnight = 24*60
  
  DaysPassed = 0
  timeReturnInMins = 0

  if endTime > midnight:
    DaysPassed = math.floor(endTime / midnight)
    timeReturnInMins = endTime % midnight
  else:
    timeReturnInMins = endTime

  hourOutput = str(math.floor(timeReturnInMins / 60))
  minOutput = str(timeReturnInMins % 60)
  amOrPmOutput = "AM"

  if int(hourOutput) > 12:
    hourOutput = str(int(hourOutput) - 12)
    amOrPmOutput = "PM"

# for loop yaz gunler için her geçen haftada 7 eksilterek 


  print(hourOutput, minOutput, amOrPmOutput, DaysPassed, day)

  # if amOrPmInput == "AM" and endTime > 12*60:


  # print(startHour)
  # print(startMin)
  # print(startInMins)
  # print(midnight)
  # print(durationInMins)
  # print(amOrPmInput)


add_time("3:00 PM", "3:10", "Tuesday")