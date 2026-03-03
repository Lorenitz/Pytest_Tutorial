import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [
    (5, 25),
    (4, 16),
    (9, 81)
])


def test_multiple_square_areas(side_length, expected_area):
    """Test multiple square areas with different side lengths."""
    square = shapes.Square(side_length)
    assert square.area() == expected_area




@pytest.mark.parametrize("side_length, expected_perimeter", [
    (3, 12),
    (4, 16),
    (5, 20)
])
def test_multiple_perimeters(side_length, expected_perimeter):
    """Test multiple square perimeters with different side lengths."""
    square = shapes.Square(side_length)
    assert square.perimeter() == expected_perimeter


