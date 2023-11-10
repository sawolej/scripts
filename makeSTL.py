import numpy as np
import csv
from stl import mesh
import sys

def read_csv_to_numpy_array(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header
        data_list = list(reader)
    return np.array(data_list).astype(np.float64)

def create_mesh(data, scale_factor=3):
    points = []
    for i in range(data.shape[0] - 1):
        for j in range(data.shape[1] - 1):
            z1 = data[i][j] * scale_factor
            z2 = data[i][j + 1] * scale_factor
            z3 = data[i + 1][j] * scale_factor
            z4 = data[i + 1][j + 1] * scale_factor
            points.append([[j, i, z1], [j + 1, i, z2], [j, i + 1, z3]])
            points.append([[j + 1, i, z2], [j + 1, i + 1, z4], [j, i + 1, z3]])
    your_mesh = mesh.Mesh(np.zeros(len(points), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(points):
        for j in range(3):
            your_mesh.vectors[i][j] = np.array(f[j])
    return your_mesh

def save_stl(mesh, filename):

    mesh.save(filename)


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: python script.py data.csv")

        sys.exit(1)

    csv_file_path = sys.argv[1]

    try:

        data = read_csv_to_numpy_array(csv_file_path)
        your_mesh = create_mesh(data)
        stl_file_name = csv_file_path.replace('.csv', '.stl')
        save_stl(your_mesh, stl_file_name)
        print(f"STL file '{stl_file_name}' has been created successfully.")

    except Exception as e:

        print(f"An error occurred: {e}")

