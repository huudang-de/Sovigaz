import sys
import codecs
import argparse
import os

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

from docling.document_converter import DocumentConverter

def main():
    parser = argparse.ArgumentParser(description="Convert docx to markdown using Docling")
    parser.add_argument("input", help="Path to the input .docx file")
    parser.add_argument("output", help="Path to the output .md file")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    print(f"Starting Docling Converter...")
    converter = DocumentConverter()
    
    print(f"Reading file: {input_file}")
    result = converter.convert(input_file)
    
    print("Exporting to Markdown...")
    markdown_output = result.document.export_to_markdown()
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_output)
        
    print(f"Done! Output saved to: {output_file}")

if __name__ == "__main__":
    main()
