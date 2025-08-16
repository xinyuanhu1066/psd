# Develop a new project that reads demo.txt and returns the total number of words. 
# Share the GitHub repository link and a screenshot of the result.

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_words(self):
        file = open(self.file_path, 'r', encoding='utf-8')
        # Count words for each line because spliting string by space, so '\n' in the end of line
        # will not be splited
        result = 0
        for line in file:
            result += len(line.split(' '))
        return result
    

if __name__ == '__main__':
    file_processor = FileProcessor('demo.txt')
    print(f'\ndemo.txt has {file_processor.count_words()} words.\n')