import face_recognition

def validate_face(id_image_path, selfie_image_path):
    """Validate if the face in the ID matches the face in the selfie."""
    # Load the images
    id_image = face_recognition.load_image_file(id_image_path)
    selfie_image = face_recognition.load_image_file(selfie_image_path)

    # Get face encodings
    id_face_encoding = face_recognition.face_encodings(id_image)[0]
    selfie_face_encoding = face_recognition.face_encodings(selfie_image)[0]

    # Compare faces
    results = face_recognition.compare_faces([id_face_encoding], selfie_face_encoding)
    return results[0]
