# 🔍 Python-OCR: AI Vision-Powered Text to Markdown Converter

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange.svg)](https://console.groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ankitprasad81/python_ocr/pulls)

> 🚀 Transform images into beautifully formatted markdown in seconds using Groq's state-of-the-art Vision AI!

## Why Python-OCR? 🤔

- 📸 **Instant Text Extraction**: Convert any image containing text into clean markdown
- 🎯 **High Accuracy**: Powered by Groq's advanced LLaMA vision models
- 🎨 **Format Preservation**: Maintains original styling, lists, and tables
- 🌐 **Simple Web Interface**: User-friendly Gradio UI, no coding needed
- 🔒 **Secure**: Your API key, your control - no data storage

## 🚀 Quick Start

### Prerequisites

```bash
# Requirements
Python 3.8+
Groq API Key (Get yours at https://console.groq.com/)
```

### ⚡ One-Line Installation

```bash
pip install -r requirements.txt
```

### 🏃‍♂️ Run It

```bash
python run.py
```

Then open http://localhost:7860 in your browser!

## 🎮 How to Use

1. 🔑 **Get Your API Key**
   - Sign up at [Groq Console](https://console.groq.com/)
   - Create an API key
   - Keep it secure!

2. 🖼️ **Convert Images**
   - Paste your API key
   - Upload any image with text
   - Choose your model:
     * Fast Mode: `llama-3.2-11b-vision-preview`
     * Accurate Mode: `llama-3.2-90b-vision-preview`
   - Click "✨ Convert Now!"

3. 📝 **Get Results**
   ```markdown
   # Your markdown appears here!
   - With perfect formatting
   - And structure preserved
   ```

## 🐍 Python API

The Python-OCR package provides a simple yet powerful API through the `OCRProcessor` class.

### Basic Usage
```python
from python_ocr.processor import OCRProcessor

# Initialize with your Groq API key
processor = OCRProcessor(api_key="your_key")

# Convert image to markdown
markdown_text = processor.convert_to_markdown("path/to/image.jpg")
print(markdown_text)
```

### Advanced Configuration
```python
# Use the more accurate 90B model
processor = OCRProcessor(
    api_key="your_key",
    model_name="llama-3.2-90b-vision-preview"
)
```

### API Response Format
The `convert_to_markdown` method returns a string with two sections:

```markdown
# Raw Text
[Exact text from the image, preserving formatting]

# Content Analysis
[Detailed analysis of layout and structure]
```

### Error Handling
```python
try:
    markdown_text = processor.convert_to_markdown("image.jpg")
except ValueError as e:
    print(f"Configuration error: {e}")  # Invalid API key or model
except Exception as e:
    print(f"Processing error: {e}")  # Network or API errors
```

### Supported Image Formats
- JPEG/JPG
- PNG
- BMP
- TIFF

### Model Options
1. `llama-3.2-11b-vision-preview`
   - Faster processing
   - Good for simple text
   - Default choice

2. `llama-3.2-90b-vision-preview`
   - Higher accuracy
   - Better for complex layouts
   - Recommended for handwriting

### Best Practices
- Keep your API key secure (use environment variables)
- Use appropriate model for your use case
- Ensure good image quality for better results
- Handle API rate limits in production

## 🎯 Perfect For

- 📚 **Documentation Teams**: Convert handwritten notes to digital docs
- 🎓 **Students**: Transform textbook pages into study notes
- 💼 **Developers**: Extract code snippets from screenshots
- 📊 **Analysts**: Convert tables from images to markdown
- 📝 **Content Creators**: Streamline content migration

## 🔧 Technical Details

### Architecture
```
Python-OCR/
├── python_ocr/
│   ├── __init__.py     # Package initialization
│   ├── processor.py    # Core OCR & API logic
│   └── interface.py    # Gradio UI
└── run.py             # Entry point
```

### Dependencies
- 🔄 `groq`: Vision API integration
- 🌐 `httpx`: Modern HTTP client
- 🎨 `gradio`: Interactive UI
- 📸 `Pillow`: Image processing
- ✨ `markdown`: Text formatting

## 🤝 Contributing

We love your input! Want to help? Check out our [Contributing Guide](CONTRIBUTING.md).

Quick ways to contribute:
- 🌟 Star this repo
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit PRs

## 📈 Roadmap

- [ ] Multi-language support
- [ ] Batch processing
- [ ] Custom markdown templates
- [ ] API rate limiting handling
- [ ] Enhanced error recovery

## 💬 Community & Support

- 🐛 Found a bug? [Open an issue](https://github.com/ankitprasad81/python_ocr/issues)
- 💡 Have an idea? [Start a discussion](https://github.com/ankitprasad81/python_ocr/discussions)
- 📧 Need help? [Contact us](https://github.com/ankitprasad81/python_ocr/issues)

## 📜 License

MIT © [Ankit Kumar](https://github.com/ankitprasad81)

---

<div style="text-align: center;">

Made with ❤️ in India 🇮🇳

⭐ Star us on GitHub — it motivates me a lot!

</div>
