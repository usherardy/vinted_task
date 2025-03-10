import unittest
from shipment_processor import ShipmentProcessor

class TestShipmentProcessor(unittest.TestCase):
    def setUp(self):
        """Create a fresh instance of ShipmentProcessor for each test."""
        self.processor = ShipmentProcessor()

    def test_valid_input(self):
        """Test that a valid input line is correctly processed."""
        line = "2025-01-01 S LP"
        result = self.processor.process_line(line)
        self.assertIn("2025-01-01 S LP", result)

    def test_invalid_size(self):
        """Test that an invalid size returns 'Ignored'."""
        line = "2025-01-01 X LP"
        result = self.processor.process_line(line)
        self.assertIn("Ignored", result)

    def test_invalid_provider(self):
        """Test that an invalid provider returns 'Ignored'."""
        line = "2025-01-01 S XYZ"
        result = self.processor.process_line(line)
        self.assertIn("Ignored", result)

    def test_missing_data(self):
        """Test that missing data is handled correctly."""
        line = "2025-01-01 S"
        result = self.processor.process_line(line)
        self.assertIn("Ignored", result)

if __name__ == "__main__":
    unittest.main()
