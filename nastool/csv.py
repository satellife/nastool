import numpy as np

def read_mass_point_from_csv(filename):
    '''
    Read mass point data with coordinates from .csv file.
    '''
    data = np.loadtxt(filename, delimiter=',', skiprows=0, encoding="utf-8-sig", dtype=str)
    massmap = []
    for i in range(data.shape[0]):
        mass_point = [data[i, 1], data[i, 2], data[i, 3], data[i, 4]]
        mass_point = [float(i) for i in mass_point]
        massmap.append(mass_point)
    return massmap