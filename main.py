def main():
  path_to_file = "books/frankenstein.txt"
  with open(path_to_file) as f:
    file_contents = f.read()
    # print(file_contents)
    words = count_words(file_contents)
    chars_dict = count_chars(file_contents)
    # print(chars_dict)

    chars_list = []
    
    for key, value in chars_dict.items():
      # print(f"key: {key}, value: {value}")
      chars_list.append({"letter": key, "count": value})
    
    chars_list.sort(reverse=True, key=sort_on)
    # print(chars_list)

    # print report to console
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words} words found in the document")
    print()
    for char in chars_list:
      # print(char)
      print(f"The '{char['letter']}' character was found {char['count']} times")
    print("--- End report ---")


def count_words(text):
  count = len(text.split())
  # print(count)
  return count


def count_chars(text):
  lowered_text = text.lower()
  alphas = "abcdefghijklmnopqrstuvwxyz"
  count_dict = {}
  for letter in alphas:
    count_dict[letter] = 0

  for char in lowered_text:
    if char in count_dict:
      count_dict[char] += 1

  # print(count_dict)
  return count_dict


def sort_on(dict):
  return dict["count"]

main()