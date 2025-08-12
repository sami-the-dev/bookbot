
def count_book_words(book):
   words_list = book.replace("\n"," ").split(" ")
   words_list = [word for word in words_list if word != ""]
   return len(words_list) 


def count_Occurance_of_char(book):
   words_list = [char.lower() if char.isalpha()
                  else char
                      for char in book ]

   result = {}
   for char in words_list:
        if (char in result):
            result[char] += 1
        else:
            result[char] = 1
   print(result)
   return result


def sort_dic(chars_count_dic):
    new_list = []
    for key,value in chars_count_dic.items() :
        if key.isalpha():
            new_list.append({"char":key,"num":value})
    

    new_list.sort(reverse=True, key=lambda x: x["num"])
    return new_list


def print_report(sorted_list,word_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
