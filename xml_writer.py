""" A module of xml writer which writes feature data set into a xml file. """

from lxml import etree


def write_data_to_xml(feature_data, xml_name):
    """ write data to xml file. """

    root = etree.Element('attributes')

    for column in feature_data:

        column_branch = etree.SubElement(root, 'attribute')
        column_branch.attrib["type"] = column['data_type']

        name_branch = etree.SubElement(column_branch, 'name')
        name_branch.text = column['attribute_name']

        if column['data_type'] != 'string':

            properties_branch = etree.SubElement(column_branch, 'properties')
            for key, attribute_value in (('minimum_value', 'min'),
                                         ('first_quartile', 'q1'),
                                         ('median', 'median'),
                                         ('third_quartile', 'q3'),
                                         ('maximum_value', 'max')
                                         ):

                build_property_branch(properties_branch, column[key],
                                      'property', 'name', attribute_value)

        try:
            get_modes = column['modes']
            modes_branch = etree.SubElement(column_branch, 'modes')
            for mode in get_modes:
                mode_branch = etree.SubElement(modes_branch, 'mode')
                mode_branch.text = mode
        except ValueError:
            pass

        if column['data_type'] == 'string':
            uniques_branch = etree.SubElement(column_branch, 'uniques')
            for value in column['unique_values']:
                unique_branch = etree.SubElement(uniques_branch, 'unique')
                unique_branch.text = value

    output = etree.tostring(root,
                            pretty_print=True,
                            encoding="UTF-8",
                            xml_declaration=True)

    open(xml_name, 'w').write(output)


def build_property_branch(root, branch_content, branch_name, attribute,
                          attribute_value):
    """ Build property branch on the basis of root. """

    branch = etree.SubElement(root, branch_name)
    branch.attrib[attribute] = attribute_value
    branch.text = branch_content

