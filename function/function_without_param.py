from datetime import datetime
def greet():
    current_time=datetime.now().hour
    # current_time=21
    if 5<=current_time<12:
        print(f"Hello, Good Morning! ")
    elif 12<=current_time<=17:
        print(f"Hello, Good Afternoon! ")
    elif 17 <= current_time <= 20:
        print(f"Hello, Good Evening! ")
    else:
        print(f"Hello, Good Night! ")

greet()
