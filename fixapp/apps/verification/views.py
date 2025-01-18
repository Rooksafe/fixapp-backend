from django.http import JsonResponse
from .services import verify_user

def verify_user_view(request):
    if request.method == 'POST':
        id_image = request.FILES['id_image']
        selfie_image = request.FILES['selfie_image']

        # Save the uploaded files temporarily
        id_image_path = f"/tmp/{id_image.name}"
        selfie_image_path = f"/tmp/{selfie_image.name}"
        with open(id_image_path, 'wb') as f:
            f.write(id_image.read())
        with open(selfie_image_path, 'wb') as f:
            f.write(selfie_image.read())

        # Perform verification
        result = verify_user(id_image_path, selfie_image_path)
        return JsonResponse(result)
