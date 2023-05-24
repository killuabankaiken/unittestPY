import unittest
from find_free_slots import find_free_slots
from datetime import datetime, timedelta
class TestFreeSlots(unittest.TestCase):
    def test_busy_slots(self):
        start_times = [
            datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),
            datetime.now().replace(hour=10, minute=30, second=0, microsecond=0),
            datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)
        ]
        durations = [90, 60, 120]

        free_slots = find_free_slots(start_times, durations)

        self.assertEqual(free_slots, ['11:00-14:00', '16:00-18:00'])

if __name__ == '__main__':
    unittest.main()