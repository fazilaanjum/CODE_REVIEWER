import os

import gradio as gr
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "Please set the GEMINI_API_KEY environment variable."
    )

client = genai.Client(api_key=API_KEY)

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
