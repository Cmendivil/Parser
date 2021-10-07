import sys
import re


def parser(lines):
    data = {}
    for line in lines:
        line = line.strip(" \n")

        if re.match('^#.', line):  # check for comments
            pass
        elif re.match('^([\w]+[ ]*)(=){1}([^=].)+',line):  # check for valid input
            value = line.split('=', 1)
            value[0] = value[0].strip()
            value[1] = value[1].strip()

            styled_value = None
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
        else:
            raise Exception("Invalid data \'%s\'" % line)
            pass

    return data


def main():
    if sys.argv[1] is None:
        return

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    data = parser(lines)

    print("Data for host %s with server id %d was saved" % (data['host'], data['server_id']))


main()
