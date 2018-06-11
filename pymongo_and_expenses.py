from pymongo import mongo_client
import pprint, time, datetime, openpyxl as px

def create_posts():
    expenses = []
    for i in range(2, max+1):
        expenses.append({
        "Expense": month_data['A{}'.format(i)].value,
        "Category": month_data['B{}'.format(i)].value,
        "Notes": month_data['C{}'.format(i)].value,
        "Cost": month_data['D{}'.format(i)].value,
        })
    return expenses

print('(Make sure mongod is running...)')
time.sleep(1)

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
year = '2016'
# year = datetime.datetime.today().strftime('%Y')
# month = datetime.datetime.today().strftime('%m')
wb = px.load_workbook('{} Monthly Expenses.xlsx'.format(year))
month = input('what month?\n')
month_data = wb.get_sheet_by_name(labels[int(month)-1])
max = month_data.max_row


client = mongo_client.MongoClient('localhost', 27017)

db = client.month_expenses

expenses = create_posts()

post = {
    "Month": month,
    "Expenses": expenses
}

posts = db["yr{}".format(year)]

posts.insert_one(post)

pprint.pprint(posts.find())
print('Success!')
