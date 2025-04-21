import pytest
from product.serializers.product_serializer import ProductSerializer
from product.factories import ProductFactory


@pytest.mark.django_db
def test_product_serializer_basic():
    # Arrange
    product = ProductFactory(title="Simple Product", price=1000, active=True)

    # Act
    serializer = ProductSerializer(product)

    # Assert
    data = serializer.data
    assert data["title"] == "Simple Product"
    assert data["price"] == 1000
    assert data["active"] is True
