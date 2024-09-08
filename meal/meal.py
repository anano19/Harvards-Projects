def main():
    time = input("What time is it? ")
    if 7.0 <= convert(time) <= 8.0:
        print("Breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("Lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("Dinner time")


def convert(time):
    time = time.strip()
    if ":" in time:
        if " " in time:
            hours_minutes, period = time.split(" ")
            hours, minutes = hours_minutes.split(":")
            period = period.lower()
        else:
            hours, minutes = time.split(":")
            period = None
        hours = float(hours)
        minutes = float(minutes) / 60
        clock = hours + minutes
        if period == "pm" and hours != 12:
            return clock + 12
        elif period == "am" and hours == 12:
            return clock - 12
        else:
            return clock


if __name__ == "__main__":
    main()
