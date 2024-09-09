import random

print("Developer : Sadra Abbaszadeh")
def welcome():
    samplename = ["Anonymous", "Guest", "unknown"]
    global Name
    Name = random.choice(samplename)
    print(f"Hi {Name}, Welcome To App")
    Name = input("Please Enter Your Name: ")
    Price_per_square_meter,Currency = int(input('Please enter the price per square meter: ')),str(input("What is your currency?"))
    square_footage = int(input("What is the size of your house? Please enter it in square meters: "))
    Total_Price = square_footage*Price_per_square_meter
    
    # لیست خطوط برای نوشتن به فایل
    lines = [
        f'Name : {Name}\n',
        f'Price Price_per_square_meter:  {Price_per_square_meter}\n',
        f'square_footage : {square_footage}\n'
        f'Total Price : {Total_Price} {Currency}'
    ]
    
    # نوشتن اطلاعات به فایل متنی
    with open(f'{Name}.txt', 'w') as file:
        file.writelines(lines)

# فراخوانی تابع welcome برای تعریف و مقداردهی به متغیر Name
welcome()



