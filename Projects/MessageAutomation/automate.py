import pywhatkit
from pywhatkit.core.exceptions import (
    CallTimeException,
    CountryCodeException,
    InternetException,
    UnableToAccessApi
)
import os

print("""
*Hello before you start there is a note for you: This app will open your default brower and open whatsapp web so make sure you are signed in into it.*
      
1) Send message to whatsapp at specified time
2) Send message to group
3) Play a video on youtube by search item
4) Google search
5) Text to handwriting
6) Take screenshot of the screen
7) System shutdown after a specific time period

""")

userno = int(input("Enter the number: "))

try: 
    if userno == 1:
        print("You have selected to send message to whatsapp")
        phone_no = input("Enter phone no. including country code: ")
        message = input("Enter the message: ")
        time = input("Enter the timing (hour:minutes): ").strip().split(":")
        time = [int(i) for i in time]
        pywhatkit.sendwhatmsg(phone_no, message,time[0], time[1], 10)
        print("***End***")

    elif userno == 2:
        print("You have selected to send a message to the group")
        group_id = input("Enter the invite link of the group: ").strip().split(".com/")[1]  
        message = input("Enter the message: ")
        time = input("Enter the timing (hour:minutes): ").strip().split(":")
        time = [int(i) for i in time]
        pywhatkit.sendwhatmsg_to_group(group_id,message, time[0], time[1])
        print("***End***")

    elif userno == 3:
        print("You have selected to search a video on youtube")
        title = input("Enter the title of video: ")
        pywhatkit.playonyt(title)
        print("***End***")

    elif userno == 4:
        print("You have selected to search a topic on google")
        title = input("Enter the search prompt: ")
        pywhatkit.search(title)
        print("***End***")

    elif userno == 5:
        print("You have selected to convert text into handwriting")
        text = input("Enter the text you want to convert to handwriting: ")
        pywhatkit.text_to_handwriting(text, save_to="handwriting.png")
        print("***End***")

    elif userno == 6:
        print("You have selected to take a screenshot of the screen")
        time = int(input("Enter the delay for the screenshot(in seconds): "))
        pywhatkit.take_screenshot("screenshot",time, True)
        print("***End***")

    elif userno == 7:
        print("You have selected to shutdown the system in some time:")
        time = int(input("Enter the delay for the screenshot(in seconds): "))
        pywhatkit.shutdown(time)
        print("***End***")

    else:
        print("Invalid!!!")

except CallTimeException:
    print("Message must be scheduled at least 1 minute ahead of current time.")
except CountryCodeException:
    print("Phone number must include the correct country code.")
except UnableToAccessApi:
    print("Could not access the handwriting API. Try again later.")
except InternetException:
    print("Internet connection problem.")
except ValueError:
    print("Invalid number or time format. Please enter in hh:mm.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


if os.path.exists("PyWhatKit_DB.txt"):
    try:
        os.remove("PyWhatKit_DB.txt")
        print("Cleaned up PyWhatKit_DB.txt")
    except Exception as e:
        print(f"Warning: Couldn't delete PyWhatKit_DB.txt — {e}")
