from rest_framework import serializers
from apps.patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for the Patient model."""

    created_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'age', 'gender', 'address',
            'phone', 'medical_history', 'created_by',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_created_by(self, obj):
        return {
            'id': obj.created_by.id,
            'name': obj.created_by.name,
            'email': obj.created_by.email,
        }

    def validate_age(self, value):
        if value <= 0 or value > 150:
            raise serializers.ValidationError("Age must be between 1 and 150.")
        return value

    def validate_gender(self, value):
        allowed = ['Male', 'Female', 'Other']
        if value not in allowed:
            raise serializers.ValidationError(f"Gender must be one of: {', '.join(allowed)}")
        return value