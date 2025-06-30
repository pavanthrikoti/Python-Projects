def flames_game(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    # Create lists of characters
    name1_list = list(name1)
    name2_list = list(name2)
    
    # Remove common characters
    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
    
    # Count remaining characters
    count = len(name1_list) + len(name2_list)
    
    # FLAMES list
    flames = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    
    # Calculate the result
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:-1]
    
    return flames[0]

def main():
    print("Welcome to FLAMES Game!")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    
    result = flames_game(name1, name2)
    print(f"\nThe relationship between {name1} and {name2} is: {result}")

if __name__ == "__main__":
    main()