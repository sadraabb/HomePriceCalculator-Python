---

### English Description

#### **Welcome to the Real Estate Price Calculator App! 🏠💰**

This Python script calculates the total price of a house based on user inputs. The program will:

1. **Greet the User**: It starts by greeting the user with a random name from a predefined list and then prompts the user to enter their own name.
2. **Collect Data**: The user is asked to input:
   - The price per square meter.
   - The currency they wish to use.
   - The size of the house in square meters.
3. **Calculate Total Price**: The script calculates the total price by multiplying the size of the house by the price per square meter.
4. **Save to File**: All the collected information is written to a text file named after the user.

#### **Code Overview** 📜

```python
import random
import subprocess

def welcome():
    samplename = ["Anonymous", "Guest", "unknown"]
    global Name
    Name = random.choice(samplename)
    print(f"Hi {Name}, Welcome To App")
    Name = input("Please Enter Your Name: ")
    Price_per_square_meter, Currency = int(input('Please enter the price per square meter: ')), str(input("What is your currency?"))
    square_footage = int(input("What is the size of your house? Please enter it in square meters: "))
    Total_Price = square_footage * Price_per_square_meter
    
    # List of lines to write to the file
    lines = [
        f'Name : {Name}\n',
        f'Price per square meter: {Price_per_square_meter}\n',
        f'Square footage: {square_footage}\n',
        f'Total Price: {Total_Price} {Currency}'
    ]
    
    # Writing information to a text file
    with open(f'{Name}.txt', 'w') as file:
        file.writelines(lines)

# Calling the welcome function to initialize and process the inputs
welcome()
```

**Features**:
- Randomly selects a sample name and greets the user.
- Takes user inputs for house pricing and size.
- Computes the total price and writes all information to a user-specific text file.

**Usage**:
- Run the script.
- Follow the prompts to enter your name, the price per square meter, currency, and the house size.
- Check the generated text file for details.

---

### توضیحات فارسی

#### **خوش آمدید به اپلیکیشن محاسبه قیمت خانه! 🏠💰**

این اسکریپت پایتون برای محاسبه قیمت کل خانه بر اساس ورودی‌های کاربر طراحی شده است. برنامه به صورت زیر عمل می‌کند:

1. **خوش آمدگویی به کاربر**: برنامه با استفاده از یک نام تصادفی از لیست پیش‌فرض به کاربر خوشامد می‌گوید و سپس از کاربر می‌خواهد نام خود را وارد کند.
2. **جمع‌آوری اطلاعات**: از کاربر خواسته می‌شود:
   - قیمت هر متر مربع را وارد کند.
   - واحد پول مورد نظر خود را وارد کند.
   - اندازه خانه را به متر مربع وارد کند.
3. **محاسبه قیمت کل**: برنامه قیمت کل را با ضرب اندازه خانه در قیمت هر متر مربع محاسبه می‌کند.
4. **ذخیره در فایل**: تمامی اطلاعات جمع‌آوری شده در یک فایل متنی با نام کاربر ذخیره می‌شود.

#### **بررسی کد** 📜

```python
import random
import subprocess

def welcome():
    samplename = ["Anonymous", "Guest", "unknown"]
    global Name
    Name = random.choice(samplename)
    print(f"Hi {Name}, Welcome To App")
    Name = input("Please Enter Your Name: ")
    Price_per_square_meter, Currency = int(input('Please enter the price per square meter: ')), str(input("What is your currency?"))
    square_footage = int(input("What is the size of your house? Please enter it in square meters: "))
    Total_Price = square_footage * Price_per_square_meter
    
    # لیست خطوط برای نوشتن به فایل
    lines = [
        f'Name : {Name}\n',
        f'Price per square meter: {Price_per_square_meter}\n',
        f'Square footage: {square_footage}\n',
        f'Total Price: {Total_Price} {Currency}'
    ]
    
    # نوشتن اطلاعات به فایل متنی
    with open(f'{Name}.txt', 'w') as file:
        file.writelines(lines)

# فراخوانی تابع welcome برای تعریف و مقداردهی به متغیر Name
welcome()
```

**ویژگی‌ها**:
- انتخاب نام تصادفی و خوشامدگویی به کاربر.
- دریافت ورودی‌های کاربر برای قیمت و اندازه خانه.
- محاسبه قیمت کل و ذخیره تمامی اطلاعات در فایل متنی با نام کاربر.

**نحوه استفاده**:
- اجرای اسکریپت.
- دنبال کردن پیام‌های متنی برای وارد کردن نام، قیمت هر متر مربع، واحد پول و اندازه خانه.
- بررسی فایل متنی ایجاد شده برای جزئیات.

---
