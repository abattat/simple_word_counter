#!/usr/bin/python
# Author  : Andrew Battat
# Date    : 7-23-18

'''
Description:
  This program accepts a text file and returns the number of occurences of each word in the file

  The programm is called like such:
    ./wordcount.py {--count | --topcount} input_file [output_file]

  The user must give the program one of two count options:
    count:
      prints a sorted list of every word found in the text file along with each word's number of occurences
    topcount:
      prints the 20 most common words found in the text file along with each word's number of occurences

  The user must give the program an input file, which is the text file the program reads from

  The user has the option of giving the program an output_file
    If an output file is given, the program will output to that file
    If no output file is given, the program will output to stdout

  The program will output as such:
    word1 word1_count
    word2 word2_count
    ...
'''

import sys
import re

'''
returns_sorted_lowercase_word_list is a helper-function that takes in a text file and returns a sorted list of all the words that appear in the text file
notes: Punctuation (except 's) have been filtered out; text is converted to lowercase
'''
def returns_sorted_lowercase_word_list(filename):
  input_file = open(filename, 'r')
  text = re.sub('--', ' ', input_file.read())
  text = text.lower()
  sorted_lowercase_word_list = sorted(re.findall(r'([a-zA-Z]+(?:\'[a-zA-Z]+)*)', text))
  input_file.close()
  return sorted_lowercase_word_list
  # finds all the words that match 1 or more alphas followed by 0 or more (' followed by 1 or more alphas) and returns a sorted list out of them


'''
returns_word_count_dict is a function that takes in a text file and returns word_count_dict
word_count_dict is a dictionary that pairs each word with its count--the word's number of occurences in the text file
'''
def returns_word_count_dict(filename):
  sorted_lowercase_word_list = returns_sorted_lowercase_word_list(filename)

  word_count_dict = {}  # maps each word to its count
  for word in sorted_lowercase_word_list:
    if word not in word_count_dict:  # word not found in dict -> set count to 1
      word_count_dict[word] = 1
    else:  # word found in dict -> add 1 to count
      word_count_dict[word] += 1
  return word_count_dict


'''
print_words is a function that takes in a text file and returns a string content
content contains all the unique word in the text file along with each word's number of occurences
'''
def print_words(filename):
  content = ''
  word_count_dict = returns_word_count_dict(filename)
  for word in word_count_dict.keys():
    content += word + ' ' + str(word_count_dict[word]) + '\n'
  return content


'''
sort_by_value is a custom-sort helper-function that returns the value in the key-value pair
'''
def sort_by_value(item):
  return item[1]


'''
print_top is a function that takes in a text file and returns a string containing the 20 most common words in the text file along with each word's number of occurences
'''
def print_top(filename):
  content = ''
  word_count_dict = returns_word_count_dict(filename)
  sorted_count_list = sorted(word_count_dict.items(), key=sort_by_value, reverse=True)
  for item in sorted_count_list[:20]:
    content += item[0] + ' ' + str(item[1]) + '\n'
  return content


def main():
  if len(sys.argv) != 3 and len(sys.argv) != 4:  # ADDED
    print('usage: ./wordcount.py {--count | --topcount} input_file [output_file]')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  saveFile = ''
  if len(sys.argv) == 4:  # if length is 4, an output file has been given
    saveFile = open(sys.argv[3], 'w')

  if option == '--count':
    content = print_words(filename)  # ADDED CONTENT
  elif option == '--topcount':
    content = print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

  # if an output file is given, output to that file.
  # if no output file given, output to stdout
  if saveFile:
    saveFile.write(content)
    saveFile.close()
  else:
    sys.stdout.write(content)


if __name__ == '__main__':
  main()
