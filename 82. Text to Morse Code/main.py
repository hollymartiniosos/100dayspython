
import morseconv

text = input("Please write your message here:").upper()
# print(text)

if __name__ == "__main__":
    morseconv.morse_converter(text)

