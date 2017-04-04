""" A module of data analyzer which returns feature data for input data. """

from collections import defaultdict

MINIMUM_MODE_APPEARANCE_TIME = 2


def process_data(data):
    """ Main worker function which returns the feature data set. """

    data = data_in_columns(data)
    feature_data = []

    for column in data:

        column_feature_data = {}
        column_feature_data['attribute_name'] = get_attribute_name(column)

        # Get rid of the header
        column = column[1:]

        column_feature_data['data_type'] = data_type(column)
        frequency_stats = frequency_stats_of_values(column)
        modes, max_frequency = modes_data(frequency_stats)

        if max_frequency >= MINIMUM_MODE_APPEARANCE_TIME:
            column_feature_data['modes'] = modes

        if data_type(column) == 'string':
            column_feature_data['unique_values'] = frequency_stats.keys()

        else:

            column = sorted(column, key=float)
            column_feature_data['minimum_value'] = column[0]
            column_feature_data['maximum_value'] = column[-1]

            column_feature_data['median'], \
                column_feature_data['first_quartile'],\
                column_feature_data['third_quartile'] = get_medians(column)
        feature_data.append(column_feature_data)

    return feature_data


def get_median_data(nums):
    """ Return the data of median of a group of sorted number. """

    nums = map(float, nums)

    median_position = (1 + len(nums)) / 2

    if (1 + len(nums)) % 2:

        median_number = (nums[median_position] + nums[median_position - 1]) / 2
        # Shown result as integer if possible
        if median_number.is_integer():
            median_number = int(median_number)
    else:
        median_number = nums[median_position]

    return median_number, median_position


def get_medians(nums):
    """ Return median number, first and third quartile for a group of
    sorted numbers.
    """
    median_number, position = get_median_data(nums)
    first_quartile, _ = get_median_data(nums[:position])
    third_quartile, _ = get_median_data(nums[position:])

    return map(str, (median_number, first_quartile, third_quartile))


def data_in_columns(data):
    """ Convert and return the nested list containing data in columns. """

    return zip(*data)


def get_attribute_name(column):
    """ Return the attribute name of the column. """

    return column[0]


def data_type(column):
    """ Return the data type of the column. """

    for unit in column:
        try:
            int(unit)

        except ValueError:
            try:
                # Stop and return type if it can be determined
                float(unit)
                return 'float'
            except ValueError:
                return 'string'

    return 'integer'


def frequency_stats_of_values(column):
    """ Return a dict containing the frequency data of values in the column.
    """

    frequency_data = defaultdict(int)

    for unit in column:
        frequency_data[unit] += 1
    return frequency_data


def modes_data(stats):
    """ Return the data of modes according to the statistics. """

    max_frequency = max(stats.values())

    return [key
            for key, value in stats.items()
            if value == max_frequency], max_frequency



