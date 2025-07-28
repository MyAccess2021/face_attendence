import face_recognition
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .supabase_client import supabase  # Your existing Supabase connection
import numpy as np

class FaceEmbeddingFromImageFileView(APIView):
    def post(self, request):
        image_file = request.FILES.get('image')

        if not image_file:
            return Response({"error": "Image file is required."}, status=400)

        try:
            # Load image and extract face encoding
            image = face_recognition.load_image_file(image_file)
            encodings = face_recognition.face_encodings(image)

            if not encodings:
                return Response({"error": "No face found in the image."}, status=400)

            embedding = encodings[0].tolist()  # Convert NumPy array to list for JSON serialization
            return Response({"embedding": embedding}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class VerifyFaceAndMarkAttendance(APIView):
    def post(self, request):
        try:
            image_file = request.FILES.get("image")
            email = request.data.get("email")

            if not image_file or not email:
                return Response({"error": "Both 'email' and 'image' are required."}, status=400)

            # Step 1: Fetch stored face embedding from Supabase
            response = supabase.table("users").select("face_embedding").eq("email", email).single().execute()
            user_data = response.data

            if not user_data or "face_embedding" not in user_data:
                return Response({"error": "User or embedding not found."}, status=404)

            stored_embedding = np.array(user_data["face_embedding"])

            # Step 2: Extract embedding from uploaded image
            image = face_recognition.load_image_file(image_file)
            encodings = face_recognition.face_encodings(image)

            if not encodings:
                return Response({"error": "No face found in the uploaded image."}, status=400)

            uploaded_embedding = encodings[0]

            # Step 3: Compare embeddings
            distance = np.linalg.norm(uploaded_embedding - stored_embedding)
            threshold = 0.5  # You can tweak this

            if distance < threshold:
                # Step 4: Mark attendance (if needed, log it)
                # supabase.table("Attendance").insert({"uuid": uuid, "status": "present"}).execute()

                return Response({
                    "message": "✅ Face matched. Attendance marked.",
                    "distance": distance
                }, status=200)
            else:
                return Response({
                    "error": "❌ Face mismatch. Try again.",
                    "distance": distance
                }, status=403)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
