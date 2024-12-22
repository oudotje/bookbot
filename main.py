def pretty_print(count_chars):
    for k in count_chars: 
        print(f"The {k} character was found {count_chars[k]} times.")

def count_char(input):
    input_lower = input.lower()
    results = {}
    
    for c in input_lower:
        if c in results:
            results[c] += 1
        else:
            results[c] = 1
    return results

def count_words(input):
    return len(input.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = count_words(file_contents)
        print(words)
        count_chars = count_char(file_contents)
        pretty_print(count_chars)

main()        

