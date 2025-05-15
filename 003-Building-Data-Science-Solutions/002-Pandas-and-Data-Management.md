### 📦 What is Data Management?

**Data Management** refers to the systematic process of **collecting, organizing, storing, processing, and maintaining data** throughout its lifecycle. It includes practices that ensure data is **accurate, accessible, consistent, secure, and usable** for analysis or decision-making.

For a data scientist, data management is not just a backend operation—it's a **core competency** that directly influences the quality and success of any data science project.

---

### 🧠 Why is Data Management Important for Data Scientists?

1. **Foundation for Analysis**  
   Poorly managed data leads to inaccurate insights. Clean, well-structured data is the starting point for any model or analysis.

2. **Efficiency and Reusability**  
   Well-organized data reduces repetitive work and enables faster iterations, especially in large or collaborative projects.

3. **Scalability**  
   Robust data management allows you to handle increasing data volumes and complexity with ease.

4. **Reproducibility**  
   A managed dataset ensures your results can be reliably reproduced—a must in research and enterprise settings.

5. **Compliance and Ethics**  
   Ensures that sensitive or personal data is handled securely and responsibly, aligning with legal and ethical standards.

6. **Model Performance**  
   The best machine learning algorithms cannot compensate for poor data. Proper preprocessing, imputation, and transformation are key to model success.

---

### ✅ Summary:

> **"Good data science starts with good data management."**  
> Without it, even the most advanced algorithms are built on shaky ground.

---

### 📘 **Introduction**

> **Data management and manipulation** are foundational skills for data scientists. They involve preparing, cleaning, transforming, and organizing data to make it suitable for analysis and modeling. Without strong data handling practices, even the most advanced algorithms will fail to produce meaningful results.

---

### 📋 **Table: Data Management & Manipulation Tasks**

| **Main Task**                  | **Subtasks**                                                 | **Purpose / Description**                                       |
| ------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **1. Data Loading**            | Load from CSV, Excel, JSON, SQL, API                         | Bring raw data into your working environment                    |
| **2. Data Inspection**         | `.head()`, `.info()`, `.describe()`, `.shape`, `.columns`    | Understand structure, types, completeness, and distributions    |
| **3. Data Subsetting**         | Select rows/columns, use `iloc`, `loc`, filtering conditions | Work with relevant slices of the data                           |
| **4. Data Cleaning**           | Handle missing values, fix typos, remove duplicates          | Improve quality and integrity of the data                       |
| **5. Type Conversion**         | Convert strings to dates, floats to integers, etc.           | Ensure variables have correct formats for processing            |
| **6. Data Transformation**     | Create new columns, `apply()`, `map()`, use of `lambda`      | Derive features or reframe values for modeling or visualization |
| **7. Aggregation**             | `groupby()`, mean, sum, count                                | Summarize data by groups to extract patterns                    |
| **8. Sorting & Ranking**       | `sort_values()`, `rank()`                                    | Organize data for readability or stepwise processing            |
| **9. Merging & Joining**       | `merge()`, `join()`, `concat()`                              | Combine datasets from different sources or views                |
| **10. Reshaping Data**         | `melt()`, `pivot()`, `stack()`, `unstack()`                  | Convert between wide and long formats                           |
| **11. Exporting Data**         | Save to CSV, Excel, SQL, etc.                                | Store cleaned or transformed data for reuse or sharing          |
| **12. Time Series Management** | Parse datetime, resample, shift, rolling mean                | Prepare and analyze data that has a temporal component          |

---

### 🐼 **Pandas Library in Python: A Brief Overview**

---

### 📚 **What is Pandas?**

**Pandas** is an open-source Python library used for **data manipulation, analysis, and cleaning**. It provides high-performance, easy-to-use data structures such as:

- **Series** – a one-dimensional labeled array.

- **DataFrame** – a two-dimensional, tabular data structure (like an Excel sheet in code).

It is widely used by data scientists, analysts, and developers to **handle structured data efficiently**, especially in data preprocessing and exploratory data analysis (EDA).

---

### 🕰️ **Brief History**

- Developed by **Wes McKinney** in **2008** at AQR Capital to solve the lack of robust data tools in Python.

- Initially designed for financial modeling, but its flexibility led to widespread use in **scientific computing**, **machine learning**, and **business analytics**.

- The name "pandas" is derived from "**panel data**," an econometrics term referring to multidimensional structured data.

---

### ⚙️ **How to Install Pandas**

To install Pandas, you can use pip or conda:

#### ✅ Using pip (Python’s default package manager):

```bash
pip install pandas
```

#### ✅ Using conda (Anaconda distribution):

```bash
conda install pandas
```

Make sure your Python version is 3.7 or higher for full feature support.

---

### 🧪 **How to Load Pandas in Your Python Script or Notebook**

Once installed, import it in your code using the conventional alias `pd`:

```python
import pandas as pd
```

This `pd` alias is a widely accepted convention in the Python community.

---

### 🚀 Example of Basic Usage

```python
import pandas as pd

# Creating a simple DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

print(df)
```

**Output:**

```
    Name  Age
0  Alice   25
1    Bob   30
```

---

### 📌 In Summary:

> **Pandas is to Python what Excel is to spreadsheets**—but vastly more powerful, programmable, and scalable.  
> Learning Pandas is foundational for any data-driven role in Python.





### 🧪 Case Study 1: **Loading and Exploring a Sales Dataset**

---

#### 1. **Case Study Title**

**Loading and Exploring Raw Sales Data**

---

#### 2. **Case Study Description**

As a data analyst at a retail firm, you've been given a sales dataset stored in an Excel file. Your task is to load this dataset and perform a basic exploration to understand its structure, data types, and value distributions. This initial exploration is crucial before any cleaning, transformation, or modeling is done.

---

#### 3. **Problem Solving Approach**

- Load the dataset using Pandas.

- Inspect the top and bottom records.

- Check the structure: number of rows and columns.

- Identify data types of each column.

- Examine summary statistics and detect missing values.

---

#### 4. **Python Code**

```python
import pandas as pd

# 🧭 Step 1: Load the dataset from Excel
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")

# 👀 Step 2: View the first 5 rows to get a feel for the data
print("Top 5 rows:")
print(df_sales.head())

# 🔍 Step 3: Check the shape (number of rows and columns)
print("\nShape of the dataset:")
print(df_sales.shape)

# 🧱 Step 4: Inspect column names and data types
print("\nData types and non-null counts:")
print(df_sales.info())

# 📊 Step 5: Summary statistics for numerical columns
print("\nDescriptive statistics:")
print(df_sales.describe())

# ❓ Step 6: Identify columns with missing values
print("\nMissing values per column:")
print(df_sales.isnull().sum())
```

---

Perfect! Let's structure this **Case Study 2** with a progression—starting from **filtering with one condition**, then moving to **multiple criteria filtering**.

---

### 🧪 Case Study 2: **Subsetting and Filtering Sales Data**

---

#### 1. **Case Study Title**

**From Simple to Complex: Filtering Sales Records Using One or More Conditions**

---

#### 2. **Case Study Description**

As a data analyst, you often need to isolate specific slices of data. In this case, you want to:

- First, focus on one **product category** (e.g., *Electronics*).

- Then, apply additional filters such as **sales region** or **payment method**.

This step-by-step filtering is important for running focused analyses like regional performance, customer behavior, or seasonal trends.

---

#### 3. **Problem Solving Approach**

- Load the dataset from Excel.

- Start with a single-condition filter (e.g., product category).

- Expand to a multi-condition filter using logical operators (`&`, `|`).

- Use `.loc[]` for clear and safe subsetting.

- Preview and validate the resulting subset.

---

#### 4. **Python Code (Documented & Inline Comments)**

```python
import pandas as pd

# 📥 Step 1: Load the sales dataset
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")

# ------------------------------------------------------
# 🎯 PART A: Filter by One Condition
# Goal: Select all sales records where Product_Category is "Electronics"
# ------------------------------------------------------

# 🔍 Filter using boolean indexing with .loc[]
electronics_sales = df_sales.loc[df_sales['Product_Category'] == 'Electronics']

# 🖥️ View the first few rows of the filtered dataset
print("Sales records for Electronics category:")
print(electronics_sales.head())

# 📊 Display number of records retrieved
print(f"Total Electronics Records: {electronics_sales.shape[0]}")

# ------------------------------------------------------
# 🎯 PART B: Filter by Multiple Conditions
# Goal: Now further filter where Region is either 'North' or 'East'
# ------------------------------------------------------

# 🧠 Use logical AND (&) and .isin() for region filtering
filtered_sales = df_sales.loc[
    (df_sales['Product_Category'] == 'Electronics') &
    (df_sales['Region'].isin(['North', 'East']))
]

# 📋 Review the filtered records
print("\nElectronics sales in North or East regions:")
print(filtered_sales.head())

# 📊 Display number of records retrieved
print(f"Total Filtered Records: {filtered_sales.shape[0]}")
```

---

### 🧪 Case Study 3: **Data Cleaning and Missing Value Handling**

---

#### 1. **Case Study Title**

**Identifying and Handling Missing Customer Ratings in Sales Data**

---

#### 2. **Case Study Description**

You're analyzing customer satisfaction using the `Customer_Rating` column. However, you discover that some records have missing ratings. Your task is to:

- Detect these missing values,

- Decide whether to fill them with a meaningful default (e.g., average rating), or

- Remove records if appropriate.

This step ensures **data quality** and avoids issues in downstream statistical or ML models.

---

#### 3. **Problem Solving Approach**

- Use `.isnull().sum()` to count missing values in each column.

- Focus on `Customer_Rating` to see how many are missing.

- Apply different strategies: drop missing values vs. fill with average.

- Validate changes using `.info()` and value counts.

---

#### 4. **Python Code (Documented & Inline Comments)**

```python
import pandas as pd

# 📥 Step 1: Load the sales dataset
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")

# 🔍 Step 2: Identify columns with missing values
print("Missing values per column:")
print(df_sales.isnull().sum())

# 🎯 Focus on the Customer_Rating column
missing_ratings = df_sales['Customer_Rating'].isnull().sum()
print(f"\nTotal missing customer ratings: {missing_ratings}")

# 🧪 Step 3a: Strategy 1 - Fill missing values with mean rating
mean_rating = df_sales['Customer_Rating'].mean()
df_filled = df_sales.copy()
df_filled['Customer_Rating'] = df_filled['Customer_Rating'].fillna(mean_rating)

print("\nCustomer ratings after filling missing values with mean:")
print(df_filled['Customer_Rating'].describe())

# 🧪 Step 3b: Strategy 2 - Drop rows with missing ratings
df_dropped = df_sales.dropna(subset=['Customer_Rating'])

print(f"\nRecords after dropping rows with missing Customer_Rating: {df_dropped.shape[0]}")

# ✅ Step 4: Choose a final cleaned version for downstream tasks
# Let's assume we go with the filled version for further use.
df_cleaned = df_filled
```

---

### 🧪 Case Study 4: **Type Conversion and Column Transformation**

---

#### 1. **Case Study Title**

**Converting Order Dates and Creating a New Sales Week Column**

---

#### 2. **Case Study Description**

You’ve been asked to perform **time-based sales analysis**, but the `Order_Date` column is currently in object (string) format. Your task is to:

- Convert the column to proper datetime format.

- Extract new useful columns like *year*, *month*, or *week*.

- This will enable time-series visualizations and period-based aggregation.

---

#### 3. **Problem Solving Approach**

- Use `pd.to_datetime()` to convert the `Order_Date` column.

- Use `.dt` accessor to extract date components (like year, month, day of week).

- Create new columns: `Order_Year`, `Order_Month`, and `Sales_Week`.

- Validate the transformations by checking new column types and values.

---

#### 4. **Python Code (Documented & Inline Comments)**

```python
import pandas as pd

# 📥 Step 1: Load the dataset
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")

# 👁️ Step 2: Check the current type of 'Order_Date'
print("Data type before conversion:")
print(df_sales['Order_Date'].dtype)

# 🔁 Step 3: Convert 'Order_Date' to datetime format
df_sales['Order_Date'] = pd.to_datetime(df_sales['Order_Date'])

# 🧠 Step 4: Extract date parts into new columns
df_sales['Order_Year'] = df_sales['Order_Date'].dt.year
df_sales['Order_Month'] = df_sales['Order_Date'].dt.month
df_sales['Order_Week'] = df_sales['Order_Date'].dt.isocalendar().week
df_sales['Day_of_Week'] = df_sales['Order_Date'].dt.day_name()

# ✅ Step 5: Verify transformation
print("\nTransformed dataset with date features:")
print(df_sales[['Order_Date', 'Order_Year', 'Order_Month', 'Order_Week', 'Day_of_Week']].head())
```

---



### 🧪 Case Study 5: **Creating New Columns and Derived Features**

---

#### 1. **Case Study Title**

**Calculating Discounted Sales and Engagement Score Using Pure Pandas**

---

#### 2. **Case Study Description**

As part of business enrichment:

- Apply a **10% discount** to orders above ₹3000 and retain others as-is.

- Create a **Customer Engagement Score** that multiplies quantity by rating.

The challenge: Perform all transformations **using only Pandas methods**—ideal for pure Pandas learners and environments where NumPy is restricted.

---

#### 3. **Problem Solving Approach**

- Use `pd.Series.where()` to apply conditions inside Pandas.

- Use `*` operator and fill missing values using `.fillna()` before mathematical operations.

- Add the new columns to the DataFrame and validate the results.

---

#### 4. **Python Code (Pandas-Only, Fully Documented)**

```python
import pandas as pd

# 📥 Step 1: Load the sales dataset
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")

# 🧼 Step 2: Handle missing Customer_Rating before using it
# Fill NaN ratings with the column mean
mean_rating = df_sales['Customer_Rating'].mean()
df_sales['Customer_Rating'] = df_sales['Customer_Rating'].fillna(mean_rating)

# 💰 Step 3: Create 'Discounted_Price' using pandas where()
# If Total_Price > 3000, apply 10% discount, else keep original value
df_sales['Discounted_Price'] = df_sales['Total_Price'].where(
    df_sales['Total_Price'] <= 3000,  # Condition
    df_sales['Total_Price'] * 0.9     # Value if condition is False
)

# 📈 Step 4: Create 'Engagement_Score' using Quantity × Customer_Rating
df_sales['Engagement_Score'] = df_sales['Quantity'] * df_sales['Customer_Rating']

# 🖥️ Step 5: Preview new features
print("Newly engineered columns preview:")
print(df_sales[['Total_Price', 'Discounted_Price', 'Quantity', 'Customer_Rating', 'Engagement_Score']].head())
```

---

### 🧪 Case Study 6: **Joining Sales Data with Customer, Product, and Region Information**

---

#### 1. **Case Study Title**

**Merging Multiple Data Sources to Create a Unified Sales View**

---

#### 2. **Case Study Description**

Your raw sales data only contains IDs for customers, products, and regions. To perform meaningful analysis (like understanding customer loyalty, product brands, or regional management), you need to join additional datasets:

- **Customer Info**

- **Product Info**

- **Region Info**

Your goal is to build a single, enriched DataFrame containing all relevant descriptive information for each sale.

---

#### 3. **Problem Solving Approach**

- Load all four datasets: Sales, Customers, Products, Regions.

- Use `merge()` to join datasets step-by-step based on shared keys:
  
  - `Customer_ID` for customer details.
  
  - `Product_ID` for product details.
  
  - `Region` for region-level details.

- Validate the merged DataFrame by checking shape and columns.

---

#### 4. **Python Code**

```python
import pandas as pd

# 📥 Step 1: Load all datasets
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")
df_customers = pd.read_excel("customer_info.xlsx")
df_products = pd.read_excel("product_info.xlsx")
df_regions = pd.read_excel("region_info.xlsx")

# 👤 Step 2: Merge sales with customer info on 'Customer_ID'
df_merged = pd.merge(df_sales, df_customers, on='Customer_ID', how='left')

# 📦 Step 3: Merge with product info on 'Product_ID'
df_merged = pd.merge(df_merged, df_products, on='Product_ID', how='left')

# 🌍 Step 4: Merge with region info on 'Region'
df_merged = pd.merge(df_merged, df_regions, on='Region', how='left')

# ✅ Step 5: Preview the enriched dataset
print("Unified sales dataset with customer, product, and region info:")
print(df_merged.head())

# 🧾 Step 6: Verify shape and columns
print("\nShape of merged dataset:", df_merged.shape)
print("\nColumns in merged dataset:")
print(df_merged.columns.tolist())
```

---

### 🧪 Case Study 7: **Grouping, Aggregating, and Creating Summary Reports**

---

#### 1. **Case Study Title**

**Generating Regional Sales and Customer Satisfaction Summary Using GroupBy**

---

#### 2. **Case Study Description**

Now that we have a unified dataset (from Case Study 6), we want to generate meaningful business summaries:

- Total and average sales per **region**.

- Average customer rating and quantity sold per **product category**.

- Summary statistics for **payment methods**.

Such grouped analyses are frequently used in **dashboards, reports, and executive summaries**.

---

#### 3. **Problem Solving Approach**

- Use `groupby()` to aggregate data by region, product category, and payment method.

- Apply multiple aggregation functions like `sum()`, `mean()`, and `count()`.

- Reset index to convert grouped data into standard DataFrame format.

- Sort and format output for easy interpretation.

---

#### 4. **Python Code (Pandas Only, Fully Documented)**

```python
import pandas as pd

# 📥 Step 1: Load merged dataset
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")
df_customers = pd.read_excel("customer_info.xlsx")
df_products = pd.read_excel("product_info.xlsx")
df_regions = pd.read_excel("region_info.xlsx")

df_merged = pd.merge(df_sales, df_customers, on='Customer_ID', how='left')
df_merged = pd.merge(df_merged, df_products, on='Product_ID', how='left')
df_merged = pd.merge(df_merged, df_regions, on='Region', how='left')

# ------------------------------------------------------
# 📊 Grouping 1: Total and Average Sales by Region
# ------------------------------------------------------
region_summary = df_merged.groupby('Region').agg(
    Total_Sales=('Total_Price', 'sum'),
    Average_Sales=('Total_Price', 'mean'),
    Order_Count=('Order_ID', 'count')
).reset_index()

print("Regional Sales Summary:")
print(region_summary)

# ------------------------------------------------------
# 🎯 Grouping 2: Avg Rating and Quantity by Product Category
# ------------------------------------------------------
product_summary = df_merged.groupby('Product_Category').agg(
    Avg_Rating=('Customer_Rating', 'mean'),
    Total_Quantity_Sold=('Quantity', 'sum')
).reset_index()

print("\nProduct Category Summary:")
print(product_summary)

# ------------------------------------------------------
# 💳 Grouping 3: Payment Method Summary
# ------------------------------------------------------
payment_summary = df_merged.groupby('Payment_Method').agg(
    Count=('Order_ID', 'count'),
    Avg_Purchase_Amount=('Total_Price', 'mean')
).reset_index()

print("\nPayment Method Summary:")
print(payment_summary)
```

---

### 🧪 Case Study 8: **Sorting, Ranking, and Identifying Top Performers**

---

#### 1. **Case Study Title**

**Finding Top-Selling Products and High-Spending Customers**

---

#### 2. **Case Study Description**

Business stakeholders often want answers to questions like:

- Which products generated the highest revenue?

- Who are our top customers based on spending?

- What regions perform the best?

To answer such questions, we’ll use **sorting**, **ranking**, and **top-N filtering**.

---

#### 3. **Problem Solving Approach**

- Use `groupby()` to calculate totals by product or customer.

- Apply `sort_values()` to rank by revenue or quantity.

- Use `.head()` to extract top-N records.

- Optionally use `rank()` to assign ranking positions.

---

#### 4. **Python Code (Fully Documented & Pandas-Only)**

```python
import pandas as pd

# 📥 Step 1: Load and merge datasets
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")
df_customers = pd.read_excel("customer_info.xlsx")
df_products = pd.read_excel("product_info.xlsx")
df_regions = pd.read_excel("region_info.xlsx")

df_merged = pd.merge(df_sales, df_customers, on='Customer_ID', how='left')
df_merged = pd.merge(df_merged, df_products, on='Product_ID', how='left')
df_merged = pd.merge(df_merged, df_regions, on='Region', how='left')

# ------------------------------------------------------
# 🛍️ Top 5 Best-Selling Products (By Revenue)
# ------------------------------------------------------
product_revenue = df_merged.groupby('Product_ID').agg(
    Product_Name=('Product_Name', 'first'),
    Total_Revenue=('Total_Price', 'sum')
).sort_values(by='Total_Revenue', ascending=False).reset_index()

top_5_products = product_revenue.head(5)

print("Top 5 Best-Selling Products by Revenue:")
print(top_5_products)

# ------------------------------------------------------
# 🧑‍💼 Top 5 High-Spending Customers
# ------------------------------------------------------
customer_revenue = df_merged.groupby('Customer_ID').agg(
    Customer_Name=('Customer_Name', 'first'),
    Total_Spent=('Total_Price', 'sum')
).sort_values(by='Total_Spent', ascending=False).reset_index()

top_5_customers = customer_revenue.head(5)

print("\nTop 5 Customers by Total Spend:")
print(top_5_customers)

# ------------------------------------------------------
# 🗂️ Optional: Add Rank Column
# ------------------------------------------------------
top_5_customers['Rank'] = top_5_customers['Total_Spent'].rank(method='dense', ascending=False)
print("\nRanked Top Customers:")
print(top_5_customers)
```

---

### 🧪 Case Study 9: **Reshaping Data with Pivot and Melt**

---

#### 1. **Case Study Title**

**Restructuring Sales Data for Comparative Analysis Using Pivot and Melt**

---

#### 2. **Case Study Description**

Sometimes, you need to transform your dataset layout:

- Pivot tables are great for generating summary matrices (e.g., region-wise monthly sales).

- Melting helps reverse the process, converting wide-form data back to long-form for further analysis or plotting.

This case study demonstrates how to reshape data for better **reporting**, **visualization**, or **model input preparation**.

---

#### 3. **Problem Solving Approach**

- Use `pivot_table()` to summarize monthly revenue per region.

- Use `.melt()` to unpivot the table back to long-form.

- Handle missing values and column formatting as needed.

- Verify output at each stage.

---

#### 4. **Python Code (Fully Documented & Pandas-Only)**

```python
import pandas as pd

# 📥 Step 1: Load and merge datasets
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")
df_regions = pd.read_excel("region_info.xlsx")

# 🔁 Step 2: Convert Order_Date to datetime and extract Month-Year
df_sales['Order_Date'] = pd.to_datetime(df_sales['Order_Date'])
df_sales['Month_Year'] = df_sales['Order_Date'].dt.to_period('M').astype(str)

# 🧮 Step 3: Pivot Table – Monthly Sales by Region
pivot_table = df_sales.pivot_table(
    index='Region',
    columns='Month_Year',
    values='Total_Price',
    aggfunc='sum',
    fill_value=0
)

# 🖥️ Step 4: View pivot table
print("Pivot Table: Total Sales by Region and Month")
print(pivot_table)

# 🔄 Step 5: Melt the Pivot Table to Long Format
melted_table = pivot_table.reset_index().melt(
    id_vars='Region',
    var_name='Month_Year',
    value_name='Total_Sales'
)

# 🧾 Step 6: View reshaped long-format table
print("\nMelted Table: Long-form Region-Month Sales")
print(melted_table.head())
```

---

### 🧪 Case Study 10: **Exporting Cleaned and Transformed Data**

---

#### 1. **Case Study Title**

**Saving Final Sales Dataset for Analysis and Reporting**

---

#### 2. **Case Study Description**

Once your data is cleaned, enriched, and transformed, you’ll want to **save it** for:

- Reporting

- Sharing with team members

- Use in dashboards or downstream ML tasks

This case study focuses on exporting the **final DataFrame** in common formats like Excel and CSV using **Pandas’ I/O functions**.

---

#### 3. **Problem Solving Approach**

- Use `.to_csv()` for lightweight, portable storage.

- Use `.to_excel()` for Excel-compatible formatting (e.g., charts, pivots).

- Validate that the file has been saved with the desired columns.

- Use `index=False` to keep the file clean.

---

#### 4. **Python Code (Fully Documented & Pandas-Only)**

```python
import pandas as pd

# 📥 Step 1: Reload and merge all relevant datasets
df_sales = pd.read_excel("sales_case_study_dataset.xlsx")
df_customers = pd.read_excel("customer_info.xlsx")
df_products = pd.read_excel("product_info.xlsx")
df_regions = pd.read_excel("region_info.xlsx")

df_merged = pd.merge(df_sales, df_customers, on='Customer_ID', how='left')
df_merged = pd.merge(df_merged, df_products, on='Product_ID', how='left')
df_merged = pd.merge(df_merged, df_regions, on='Region', how='left')

# ✅ Step 2: Perform transformations
df_merged['Order_Date'] = pd.to_datetime(df_merged['Order_Date'])
df_merged['Month_Year'] = df_merged['Order_Date'].dt.to_period('M').astype(str)
df_merged['Customer_Rating'] = df_merged['Customer_Rating'].fillna(df_merged['Customer_Rating'].mean())
df_merged['Discounted_Price'] = df_merged['Total_Price'].where(
    df_merged['Total_Price'] <= 3000, df_merged['Total_Price'] * 0.9
)
df_merged['Engagement_Score'] = df_merged['Quantity'] * df_merged['Customer_Rating']

# 💾 Step 3: Save to Excel and CSV formats
output_excel = "/mnt/data/final_sales_dataset.xlsx"
output_csv = "/mnt/data/final_sales_dataset.csv"

df_merged.to_excel(output_excel, index=False)
df_merged.to_csv(output_csv, index=False)

# 🧾 Step 4: Confirm file creation
print("Data exported successfully!")
print("Excel file:", output_excel)
print("CSV file:", output_csv)
```

---


