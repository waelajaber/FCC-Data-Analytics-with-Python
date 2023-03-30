import numpy as np

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def calculate(list):
    length = len(list)
    if length != 9:
        raise ValueError("List must contain nine numbers.")

    arrays = np.array_split(list, 3, axis=0)
    matrix = np.reshape(arrays, (3, 3))

    mean_axis_0 = np.mean(matrix, axis=0).tolist()
    mean_axis_1 = np.mean(matrix, axis=1).tolist()
    mean_flat = np.mean(list).tolist()

    var_axis_0 = np.var(matrix, axis=0).tolist()
    var_axis_1 = np.var(matrix, axis=1).tolist()
    var_flat = np.var(list).tolist()

    std_axis_0 = np.std(matrix, axis=0).tolist()
    std_axis_1 = np.std(matrix, axis=1).tolist()
    std_flat = np.std(list).tolist()

    max_axis_0 = np.max(matrix, axis=0).tolist()
    max_axis_1 = np.max(matrix, axis=1).tolist()
    max_flat = np.max(list).tolist()

    min_axis_0 = np.min(matrix, axis=0).tolist()
    min_axis_1 = np.min(matrix, axis=1).tolist()
    min_flat = np.min(list).tolist()

    sum_axis_0 = np.sum(matrix, axis=0).tolist()
    sum_axis_1 = np.sum(matrix, axis=1).tolist()
    sum_flat = np.sum(list).tolist()

    calculations = {
        'mean': [mean_axis_0, mean_axis_1, mean_flat],
        'variance': [var_axis_0, var_axis_1, var_flat],
        'standard deviation': [std_axis_0, std_axis_1, std_flat],
        'max': [max_axis_0, max_axis_1, max_flat],
        'min': [min_axis_0, min_axis_1, min_flat],
        'sum': [sum_axis_0, sum_axis_1, sum_flat],
    }

    return calculations


# calculate(l)
print(calculate(l))

# print(arrays)
# print(matrix)

# print(mean_axis_0)
# print(mean_axis_1)
# print(mean_flat)

# print(var_axis_0)
# print(var_axis_1)
# print(var_flat)

# print(max_axis_0)
# print(max_axis_1)
# print(max_flat)

# print(min_axis_0)
# print(min_axis_1)
# print(min_flat)

# print(sum_axis_0)
# print(sum_axis_1)
# print(sum_flat)
