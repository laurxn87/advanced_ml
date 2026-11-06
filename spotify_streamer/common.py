import requests
import climage

class Common:
    def download_album_art(self, album_art_uri: str) -> str:
        """
        Downloads the album art image from the given URI and saves it to a temporary file.
        Returns the path to the saved image file.
        """
        response = requests.get(album_art_uri)
        if response.status_code == 200:
            # Save the image to a temporary file
            temp_file_path = "temp_album_art.jpg"
            with open(temp_file_path, 'wb') as f:
                f.write(response.content)
            return temp_file_path
        else:
            raise Exception(f"Failed to download album art from {album_art_uri}. Status code: {response.status_code}")

    def convert_album_art_to_ascii(self, album_art_uri: str, width: int = 50) -> str:
        """
        Converts the album art image from the given URI to an ASCII representation.
        Returns the ASCII string.
        """
        try:
            # Download the album art image
            img_path = self.download_album_art(album_art_uri)
            # Convert the image to ASCII using climage
            ascii_art = climage.convert(img_path, width=width)
            return ascii_art
        except Exception as e:
            raise Exception(f"Error converting album art to ASCII: {e}")

