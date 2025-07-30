from openai import OpenAI
def summarize_text(text, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"Summarize the following text:\n{text}"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during summarization: {e}"
