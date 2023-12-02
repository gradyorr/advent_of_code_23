import os
import sys
import regex

def day2_minimal_bag_game(filename):
    path = os.getcwd() + "/" + filename
    running_total = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            print(line[:-1]) # each game print out the line
            indexColon = line.find(":")
            rounds = line[indexColon+1:].split(";")
            rgb = {"red":0,"green":0,"blue":0}
            for round in rounds:
                eaches = round.split(", ")
                print(eaches)
                for each in eaches:
                    number_re = regex.match("[^0-9]*([0-9]+)[^0-9]*", each)
                    color_re = regex.match(".*[0-9] ([a-z]*).*", each)
                    number = int(number_re.group(1))
                    color = color_re.group(1)
                    if rgb[color] < number:
                        rgb[color] = number
            print(f"Minimal set is {rgb}")
            power = rgb["red"] * rgb["green"] * rgb["blue"]
            running_total += power
        print(running_total)

def day2_bag_game(filename):
    path = os.getcwd() + "/" + filename
    running_total = 0
    with open(path, 'r') as file:
        for line in file.readlines(filename):
            print(line[:-1])
            indexColon = line.find(":")
            game_id_re = regex.match("[^0-9]*([0-9]+)[^0-9]*", line[0:indexColon])
            game_id = int(game_id_re.group(1))
            running_total += game_id
            rounds = line[indexColon+1:].split(";")
            round_impossible = False
            for round in rounds:
                rgb = {"red":12,"green":13,"blue":14}
                eaches = round.split(", ")
                print(eaches)
                for each in eaches:
                    number_re = regex.match("[^0-9]*([0-9]+)[^0-9]*", each)
                    color_re = regex.match(".*[0-9] ([a-z]*).*", each)
                    number = int(number_re.group(1))
                    color = color_re.group(1)
                    if (rgb[color] - number) < 0:
                        print(f"{number} {color} is impossible. Expected max of {rgb[color]} {color}. Subtracting {game_id} from {running_total}")
                        running_total -= game_id
                        round_impossible = True
                        break
                if round_impossible:
                    round_impossible = False
                    break
        print(running_total)
def main():
    if len(sys.argv) == 3 and sys.argv[1] == 'power':
        day2_minimal_bag_game(sys.argv[2])
    elif len(sys.argv) == 2:
        day2_bag_game(sys.argv[1])
    else:
        print("python3 day1.py \"opt power\" datafile")

if __name__ == "__main__":
    main()