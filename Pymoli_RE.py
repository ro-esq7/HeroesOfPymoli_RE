#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = "Resources/purchase_data.csv"
pymoli_df = pd.read_csv(file)
pymoli_df.head()


# In[3]:


#Player Count
player_count = len(pymoli_df["SN"].value_counts())

total_players = pd.DataFrame({"Total Players": [player_count]})
total_players


# In[4]:


pymoli_df.columns


# In[5]:


#Purchasing Analysis (Totals)
purchase_analysis = {
    "Number of Unique Items": [len((pymoli_df["Item ID"]).unique())], 
    "Average Price": [pymoli_df["Price"].mean()],
    "Number of Purchases": [(pymoli_df["Purchase ID"]).count()], 
    "Total Revenue": [(pymoli_df["Price"]).sum()]
}

total_revenue = pd.DataFrame(purchase_analysis, columns=[
    "Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"])
total_revenue

total_revenue['Average Price'] = total_revenue['Average Price'].map("${:.2f}".format)
total_revenue['Total Revenue'] = total_revenue['Total Revenue'].map("${:,.2f}".format)
total_revenue.head()


# In[6]:


#Gender Demographics
gender_demo = pymoli_df.groupby("Gender")

gender_count = gender_demo.nunique()["SN"]
gender_per = gender_count / player_count * 100

gender_df = pd.DataFrame({"Total Count": gender_count,
                          "Percentage of Players": gender_per})

gender_df["Percentage of Players"] = gender_df["Percentage of Players"].map("{:.2f}".format)
gender_df.sort_values(["Total Count"], ascending = False)


# In[7]:


#Purchasing Analysis (by gender)
pur_count = gender_demo["Purchase ID"].count()
avg_price = gender_demo["Price"].mean()
avg_total = gender_demo["Price"].sum()
avg_pur = avg_total/gender_count

gen_analysis = pd.DataFrame({"Purchase Count": pur_count, 
                             "Average Purchase Price": avg_price, 
                             "Total Purchase Value": avg_total, 
                             "Avg Purchase Total per Person": avg_pur})

gen_analysis["Average Purchase Price"] = gen_analysis["Average Purchase Price"].map("${:,.2f}".format)
gen_analysis["Total Purchase Value"] = gen_analysis["Total Purchase Value"].map("${:,.2f}".format)
gen_analysis["Avg Purchase Total per Person"] = gen_analysis["Avg Purchase Total per Person"].map("${:,.2f}".format)
gen_analysis.head()


# In[8]:


#Age Demographics
bins = [0, 9, 14, 19, 24, 29, 34, 39, 50]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

pymoli_df["Age"] = pd.cut(pymoli_df["Age"], bins, labels=group_names)

age_demo = pymoli_df.groupby("Age")
age_total = age_demo["SN"].nunique()
age_per = age_total/player_count * 100

age_df = pd.DataFrame({"Total Count": age_total,
                      "Percentage of Players": age_per})

age_df["Percentage of Players"] = age_df["Percentage of Players"].map("{:.2f}".format)
age_df


# In[9]:


#Purchasing Analysis (by age)
age_count = age_demo["Purchase ID"].count()
age_price = age_demo["Price"].mean()
age_total_pur = age_demo["Price"].sum()
age_pur = age_total_pur/age_total

age_analysis = pd.DataFrame({"Purchase Count": age_count, 
                             "Average Purchase Price": age_price, 
                             "Total Purchase Value": age_total_pur, 
                             "Avg Purchase Total per Person": age_pur})

age_analysis["Average Purchase Price"] = age_analysis["Average Purchase Price"].map("${:,.2f}".format)
age_analysis["Total Purchase Value"] = age_analysis["Total Purchase Value"].map("${:,.2f}".format)
age_analysis["Avg Purchase Total per Person"] = age_analysis["Avg Purchase Total per Person"].map("${:,.2f}".format)
age_analysis


# In[10]:


#Top Spenders
top_spender = pymoli_df.groupby("SN")
spender_count = top_spender["Purchase ID"].count()
spender_avg_pur = top_spender["Price"].mean()
spender_total = top_spender["Price"].sum()

top_df = pd.DataFrame({"Purchase Count": spender_count,
                      "Average Purchase Price": spender_avg_pur,
                      "Total Purchase Value": spender_total})

top_df["Average Purchase Price"] = top_df["Average Purchase Price"].map("${:,.2f}".format)
top_df["Total Purchase Value"] = top_df["Total Purchase Value"].map("${:,.2f}".format)
top_df

spender_analysis = top_df.sort_values(by=["Purchase Count", "Average Purchase Price", "Total Purchase Value"], ascending=False)
spender_analysis.head()


# In[11]:


#Most Popular Items

#Retrieve the Item ID, Item Name, and Item Price columns
items = pymoli_df[["Item ID", "Item Name", "Price"]]

#Group by Item ID and Item Name
popular_items = pymoli_df.groupby(["Item ID", "Item Name"])

item_count = popular_items["Price"].count()
item_tvalue = popular_items["Price"].sum()
item_price = item_tvalue/item_count

most_popular = pd.DataFrame({"Purchase Count": item_count,
                            "Item Price": item_price,
                            "Total Purchase Value": item_tvalue})

most_popular["Item Price"] = most_popular["Item Price"].map("${:,.2f}".format)
most_popular["Total Purchase Value"] = most_popular["Total Purchase Value"].map("${:,.2f}".format)
most_popular

item_analysis = most_popular.sort_values(by=["Purchase Count"], ascending=False)
item_analysis.head()


# In[12]:


#Most Profitable Items
item_analysis = most_popular.sort_values(by=["Purchase Count", "Item Price", "Total Purchase Value"], ascending=False)
item_analysis.head()


# In[13]:


#Sources:
    #Percentage of unique values syntax (https://stackoverflow.com/questions/50558458/pandas-percentage-by-value-in-a-column)
    #Data Wrangling with Pandas Cheat Sheet (http://pandas.pydata.org)
    #Python for Data Science Cheat Sheet: Pandas Basics (www.DataCamp.com)
    #Pandas PyData (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)

