'''
Main purpose:
    Read/write mass point data from/to a .bdf file.

    1. To read mass point data from .csv or .xlsx/.xls file.
    2. To write mass point data to .bdf object.
    3. Read mass point data from .bdf object.
'''


import nastool.csv as csv


def massmap_to_bdf(massmap, bdf):
    '''
    Write mass point data to .bdf object.
    '''
    nid = 0
    eid = 0
    for mass_point in massmap:
        nid += 1
        eid += 1
        bdf.add_grid(nid=nid, xyz=[-(mass_point[1] + 10), -mass_point[2], mass_point[3] - 222.725])
        bdf.add_conm2(eid=eid, mass=mass_point[0], nid=nid)

    bdf.cross_reference()
    return bdf


if __name__ == '__main__':
    import sys
    # Read mass point data from .csv file.
    # path = "D:/ProjectX/Workp/CATCH/Input/质量点信息.csv"
    path = sys.argv[1]
    massmap = csv.read_mass_point_from_csv(path)
    print(massmap)