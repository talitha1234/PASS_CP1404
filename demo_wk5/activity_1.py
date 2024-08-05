"""Splitting strings"""

short_sentence = "The cake is a lie"
long_sentence = "Don't worry if it doesn't work right. If everything did, you'd be out of a job"

# What will the following print statements show?
print(len(short_sentence))  # 1
print(len(long_sentence))  # 2
print(short_sentence.find("i"))  # 3
print(short_sentence[9])
print(short_sentence[:4] + long_sentence[:8])  # 4
print(short_sentence[4:9] + long_sentence[18:30])  # 5
print(short_sentence[:4] + long_sentence[-3:] + short_sentence[8:])  # 6
print(short_sentence[:-5])  # 7
print(short_sentence[:-5] + long_sentence[-5:])  # 8
print(short_sentence[-5:].capitalize() + " " + short_sentence[:11].lower())  # 9
print(long_sentence[-21:].title())  # 10
print("Short: {}. Long: {}.".format(long_sentence, short_sentence))  # 11
print(f"Short: {long_sentence}.Long{short_sentence}")  # 12
print("Short: {}. Also Short: {}.".format(short_sentence, long_sentence[:36]))  # 13

second_word, third_word, fourth_word, fifth_word, = short_sentence.split()
words = short_sentence.split()
print(words[1], words[3], words[2], words[0], words[4])  # 14
print(second_word, fourth_word, third_word, first_word, fifth_word)  # 15
