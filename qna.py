from openai import OpenAI
def ask_question_about_text(text, question, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"The following text was extracted from an image:\n{text}\n\nNow answer this question about it:\n{question}"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during Q&A: {e}"
