import sqlite3

conn = sqlite3.connect('school_db.db')
cursor = conn.cursor()


# Create groups table
cursor.execute('''
    create table if not exists groups (
        group_id integer primary key autoincrement,
        group_name varchar(255)
    )
''')

# Create students table
cursor.execute('''
    create table if not exists students (
        student_id integer primary key autoincrement,
        student_name varchar(255),
        group_id int,
        foreign key (group_id) references groups(group_id)
    )
''')

# Create teachers table
cursor.execute('''
    create table if not exists teachers (
        teacher_id integer primary key autoincrement,
        teacher_name varchar(255)
    )
''')

# Create subjects table
cursor.execute('''
    create table if not exists subjects (
        subject_id integer primary key autoincrement,
        subject_name varchar(255),
        teacher_id int,
        foreign key (teacher_id) references teachers(teacher_id)
    )
''')

# Create grades table
cursor.execute('''
    create table if not exists grades (
        grade_id integer primary key autoincrement,
        student_id int,
        subject_id int,
        grade float,
        date date,
        foreign key (student_id) references students(student_id),
        foreign key (subject_id) references subjects(subject_id)
    )
''')

conn.commit()
conn.close()
