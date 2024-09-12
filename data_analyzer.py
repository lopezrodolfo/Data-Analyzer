"""
Module: data_analyzer

Module that allows us to import, analyze, and graph data that has a linear relationship.

Authors:
1) Rodolfo Lopez (rodolfolopez@sandiego.edu)
"""

import matplotlib.pyplot as pp


def mean(num_list):
    """
    Calculates and returns the arithmetic mean of num_list.

    Parameters:
    num_list (type: list) - A list of numbers

    Returns:
    total / len(num_list) (type: float) - The arithmetic mean of the input list
    """

    if len(num_list) == 0:
        return 0.0

    total = 0
    for num in num_list:
        total += num
    return total / len(num_list)


def separate(data_points):
    """
    Splits the provided list of (x, y) tuples into two separate lists:
    one for x-values and another for y-values and returns them.

    Parameters:
    data_points (type: list) - A list of (x, y) tuples

    Returns:
    x_values (type: list) - A list of x-values
    y_values (type: list) - A list of y-values
    """

    x_values = [x for (x, y) in data_points]
    y_values = [y for (x, y) in data_points]

    return x_values, y_values


def regression_slope(data_points):
    """
    Calculates and returns the slope of the linear regression line for the given data points.

    Parameters:
    data_points (type: list) - A list of (x, y) tuples representing data points

    Returns:
    m (type: float) - The slope of the linear regression line
    """

    x_values, y_values = separate(data_points)
    x_mean = mean(x_values)
    y_mean = mean(y_values)

    xy_sum = 0
    x2_sum = 0
    for i, x in enumerate(x_values):
        xy_sum += x * y_values[i]
        x2_sum += x**2
    m = xy_sum - len(data_points) * x_mean * y_mean
    m = m / (x2_sum - len(data_points) * x_mean**2)

    print("Regression Slope: ", m)
    return m


def plot_regression(data_points):
    """
    Plots a pyplot linear regression line of the given (x,y) data_points.

    Parameters:
    data_points (type: list) - A list of (x, y) tuples representing data points

    Returns:
    None
    """

    x_values, y_values = separate(data_points)
    x_mean = mean(x_values)
    y_mean = mean(y_values)
    m = regression_slope(data_points)

    x_values_line = [0, max(x_values)]
    y_values_line = []

    for x in x_values_line:
        y_values_line.append(y_mean + m * (x - x_mean))

    pp.plot(x_values_line, y_values_line)


def plot_data(data_points):
    """
    Creates a pyplot scatter plot of the given (x,y) data_points.

    Parameters:
    data_points (type: list) - A list of (x, y) tuples representing data points

    Returns:
    None
    """

    x_values, y_values = separate(data_points)
    pp.scatter(x_values, y_values)


def get_data(filename):
    """
    Reads data points from a CSV file.

    Parameters:
    filename (type: str) - The name of the CSV file to read

    Returns:
    data_points (type: list) - A list of (x, y) tuples representing data points
    x_label (type: str) - The label for the x-axis
    y_label (type: str) - The label for the y-axis
    """

    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline()
        x_label, y_label = header.split(",")
        y_label = y_label.strip()

        data_points = []
        for line in f:
            x_value, y_value = line.split(",")
            if y_value.find("\n") != -1:
                y_value = y_value.strip()
            data_points.append((float(x_value), float(y_value)))

    return (data_points, x_label, y_label)


def main():
    """
    Generates a scatter plot along with a line of best fit for the dataset
    specified by the user through a filename input.

    Parameters:
    None

    Returns:
    None
    """

    data_filename = input("Enter the name of the csv data file: ")
    data_points, x_label, y_label = get_data(data_filename)
    pp.xlabel(x_label)
    pp.ylabel(y_label)
    plot_data(data_points)
    plot_regression(data_points)
    pp.show()


# Don't modify anything below this point.


if __name__ == "__main__":
    main()
