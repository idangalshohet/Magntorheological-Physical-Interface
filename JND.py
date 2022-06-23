import numpy as np
import socket
import time
import pandas as pd
import serial


arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=1)


NUM_TRIALS = 1000
MAXIMUM_DELTA = 7
N_STEPS = 10
N_DOWN = 1


def JND_Linear(name):
    time.sleep(2)
    DELTA = MAXIMUM_DELTA
    CONTROL_VALUE = 230
    correct_counter = 0
    y = []
    y_hat = []
    control = []
    delta = []
    counter = 0
    # print("new_position = 0, speed = 500")
    new_position = 0
    speed = 500
    time.sleep(5)
    print("running")
    for i in range(NUM_TRIALS):
        print('='*10, i, '='*10)
        
        position_command = 0
        comm = str(position_command)+"|"
        # print(comm)
        prev_command = 0
        arduino.write(comm.encode())
        print('LIFT')
        prev_command = position_command

        time.sleep(2)

        position_command = CONTROL_VALUE
        comm = str(position_command)+"|"
        # print(comm)
        arduino.write(comm.encode())
        time.sleep(0.8)
        print('Force 1')
        prev_command = position_command

        time.sleep(4)

        position_command = 0
        comm = str(position_command)+"|"
        # print(comm)
        arduino.write(comm.encode())
        print('LIFT')
        prev_command = position_command

        time.sleep(2.0)

        change_flag = np.random.randint(2)
        if change_flag:
            position_command = CONTROL_VALUE + DELTA
        else:
            position_command = CONTROL_VALUE
        comm = str(position_command)+"|"
        arduino.write(comm.encode())
        time.sleep(0.8)
        print('Force 2')
        prev_command = position_command

        time.sleep(4)

        position_command = 0
        comm = str(position_command)+"|"
        # print(comm)
        arduino.write(comm.encode())
        # print('LIFT')
        prev_command = position_command
        time.sleep(0.5)

        change = ""
        while change != "0" and change != "1" and change != "2":
            change = input("Same (0) or different (1)?")
            if change == "quit":
                break
        if change == "quit":
            break
        if change != "2":
            y_hat.append(change)
            y.append(change_flag)
            control.append(CONTROL_VALUE)
            delta.append(DELTA)
            counter += 1
            # if counter >= N_STEPS:
            #     DELTA -= N_DOWN
            #     print('Reducing DELTA to:', DELTA)
            #     counter = 0
            if DELTA < 1:
                break
            if int(change) == change_flag:
                correct_counter += 1
                print('Correct')
            else:
                print('Incorrect')
                correct_counter -= 1
                correct_counter = np.clip(correct_counter, 0, 5)
                # DELTA += N_DOWN
                # DELTA = np.clip(DELTA, 0, MAXIMUM_DELTA)
                print('Incorrect', DELTA)
            if correct_counter >= 5:
                DELTA -= N_DOWN
                DELTA = np.clip(DELTA, 0, MAXIMUM_DELTA)
                print('5 correct in a row - reducing delta to: ', DELTA)
                correct_counter = 0
    control.append(60)
    delta.append(0)
    y_hat.append(0)
    y.append(1)
    control.append(60)
    delta.append(0)
    y_hat.append(0)
    y.append(0)
    df = pd.DataFrame({'control': control, 'delta': delta, 'yhat': y_hat, 'y': y})
    print(df)
    df.to_csv('JND' + name + ".csv", mode='a')


def main():
    print('Connecting to Magnetorheological Physical Interface')
    name = input('what is your name? ')
    JND_Linear(name)


if __name__ == "__main__":
    main()
