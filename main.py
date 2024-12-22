def count_words(input):
    return len(input.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = count_words(file_contents)
        print(words)

main()        

