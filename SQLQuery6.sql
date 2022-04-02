--/****** Script for SelectTopNRows command from SSMS  ******/
--SELECT TOP (1000) [Order ID]
--      ,[Customer ID]
--      ,[Customer Name]
--      ,[Customer Email]
--      ,[Customer Phone]
--      ,[Order Date]
--      ,[Order Status]
--      ,[Subtotal (inc tax)]
--      ,[Subtotal (ex tax)]
--      ,[Tax Total]
--      ,[Shipping Cost (inc tax)]
--      ,[Shipping Cost (ex tax)]
--      ,[Ship Method]
--      ,[Order Total (inc tax)]
--      ,[Order Total (ex tax)]
--      ,[Payment Method]
--      ,[Total Quantity]
--      ,[Total Shipped]
--      ,[Date Shipped]
--      ,[Order Notes]
--      ,[Customer Message]
--      ,[Billing State]
--      ,[Billing Zip]
--      ,[Billing Country]
--      ,[Address]
--      ,[Town/City]
--      ,[State]
--      ,[Zip]
--      ,[Shipping Country]
--      ,[Product Details]
--  FROM [OCF].[dbo].[orders$]


----Customer contact info
--  select [Customer ID],[Customer Name],[Customer Email] ,[Customer Phone],count(*) as Orders
--  from orders$
--  WHERE [Customer Name] is not null 
--group by [Customer ID], [Customer Name],[Customer Email],[Customer Phone];
--  

-------
--select [Customer ID],[Customer Name],[Customer Email] ,[Customer Phone],[Product Details],[Order Date],[Date Shipped],[Shipping Cost (inc tax)],[Subtotal (inc tax)],[Address],[Zip]
--from orders$
--Where [Date Shipped] is not null;



--select [Order Date],[Date Shipped], [Product Details]
--from orders$
--Where [Date Shipped] is not null;


--select [Customer ID],[Order Date],[Date Shipped]
--from orders$
--SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y') today;

--select DATEDIFF(HOUR, [Order Date], [Date Shipped])
--from orders$
