from rest_framework import serializers, validators
from .models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    def even_number(value):
        if value % 2 != 0:
            raise serializers.ValidationError('This field must be an even number.')

    email = serializers.EmailField(required=True, error_messages={'required': 'Custom error message'}, validators=[
        validators.UniqueValidator(NewUser.objects.all(), "Пользователь уже существует"),
    ])
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'error_messages': {'required': 'НЕ может'}}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance