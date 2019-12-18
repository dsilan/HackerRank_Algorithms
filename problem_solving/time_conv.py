time = "12:45:54PM"

if time[-2:] == "AM":
    print("{:02}".format(int(time[:2])%12)+time[2:-2])
else:
    hour=int(time[:2])
    if hour != 12:
        hour += 12
    print(str(hour)+time[2:-2])