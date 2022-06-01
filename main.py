# 25 May 2022
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in nato_df.iterrows():
    # print(index)
    # print(row.letter)
    nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
    # print(nato_alphabet_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    change_this = input("Enter a word to be transcribed into the NATO phonetic alphabet: ").upper()
    try:
        changed_word = [nato_alphabet_dict[letter] for letter in change_this]
    except KeyError:
        print("Only input letters in the alphabet please.")
        generate_phonetic()
    else:
        print(changed_word)


generate_phonetic()
