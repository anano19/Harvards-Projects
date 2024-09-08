import re


def main():
    time = input("hours: ")
    start_time, end_time = time.split(" to ")
    start_result = convert(start_time.strip())
    end_result = convert(end_time.strip())
    print(start_result, "to", end_result)



def convert(s):
    match = re.match(r"(\d{1,2}):?(\d{2})? (\w{2})", s)
    if match is None:
        raise ValueError("invalid time format")
    hours, minutes, period = match.groups()
    hours = int(match.group(1))
    if hours < 1 or hours > 12:
        raise ValueError("invalid hour input")
    if minutes != None:
        minutes = int(match.group(2) or 0)
    else:
        minutes = 0
    period = match.group(3).upper()
    if period == "PM" and hours < 12:
        hours += 12
    if period == "AM" and hours == 12:
        hours = 0
    if hours > 23:
        raise ValueError("invalid hour input")
    if minutes > 59:
        raise ValueError("invalid minute input")
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"


if __name__ == "__main__":
    main()
