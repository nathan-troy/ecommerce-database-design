#SQL commands, utilising my data theory equations to showcase a variety of unique queries

This document demonstrates how the theoretical core of my relational database equations translate into production-ready SQLite queries that represent the NexusMart marketplace ecosystem. Each scenario represents a critical query that would be used in data analysis or data science on behalf of a business.

---

### 1. Calculating Total Shopping Cart Value
* **Business Case:** Finding exactly how much money a customer owes for the items currently sitting in their active basket so we can display it on their checkout screen. 

```sql
SELECT 
    c.UserID,
    SUM(c.Quantity * p.ProductPrice) AS CartTotal
FROM Cart_items c
JOIN Products p ON c.ProductID = p.ProductID
WHERE c.UserID = ? 
GROUP BY c.UserID;
```

---

### 2. The Restock Trigger Rule
* **Business Case:** Scanning the entire warehouse ledger to automatically identify which items have fallen below an emergency stock threshold ($t$) and need a reorder from our distributors.

```sql
SELECT 
    ProductID,
    SUM(QuantityChange) AS StockLevel
FROM InventoryLedger
GROUP BY ProductID
--Crucial note: I use HAVING instead of WHERE because we are filtering on an aggregated calculation (SUM)
HAVING SUM(QuantityChange) < ?; 
```

---

### 3. Generating a Complete Warehouse Packing Slip
* **Business Case:** Outputting a clean, highly specific manifest for warehouse workers so they know exactly what products to grab, the quantity needed, and where to ship the final box.

```sql
-- Projecting only the exact logistics data the packager needs on the physical shipping label
SELECT 
    p.ProductName,
    oi.Quantity,
    u.FirstName,
    u.Surname,
    u.AddressLine1,
    u.AddressLine2
FROM Orders o
JOIN Users u ON o.UserID = u.UserID
JOIN Order_items oi ON o.OrderID = oi.OrderID
JOIN Products p ON oi.ProductID = p.ProductID
--Target only the specific order currently sitting at the packing station
WHERE o.OrderID = ?; 
```

---

### 4. User Balance Equation

* **Business Case:** Verifying a customer's total liquid spending power before allowing them to check out by auditing their historical ledger records.

```sql
SELECT 
    UserID,
    -- Since deposits are positive and purchases are stored as negative floats, 
    -- a simple SUM() gives us their exact real-time wallet balance.
    SUM(Amount) AS NetBalance
FROM UserTransactions
WHERE UserID = ? 
GROUP BY UserID;
```