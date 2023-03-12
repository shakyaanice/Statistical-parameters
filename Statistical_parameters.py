import statistics

def calculate_mean(lst):
    """
    Calculates the arithmetic mean of a list.

    Args:
    - lst (list): the list of numbers to be averaged

    Returns:
    - mean (float): the arithmetic mean of the list
    """
    mean = sum(lst) / len(lst)
    return mean


def calculate_median(lst):
    """
    Calculates the median of a list.

    Args:
    - lst (list): the list of numbers to be sorted and analyzed

    Returns:
    - median (float): the median of the list
    """
    lst_sorted = sorted(lst)
    mid = len(lst_sorted) // 2
    if len(lst_sorted) % 2 == 0:
        median = (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        median = lst_sorted[mid]
    return median


def calculate_mode(lst):
    """
    Calculates the mode of a list.

    Args:
    - lst (list): the list of numbers to be analyzed

    Returns:
    - mode (float or str or None): the mode of the list, or None if there is no mode
    """
    try:
        mode = statistics.mode(lst)
    except statistics.StatisticsError:
        mode = None
    return mode


def calculate_range(lst):
    """
    Calculates the range of a list.

    Args:
    - lst (list): the list of numbers to be analyzed

    Returns:
    - range (float or int): the range of the list
    """
    lst_sorted = sorted(lst)
    range_ = lst_sorted[-1] - lst_sorted[0]
    return range_


def calculate_variance(lst):
    """
    Calculates the variance of a list.

    Args:
    - lst (list): the list of numbers to be analyzed

    Returns:
    - variance (float): the variance of the list
    """
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance


def calculate_std(lst):
    """
    Calculates the standard deviation of a list.

    Args:
    - lst (list): the list of numbers to be analyzed

    Returns:
    - std (float): the standard deviation of the list
    """
    std = statistics.stdev(lst)
    return std
