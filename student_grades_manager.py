students=[]
def main():
    while True:
        print("""1- Add new studends and marks 
                 2- Show students and their marks
                 3- Average students marks
                 4- Show if the student faild or passed
                 5- Quit""")
        choice=input('choose what you want: ').strip()
        if choice =='1':
            add_new_students()
        elif choice=='2':
            display_students()
        elif choice =='3':
            show_average()
        elif choice =='4':
            check_result()
        elif choice=='5':
            print('Goodbye!')
            break
        else:
            print('invalid choice , please enter number between 1 and 5')


def get_valid_mark(subject):
    while True:
        try:
            marks= float(input(f'Enter {subject} mark between 0 and 100: '))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid mark! Enter a number between 0 and 100")
        except ValueError:
            print("please enter a valid number")
            continue

def add_new_students():
    while True:
        try:
            count = int(input('how many students you want to add: '))
            break        
        except ValueError:
            print("please enter a valid number")    
    for _ in range(count):    
        name = input('enter the student name: ').strip()
        math = get_valid_mark('math')
        english = get_valid_mark('english')
        python = get_valid_mark('python')
        students.append({
            'name': name,
            'math': math,
            'english': english,
            'python': python })
        print('student and marks added successfully')


def display_students():
    if not students:
        print('no students yet')
        return
    for student in students:
        print(f'Name: {student['name']} ,Math: {student['math']}, English: {student['english']}, Python: {student['python']}')

    
def show_average():
    if not students:
        print('no students yet')
        return
    for student in students:
        total_marks = student['math']+ student['english']+ student['python']
        average= total_marks/3
        print(f"{student['name']} : {average:.2f}")


def check_result():
    if not students:
        print('no students yet')
        return
    for student in students:
        result= (student['math']+ student['english']+ student['python'])/3
        status= "passed" if result >= 50 else "failed"
        print(f'{student["name"]} has {status}')

main()