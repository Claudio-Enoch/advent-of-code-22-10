from app.nav_calculator import NavCalculator

NAV_FILE_PATH = "data/puzzle_data.txt"

with open(NAV_FILE_PATH) as nav_data:
    nav_lines = nav_data.read().splitlines()
calculator = NavCalculator(navigations=nav_lines)
print(f"PART ONE: {calculator.corrupt_line_score}")
print(f"PART TWO: {calculator.incomplete_line_score}")
