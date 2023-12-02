import regex
import os
import sys

def day1_calibration(file_name):
    path = os.getcwd() + "/" + file_name
    running_total = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            match = regex.findall("([0-9])", line)
            end = len(match) -1
            arg_one = match[0]
            arg_two = match[end]
            calibration = int(arg_one+arg_two)
            print(f"{line[:-1]}|{match}|{calibration}")
            running_total += calibration
    print(running_total)

def day1_calibration_adjust(file_name):
    spell_to_number = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    path = os.getcwd() + "/" + file_name
    running_total = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            line_whole = line
            match = regex.search("([0-9]|one|two|three|four|five|six|seven|eight|nine)", line)
            matches = []
            while match != None and len(line) > 1:
                matches.append(match[0])
                if not match[0].isdigit():
                    line = line[match.span()[1]-1:]
                else:
                    line = line[match.span()[1]:]
                match = regex.search("([0-9]|one|two|three|four|five|six|seven|eight|nine)", line)
            end = len(matches) - 1
            arg_one = matches[0] if matches[0].isdigit() else spell_to_number[matches[0]]
            arg_two = matches[end] if matches[end].isdigit() else spell_to_number[matches[end]]
            calibration = int(arg_one+arg_two)
            print(f"{line_whole[:-1]}|{matches}|{calibration}")
            running_total += calibration
    print(running_total)
            
def main():
    if len(sys.argv) == 3 and sys.argv[1] == 'adjust':
        day1_calibration_adjust(sys.argv[2])
    else:
        day1_calibration(sys.argv[1])

if __name__ == "__main__":
    main()