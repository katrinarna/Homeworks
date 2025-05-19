from asteroids.api import get_asteroids

def test_get_asteroids_structure():
    result = get_asteroids("2024-05-01")
    assert "date" in result
    assert "asteroids" in result
    assert isinstance(result["asteroids"], list)
