

```python
import pandas as pd
```


```python
file = "Resources/purchase_data.csv"
pymoli_df = pd.read_csv(file)
display(pymoli_df.head())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



```python
#Player Count
player_count = len(pymoli_df["SN"].value_counts())

total_players = pd.DataFrame({"Total Players": [player_count]})
display(total_players)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



```python
pymoli_df.columns
```




    Index(['Purchase ID', 'SN', 'Age', 'Gender', 'Item ID', 'Item Name', 'Price'], dtype='object')




```python
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
display(total_revenue.head())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>



```python
#Gender Demographics
gender_demo = pymoli_df.groupby("Gender")

gender_count = gender_demo.nunique()["SN"]
gender_per = gender_count / player_count * 100

display(gender_df = pd.DataFrame({"Total Count": gender_count,
                          "Percentage of Players": gender_per})

gender_df["Percentage of Players"] = gender_df["Percentage of Players"].map("{:.2f}".format)
gender_df.sort_values(["Total Count"], ascending = False))
```


      File "<ipython-input-6-cfe5bda7ac11>", line 10
        gender_df["Percentage of Players"] = gender_df["Percentage of Players"].map("{:.2f}".format)
                ^
    SyntaxError: invalid syntax
    



```python
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
display(gen_analysis.head())
```


```python
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
display(age_df)
```


```python
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
display(age_analysis)
```


```python
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
display(spender_analysis.head())
```


```python
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
display(item_analysis.head())
```


```python
#Most Profitable Items
item_analysis = most_popular.sort_values(by=["Purchase Count", "Item Price", "Total Purchase Value"], ascending=False)
display(item_analysis.head())
```


```python
#Sources:
    #Percentage of unique values syntax (https://stackoverflow.com/questions/50558458/pandas-percentage-by-value-in-a-column)
    #Data Wrangling with Pandas Cheat Sheet (http://pandas.pydata.org)
    #Python for Data Science Cheat Sheet: Pandas Basics (www.DataCamp.com)
    #Pandas PyData (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)
```
