# AI Prompt Generator

AI Prompt Generator is an intelligent web application that creates high-quality AI prompts from uploaded media.

Users can upload an **image**, **poster**, or **short video**, and the application analyzes the content and generates a detailed AI-ready prompt automatically.

It is useful for prompt generation for:
- AI image generators
- Cinematic scenes
- Creative storytelling
- Professional photography prompts
- Video prompt descriptions
- Poster recreation prompts

---

# Live Demo

🚀 Try the project live here:

https://prompt-generator-c30o.onrender.com

---

# Features

## Upload Media & Generate Prompt
Users can upload:

- Image (`jpg`, `jpeg`, `png`)
- Poster
- Video (`mp4`, `mov`, etc.)

After upload, the application analyzes the content and generates a descriptive AI prompt automatically.

---

## Prompt Tone Selection

Users can choose the prompt style/tone before generating.

Supported tones include:

- Natural
- Realistic
- Cinematic
- Professional
- Dramatic
- Hyper-realistic
- Creative
- Storytelling
- Detailed
- Artistic

---

## Video Upload Restriction

⚠️ Note:

Currently users can upload **video up to 15 seconds only**.

This keeps processing fast and improves prompt generation performance.

---

# Example Workflow

## 1 Upload Image / Poster / Video

User uploads media file.

↓

## 2 Select Prompt Tone

Example:
- Cinematic
- Realistic
- Professional

↓

## 3 Generate Prompt

Application processes uploaded file using AI.

↓

## 4 Get AI Prompt Output

Example output:

```text
A cinematic hyper-realistic portrait of a young man standing under soft natural lighting,
highly detailed skin texture, professional photography, dramatic mood, sharp focus,
8K ultra realistic render.
```

---

# Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## AI
- Google Gemini API

## Deployment
- Render

---

# Project Structure

```bash
AI-Prompt-Generator/
│
├── app.py
├── crews.py
├── requirements.txt
├── Procfile
├── README.md
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── uploads/
│
└── venv/
```

---

# Installation

## Clone Project

```bash
git clone <your-github-repository-url>
cd AI-Prompt-Generator
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Environment Variable

Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run Project

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Use Cases

- AI Image Prompt Creation
- Poster Description Prompt
- Video Scene Prompt Generation
- Cinematic Prompt Writing
- Professional Photography Prompt Creation
- Creative Content Generation

---

# Future Improvements

- Prompt history
- Download generated prompt
- Copy prompt button
- More tone styles
- Longer video support
- User accounts
- Save favorite prompts

---

# Author

Developed by **Abrar Alam**

---

# Live Project

https://prompt-generator-c30o.onrender.com
