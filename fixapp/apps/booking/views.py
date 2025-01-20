from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from .models import Category, Job, Apply, Booking
from .serializers import CategorySerializer, JobSerializer, ApplySerializer, BookingSerializer
from users.models import Client, Professional
from rest_framework.views import APIView
from rest_framework.response import Response

# Crear y listar reservas
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        professional_id = self.request.data.get('professional')
        # Verifica que el profesional exista
        if not professional_id:
            raise PermissionDenied("Debes proporcionar un profesional válido.")
        serializer.save(user=user)

# Confirmar o rechazar una reserva (solo para profesionales)
class BookingUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        booking = self.get_object()
        # Verifica que el usuario autenticado sea el profesional relacionado
        if booking.professional.user != self.request.user:
            raise PermissionDenied("No tienes permiso para actualizar esta reserva.")
        serializer.save()

class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({"detail": "Reserva no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        if booking.user != request.user:
            raise PermissionDenied("No tienes permiso para cancelar esta reserva.")

        if booking.status in ['confirmed', 'rejected', 'cancelled']:
            return Response(
                {"detail": "No se puede cancelar una reserva ya confirmada, rechazada o cancelada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = 'cancelled'
        booking.save()
        return Response({"detail": "Reserva cancelada exitosamente."}, status=status.HTTP_200_OK)



# CRUD para Categorías -*-
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# CRUD para Trabajos
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Asociar el cliente autenticado al trabajo
        user = self.request.user
        if user.role != 'user':
            raise PermissionDenied("Solo los clientes pueden crear trabajos.")
        client = Client.objects.get(user=user)
        serializer.save(client=client)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Solo el propietario del trabajo puede actualizarlo
        job = self.get_object()
        if job.client.user != self.request.user:
            raise PermissionDenied("No tienes permiso para actualizar este trabajo.")
        serializer.save()

# CRUD para Postulaciones - + -
class ApplyListCreateView(generics.ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Asociar el profesional autenticado a la postulación
        user = self.request.user
        if user.role != 'professional':
            raise PermissionDenied("Solo los profesionales pueden postularse a trabajos.")
        professional = Professional.objects.get(user=user)
        serializer.save(professional=professional)

class ApplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Solo el profesional que creó la postulación puede actualizarla
        Apply = self.get_object()
        if Apply.professional.user != self.request.user:
            raise PermissionDenied("No tienes permiso para actualizar esta postulación.")
        serializer.save()
