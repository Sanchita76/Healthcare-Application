from rest_framework import serializers
from apps.doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for the Doctor model."""

    created_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'specialization', 'phone', 'email',
            'experience_years', 'created_by', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_created_by(self, obj):
        return {
            'id': obj.created_by.id,
            'name': obj.created_by.name,
            'email': obj.created_by.email,
        }

    def validate_experience_years(self, value):
        if value < 0 or value > 70:
            raise serializers.ValidationError("Experience years must be between 0 and 70.")
        return value