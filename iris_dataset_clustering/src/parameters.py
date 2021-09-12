import os
import sys

NO_OF_CLUSTERS = int(os.environ.get('NO_OF_CLUSTERS') or 2)
CONVERGENCE = float(os.environ.get('THRESHOLD_VALUE') or 0.0001)
EPSILON = float(os.environ.get('EPSILON') or sys.float_info.epsilon)
DATASET_NAME = os.environ.get('DATASET_NAME') or 'IRIS'
DATASET = {'IRIS': {'dimension': 4}}
DIM = DATASET[DATASET_NAME]['dimension']
