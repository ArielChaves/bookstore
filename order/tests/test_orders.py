import pytest
from order.serializers import OrderSerializer
from order.factories import OrderFactory, ProductFactory


@pytest.mark.django_db
def test_order_serializer_total_calculation():
    # Arrange
    product1 = ProductFactory(price=10)
    product2 = ProductFactory(price=20)
    order = OrderFactory(product=[product1, product2])

    # Act
    serializer = OrderSerializer(order)

    # Assert
    assert serializer.data["total"] == 30
    assert len(serializer.data["product"]) == 2

