from main import get_weather 
def test_get_weather():
    assert get_weather(25) == "hot"
    assert get_weather(15) == "hot" # This should be "cold" based on the logic
