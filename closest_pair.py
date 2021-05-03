import os
import csv
import matplotlib.pyplot as plt
import math

cwd_path = os.getcwd()
file_path = 'files'


def read_file(file_name):
    """
    Reads csv file from given folder
    :param file_name: (str) the name of csv file
    :return:
    """
    data_points = []
    with open(os.path.join(cwd_path, file_path, file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip header
        next(csv_reader)

        # read each row
        for row in csv_reader:
            data_points.append([float(number) for number in row])

    return data_points


def draw_data(data_points, closest_pair=[]):
    """
    Function creates new figure and draw data points into scatter plot.
    :param data_points: (list of lists): each sublist is 1x2 list with x and y coordinate of a point.
    :param closest_pair: (tuple of ints): indices of the closest pair of points, default = empty list
    :return:
    """

    plt.scatter(
        x=[point[0] for point in data_points],
        y=[point[1] for point in data_points],
        color=['blue' if point not in closest_pair else 'red' for point in data_points]
    )
    plt.show()
    
def closest_pair_BF(array):
    min_dist = math.dist(array[0], array[1])
    point_1 = array[0]
    point_2 = array[1]
    num_points = len(array)

    if num_points == 2:
        return point_1, point_2, min_dist

    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            if i != 0 and j != 1:
                dist = math.dist(array[i], array[j])
                if dist < min_dist:
                    min_dist = dist
                    point_1, point_2 = array[i], array[j]
    return point_1, point_2, min_dist


def closest_split_pair(x_wise, y_wise, min_dist, points):
    num_points = len(x_wise)
    midpoint_x = x_wise[num_points // 2][0]

    subarray_y = [x for x in y_wise if midpoint_x - min_dist <= midpoint_x <= midpoint_x + min_dist]
    min_dist_new = min_dist
    len_y = len(subarray_y)

    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            point_1, point_2 = subarray_y[i], subarray_y[j]
            dst = math.dist(point_1, point_2)
            if dst < min_dist_new:
                min_dist_new = dst
                points = point_1, point_2

    return points[0], points[1], min_dist_new

def closest_pair(x_wise, y_wise):
    num_points = len(x_wise)
    mid_idx = num_points // 2

    if num_points <= 3:
        point_1, point_2, min_dist = closest_pair_BF(x_wise)
        return point_1, point_2, min_dist

    left_x = x_wise[:mid_idx]
    right_x = x_wise[mid_idx:]

    mid_point = x_wise[mid_idx][0]
    left_y = list()
    right_y = list()

    for point in y_wise:
        if point[0] <= mid_point:
            left_y.append(point)
        else:
            right_y.append(point)

    (p1, q1, md1) = closest_pair(left_x, left_y)
    (p2, q2, md2) = closest_pair(right_x, right_y)

    if md1 <= md2:
        min_dist = md1
        points = (p1, q1)
    else:
        min_dist = md2
        points = (p2, q2)

    (p3, q3, md3) = closest_split_pair(x_wise, y_wise, min_dist, points)
    if min_dist <= md3:
        return points[0], points[1], min_dist
    else:
        return p3, q3, md3


def main(file_name):
    # read data points
    data_points = read_file(file_name)

    # draw points
    draw_data(data_points)

    sorted_by_x = sorted(data_points, key = lambda x: x[0])
    sorted_by_y = sorted(data_points, key = lambda x: x[1])
    p1, p2, mi = closest_pair_BF(sorted_by_y)
    point_1, point_2, min_dist = closest_pair(sorted_by_x, sorted_by_y)
    print(min_dist)
    print(point_1)
    print(point_2)

    draw_data(data_points, [p1, p2])

if __name__ == '__main__':
    my_file = 'points.csv'
    main(my_file)
