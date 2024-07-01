from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Buyer, Seller, User
from .serializers import BuyerSerializer, SellerSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateBuyerView(generics.CreateAPIView):
    """Create a new Buyer in the system"""

    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()


class CreateSellerView(generics.CreateAPIView):
    """Create a new Seller in the system"""

    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class GetAllUsersView(generics.ListAPIView):
    """List All Users"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        role = self.kwargs["role"]

        if role == "buyer":
            return Buyer.objects.all()
        else:
            return Seller.objects.all()

    def get_serializer_class(self):

        role = self.kwargs["role"]
        if role == "buyer":
            return BuyerSerializer
        else:
            return SellerSerializer


class GetUserView(generics.ListAPIView):
    """Get a User"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        role = self.kwargs["role"]
        identifier = self.kwargs["identifier"]

        if role == "buyer":
            return Buyer.objects.filter(identifier=identifier)
        else:
            return Seller.objects.filter(identifier=identifier)

    def get_serializer_class(self):

        role = self.kwargs["role"]
        if role == "buyer":
            return BuyerSerializer
        else:
            return SellerSerializer


class UpdateUserView(APIView):
    """Update a user"""

    def put(self, request, role, identifier):
        try:
            print(role)
            if role == "buyer":
                user = Buyer.objects.get(identifier=identifier)
                serializer = BuyerSerializer(user, data=request.data, partial=True)
            else:
                user = Seller.objects.get(identifier=identifier)
                serializer = SellerSerializer(user, data=request.data, partial=True)

        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserPasswordView(APIView):
    "update password of a user"

    def put(self, request, role, identifier):
        try:
            if role == "buyer":
                user = Buyer.objects.get(identifier=identifier)
                serializer = BuyerSerializer(user, data=request.data, partial=True)
            else:
                user = Seller.objects.get(identifier=identifier)
                serializer = SellerSerializer(user, data=request.data, partial=True)

        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if serializer.is_valid():
            serializer.update_password(user, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    """Delete a user"""

    def delete(self, request):
        try:
            role = self.kwargs["role"]
            identifier = self.kwargs["identifier"]
            if role == "buyer":
                Buyer.objects.get(identifier=identifier).delete()
            else:
                Seller.objects.get(identifier=identifier).delete()

        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
