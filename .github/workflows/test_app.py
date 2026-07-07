from app import add_numbers

def test_addition():
    assert add_numbers(2, 3) == 5
    print("The test passed perfectly!")

if __name__ == "__main__":
    test_addition()