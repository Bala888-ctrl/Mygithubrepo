from app import add_numbers

def test_addition():
    # This checks if 2 + 3 really equals 5
    assert add_numbers(2, 3) == 5
    print("The test passed perfectly!")

if __name__ == "__main__":
    test_addition()