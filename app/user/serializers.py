from django.contrib.auth import get_user_model

# from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Buyer, Seller


class UserSerializer(serializers.ModelSerializer):
    """Seralizer for the users objects"""

    class Meta:
        model = get_user_model()
        fields = (
            "identifier",
            "email",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
            "gender",
            "photo",
        )
        extra_kwargs = {
            "password": {"required": False, "write_only": True, "min_length": 5},
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user"""
        # Ensure the password is not updated here
        validated_data.pop("password", None)
        return super().update(instance, validated_data)

    def update_password(self, instance, validated_data):
        """Update a user's password correctly and return it"""
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class BuyerSerializer(UserSerializer):
    """Seralizer for the Buyer objects"""

    class Meta:
        model = Buyer
        fields = (
            "identifier",
            "number",
            "email",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
            "gender",
            "photo",
        )
        read_only_fields = ("id",)
        extra_kwargs = {
            "identifier": {"read_only": True},
            "password": {"write_only": True, "min_length": 5},
        }

    def create(self, validated_data):
        """Create a new Customer with encrypted password and return it"""
        try:
            return Buyer.objects.create_user(**validated_data)
        except Exception as e:
            print(e)
            raise serializers.ValidationError(
                "Error accured when trying to create a user", 500
            )


class SellerSerializer(UserSerializer):
    """Seralizer for the Seller objects"""

    class Meta:
        model = Seller
        fields = (
            "identifier",
            "email",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
            "gender",
            "photo",
        )
        read_only_fields = ("id", "identifier")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new RestaurentOwner with encrypted password and return it"""
        try:
            return Seller.objects.create_user(**validated_data)
        except Exception as e:
            print(e)
            raise serializers.ValidationError(
                "Error accured when trying to create a user", 500
            )
