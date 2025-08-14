def main():
    user_time = input("What time is it? ")
    hours = convert(user_time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= time <= 8:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    minutes = round(int(minutes) / 60, 2)
    time_in_hours = float(hours) + minutes
    return time_in_hours
    
if __name__ == "__main__":
    main()
