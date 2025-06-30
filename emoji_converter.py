# Emoji to text and text to emoji converter
def create_emoji_map():
    return {
        ':)': '😊',
        ':D': '😄',
        ':(': '😢',
        '<3': '❤️',
        ':P': '😜',
        ':O': '😮',
        ';)': '😉',
        ':/': '😕',
        'text': '📝',
        'love': '💕',
        'happy': '😊',
        'sad': '😢',
        'wink': '😉',
        'surprised': '😮'
    }

def text_to_emoji(text, emoji_map):
    result = text
    for text_key, emoji in emoji_map.items():
        result = result.replace(text_key, emoji)
    return result

def emoji_to_text(text, emoji_map):
    result = text
    for text_key, emoji in emoji_map.items():
        result = result.replace(emoji, text_key)
    return result

def main():
    emoji_map = create_emoji_map()
    
    while True:
        print("\nEmoji Converter")
        print("1. Text to Emoji")
        print("2. Emoji to Text")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            text = input("Enter text to convert to emoji: ")
            converted = text_to_emoji(text, emoji_map)
            print("Converted text:", converted)
        elif choice == '2':
            text = input("Enter text with emojis to convert to text: ")
            converted = emoji_to_text(text, emoji_map)
            print("Converted text:", converted)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()