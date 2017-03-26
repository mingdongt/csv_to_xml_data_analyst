"""A pure csv reader which returns a data in rows"""

import csv


class NotEnoughDataException(Exception):
    pass


def get_data(file_name):
    """ Return a nested list containing data of the csv file with file_name
     which is under the current directory"""

    with open(file_name) as fp:
        rows = csv.reader(fp)

        data = [row for row in rows]

        # Raise Exception if the file is empty or only has header.
        if len(data) <= 1:
            raise NotEnoughDataException
        else:
            return data
