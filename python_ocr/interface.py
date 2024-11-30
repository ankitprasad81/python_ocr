import gradio as gr
import logging
from .processor import OCRProcessor, AVAILABLE_MODELS

logger = logging.getLogger(__name__)

class OCRInterface:
    def __init__(self):
        """Initialize the Gradio interface with OCR processor."""
        self.processor = None
        self.available_models = AVAILABLE_MODELS
        
        try:
            # Create interface components
            self.interface = create_interface()
            
        except Exception as e:
            error_msg = f"Error initializing interface: {str(e)}"
            logger.error(error_msg)
            raise
    
    def launch(self, share=False, server_name="0.0.0.0", server_port=7860):
        """Launch the Gradio interface.
        
        Args:
            share (bool): Whether to create a public link
            server_name (str): Server name for hosting
            server_port (int): Port number for hosting
        """
        try:
            self.interface.launch(
                share=share,
                server_name=server_name,
                server_port=server_port
            )
        except Exception as e:
            error_msg = f"Error launching interface: {str(e)}"
            logger.error(error_msg)
            raise

def create_interface():
    def process_image(image_path, api_key, model_name):
        """Handles the image processing request"""
        try:
            if not api_key:
                return "# Error\n\nBhai API key toh daalo! Get one from https://console.groq.com/"
            
            processor = OCRProcessor(api_key=api_key, model_name=model_name)
            return processor.convert_to_markdown(image_path)
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return f"# Error\n\n{str(e)}"

    # Build the UI
    with gr.Blocks(title="Image to Markdown Converter") as interface:
        gr.Markdown("""
        # 📸 Image to Markdown Converter
        
        Upload any image with text, and I'll convert it to proper markdown format!
        
        ⚡ Features:
        - Handles handwritten text
        - Supports multiple languages
        - Preserves formatting
        
        👉 First time? Get your API key from [Groq Console](https://console.groq.com/)
        """)
        
        with gr.Row():
            with gr.Column():
                api_key = gr.Textbox(
                    label="Your Groq API Key",
                    placeholder="Paste your API key here...",
                    type="password",
                    info="Keep this safe! Don't share with anyone"
                )
                image_input = gr.Image(
                    label="Drop your image here",
                    type="filepath"
                )
                model_dropdown = gr.Dropdown(
                    choices=AVAILABLE_MODELS,
                    value=AVAILABLE_MODELS[0],
                    label="Choose Model",
                    info="11B = Fast, 90B = Smart"
                )
                submit_btn = gr.Button("✨ Convert Now!", variant="primary")
            
            with gr.Column():
                output = gr.Markdown(
                    label="Your Markdown",
                    show_label=True
                )
        
        # Wire up the button
        submit_btn.click(
            fn=process_image,
            inputs=[image_input, api_key, model_dropdown],
            outputs=output
        )
    
    return interface
