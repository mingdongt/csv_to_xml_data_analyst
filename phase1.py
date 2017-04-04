import csv_reader
import data_processor
import xml_writer

INPUT_CSV_FILE_NAME = 'input.csv'
OUTPUT_XML_FILE_NAME = 'output.xml'


def main():

    data = csv_reader.get_data(INPUT_CSV_FILE_NAME)
    feature_data = data_processor.process_data(data)
    xml_writer.write_data_to_xml(feature_data, OUTPUT_XML_FILE_NAME)


if __name__ == "__main__":
    main()
