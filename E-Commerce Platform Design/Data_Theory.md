**Theory behind the queries**



1. Calculating the Total Value of an Active User's Shopping Cart



Finding how much money a user (u) owes for the items currently sitting in their basket. You join the cart to the product catalog and multiply out the totals.


```sql
γSUM(Quantity X ProductPrice) AS CartTotal(σUserID=u(Cart_items ⨝ Products))
```


2. The Restock Trigger Rule



To identify which products have fallen below the emergency threshold (t) and require and automated restock order from distributors.


```sql
σStockLevel<t(γProductID,SUM(QuantityChange) AS StockLevel(InventoryLedger))
```


3. Generating a Complete Packing Slip for a Warehouse Packager



To output exactly what products, quantities, and delivery addresses need to be boxed up for a specific order (o).


```sql
πProductName,Quantity,FirstName,Surname,AddressLine1(σOrderID=o(Orders ⨝ Users ⨝ Order_items ⨝ Products))
```


4. User Balance Equation



Verifying if a user has enough money before they reach checkout. We must calculate the net liquid capital of the user (u) by aggregating their historical deposit and purchase ledger.


```sql
γSUM(Amount) AS NetBalance(σUserID=u(UserTransactions))
```
