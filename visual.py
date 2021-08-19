import streamlit as st
from PIL import Image 
import pandas as pd

def main():
    # Register your pages
    pages = {
        "Home" : page_home,
        "Sales per Hour": page_sales,
        "Product Analysis": page_product,
        "Customer Analysis": page_customer,
    }
    pages1 = {
        "Home" : page1_home,
        "Health and Beauty": page1_hb,
        "Electronic Accessories": page1_ea,
        "Home and Lifestyle": page1_hl,
        "Sports and Travel": page1_st,
        "Food and Beverages": page1_fb,
        "Fashion Accessories": page1_fa
    }
        
    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.selectbox("Exploratory Data Analysis", tuple(pages.keys()))
    page1 = st.sidebar.radio("ARIMA Forecasting", tuple(pages1.keys()))

    # Display the selected page with the session state
    pages[page]()
    pages1[page1]()
    
def page_home():
    st.title("Demand Forecasting for Supermarket Product Sales")
    st.write('''Demand forecasting is an analytical technique used for predicting the demand for a product over time. 
    In simple terms, it enables you to estimate future sales so that you can plan your stock levels accordingly.
But, demand forecasting has much bigger superpowers than simply telling you how much stock to order. 
It can also help you to achieve the following.  \n

**1. Practice informed inventory planning**  \n
Informed inventory planning reduces the amount of unsellable stock that you hold while ensuring that you don’t sell out of popular items. 
This means that you can meet demand without slow-moving stock draining your warehouse space or profits.  \n

**2. Better manage your cashflow**  \n
With less money tied up in slow-moving stock and more awareness of when to buy more stock, 
you can better plan your other budgets throughout the year, such as research and development.  \n

**3. Plan marketing, advertisements, and discounts**  \n
Knowing the points in the year when a product will sell well or struggle can help you to 
better plan your marketing, advertising, and discounting activities.  \n

**4. Negotiate**  \n
And, being able to forecast your sales can also assist with supplier, lender, and other negotiations that are taking place.  \n
''')
def page1_home():    
    st.write("")
    

def page_sales():
    st.title("Sales per Hour")
    
    st.markdown("***Sales by the hour in the company***")
    st.markdown("Most of the item were sold around 14:00 hrs local time")
    img=Image.open('sales_hour.png')
    st.image(img)
    
    st.markdown("**Every branch's sales per hour by quantity and gender for each of the three months**")
    img1=Image.open('sales_hour_gender.png')
    st.image(img1)
    
    st.markdown("**Each branch's sales by the hour in a monthly fashion**")
    img2=Image.open('sales_hour_branch.png')
    st.image(img2)
    


def page_product():
    st.title("Product Analysis")
    
    st.markdown("**Number of products sold under 6 categories in the period of 3 months cumulative of all the 3 stores**")
    image1=Image.open('product_count.png')
    st.image(image1)
    
    st.markdown("**Product rating received from customer over their products purchased in the period of 3 months **")
    image2=Image.open('product_rating.png')
    st.image(image2)
    
    st.markdown("**Products purchased under 6 product lines by Men and Women in the period of 3 months cumulative of all the 3 stores**")
    image3=Image.open('product_gender.png')
    st.image(image3)
    

def page_customer():
    st.title("Customer Analysis")
    
    st.markdown("**Rating for Stores received from customers in the period of 3 months**")
    imagee1=Image.open('branch_rating.png')
    st.image(imagee1)
    st.markdown("Store B has the least rating compared to Store A and C")
    
    st.markdown("**Count of customers who purchased their products at 3 differnt stores in the period of 3 months**")
    st.write('''Types of Customers  \n 1) **Registered Memebers**  \n 2) **Normal Customers**  \n''')
    imagee2=Image.open('customer_type_branch.png')
    st.image(imagee2)
    
    st.markdown("**Customer Rating for 3 different stores based on the Type of customer they are**")
    imagee3=Image.open('cust_rating_city.png')
    st.image(imagee3)
    
    st.markdown("**Count of customers with Payment Methods at 3 stores**")
    imagee4=Image.open('payment_branch.png')
    st.image(imagee4)
    
    
def page1_hb():
    st.title("Health and Beauty with ARIMA Model")
    st.markdown("Demand Forecasting for Health and Beauty with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Health and Beauty products at Store A**")  
    pic1a=Image.open('HBA.png')
    st.image(pic1a)
    st.markdown("**Forecasting the sales for Health and Beauty products at Store B**")    
    pic1b=Image.open('HBB.png')
    st.image(pic1b)    
    st.markdown("**Forecasting the sales for Health and Beauty products at Store C**")    
    pic1c=Image.open('HBC.png')
    st.image(pic1c)
def page1_ea():
    st.title("Electronic Accessories with ARIMA Model")
    st.markdown("Demand Forecasting for Electronic Accessories with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Electronic Accessories products at Store A**")  
    pic2a=Image.open('EAA.png')
    st.image(pic2a)
    st.markdown("**Forecasting the sales for Electronic Accessories products at Store B**")    
    pic2b=Image.open('EAB.png')
    st.image(pic2b)    
    st.markdown("**Forecasting the sales for Electronic Accessories products at Store C**")    
    pic2c=Image.open('EAC.png')
    st.image(pic2c)
def page1_hl():
    st.title("Home and Lifestyle with ARIMA Model")
    st.markdown("Demand Forecasting for Home and Lifestyle with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Home and Lifestyle products at Store A**")  
    pic3a=Image.open('HLA.png')
    st.image(pic3a)
    st.markdown("**Forecasting the sales for Home and Lifestyle products at Store B**")    
    pic3b=Image.open('HLB.png')
    st.image(pic3b)    
    st.markdown("**Forecasting the sales for Home and Lifestyle products at Store C**")    
    pic3c=Image.open('HLC.png')
    st.image(pic3c)
def page1_st():
    st.title("Sports and Travel with ARIMA Model")
    st.markdown("Demand Forecasting for Sports and Travel with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Sports and Travel products at Store A**")  
    pic4a=Image.open('STA.png')
    st.image(pic4a)
    st.markdown("**Forecasting the sales for Sports and Travel products at Store B**")    
    pic4b=Image.open('STB.png')
    st.image(pic4b)    
    st.markdown("**Forecasting the sales for Sports and Travel products at Store C**")    
    pic4c=Image.open('STC.png')
    st.image(pic4c)
def page1_fb():
    st.title("Food and Beverages with ARIMA Model")
    st.markdown("Demand Forecasting for Food and Beverages with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Food and Beverages products at Store A**")  
    pic5a=Image.open('FBA.png')
    st.image(pic5a)
    st.markdown("**Forecasting the sales for Food and Beverages products at Store B**")    
    pic5b=Image.open('FBB.png')
    st.image(pic5b)    
    st.markdown("**Forecasting the sales for Food and Beverages products at Store C**")    
    pic5c=Image.open('FBC.png')
    st.image(pic5c)
    
def page1_fa():
    st.title("Fashion Accessories with ARIMA Model")
    st.markdown("Demand Forecasting for Fashion Accessories with ARIMA Model across all the 3 stores in the perios of 3 months")
    st.markdown("**Forecasting the sales for Fashion Accessories products at Store A**")    
    pic6a=Image.open('FAA.png')
    st.image(pic6a)
    st.markdown("**Forecasting the sales for Fashion Accessories products at Store B**")    
    pic6b=Image.open('FAB.png')
    st.image(pic6b)    
    st.markdown("**Forecasting the sales for Fashion Accessories products at Store C**")    
    pic6c=Image.open('FAC.png')
    st.image(pic6c)
    
    
    
if __name__ == "__main__":
    main()