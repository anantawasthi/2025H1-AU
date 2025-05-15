









### 🧪 Case Study 1

**Loading and Exploring Raw Sales Data**

---

#### 1. **Case Study Title**

Loading and Exploring Raw Sales Data using PySpark

---

#### 2. **Case Study Description**

You are given a large sales dataset stored as an Excel/CSV file. Your task is to load this dataset into a **Spark DataFrame**, explore its structure, check data types, and understand basic metrics such as row count, schema, and null value distributions.

---

#### 3. **Problem Solving Approach**

- Use `spark.read` to load the data into a DataFrame.

- Display sample rows using `.show()`.

- Examine schema using `.printSchema()`.

- Count rows and nulls using `.count()` and aggregation functions.

- Use `.describe()` for basic summary statistics.

---

#### 4. **PySpark Code**

```python
# ⚙️ Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan, when, count

# 🔁 Step 1: Initialize Spark session (skip this if already in Databricks)
spark = SparkSession.builder \
    .appName("Sales Data Exploration") \
    .getOrCreate()

# 📥 Step 2: Load CSV data (assumed exported from Excel)
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")

# 👁️ Step 3: Show top rows
df_sales.show(5)

# 🔎 Step 4: Check schema (column names and types)
df_sales.printSchema()

# 📊 Step 5: Total number of records
print(f"Total Rows: {df_sales.count()}")

# 📈 Step 6: Describe numerical columns
df_sales.describe().show()

# 🧼 Step 7: Count missing values in each column
df_sales.select([
    count(when(col(c).isNull() | isnan(c), c)).alias(c)
    for c in df_sales.columns
]).show()
```

---

### 🧪 Case Study 2

**Filtering with One and Multiple Criteria**

---

#### 1. **Case Study Title**

Filtering Sales Records Using Single and Combined Conditions in PySpark

---

#### 2. **Case Study Description**

In this case, you need to:

- First, extract all records related to the **Electronics** product category.

- Then, further narrow down to only those sold in the **North** or **East** regions.

This showcases how filtering is done in PySpark using logical operations (`==`, `&`, `isin()`), similar to Pandas but using Spark syntax.

---

#### 3. **Problem Solving Approach**

- Use `.filter()` or `.where()` for condition-based selection.

- Apply single and multiple conditions using logical operators (`&`, `|`).

- Use `.isin()` for multiple match values.

- Use `.select()` and `.show()` to view the results.

---

#### 4. **PySpark Code (With Comments)**

```python
# ⚙️ Import required functions
from pyspark.sql.functions import col

# 🔁 Step 1: Load dataset if not already loaded
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")

# --------------------------------------------------------
# 🎯 PART A: Filter by One Condition (Electronics category)
# --------------------------------------------------------

# Filter using .filter() and .col() expression
df_electronics = df_sales.filter(col("Product_Category") == "Electronics")

# Show top results
df_electronics.show(5)

# Count records
print(f"Electronics Records: {df_electronics.count()}")

# --------------------------------------------------------
# 🎯 PART B: Filter by Multiple Conditions (Category + Region)
# --------------------------------------------------------

# Region filter using .isin()
df_filtered = df_sales.filter(
    (col("Product_Category") == "Electronics") &
    (col("Region").isin("North", "East"))
)

# Show results
df_filtered.select("Order_ID", "Region", "Product_Category", "Total_Price").show(5)

# Record count
print(f"Electronics in North or East: {df_filtered.count()}")
```

---

### 🧪 Case Study 3

**Handling Missing Values**

---

#### 1. **Case Study Title**

Detecting and Handling Missing Customer Ratings in PySpark

---

#### 2. **Case Study Description**

In your sales dataset, the `Customer_Rating` column has missing values. You must:

- Identify how many values are missing.

- Decide between dropping those rows or imputing missing values (e.g., using the mean).

- Apply appropriate actions to ensure clean and analyzable data.

This case study demonstrates **null detection and imputation** in PySpark using `when()`, `isNull()`, and aggregation.

---

#### 3. **Problem Solving Approach**

- Use `.select()` and `when().isNull()` to count missing values.

- Use `.dropna()` to remove rows.

- Use `.fillna()` or a calculated mean value to fill missing ratings.

- Validate results with `.show()` and `.count()`.

---

#### 4. **PySpark Code (With Comments)**

```python
from pyspark.sql.functions import col, when, count, avg

# 🔁 Step 1: Load dataset
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")

# 🧮 Step 2: Count missing values in 'Customer_Rating'
df_sales.select([
    count(when(col("Customer_Rating").isNull(), "Customer_Rating")).alias("Missing_Ratings")
]).show()

# ---------------------------------------------------
# Strategy 1: Fill Missing Ratings with Column Mean
# ---------------------------------------------------
# 💡 Step 3a: Calculate mean rating
mean_rating = df_sales.select(avg("Customer_Rating")).first()[0]

# 🧼 Step 4a: Fill missing with mean
df_filled = df_sales.fillna({"Customer_Rating": mean_rating})

# ✅ Check if missing values remain
df_filled.select([
    count(when(col("Customer_Rating").isNull(), "Customer_Rating")).alias("Missing_Ratings_After_Fill")
]).show()

# ---------------------------------------------------
# Strategy 2: Drop Rows with Missing Ratings
# ---------------------------------------------------
df_dropped = df_sales.dropna(subset=["Customer_Rating"])

print(f"Original row count: {df_sales.count()}")
print(f"After dropping missing ratings: {df_dropped.count()}")
```

---

### 🧪 Case Study 4

**Type Conversion and Date Part Extraction**

---

#### 1. **Case Study Title**

Converting `Order_Date` to Datetime and Extracting Year, Month, and Week in PySpark

---

#### 2. **Case Study Description**

The `Order_Date` field in your dataset is read as a string. To enable time-based analysis, you need to:

- Convert it into a proper `DateType`.

- Extract components like **year**, **month**, **week**, and **day of the week** for further analysis and visualization.

This case study focuses on **type casting** and **feature extraction** from date fields using PySpark’s `to_date()` and `date_format()` functions.

---

#### 3. **Problem Solving Approach**

- Use `to_date()` to convert string columns to date format.

- Use functions like `year()`, `month()`, `weekofyear()`, and `date_format()` to derive new date-related columns.

- Use `.select()` and `.withColumn()` to create and inspect the output.

---

#### 4. **PySpark Code (With Comments)**

```python
from pyspark.sql.functions import to_date, year, month, weekofyear, date_format

# 📥 Step 1: Load sales data
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")

# 🗓️ Step 2: Convert 'Order_Date' to proper DateType
df_sales = df_sales.withColumn("Order_Date", to_date(col("Order_Date"), "yyyy-MM-dd"))

# ✅ Step 3: Extract Year, Month, Week, Day of Week
df_sales = df_sales.withColumn("Order_Year", year(col("Order_Date")))
df_sales = df_sales.withColumn("Order_Month", month(col("Order_Date")))
df_sales = df_sales.withColumn("Order_Week", weekofyear(col("Order_Date")))
df_sales = df_sales.withColumn("Day_of_Week", date_format(col("Order_Date"), "EEEE"))

# 👀 Step 4: View transformed date columns
df_sales.select("Order_Date", "Order_Year", "Order_Month", "Order_Week", "Day_of_Week").show(5)
```

---

### 🧪 Case Study 5

**Creating Derived Columns Without NumPy**

---

#### 1. **Case Study Title**

Calculating Discounted Price and Engagement Score Using PySpark Expressions

---

#### 2. **Case Study Description**

You want to enrich your sales dataset by adding two derived features:

- `Discounted_Price`: Apply a 10% discount on total prices over ₹3000.

- `Engagement_Score`: Multiply `Quantity` with `Customer_Rating`.

The goal is to use **PySpark expressions only**—no external libraries like NumPy—making it ideal for Databricks and large-scale processing.

---

#### 3. **Problem Solving Approach**

- Use `when()` from `pyspark.sql.functions` for conditional logic.

- Use `withColumn()` to create new columns.

- Fill missing ratings before using them in calculations.

- Use arithmetic operations directly within expressions.

---

#### 4. **PySpark Code (Pandas-Free, Fully Documented)**

```python
from pyspark.sql.functions import when, col, avg

# 📥 Step 1: Load dataset
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")

# 🧼 Step 2: Fill missing Customer_Rating values with mean
mean_rating = df_sales.select(avg("Customer_Rating")).first()[0]
df_sales = df_sales.fillna({"Customer_Rating": mean_rating})

# 💰 Step 3: Create 'Discounted_Price' column
# Apply 10% discount if Total_Price > 3000
df_sales = df_sales.withColumn(
    "Discounted_Price",
    when(col("Total_Price") > 3000, col("Total_Price") * 0.90).otherwise(col("Total_Price"))
)

# 📈 Step 4: Create 'Engagement_Score' column
df_sales = df_sales.withColumn(
    "Engagement_Score",
    col("Quantity") * col("Customer_Rating")
)

# 👀 Step 5: Show newly created features
df_sales.select("Order_ID", "Total_Price", "Discounted_Price", "Quantity", "Customer_Rating", "Engagement_Score").show(5)
```

---

### 🧪 Case Study 6 (PySpark Version)

**Joining and Merging Multiple DataFrames**

---

#### 1. **Case Study Title**

Joining Sales, Customer, Product, and Region DataFrames in PySpark

---

#### 2. **Case Study Description**

To create a unified sales view for enriched analysis, you need to merge:

- **Customer data** using `Customer_ID`

- **Product data** using `Product_ID`

- **Region data** using `Region`

This case highlights how to perform **relational joins** using PySpark's `join()` method, mimicking SQL-like operations on distributed data.

---

#### 3. **Problem Solving Approach**

- Load all four datasets as individual Spark DataFrames.

- Use `.join()` with the appropriate keys and join types.

- Chain the joins to build a master dataset.

- Inspect the final schema and preview the result.

---

#### 4. **PySpark Code (Fully Documented)**

```python
# 📥 Step 1: Load all datasets
df_sales = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/sales_case_study_dataset.csv")
df_customers = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/customer_info.csv")
df_products = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/product_info.csv")
df_regions = spark.read.option("header", True).option("inferSchema", True).csv("/path/to/region_info.csv")

# 🔁 Step 2: Join Sales with Customer Data on Customer_ID
df_joined = df_sales.join(df_customers, on="Customer_ID", how="left")

# 🔁 Step 3: Join with Product Data on Product_ID
df_joined = df_joined.join(df_products, on="Product_ID", how="left")

# 🔁 Step 4: Join with Region Data on Region
df_joined = df_joined.join(df_regions, on="Region", how="left")

# ✅ Step 5: Inspect the result
df_joined.select("Order_ID", "Customer_Name", "Product_Name", "Region", "Regional_Manager").show(5)

# 🔍 Step 6: Print schema for validation
df_joined.printSchema()
```

---

### 🧪 Case Study 7

**Grouping, Aggregation, and Summary Reports**

---

#### 1. **Case Study Title**

Generating Region and Product-Level Summaries Using PySpark GroupBy and Aggregation

---

#### 2. **Case Study Description**

After joining all datasets, you are now ready to answer business questions like:

- What is the **total and average revenue** per region?

- What is the **average customer rating and quantity sold** per product category?

- How does each **payment method** perform?

This case demonstrates **grouped summaries** using `.groupBy().agg()` in PySpark, ideal for dashboards and KPI reporting.

---

#### 3. **Problem Solving Approach**

- Use `.groupBy()` on Region, Product_Category, or Payment_Method.

- Apply aggregation functions: `sum()`, `avg()`, `count()`.

- Use `.alias()` to rename aggregated columns.

- Preview each result using `.show()`.

---

#### 4. **PySpark Code (Fully Documented)**

```python
from pyspark.sql.functions import sum, avg, count

# 📥 Step 1: Load or reuse the merged DataFrame from Case Study 6
# Assuming df_joined is already available

# --------------------------------------------
# 📊 Region-Level Sales Summary
# --------------------------------------------
region_summary = df_joined.groupBy("Region").agg(
    sum("Total_Price").alias("Total_Sales"),
    avg("Total_Price").alias("Average_Sales"),
    count("Order_ID").alias("Order_Count")
)

print("📍 Regional Sales Summary:")
region_summary.show()

# --------------------------------------------
# 📦 Product Category Summary
# --------------------------------------------
category_summary = df_joined.groupBy("Product_Category").agg(
    avg("Customer_Rating").alias("Avg_Rating"),
    sum("Quantity").alias("Total_Quantity_Sold")
)

print("🛒 Product Category Summary:")
category_summary.show()

# --------------------------------------------
# 💳 Payment Method Summary
# --------------------------------------------
payment_summary = df_joined.groupBy("Payment_Method").agg(
    count("Order_ID").alias("Transaction_Count"),
    avg("Total_Price").alias("Avg_Transaction_Value")
)

print("💰 Payment Method Summary:")
payment_summary.show()
```

---

### 🧪 Case Study 8

**Sorting, Ranking, and Top-N Identification**

---

#### 1. **Case Study Title**

Identifying Top-Selling Products and High-Spending Customers in PySpark

---

#### 2. **Case Study Description**

Business stakeholders want to know:

- Which products generate the **most revenue**?

- Who are the **highest-spending customers**?

- How do we **rank** them accordingly?

This case study demonstrates how to use `.groupBy()`, `.agg()`, `.orderBy()`, and `.rank()` for **leaderboards and ranking**.

---

#### 3. **Problem Solving Approach**

- Group sales data by `Product_ID` and `Customer_ID`.

- Aggregate total revenue and sort in descending order.

- Use `.rank()` from `pyspark.sql.window` to assign ranks.

- Extract top 5 rows using `.limit()`.

---

#### 4. **PySpark Code (Fully Documented)**

```python
from pyspark.sql.functions import sum, rank
from pyspark.sql.window import Window

# 📥 Step 1: Reuse the merged DataFrame
# Assuming df_joined is already available from previous case studies

# --------------------------------------------
# 🏆 Top 5 Products by Total Revenue
# --------------------------------------------
product_revenue = df_joined.groupBy("Product_ID", "Product_Name").agg(
    sum("Total_Price").alias("Total_Revenue")
).orderBy(col("Total_Revenue").desc())

print("📦 Top 5 Products by Revenue:")
product_revenue.show(5)

# --------------------------------------------
# 🧑‍💼 Top 5 High-Spending Customers
# --------------------------------------------
customer_revenue = df_joined.groupBy("Customer_ID", "Customer_Name").agg(
    sum("Total_Price").alias("Total_Spent")
)

# Define a window for ranking
rank_window = Window.orderBy(col("Total_Spent").desc())

# Apply rank
ranked_customers = customer_revenue.withColumn("Rank", rank().over(rank_window))

print("💳 Top 5 Customers by Spending:")
ranked_customers.orderBy("Rank").show(5)
```

---

### 🧪 Case Study 9

**Reshaping Data Using Pivot and Melt**

---

#### 1. **Case Study Title**

Monthly Region-Wise Sales Summary Using Pivot and Melt in PySpark

---

#### 2. **Case Study Description**

To build performance dashboards and comparative reports, you need to:

- **Pivot** the dataset to show total sales by `Region` and `Month`.

- **Melt** (or unpivot) the result back into long format.

While PySpark supports **pivoting** natively, **melting** (unpivoting) is done using `selectExpr()` or manual reshaping logic.

---

#### 3. **Problem Solving Approach**

- Convert `Order_Date` to a `Month-Year` format.

- Use `.groupBy().pivot().agg()` to summarize total sales.

- For unpivoting, use `stack()` inside `selectExpr()` or restructure manually.

---

#### 4. **PySpark Code (Pivot & Melt Logic)**

```python
from pyspark.sql.functions import to_date, date_format, sum

# 📥 Step 1: Load or reuse df_joined
# Convert Order_Date to DateType if needed
df_joined = df_joined.withColumn("Order_Date", to_date(col("Order_Date"), "yyyy-MM-dd"))

# 🗓️ Step 2: Extract Month-Year format
df_joined = df_joined.withColumn("Month_Year", date_format(col("Order_Date"), "yyyy-MM"))

# 📊 Step 3: Pivot table – total sales by Region and Month_Year
pivot_df = df_joined.groupBy("Region").pivot("Month_Year").agg(
    sum("Total_Price").alias("Total_Sales")
)

print("📈 Pivot Table (Region x Month):")
pivot_df.show()

# 🔄 Step 4: Melt (Unpivot) the pivoted table using stack()
# Step requires knowing column names to unpivot
month_cols = pivot_df.columns[1:]  # Exclude 'Region'

# Prepare the stack expression
expr = "stack({0}, {1}) as (Month_Year, Total_Sales)".format(
    len(month_cols),
    ", ".join([f"'{m}', `{m}`" for m in month_cols])
)

melted_df = pivot_df.selectExpr("Region", expr)

print("🔁 Melted (Long-Form) Table:")
melted_df.show()
```

---


