from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from rembg import remove
from PIL import Image
import io
import base64

def remove_background(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        input_image = image_file.read()

        # Proses penghapusan background
        output_image = remove(input_image)

        # Konversi ke format Base64 untuk menampilkan tanpa menyimpan file
        output_image_stream = io.BytesIO(output_image)
        output_image_base64 = base64.b64encode(output_image_stream.getvalue()).decode('utf-8')

        return render(request, 'remover/result.html', {
            'output_image': f"data:image/png;base64,{output_image_base64}"
        })

    return render(request, 'remover/index.html')
