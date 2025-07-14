from image_ocr.ocr import extract_text_from_image
from image_ocr.qna import ask_question_about_text
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python app.py <image_path> <question> <openai_api_key>")
    else:
        image_path = sys.argv[1]
        question = sys.argv[2]
        api_key = sys.argv[3]
        text = extract_text_from_image(image_path)
        answer = ask_question_about_text(text, question, api_key)
        print("\nAnswer:\n", answer)
