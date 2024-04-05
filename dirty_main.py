from application.salary import *
from application.db.people import *
from datetime import *
import emoji




def test_function():
    date = datetime.today()
    print(date.date())
    get_employees()
    calculate_salary()

    print(emoji.emojize(':thumbs_up:') * 5)
if __name__ == '__main__':
    test_function()