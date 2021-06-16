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
  
  daysPassed = 0
  timeReturnInMins = 0

  if endTime > midnight:
    daysPassed = math.floor(endTime / midnight)
    timeReturnInMins = endTime % midnight
  else:
    timeReturnInMins = endTime

  hourOutput = str(math.floor(timeReturnInMins / 60))
  minOutput = str(timeReturnInMins % 60)
  if len(minOutput) == 1:
    minOutput = "0" + minOutput

  amOrPmOutput = "AM"
  
  if hourOutput == 0:
    hourOutput == "12"
  print(hourOutput)
  if int(hourOutput) >= 12:
    if int(hourOutput) > 12:
      print(hourOutput)
      hourOutput = str(int(hourOutput) - 12)
    amOrPmOutput = "PM"

  daysLater = ""
  
  if daysPassed == 1:
    daysLater += '(next day)'
  elif daysPassed > 1:
    daysLater += '({} days later)'.format(daysPassed)

  dayOutput = ""
  if day:
    day = day.capitalize()
    if daysPassed == 0:
      dayOutput = day
    elif daysPassed >= 0:
      dayNum = int(daysPassed) % 7
      dayIndex = int(days.index(day))
      wantedNum = (dayNum + dayIndex) % 7
      dayOutput = days[wantedNum]


  finalString = "{}:{} {}".format(hourOutput,minOutput,amOrPmOutput)
  if day:
    finalString += ", {}".format(dayOutput)
  if int(daysPassed) > 0:
    finalString += " {}".format(daysLater)

  print(finalString)
  return finalString


add_time("11:59 PM", "24:05")


        # actual = add_time("11:59 PM", "24:05")
        # expected = "12:04 AM (2 days later)"