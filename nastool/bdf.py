from pyNastran.bdf.bdf import BDF

def create_bdf(debug=False):
    bdf = BDF(debug=debug)
    return bdf

def write_bdf(bdf, filename):
    bdf.write_bdf(filename)

def read_bdf(filename, debug=False):
    bdf = BDF(debug=debug)
    bdf.read_bdf(filename)
    return bdf

if __name__ == '__main__':
    pass