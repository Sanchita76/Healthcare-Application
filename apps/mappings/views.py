from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.mappings.models import PatientDoctorMapping
from apps.mappings.serializers import PatientDoctorMappingSerializer
from apps.patients.models import Patient


class MappingListCreateView(APIView):
    """
    POST /api/mappings/ - Assign a doctor to a patient.
    GET  /api/mappings/ - Retrieve all patient-doctor mappings.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.select_related('patient', 'doctor').all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(
            {
                "count": mappings.count(),
                "mappings": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if serializer.is_valid():
            mapping = serializer.save()
            return Response(
                {
                    "message": "Doctor assigned to patient successfully.",
                    "mapping": PatientDoctorMappingSerializer(mapping).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class MappingByPatientView(APIView):
    """
    GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        # Verify the patient exists
        patient = get_object_or_404(Patient, pk=patient_id)
        mappings = PatientDoctorMapping.objects.filter(patient=patient).select_related('doctor')
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(
            {
                "patient": {
                    "id": patient.id,
                    "name": patient.name,
                },
                "assigned_doctors_count": mappings.count(),
                "mappings": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class MappingDeleteView(APIView):
    """
    DELETE /api/mappings/<id>/ - Remove a doctor from a patient (by mapping id).
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        patient_name = mapping.patient.name
        doctor_name = mapping.doctor.name
        mapping.delete()
        return Response(
            {
                "message": f"Doctor '{doctor_name}' removed from patient '{patient_name}' successfully."
            },
            status=status.HTTP_200_OK,
        )