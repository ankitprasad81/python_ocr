import logging
import sys
from python_ocr.interface import create_interface

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Starts up our awesome image converter"""
    try:
        logger.info("Shuru karte hain...")
        interface = create_interface()
        
        logger.info("Server start ho raha hai...")
        interface.launch(
            server_name="0.0.0.0",
            server_port=7860
        )
        
    except Exception as e:
        logger.error(f"Oops kuch gadbad ho gayi: {e}")
        raise

if __name__ == "__main__":
    main()
