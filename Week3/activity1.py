# Using the attached text file, open, read, and write the complete information for the demo.txt. 
# Share the GitHub link here(with adding the screenshot of the result).

def main():
    # Open demo.txt with append mode
    file = open('demo.txt', 'a')
    file.write('\nAdd new line')
    file.close()

    # Open demo.txt with readonly mode
    file = open('demo.txt', 'r')
    print(file.read())
    print(f'\n{"-" * 80}\ndemo.txt has {len(file.read())} lines.\n')
    file.close()


if __name__ == '__main__':
    main()