#!/usr/bin/env python3

'''json2dotnet_wireformat - Convert JSON to ASP.NET wire format'''

from json import loads
from urllib.parse import quote
from sys import stdin, stdout, stderr, exit


# -----------------------------------------------------------------------------
def process_dict(prefix, values):
    '''Process element of dictionary type'''

    results = []

    for key, value in values.items():
        sub_prefix = '%s.%s' % (prefix, quote(str(key)))
        results.extend(process_element(sub_prefix, value))

    return results


# -----------------------------------------------------------------------------
def process_list(prefix, values):
    '''Process element of list type'''

    results = []

    for index, value in enumerate(values):
        sub_prefix = '%s[%i]' % (prefix, index)
        results.extend(process_element(sub_prefix, value))

    return results


# -----------------------------------------------------------------------------
def process_element(prefix, value):
    '''Processes element in JSON structure'''

    if type(value) is bool:
        return [prefix + '=' + str(value).lower()]

    elif isinstance(value, (str, int, float)):
        return [prefix + '=' + quote(str(value))]

    elif type(value) is list:
        return process_list(prefix, value)

    elif type(value) is dict:
        return process_dict(prefix, value)

    else:
        raise Exception('Unknown data type in list')


# -----------------------------------------------------------------------------
def process_json(json_data):
    '''Main processing function - returns provided JSON data in wire format'''

    try:
        source = loads(json_data)

        if not type(source) is dict:
            raise

    except:
        raise Exception('Failed to parse provided data as complex JSON')

    # -------------------------------------------------------------------------
    results = []
    
    for key, value in source.items():
        prefix = quote(str(key))

        results.extend(process_element(prefix, value))

    return '&'.join(results)


# -----------------------------------------------------------------------------
def main():
    '''Main function for standalone execution'''

    try:
        json_data = stdin.read()
        print(process_json(json_data))

        exit(0)

    except Exception as error_msg:
        print('json2dotnet_wireformat failed: "%s"' % error_msg, file=stderr)
        exit(1)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
