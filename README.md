Read this in: [English](README.md) | [Deutsch](README_DE.md)
# ecommerce-database-design
A standard backend database design simulating an online marketplace selling electronics from a variety of retailers.

The current build functions as intended, however I do intend to add more integral business related queries to the queries.md file and the Data_Theory.md file to showcase and improve my capabilities with SQLite.
While the user tables are populated with 1000 unique records, the downstream relational layers (like products and orders) are structured on a smaller scale, making massive multi-table data joins tricky to balance.
Namely, for my products table, I am using a select few placeholder values rather than the 1000 uniquely generated items of test data I have in mock_users.sql from roughly line 2000-3000,
I am currently working on a solution.
