import gradio as gr
from google import genai

# Replace with your Gemini API key (Do NOT upload your real key to GitHub)
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")


def review_code(code):
    if not code.strip():
        return "Please enter some Python code."

    prompt = f"""
You are an expert Python code reviewer.

Review the following Python code and provide:

## 1. Summary

## 2. Bugs

## 3. Performance Improvements

## 4. Code Style

## 5. Security Issues

## 6. Improved Code

## 7. Rating (out of 10)

Code:
```python
{code}

"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

except Exception as e:
    return f"Error: {e}"

demo = gr.Interface(
fn=review_code,
inputs=gr.Textbox(
lines=20,
label="💻 Enter Python Code",
placeholder="Paste your Python code here..."
),
outputs=gr.Markdown(label="📋 AI Review"),
title="🤖 AI Code Reviewer (Gemini)",
description="Paste your Python code and get an AI-powered review including bugs, improvements, security issues, and an improved version.",
theme=gr.themes.Soft()
)

if name == "main":
demo.launch(debug=True)
