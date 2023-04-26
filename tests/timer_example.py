# timer_example.py
# example of how to set up a hardware timer interrupt

from machine import Timer

def timer_interrupt(timer):
    # this code is executed when the timer ends
    print("The timer is done!")

# this line starts the timer
# mode=Timer.ONE_SHOT tells the timer to only run once
# period=3000 sets the timer to 3000 milliseconds
# callback=timer_interrupt tells the timer to run the function timer_interrupt() when it runs out (not that there is no () after the function name
Timer(mode=Timer.ONE_SHOT, period=3000, callback=timer_interrupt)

print("This is the end of the program. But just wait a bit...")