import os
import requests
from pathlib import Path

def download_welcome_image():
    """Download a beautiful garden image from Unsplash and save it to the static/images directory."""
    # Create images directory if it doesn't exist
    image_dir = Path("app/static/images")
    image_dir.mkdir(parents=True, exist_ok=True)
    
    # The image path that's referenced in index.html
    output_path = image_dir / "about-image.jpg"
    
    # Using a beautiful garden image from Unsplash (free to use)
    # You can change the URL to any other Unsplash image by modifying the photo ID
    image_url = "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1932&q=80"
    
    try:
        print(f"Downloading image from {image_url}...")
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Successfully downloaded image to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error downloading image: {e}")
        return False

if __name__ == "__main__":
    download_welcome_image()