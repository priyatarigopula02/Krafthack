import pandas as pd
import numpy as np
from utils import *

def add_features(path_to_data):
    data = pd.read_parquet(path_to_data)
    new_data = pd.DataFrame(data)
    new_data.insert(0, 'time_difference', timepoint_difference(data))
    new_data.insert(0, 'time_start', time_since_start(new_data))
    new_data.insert(0, 'time_op', time_since_operation(new_data))
    new_data.insert(0, 'time_2', new_data['time_op'].cumsum())
    new_data.insert(0, 'track_time', track_time(new_data))
    new_data.insert(0, 'binary_mode', binarize_mode(new_data))
    X = new_data[['time_start','time_op','track_time','time_2','Unit_4_Power',
        'Unit_4_Reactive Power', 'Turbine_Guide Vane Opening','Turbine_Pressure Drafttube',
        'Turbine_Pressure Spiral Casing','Turbine_Rotational Speed','binary_mode',]].values
    Y = new_data[['Bolt_1_Tensile','Bolt_2_Tensile', 'Bolt_3_Tensile',
                'Bolt_4_Tensile','Bolt_5_Tensile','Bolt_6_Tensile',]].values
    np.savez('Input_to_NN.npz', X = X, Y = Y)


add_features('data/input_dataset-2.parquet')