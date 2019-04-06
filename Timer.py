import winsound
import time
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def timer(minutes):
    time.sleep(minutes*60)
    winsound.Beep(frequency, duration)


def washer():
    waterWash =  4
    waterRinse1 = 5
    waterRinse2 = 3

    wash = 15

    rinse1 = 3
    rinse2 = 2

    drain = 4

    leaveitout = 15

    comforttime = 5


    rinse2yesno = True
    comfort = True

    timer(waterWash)
    timer(wash)
    timer(drain)
    timer(waterRinse1)
    timer(rinse1)
    timer(drain)
    if rinse2yesno:
        timer(waterRinse2)
        timer(rinse2)
        if comfort:
            timer(comforttime)
        timer(drain)
    timer(leaveitout)


washer()