import emoji
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def test_function():
    date = datetime.today()
    print(date.date())
    get_employees()
    calculate_salary()

    print(emoji.emojize(':thumbs_up:') * 5)
if __name__ == '__main__':
    test_function()