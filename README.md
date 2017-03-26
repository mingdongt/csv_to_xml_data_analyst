# csv_to_xml_data_analyst
A python program which reads data from csv file safely then generates and writes feature data to a xml file. 
## Project Details


Given a CSV file, find out and calculate the following information for each column:

#### Attribute name, the column name

#### Data type: integer, float, or string

integer: whole number, e.g. 1, 5 and 23678

float: real number that supports decimal point, e.g. 3.14, 777.8 and 1.0

string: categorical values, e.g. Male/Female and RAIN/SUNNY/CLOUDY

Assume the first row of the CSV file contains the attribute name and each column contains data of the same type.

#### For all columns, find out their mode(s).

Mode(s), the most common value(s) in the column, except when the value only appears once. This means modes appear at least twice in the corresponding column.


#### For numerical columns (float and integer types), provide five-number-summary,

Calculate the five-number-summary of each numerical column (integer and float) of the CSV data. 

Five-number-summary is descriptive statistical properties proposed by Tukey [1]. The summary provides a concise report of central tendency and distribution of a data set. It consists of the following:

Minimum value

Lower/first quartile ()

Median ()

Upper/third quartile ()

Maximum value

#### For string, provide unique values of the column values. 

For example, if a column contains the following data ['A','B','C','A','A','C','D'], then the unique values are ['A','B','C','D'].

## XML
The result of this process should then be written into an XML file called output.xml.

This XML file should be well-formed valid against summary.dtd