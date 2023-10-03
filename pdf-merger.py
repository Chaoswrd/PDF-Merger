import PyPDF2


def merge_pdfs(
    input_files_path: str, input_files: list[str], output_file: str = "output.pdf"
):
    """Merge multiple PDF files into a single PDF file
    Args:
        input_files (list): List of PDF file paths to merge
        output_file (str): Output PDF file name
    """
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()
    # Iterate through the list of PDF files and append them to the merger
    for pdf_file in input_files:
        with open(f"{input_files_path}/{pdf_file}", "rb") as file:
            pdf_merger.append(file)
    # Write the merged PDF to the output file
    with open(output_file, "wb") as output_file:
        pdf_merger.write(output_file)
    # Close the merger
    pdf_merger.close()


if __name__ == "__main__":
    # Command line arguments
    # optional: -o <output_file>
    # positional: <input_files>

    # Only import argparse if the script is run directly
    import argparse

    parser = argparse.ArgumentParser(description="Merge PDF files")
    parser.add_argument(
        "-o", "--output_file", help="Output PDF file name", default="output.pdf"
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory containing input_files",
        default=".",
    )
    parser.add_argument(
        "input_files",
        nargs="*",
        help="PDF files to merge. PDF files will be merged in the order they are listed",
    )
    args = parser.parse_args()

    if not args.input_files:
        import sys

        pdf_files = [line.strip() for line in sys.stdin]
    else:
        pdf_files = args.input_files

    merge_pdfs(args.directory, pdf_files, args.output_file)
