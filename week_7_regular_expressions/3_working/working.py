import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    regex = r"(1[012]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[012]|0?[1-9]):?([0-5][0-9])? (AM|PM)"
    if re.search(regex, s):
        start_hour, start_minute, start_period = matches.group(1), matches.group(2), matches.group(3)
        end_hour, end_minute, end_period = matches.group(4), matches.group(5), matches.group(6)
        start_time = translator(start_hour, start_minute, start_period)
        end_time = translator(end_hour, end_minute, end_period)
        return f"{start_time} to {end_time}"
    else:
        raise ValueError

def translator(hour, minute, period):
    if period == "PM" and hour != "12":
        hour = int(hour) + 12
    elif period == "AM" and hour == "12":
        hour = 0
    else:
        hour = int(hour)
    if minute == None:
        return f"{hour:02}:00"
    else:
        return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
