import numpy as np

def calculate(list):
    try:
        array = np.array(list).reshape(3,3)

        calculations = {
            'mean' : [np.mean(array, axis = 0).tolist(), np.mean(array, axis = 1).tolist(), np.mean(array)],
            'variance' : [np.var(array, axis = 0).tolist(), np.var(array, axis = 1).tolist(), np.var(array)],
            'standard deviation' : [np.std(array, axis = 0).tolist(), np.std(array, axis = 1).tolist(), np.std(array)],
            'max' : [np.max(array, axis = 0).tolist(), np.max(array, axis = 1).tolist(), np.max(array)],
            'min' : [np.min(array, axis = 0).tolist(), np.min(array, axis = 1).tolist(), np.min(array)],
            'sum' : [np.sum(array, axis = 0).tolist(), np.sum(array, axis = 1).tolist(), np.sum(array)]
        }

        return calculations
    
    except ValueError:
        print("List must contain nine numbers")