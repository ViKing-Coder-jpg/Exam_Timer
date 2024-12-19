# Exam_Timer (Countdown Timer Application):
This is a Python-based countdown timer application built using the pygame library. The program allows the user to set a number of intervals, displays the countdown in real-time, and plays sound notifications at the end of each interval.

_Features_ <br>
User Input: Input the number of countdown intervals through a text-based interface.<br>
Timer Display: Displays the remaining time in a large, clear font.<br>
Sound Alerts: Plays a sound notification (ting_ding.wav) when an interval ends and a different alert (ting_ting_ting_ting.wav) when the countdown is complete.<br>
Graphical Interface: Utilizes pygame for a user-friendly graphical display.<br>
Automatic Exit: Exits the program automatically once all intervals are complete.<br>

_Prerequisites_ <br>
Before running the program, ensure you have the following:<br>
Python 3.x installed<br>
The pygame library installed (pip install pygame)<br>
Audio files:<br>
ting_ding.wav: Played at the end of each interval.<br>
ting_ting_ting_ting.wav: Played when all intervals are complete.<br>  

_How to Run_ <br>
Clone or download this repository.<br>
Place the required sound files (ting_ding.wav and ting_ting_ting_ting.wav) in the same directory as main.py.<br>
Open a terminal or command prompt in the project directory.<br>
Run the program using the commandline/:<br>
python main.py<br>
Follow the on-screen instructions to enter the number of intervals for the countdown.<br>

_Usage Instructions_ <br>
Home Screen: Enter the number of intervals using your keyboard and press Enter to start.<br>
To clear input, press Delete.<br>
To erase the last character, press Backspace.<br>
Countdown Screen:<br>
The countdown for each interval will be displayed.<br>
A sound will play at the end of each interval.<br>
End of Countdown: A distinct sound will play when all intervals are complete, and the program will exit automatically.<br>

_Customization_ <br>
Sounds: Replace ting_ding.wav and ting_ting_ting_ting.wav with your own audio files for custom sound effects.<br>
Timer Duration: Each interval is set to 144 seconds by default. To modify this, update the timr = 144 * int(ab) line in the code.<br>

_Dependencies_ <br>
Python 3.x <br>
pygame library <br>
_Notes_ <br>
Ensure the required sound files are available in the project directory; otherwise, the program may crash.<br>
The program automatically exits after the final interval and a short delay.<br>
