# Import necessary modules
from django.shortcuts import render
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
import os
from django.conf import settings

# Import the form class
from .forms import GetUrlForm

# Create your views here.
def index(request):
    def hex_to_rgb(hex_code):
        """Converts hex color code to RGB tuple (e.g., '#FF5733' → (255, 87, 51))."""
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    path = ''
    if request.method == "POST":
        form = GetUrlForm(request.POST)
        if form.is_valid():
            try:
                url = form.cleaned_data['url']
                fill_color = hex_to_rgb(form.cleaned_data['fill_color'])
                background_color = hex_to_rgb(form.cleaned_data['background_color'])
                
                # Create QR code
                qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=4)
                qr.add_data(url)
                
                # Generate image with styling
                img = qr.make_image(
                    fill_color=fill_color,
                    back_color=background_color
                )


                # Save the QR code
                filename = f'{request.user}.png'
                path = os.path.join('qrcodes', filename)
                full_path = os.path.join(settings.MEDIA_ROOT, path)
                
                # Ensure directory exists
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                img.save(full_path)

            except Exception as e:
                # Handle errors (e.g., invalid colors, image processing issues)
                print(f"Error generating QR code: {e}")
                path = ''  # Reset path on failure
    else:
        form = GetUrlForm()
            
    return render(request, 'QRCode/index.html', {
        'form': form,
        'path': path,  # Relative path to the saved QR code (e.g., 'qrcodes/user123.png')
    })