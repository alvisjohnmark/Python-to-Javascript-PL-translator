import re
import argparse

def translate_python_to_js(python_code):
    js_code = []

    # Line-by-line translation
    for line in python_code.splitlines():
        # Remove leading/trailing spaces
        line = line.strip()

        # Skip empty lines
        if not line:
            js_code.append("")
            continue

        # Variable declarations and assignments
        var_match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", line)
        if var_match:
            variable, value = var_match.groups()
            # Translate declaration
            js_line = f"let {variable} = {value};"
            js_code.append(js_line)
            continue

        # Print statement
        if line.startswith("print("):
            content = line[len("print("):-1]  # Extract content within print()
            js_line = f"console.log({content});"
            js_code.append(js_line)
            continue

        # Arithmetic operations are identical, no special translation needed
        js_code.append(line)

    return "\n".join(js_code)

def run_translator(input_file, output_file):
    # Read the input Python file
    try:
        with open(input_file, "r") as infile:
            python_code = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Translate the code
    try:
        js_code = translate_python_to_js(python_code)
    except Exception as e:
        print(f"Error during translation: {e}")
        return

    with open(output_file, "w") as outfile:
        outfile.write(js_code)

    print(f"Translation complete! Output saved to {output_file}")

parser = argparse.ArgumentParser(description="Python to JavaScript Translator")
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()

run_translator(args.input_file, args.output_file)
