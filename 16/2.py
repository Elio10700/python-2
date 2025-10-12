# class constructor and destructor
class employee:
    def __init__(self):
        print("Employee is created")

    def __del__(self):
        print("Employee deleted")


e1 = employee()
print("In the middle")
del e1
