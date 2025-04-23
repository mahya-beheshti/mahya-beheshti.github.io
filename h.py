import os

def concatenate_html_files(input_dir, output_file):
    """
    Reads all HTML files in a directory and combines them into one file,
    with each file's content preceded by its filename.
    
    Args:
        input_dir (str): Path to the input directory.
        output_file (str): Path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.css'):
                filepath = os.path.join(input_dir, filename)
                
                outfile.write(f"Filename: {filename}\n")
                outfile.write("-" * 50 + "\n")  # Separator line
                
                with open(filepath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                
                outfile.write("\n\n")  # Spacing between files

# Example Usage:
input_directory = "./"  # Directory containing HTML files
output_filename = "./combined_css.txt"  # Output file

concatenate_html_files(input_directory, output_filename)
print(f"All HTML files concatenated into {output_filename}")