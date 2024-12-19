# Exam_Timer (Countdown Timer Application):
This is a Python-based countdown timer application built using the pygame library. The program allows the user to set a number of intervals, displays the countdown in real-time, and plays sound notifications at the end of each interval.

Features
User Input: Input the number of countdown intervals through a text-based interface.
Timer Display: Displays the remaining time in a large, clear font.
Sound Alerts: Plays a sound notification (ting_ding.wav) when an interval ends and a different alert (ting_ting_ting_ting.wav) when the countdown is complete.
Graphical Interface: Utilizes pygame for a user-friendly graphical display.
Automatic Exit: Exits the program automatically once all intervals are complete.
Prerequisites
Before running the program, ensure you have the following:

Python 3.x installed
The pygame library installed (pip install pygame)
Audio files:
ting_ding.wav: Played at the end of each interval.
ting_ting_ting_ting.wav: Played when all intervals are complete.
How to Run
Clone or download this repository.
Place the required sound files (ting_ding.wav and ting_ting_ting_ting.wav) in the same directory as main.py.
Open a terminal or command prompt in the project directory.
Run the program using the command:
bash
Copy code
python main.py
Follow the on-screen instructions to enter the number of intervals for the countdown.
Usage Instructions
Home Screen: Enter the number of intervals using your keyboard and press Enter to start.
To clear input, press Delete.
To erase the last character, press Backspace.
Countdown Screen:
The countdown for each interval will be displayed.
A sound will play at the end of each interval.
End of Countdown: A distinct sound will play when all intervals are complete, and the program will exit automatically.
Customization
Sounds: Replace ting_ding.wav and ting_ting_ting_ting.wav with your own audio files for custom sound effects.
Timer Duration: Each interval is set to 144 seconds by default. To modify this, update the timr = 144 * int(ab) line in the code.
Dependencies
Python 3.x
pygame library
Notes
Ensure the required sound files are available in the project directory; otherwise, the program may crash.
The program automatically exits after the final interval and a short delay.
