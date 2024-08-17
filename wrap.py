import textwrap
import sys

def wrap_text(input_file, width=72):
    with open(input_file, 'r') as file:
        content = file.read()
    
    wrapped_lines = []
    paragraphs = content.split('\n')

    for paragraph in paragraphs:
        if paragraph.strip() == "":
            wrapped_lines.append("")
        else:
            wrapped_paragraph = textwrap.fill(paragraph, width=width)
            wrapped_lines.append(wrapped_paragraph)

    wrapped_content = '\n\n'.join(wrapped_lines)

    sys.stdout.write(wrapped_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 wrap.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    wrap_text(input_file)
