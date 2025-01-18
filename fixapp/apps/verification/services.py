from services.google_vision import analyze_id_card
from services.face_recognition import validate_face

def verify_user(id_image_path, selfie_image_path):
    """Verify a user using their ID card and selfie."""
    # Analyze the ID card
    id_text = analyze_id_card(id_image_path)

    if not id_text:
        return {"status": "failure", "reason": "ID text could not be detected"}

    # Validate face
    is_face_match = validate_face(id_image_path, selfie_image_path)
    if not is_face_match:
        return {"status": "failure", "reason": "Face does not match ID"}

    return {"status": "success", "id_text": id_text}
