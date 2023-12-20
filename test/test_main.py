from ..main import find_free_slots
import pytest

@pytest.fixture
def busy_schedule():
    return [
        {'start': '10:30', 'stop': '10:50'},
        {'start': '18:40', 'stop': '18:50'},
        {'start': '14:40', 'stop': '15:50'},
        {'start': '16:40', 'stop': '17:20'},
        {'start': '20:05', 'stop': '20:20'}
    ]

def test_find_free_slots(busy_schedule):
    expected_free_slots = [
        {'start': '09:00', 'stop': '09:30'},
        {'start': '09:30', 'stop': '10:00'},
        {'start': '10:00', 'stop': '10:30'},
        {'start': '10:50', 'stop': '11:20'},
        {'start': '11:20', 'stop': '11:50'},
        {'start': '11:50', 'stop': '12:20'},
        {'start': '12:20', 'stop': '12:50'},
        {'start': '12:50', 'stop': '13:20'},
        {'start': '13:20', 'stop': '13:50'},
        {'start': '13:50', 'stop': '14:20'},
        {'start': '15:50', 'stop': '16:20'},
        {'start': '17:20', 'stop': '17:50'},
        {'start': '17:50', 'stop': '18:20'},
        {'start': '18:50', 'stop': '19:20'},
        {'start': '19:20', 'stop': '19:50'},
        {'start': '20:20', 'stop': '20:50'}
        ]

    free_slots = find_free_slots(busy_schedule)
    assert free_slots == expected_free_slots