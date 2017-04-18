""" Perform the whole process of processing data. """

import csv_reader
import data_analyzer
import xml_writer


def main():

    input_file_path = \
        raw_input("Enter the relative path of the CSV file that would be processed: ")
    output_file_path = \
        raw_input("Enter the relative path of the XML file that would be generated: ")

    data = csv_reader.get_data(input_file_path)
    feature_data = data_analyzer.process_data(data)

    xml_writer.write_data_to_xml(feature_data, output_file_path)

    print ("The XML file has been successfully generated.")

if __name__ == "__main__":
    main()
