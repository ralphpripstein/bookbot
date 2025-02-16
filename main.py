def sort_on(dict):
    return dict["num"]

def character_count(text):
    character = (text.lower())
    char_count = {}
    for char in character:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_list = []
    for char, count in char_count.items():
        char_list.append({"character": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)    
    return char_list


def word_count(text):
    words = text.split()
    return(len(words))

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        print("--- Begin report of books/frankenstein.txt ---")
        word_count_result = word_count(file_contents)
        print(f"{word_count_result} words found in the document\n")
        
        char_count_result = character_count(file_contents)
        for char_data in char_count_result:
            print(f"The '{char_data['character']}' character was found {char_data['num']} times")
        
        print("--- End report ---")

if __name__ == "__main__":
    main()