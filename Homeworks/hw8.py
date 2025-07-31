import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
CREATE VIEW IF NOT EXISTS low_grades_view AS
SELECT 
    users.fio AS fio,
    grades.subject AS subject,
    grades.grade AS grade,
    users.age AS age
FROM 
    users
JOIN 
    grades ON users.id = grades.user_id
WHERE 
    grades.grade < 4;
''')

cursor.execute('SELECT * FROM low_grades_view')
print(cursor.fetchall())

conn.commit()
conn.close()

