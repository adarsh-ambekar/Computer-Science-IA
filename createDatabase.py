import pandas as pd
import sqlite3 as sl


con = sl.connect('system.db')

# Create student database
studentList = pd.DataFrame({
    'name': [],
    'studentID': [],
    'username': [],
    'password': [],
    'attendanceDates': [],
    'attendanceCodes': []
})
studentList.to_sql("studentList", con, index=False)