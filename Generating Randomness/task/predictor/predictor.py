import random


def profile(triad, data_string):
    num_of_zeroes = 0
    num_of_ones = 0
    pos = -1
    # I have no idea how this works.
    while True:
        pos = data_string.find(triad, pos + 1)
        if pos == -1:
            break
        else:
            if len(data_string) > pos + 3:
                if data_string[pos + 3] == "0":
                    num_of_zeroes += 1
                else:
                    num_of_ones += 1
    # print(f"{triad}: {num_of_zeroes}, {num_of_ones}")
    # return f"{triad} {num_of_zeroes} {num_of_ones}"
    if num_of_ones > num_of_zeroes:
        return 1
    elif num_of_zeroes > num_of_ones:
        return 0
    else:
        return random.randint(0, 1)


full_input = []
while len(full_input) < 100:
    print("Print a random string containing 0 or 1:")
    print()
    partial_input = list(input())
    for char in partial_input:
        if char == "0" or char == "1":
            full_input.append(char)
    print(f"Current data length is {len(full_input)}, {100 - len(full_input)} symbols left")
print("Final data string:")
print("".join(full_input))
print()
print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
print("")
capital = 1000
test_string = ""
while True:
    print("Print a random string containing 0 or 1:")
    test_string = input()
    if test_string == "enough":
        break
    for char in test_string:
        if char != "0" and char != "1":
            test_string = test_string.replace(char, "")
    if len(test_string) < 3:
        continue
    print("prediction:")
    predictions = {
        '000': profile("000", "".join(full_input)),
        '001': profile("001", "".join(full_input)),
        '010': profile("010", "".join(full_input)),
        '011': profile("011", "".join(full_input)),
        '100': profile("100", "".join(full_input)),
        '101': profile("101", "".join(full_input)),
        '110': profile("110", "".join(full_input)),
        '111': profile("111", "".join(full_input))
    }
    first = 0
    last = 3
    predicted_string = ['0', '1', '1']
    while last < len(test_string):
        predicted_string.append(str(predictions[test_string[first:last]]))
        first += 1
        last += 1
    print("".join(predicted_string))
    test_string_minus_3 = test_string[3:]
    predicted_string_minus_3 = predicted_string[3:]
    count = 0
    total_guessed = 0
    while count < len(test_string_minus_3):
        if test_string_minus_3[count] == predicted_string_minus_3[count]:
            total_guessed += 1
            capital -= 1
        else:
            capital += 1
        count += 1
    percentage = (float(total_guessed) / float(len(test_string_minus_3))) * 100
    print("")
    print(f"Computer guessed right {total_guessed} out of {len(test_string_minus_3)} symbols ({percentage:.2f} %)")
    print(f"Your capital is now ${capital}")
    print("")
print("Game over!")
