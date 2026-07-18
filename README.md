# 🤖 AI Code Reviewer

An AI-powered web application that reviews Python code using **Google Gemini AI**. It provides a detailed analysis, identifies bugs, suggests performance improvements, highlights security issues, and generates an improved version of the code.

## 🚀 Features

- 📄 Code summary
- 🐞 Bug detection
- ⚡ Performance improvement suggestions
- 🎨 Code style recommendations
- 🔒 Security issue analysis
- 💡 Improved version of the code
- ⭐ Overall code rating (out of 10)
- 🖥️ Simple Gradio web interface

## 🛠️ Technologies Used

- Python
- Google Gemini AI (`google-genai`)
- Gradio

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/fazilaanjum/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

#### Windows (Command Prompt)

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

#### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

#### Linux / macOS

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

### 4. Run the application

```bash
python app.py
```

The application will launch a local Gradio interface in your browser.

## 📸 How to Use

1. Open the application.
2. Paste your Python code into the text box.
3. Click **Submit**.
4. View the AI-generated review, including:
   - Code Summary
   - Bugs
   - Performance Improvements
   - Code Style Suggestions
   - Security Issues
   - Improved Code
   - Overall Rating

## 📁 Project Structure

```
AI-Code-Reviewer/
│── app.py
│── requirements.txt
│── README.md
```

## 📌 Example

**Input**

```python
def add(a,b):
 return a+b
```

**Output**

- Summary of the code
- Style improvements
- Bug analysis
- Performance suggestions
- Security review
- Improved code
- Rating (e.g., 9/10)

## ⚠️ Security

Never hardcode your Gemini API key in your source code or upload it to GitHub.

Use an environment variable instead:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed with **Python**, **Gradio**, and **Google Gemini AI**.
```
