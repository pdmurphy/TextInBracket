import re

def extract_with_regex(file_path):
    bracket_pattern = re.compile(r'\[(.*?)\]')
    highlight_split_pattern = re.compile(r'^(.*?)\bhighlight\b')

    all_bracket_contents = []
    pre_highlight_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Find all bracketed contents
            brackets = bracket_pattern.findall(line)
            all_bracket_contents.extend(brackets)

            # Find everything before "highlight"
            pre_highlight_match = highlight_split_pattern.search(line)
            if pre_highlight_match:
                pre_highlight_lines.append(pre_highlight_match.group(1).rstrip())

    # Output
    print("=== Bracketed Parts ===")
    for item in all_bracket_contents:
        print(item)

    print("\n=== Lines Before 'highlight' ===")
    for line in pre_highlight_lines:
        print(line)

# Example usage
if __name__ == "__main__":
    input_file = 'InsertFilePathHere' # Replace this with your actual file path
    extract_with_regex(input_file)
