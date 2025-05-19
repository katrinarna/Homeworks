from firstclass import Student

def test_enroll():
    s = Student("Kata", 287)
    s.enroll("Physics")
    assert "Physics" in s.get_courses()
