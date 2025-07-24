import os
import requests
from pathlib import Path

def download_image(url, filename, folder='app/static/images/portfolio'):
    """
    Download an image from a URL and save it to the specified folder.
    """
    # Skip if file already exists
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    
    if os.path.exists(filepath):
        print(f"File {filename} already exists, skipping...")
        return True
        
    try:
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"Downloading {url}...")
        response = requests.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        # Check if the response is an image
        if 'image' not in response.headers.get('content-type', ''):
            raise ValueError(f"URL does not point to an image: {url}")
            
        # Save the image
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
        
        print(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    # List of images to download (URL, filename)
    images_to_download = [
        # Castillo de Lorca - Using a different image source
        ('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Castillo_Lorca-SS-2011.JPG/800px-Castillo_Lorca-SS-2011.JPG', 'castillo-lorca.jpg'),
        
        # Working Unsplash images with direct links
        ('https://images.unsplash.com/photo-1600585154340-be6161a56a0c', 'modern-house-garden.jpg'),
        ('https://images.unsplash.com/photo-1585320806297-9794b3e4eeae', 'mediterranean-garden-1.jpg'),
        ('https://images.unsplash.com/photo-1600566752225-4dbcdd4e3a8c', 'garden-design-1.jpg'),
        ('https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3', 'garden-design-2.jpg'),
        ('https://images.unsplash.com/photo-1600585154526-990dced4cfa5', 'luxury-terrace.jpg'),
        ('https://images.unsplash.com/photo-1613490493576-7fde63acd811', 'garden-pool.jpg'),
        ('https://images.unsplash.com/photo-1600585154340-be6161a56a0c', 'modern-garden.jpg')
    ]
    
    # Download each image
    for url, filename in images_to_download:
        download_image(url, filename)

if __name__ == "__main__":
    main()
