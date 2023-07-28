import  pytest
from calculator import square

# conventional way
# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(1) == 1
#     except AssertionError:
#         print(f"1 square in not 1")
#     try:
#         assert  square(2) == 4
#     except AssertionError:
#         print(f"2 square in not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print(f"3 square in not 9")
#     try:
#         assert square(-1) == 1
#     except AssertionError:
#         print(f"-1 square in not 1")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print(f"-2 square in not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print(f"-3 square in not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print(f"0 square in not 0")





# if __name__ == "__main__":
#     main()

# =============================
# Istall pytest and import
# ------------------------
    
# def test_square():
#     assert square(1) == 1
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-1) == 1
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
    
# ===================

def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("do")
    
