from rest_framework.views import APIView

from . import domain_models, exceptions, serializers
from rest_framework.response import Response


class ProductDetailView(APIView):
    input_serializer = serializers.ProductDetailInputSerializer
    output_serializer = serializers.ProductDetailOutputSerializer

    def post(self, request, *args, **kwargs):
        input_serializer = self.input_serializer(data=request.data)
        if not input_serializer.is_valid():
            raise exceptions.InvalidInputException

        model = domain_models.ProductDetailDomainModel(input_serializer.validated_data)
        output_serializer = self.output_serializer(model.product_id)
        Response(output_serializer.data)
