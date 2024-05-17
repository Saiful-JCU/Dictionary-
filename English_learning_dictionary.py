'''
write a programme to  create an english learning dictionary, the dictionary must have three basic functions: add,
 query, and exit. the program reads the dictionary file dict.txt, and if it does not exist, it creates one. the
  dictionary file is stored in the format "English write chinese meaning", with only one pair of chinese and
  english explanation.per line, the program will enter the corresponding function module according to the user
  choice and display the corresponding operation prompts.
  when the added word already exist, display "the word has already been added to the dictionary library"; when
  the queried word does not exist, display "the word was not found in the dictionary library". when word was not
  found in the dictionary library". when the user enters other options, prompt "input error"
'''


import os
import csv # i import this module for save all data on a csv file
def load_dictionary(file_name):
    dictionary = {}

    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the row has at least two elements
                if len(row) >= 2:
                    dictionary[row[0]] = row[1]
                else:
                    print("Skipping invalid row:", row)
    return dictionary


def save_dictionary(dictionary, file_name): # in this function, we use 'cs.writer' to write each row to the CSV file.
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for english_word, chinese_meaning in dictionary.items():
            writer.writerow([english_word, chinese_meaning])

def add_word(dictionary): # this function will take input form user
    english_word = input("Enter English word: ")
    if english_word in dictionary:
        print("The word has already been added to the dictionary library.")
    else:
        chinese_meaning = input("Enter Chinese meaning: ")
        dictionary[english_word] = chinese_meaning
        print("Word added successfully!")

def query_word(dictionary): #this function will ckeck the word is available in this dictionary or not. 
    english_word = input("Enter English word to query: ")
    if english_word in dictionary:
        print(f"Chinese meaning: {dictionary[english_word]}")
    else:
        print("The word was not found in the dictionary library.")

def main():
    dictionary_file = "dict.csv" # the storese file name will be dict and csv formated. 
    dictionary = load_dictionary(dictionary_file)

    while True: # this while loop will give three option to user for chose. then whole code will work as like the user want. 
        print("\n1. Add word")
        print("2. Query word")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_word(dictionary) # if user choice 1 then this loop will run the add_word function.
        elif choice == "2":
            query_word(dictionary)
        elif choice == "3":
            save_dictionary(dictionary, dictionary_file)
            print("Dictionary saved.")
            break
        else:
            print("Input error. Please enter a valid option.")

if __name__ == "__main__":
    main()
