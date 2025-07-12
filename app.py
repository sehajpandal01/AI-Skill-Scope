from pdf_parser.parser import extract_text_from_pdf
from pdf_parser.summarizer import summarize_text
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python app.py <pdf_path> <openai_api_key>")
    else:
        pdf_path = sys.argv[1]
        api_key = sys.argv[2]
        text = extract_text_from_pdf(pdf_path)
        summary = summarize_text(text, api_key)
        print("\nSummary:\n", summary)
