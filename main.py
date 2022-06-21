import nastool.bdf as bdf
import nastool.mass_point as mp

## function: read mass-point-map from .csv file and write to .bdf file.

model = bdf.create_bdf()

massmap = mp.read_mass_point_from_csv("D:/ProjectX/Workp/CATCH/Input/质量点信息.csv")
# print(massmap)
model = mp.massmap_to_bdf(massmap, model)

model.write_bdf("D:/ProjectX/Workp/CATCH/Input/mass.bdf")