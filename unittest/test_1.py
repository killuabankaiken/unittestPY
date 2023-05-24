import unittest
from datetime import datetime, timedelta
from find_free_slots import find_free_slots
class TestFreeSlots(unittest.TestCase):
     def test_no_busy_slots(self):
        start_times = []
        durations = []

        free_slots = find_free_slots(start_times, durations)

        self.assertEqual(free_slots, ['09:00-18:00'])
if __name__ == '__main__':
    unittest.main()
