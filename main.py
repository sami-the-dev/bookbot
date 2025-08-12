import sys
from stats import count_book_words
from stats import count_Occurance_of_char
from stats import sort_dic
from stats import print_report
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    



def main():
    if len(sys.argv) <=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = count_book_words(book)
    print(f"{num_words} words found in the document")
    count_dic = count_Occurance_of_char(book)
    
    sorted_dic = sort_dic(count_dic)
    print_report(sorted_dic,num_words)


main()