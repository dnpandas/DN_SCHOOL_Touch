# project_dbconfig.py

from configparser import ConfigParser


def read_db_configuration(filename='configuration_project.ini', section='postgresql'):
    """ Read the database configuration file and generate a dictionary object.
    :param filename: configuration file name
    :param section: section of database configuration
    :return: a dictionary that contains dataabase parameter
    """

    # Create a perser and read this configuration file
    parser = ConfigParser()
    parser.read(filename)

    # Reading section, the default is postgresql
    db = {}
    if parser.has_section(section):
        arr_item = parser.items(section)
        for item in arr_item:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the file {1}'.format(section, filename))
    
    return db
    
