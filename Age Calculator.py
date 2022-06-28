def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
    
    
print("Enter Your DOB in yy-mm-dd format: ");
y = int(input("Enter Year: "));
m = int(input("Enter Month: "));
d = int(input("Enter Date: "));

ageCalculator(y, m, d)    
#ageCalculator(1998, 9, 3)