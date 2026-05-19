from rest_framework import serializers
from apps.mappings.models import PatientDoctorMapping
from apps.patients.models import Patient
from apps.doctors.models import Doctor


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """Serializer for PatientDoctorMapping model."""

    # Nested read representations
    patient_detail = serializers.SerializerMethodField(read_only=True)
    doctor_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor',
            'patient_detail', 'doctor_detail',
            'notes', 'assigned_at',
        ]
        read_only_fields = ['id', 'assigned_at', 'patient_detail', 'doctor_detail']

    def get_patient_detail(self, obj):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name,
            'age': obj.patient.age,
            'gender': obj.patient.gender,
        }

    def get_doctor_detail(self, obj):
        return {
            'id': obj.doctor.id,
            'name': obj.doctor.name,
            'specialization': obj.doctor.specialization,
        }

    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')

        # Check for duplicate assignment
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                f"Doctor '{doctor.name}' is already assigned to patient '{patient.name}'."
            )
        return attrs

    def validate_patient(self, value):
        if not Patient.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Patient not found.")
        return value

    def validate_doctor(self, value):
        if not Doctor.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Doctor not found.")
        return value