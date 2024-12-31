from django.shortcuts import render
from rembg import remove
import io
import base64

def remove_background(request):
    input_image_base64 = None
    output_image_base64 = None

    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        input_image = image_file.read()

        # Convert the input image to Base64
        input_image_base64 = base64.b64encode(input_image).decode('utf-8')

        # Process the background removal
        output_image = remove(input_image)

        # Convert the output to Base64
        output_image_stream = io.BytesIO(output_image)
        output_image_base64 = base64.b64encode(output_image_stream.getvalue()).decode('utf-8')

    return render(request, 'remover/upload_result.html', {
        'input_image': f"data:image/png;base64,{input_image_base64}" if input_image_base64 else None,
        'output_image': f"data:image/png;base64,{output_image_base64}" if output_image_base64 else None
    })
