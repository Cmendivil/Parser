# Parser
The program runs with the following command:
```bash
python parser.py config.text 
```
🚧 Pyhton 3.8.10 was used

The main function in the parse.py file will read the file from the command line and it will create an array of strings that will be passed to the parse function. This function will show a message after the parse is done. The parsed data will be saved in the `data` variable and the data could be accessed by calling `data[':variable_name']`.

```python
def main():
    if sys.argv[1] is None:
        return

    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
    file.close()

    data = parser(lines)

    print("Data for host %s with server id %d was saved" % (data['host'], data['server_id']))
```

The parser data will iterate through the array and saved valid variables into a dictionary that will be returned at the end.

```python
def parser(lines):
    '''
    :param lines: an array of lines to be parsed
    :return: a dictionary with all the valid data from the lines array
    '''
    data = {}
    for line in lines:
        line = line.strip(" \n")

        if re.match('^#.', line):  # check for comments
            continue
        elif re.match('^([\w]+[ ]*)(=){1}([^=].)+',line):  # check for valid input
            value = line.split('=', 1)
            value[0] = value[0].strip()
            value[1] = value[1].strip()

            styled_value = None
            # check variable type and save it correctly
            if re.match('true|on|yes', value[1]):
                styled_value = True
            elif re.match('false|off|no', value[1]):
                styled_value = False
            elif re.match('^(\d)+$', value[1]):
                styled_value = int(value[1])
            elif re.match('^(\d)+\\.(\d)+$', value[1]):
                styled_value = float(value[1])
            else:
                styled_value = value[1]

            data[value[0]] = styled_value
        else:  # Raise exeption in case of invalid data
            raise Exception("Invalid data - \'%s\'" % line)

    return data
```
