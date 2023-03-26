### What is PostgreSQL?

-

###### - Postgres is an open-source relational database. It has features like handling complex data types, allowing costum solutions via programming languages, several use techniques to manage concurrent data (accessing specific data at the same time), and more.

-

### What is the difference between SQL and PostgreSQL?

-

###### - SQL is a powerful tool for querying and manipulating large amounts of data in relational databases. It's designed to simplify the process of working with data by providing a standardized language and syntax that can be used across different database systems. SQL's ability to handle data collections, queries, and data manipulation makes it an essential tool for managing relational databases. Overall, SQL's tooling works well in tandem with relational databases to provide a comprehensive solution for managing data.

###### - Postgres is not a coding language like SQL is. Postgres is a relational database, although Postgres does provide additional tooling to compliment SQL. Its primary focus is allowing easy access and flexibility in storing large quantities of complex data, as well as providing efficient access to that data.

-

### In `psql`, how do you connect to a database?

-

##### - Here's a few ways:

    - when in psql env - \c name_of_database
    - from terminal - psql -d name_of_database
    - from terminal - psql name_of_database

-

### What is the difference between `HAVING` and `WHERE`?

-

###### - "WHERE" is a clause used in SQL to filter data at the row level, and it can be used with the "SELECT," "UPDATE," and "DELETE" statements. The filter conditions are applied before any data manipulation via "GROUP BY" or other operations.

###### - The "HAVING" clause is used in SQL to filter data at the group level, and it can only be used with the "SELECT" statement in conjunction with the "GROUP BY" clause. The filter conditions are applied after the grouping has been done and data has been aggregated. It allows you to filter on the results of group functions like COUNT, SUM, AVG, etc.

###### - Main Difference: The "WHERE" clause is used to filter data at the row level based on specific conditions, while the "HAVING" clause is used to filter data at the group level after the data has been aggregated by a "GROUP BY" clause. In other words, "WHERE" is used to filter individual rows before aggregation, while "HAVING" is used to filter groups after aggregation.

-

### What is the difference between an `INNER` and `OUTER` join?

-

###### - An "INNER" join only returns rows that have matching values in both tables being joined. In other words, it only returns rows where the join condition is true. If there is no matching row in one of the tables, then that row is not included in the result set.

###### - On the other hand, an "OUTER" join returns all the rows from one table and matching rows from the other table. If there is no match in the other table, the result will still contain a row for that table with NULL values for the columns that belong to the other table.

-

### What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

-

###### - A "LEFT OUTER JOIN" returns all the rows from the left table and matching rows from the right table. If there is no match in the right table, the result will still contain a row for the left table with NULL values for the columns that belong to the right table.

###### - A "RIGHT OUTER JOIN" is the opposite of a "LEFT OUTER JOIN". It returns all the rows from the right table and matching rows from the left table. If there is no match in the left table, the result will still contain a row for the right table with NULL values for the columns that belong to the left table.

-

### What is an ORM? What do they do?

-

###### - An ORM (Object-Relational Mapping) is a programming technique used to convert data between incompatible type systems, i.e., between object-oriented programming languages and relational databases.

###### ORMs map the database schema to an object-oriented model, which makes it easier for developers to work with databases using programming languages like Python, Java, or C#. They provide a higher-level abstraction of database interactions, which reduces the amount of boilerplate code that needs to be written when interacting with the database.

###### In essence, an ORM provides a way to represent database tables as classes and the relationships between tables as object references, enabling developers to interact with the database using object-oriented programming paradigms instead of writing raw SQL queries. This makes it easier to work with databases and reduces the likelihood of SQL injection vulnerabilities.

-

### What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?

-

###### - AJAX and server-side HTTP requests both fetch data from a server, but they do it differently. AJAX requests are made from the client side, without refreshing the page, and can update only specific parts of the page, making it feel more interactive. On the other hand, server-side requests are made by the server, and the response can be used to generate a new page or send data to the client. Both approaches have their pros and cons, but they can be used together to create more dynamic and responsive web applications.

-

### What is CSRF? What is the purpose of the CSRF token?

-

###### - CSRF is a security issue where someone tricks you into doing something on a website that you didn't intend to do. To prevent this, websites use something called a CSRF token which is like a secret code that only you and the website know. When you make a request to the website, you have to include the token to prove that you're not being tricked. It's like a secret handshake between you and the website to make sure nobody else can mess with your account.

-

### What is the purpose of `form.hidden_tag()`?

-

###### form.hidden_tag() is a method in Flask that generates a hidden input field in an HTML form. This field contains a random value that's unique to the user's session, and it's used to prevent CSRF attacks. CSRF, short for Cross-Site Request Forgery, is a sneaky technique where a bad actor tricks a user into submitting a form on a website without them knowing. But by including a unique token in the form, Flask can verify that the request is coming from the real user and not from some shady third party.

-
