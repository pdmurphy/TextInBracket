import re

def extract_all_brackets(file_path):
    all_bracket_contents = []
    pattern = re.compile(r'\[(.*?)\]')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = pattern.findall(line)
            all_bracket_contents.extend(matches)
    
    return all_bracket_contents

# Example usage
if __name__ == "__main__":
    input_file = 'InsertFilePathHere'  # Replace this with your actual file path
    results = extract_all_brackets(input_file)
    for item in results:
        print(item)
