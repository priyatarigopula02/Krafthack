import numpy as np
import pandas as pd


def time_since_start(df):
    time_start = np.zeros(len(df))
    for i in range(len(df)):
        if i == 0:
            time_start[i] = 1
        else:
            if (df['mode'][i] == 'start') & (df['mode'][i - 1] == 'operation') & (df['time_difference'][i] < 500):
                time_start[i] = 0
            elif (df['mode'][i] == 'start') & (df['mode'][i - 1] == 'start') & (df['time_difference'][i] < 500):
                time_start[i] = time_start[i - 1] + df['time_difference'][i]
            elif (df['time_difference'][i] > 500):
                time_start[i] = 0
            elif (df['mode'][i] == 'operation'):
                time_start[i] = time_start[i - 1]
    return time_start


def time_since_operation(df):
    time_op = np.zeros(len(df))
    for i in range(len(df)):
        if i == 0:
            time_op[i] = 1
        else:
            if (df['mode'][i] == 'operation') & (df['time_difference'][i] < 500):
                time_op[i] = time_op[i - 1] + df['time_difference'][i]
            elif (df['mode'][i] == 'operation') & (df['time_difference'][i] > 500):
                time_op[i] = time_op[i - 1]
            elif (df['mode'][i] == 'start'):
                time_op[i] = 0
    return time_op

def timepoint_difference(df):
    tps =np.array(df.index[:])
    tp_diff =np.diff(tps)/np.timedelta64(1, 's')
    tp_diff = np.insert(tp_diff, 0 , 1)
    return tp_diff


def track_time(df):
    tps =np.array(df.index[:])
    tp_diff =(tps-tps[0])/np.timedelta64(1, 's')
    return tp_diff