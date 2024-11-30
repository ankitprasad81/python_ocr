import base64
import logging
from PIL import Image
import markdown
import os
import httpx

logger = logging.getLogger(__name__)

# Supported Groq models for image processing
AVAILABLE_MODELS = [
    "llama-3.2-11b-vision-preview",
    "llama-3.2-90b-vision-preview",
]

class OCRProcessor:
    def __init__(self, api_key, model_name="llama-3.2-11b-vision-preview"):
        """Sets up the OCR processor with Groq API credentials
        
        Note: Get your API key from Groq console before using this
        """
        logger.info(f"Starting up with model: {model_name}")
        try:
            if model_name not in AVAILABLE_MODELS:
                raise ValueError(f"Bhai model {model_name} supported nahi hai. Use one of these: {AVAILABLE_MODELS}")
            
            if not api_key:
                raise ValueError("Arre API key toh daalo!")
            
            self.api_key = api_key
            self.model_name = model_name
            self.api_url = "https://api.groq.com/openai/v1/chat/completions"
            logger.info("Setup ho gaya!")
            
        except Exception as e:
            logger.error(f"Oops! Setup failed: {str(e)}")
            raise

    def encode_image(self, image_path):
        """Converts image to base64 - needed for API"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def convert_to_markdown(self, image_path):
        """Main function to convert image to markdown
        
        Just give image path, and get nicely formatted markdown back
        """
        logger.info(f"Processing with {self.model_name}")
        try:
            # First convert image to base64
            base64_image = self.encode_image(image_path)
            
            # Setup API request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """You are a precise OCR tool. Your task is to extract text EXACTLY as it appears and provide analysis.

Provide your response in two sections:

# Raw Text
Copy and paste the EXACT text from the image here, preserving:
- All line breaks and spacing
- Original formatting (lists, tables, etc.)
- Special characters and symbols
- Case sensitivity
Do not add any explanations or descriptions in this section.

# Content Analysis
Now provide a detailed analysis of:
- The overall layout and structure
- Any visual elements or formatting
- Context and purpose of the content"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "temperature": 0.2,
                "max_tokens": 1024
            }
            
            # Send to Groq API
            with httpx.Client(timeout=30.0) as client:
                try:
                    response = client.post(
                        self.api_url,
                        json=payload,
                        headers=headers
                    )
                    response.raise_for_status()
                    result = response.json()
                except httpx.HTTPError as e:
                    error_msg = f"API error: {str(e)}"
                    if response.status_code == 400:
                        try:
                            error_details = response.json()
                            error_msg += f"\nDetails: {error_details}"
                        except:
                            pass
                    logger.error(error_msg)
                    raise
            
            markdown_content = result['choices'][0]['message']['content']
            logger.info("Ho gaya convert!")
            
            return markdown_content
            
        except Exception as e:
            error_msg = f"Error ho gaya: {str(e)}"
            logger.error(error_msg)
            return f"# Error\n\n{error_msg}"

    @staticmethod
    def get_available_models():
        """Get list of available Groq models.
        
        Returns:
            list: List of available model names
        """
        return AVAILABLE_MODELS.copy()
