
-- THIS IS A SALES DATA --


CREATE TABLE sales_data(
Order_ID VARCHAR(20) NOT NULL,
Order_Date Date,
Ship_Date Date,
Ship_Mode TEXT,
Customer_ID VARCHAR(20) NOT NULL,
Customer_Segment TEXT,
Country TEXT,
Region TEXT,
State TEXT,
City TEXT,
Category TEXT,
Sub_Category TEXT,
Product_Name TEXT,
Sales FLOAT,
Quantity INT,
Discount FLOAT,
Profit FLOAT,
Payment_Mode TEXT
);

-- IMPORT CSV SALES DATA--

COPY sales_data
FROM  'D:\BlueStock_Internship\Bluestock_Sales_Dashboard.csv'
DELIMITER ','
CSV HEADER ;



------- Total Orders by Customer-------

SELECT
Customer_ID,
COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales_data
GROUP BY Customer_ID
ORDER BY Total_Orders DESC;

------- REVENUE ANALYSIS----------

SELECT SUM(Sales) AS total_revenue,SUM(Profit) AS total_profit,
AVG(Sales) AS average_sales
FROM sales_data;


-------------- Top 10 Products by Revenue


SELECT Product_Name,
SUM(Quantity) AS Total_Quantity,
SUM(Sales) AS Total_Revenue,
SUM(Profit) AS Total_Profit FROM sales_data
GROUP BY Product_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

------------ Category Performance------------


SELECT Category,SUM(Sales) AS Total_Revenue,
SUM(Profit) AS Total_Profit,SUM(Quantity) AS Total_Quantity
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC

-- ----------Monthly Revenue Analysis-------------


SELECT DATE_TRUNC('month', Order_Date) AS Month,
SUM(Sales) AS Monthly_Revenue FROM sales_data
GROUP BY Month
ORDER BY Month;


---------Region-wise Revenue----------------


SELECT Region, SUM(Sales) AS Total_Revenue,
SUM(Profit) AS Total_Profit FROM sales_data
GROUP BY Region
ORDER BY Total_Revenue DESC;


-- ALL QUERY THIS DATA --

-- THIS IS A ALL DATA --

SELECT*FROM sales_data;

-- USING WHERE --
-- Sales greater than 1000

SELECT *FROM sales_data
WHERE Sales > 1000;

-- ORDER BY --
-- Highest sales first

SELECT*FROM sales_data
ORDER BY Sales DESC;




---------- GROUP BY OR HAVING-------------

SELECT Region,COUNT(*)
FROM Sales_Data
GROUP BY Region
HAVING COUNT(*)>10;


SELECT Region ,SUM(sales) AS total_sales
FROM sales_data
GROUP BY Region 
HAVING SUM(Sales)> 1000
ORDER BY Total_Sales DESC;



------------ AGGREGATE FUNCTION---------------

SELECT 
SUM(sales) AS Total_Sales,
AVG(sales) AS Average_Sales,
COUNT(*) AS Total_Records,
MAX(sales) AS Maximum_Sales,
MIN(sales) AS Minimum_Sales
FROM sales_data;

------- INNER JOIN AND LEFT JOIN

CREATE TABLE regions(
Region_ID INT,
Region_Name TEXT
);

CREATE TABLE Customer_Details (
Customer_ID VARCHAR(20) PRIMARY KEY,
Customer_Name TEXT
);

--INNER JOIN------

SELECT s.Order_ID,s.Customer_ID,c.Customer_Name,s.Sales
FROM sales_data s
INNER JOIN customer_details c
ON s.Customer_ID = c.Customer_ID;

-- LEFT JOIN
SELECT s.Order_ID, s.Customer_ID, c.Customer_Name, s.Sales
FROM sales_data s
LEFT JOIN customer_details c
ON s.Customer_ID = c.Customer_ID;

-------------- TOTAL SALES AND PROFIT ------------------

SELECT
	SUM(Sales) AS Total_Sales,
	SUM(Profit) AS Total_Profit
	FROM sales_data;
	

----------- REGION WISE SALES-----------------------

SELECT Region,
	SUM(Sales) AS Total_Sales
	FROM Sales_data
	GROUP BY Region
	ORDER BY Total_Sales DESC;

	
---------------Category-wise Profit--------------------

SELECT 
		Category,
		SUM(Profit) AS Total_Profit
		FROM sales_data
		GROUP BY category
		ORDER BY Total_Profit DESC;

		
---------------Top 10 Products------------------

SELECT
	  Product_Name,
	  SUM(Sales) AS Total_Sales
	  FROM Sales_Data
	  GROUP BY Product_Name
	  ORDER BY Total_Sales DESC
	  LIMIT 10;
	  
