from django.shortcuts import render
from rembg import remove
import io
import base64

def remove_background(request):
    # Get the image from the POST request
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            image_file = request.FILES['image']
            input_image = image_file.read()

            # Convert input image to Base64 and store it in the session
            input_image_base64 = base64.b64encode(input_image).decode('utf-8')
            request.session['input_image'] = input_image_base64  # Save the input image to session

            # Process the image to remove background
            output_image = remove(input_image)

            # Convert the output image to Base64 and store it in the session
            output_image_base64 = base64.b64encode(output_image).decode('utf-8')
            request.session['output_image'] = output_image_base64  # Save the output image to session
        except Exception as e:
            # Handle error in image processing
            request.session['error_message'] = str(e)
            return render(request, 'remover/upload_result.html')
    # Get images from the session to render them in the template
    input_image_base64 = request.session.get('input_image', None)
    output_image_base64 = request.session.get('output_image', None)
    error_message = request.session.get('error_message', None)

    return render(request, 'remover/upload_result.html', {
        'input_image': f"data:image/png;base64,{input_image_base64}" if input_image_base64 else None,
        'output_image': f"data:image/png;base64,{output_image_base64}" if output_image_base64 else None,
        'error_message': error_message,
    })
