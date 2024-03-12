import datetime

def calculate_future_time(seconds):
    current_time = datetime.datetime.now()
    future_time = current_time + datetime.timedelta(seconds=seconds)
    return future_time

def main():
    try:
        seconds = int(input("Enter the number of seconds to add: "))
        future_time = calculate_future_time(seconds)
        print("Future time after {} seconds: {}".format(seconds, future_time.timestamp))
    except ValueError:
        print("Please enter a valid number of seconds.")

if __name__ == "__main__":
    main()
