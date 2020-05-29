# SQL Problem

This question will test some basic knowledge of SQL. The first four questions should
not take more than an hour to complete.

## Description of Tables

There are three tables involved in this question: `transactions`, `segments` and
`products`, which simulate a simplified retail data schema.  Here is a semantic
description of the tables:

1. `transactions`: contains detailed information about each product a customer
   has purchased.  A transaction consists of one or more products purchased by
   a customer indexed by a unique transaction id.
   * `trans_id`: the transaction id
   * `cust_id`: the customer id
   * `prod_id`: the product id
   * `item_qty`: the quantity of the product that is being purchased
   * `item_price`: the per unit price of the product (NOTE: the total revenue
     for a product is `item_qty * item_price`)
2. `products`: contains detailed attributes about each product.
   * `prod_id`: the product id (same meaning as in `transactions`)
   * `prod_name`: the product name
   * `brand`: the brand of the product
   * `category`: the category of the product
3. `segments`: contains a history of customer segmentation labelling for each
   customer.  Segments are computed periodically for all current customers and
   appended to the table after each computation.  The current (most up to date)
   active segment for each customer is specified by `active_flag = 'Y'` column.
   * `cust_id`: the customer id (same meaning as in `transactions`)
   * `seg_name`: the segment of this customer
   * `update_at`: the date when this segment was updated
   * `active_flag`: whether or not this segment is the active segment for this customer

## Sample Database

Included is a sample SQLite3 database for the above tables named `sample.db`.
Please refer to https://www.sqlite.org/download.html to download command-line
tools so you can run your queries against the sample data.

## Problems

Please provide the SQL for each one of these questions.  If there is not enough
information given, please make a reasonable assumption and we can discuss it in
the in-person interview. Please document any assumptions you’ve made in the comments
of each solution and include any additional queries you ran to validate that they
are reasonable.

1. Find the current active segment for each customer sorted by the segment
   update date.  The output should contain three columns: `cust_id`,
   `seg_name`, `updated_at`.  Here is some sample output:

        cust_id     seg_name        updated_at
        4402        LAPSED          2014-06-01 00:00:00
        11248       ONE-OFFS        2015-10-01 00:00:00

A: SELECT cust_id, seg_name, updated_dt FROM segments WHERE active_flag='Y' ORDER BY updated_dt


2. For each product purchased between Jan 2016 and May 2016 (inclusive), find
   the number of distinct transactions.  The output should contain `prod_id`,
   `prod_name` and distinct transaction columns.  Here is some sample output:

        prod_id     prod_name       count
        199922      Product 199922  1
        207344      Product 207344  1
        209732      Product 209732  1

A: select transactions.prod_id, products.prod_name, (Count(transactions.prod_id) as count) where trans_dt >= '01/01/2016' and trans_dt <= '05/31/2016' from transactions ON transactions.prod_id=products.prod_id;


3. Find the most recent segment of each customer as of 2016-03-01.
   *Hint*: You cannot simply use `active_flag` since that is as of the current
   date *not* 2016-03-01.  The output should contain the `cust_id`, `seg_name`
   and `update_at`  columns and should have at most one row per customer.  Here
   is some sample output:

       cust_id  seg_name    update_at
       4402     ONE-OFFS    2016-02-01 00:00:00
       11248    LOYAL       2016-02-01 00:00:00
       126169   ONE-OFFS    2015-03-01 00:00:00

A: select cust_id, seg_name, update_at from segments where update_at < '2016-03-01' ORDER BY DESC update_at LIMIT 1

4. Find the most popular category (by revenue) for each active segment.
   *Hint*: The current (most up to date) active segment is specified by `active_flag = 'Y'` column in the segments table.
   Here is the some sample output:

  	seg_name    category    revenue
	INFREQUENT  Women       20264


5. Use the current sample database to find insights. Please document your steps, include any code/documents you used (Excel, SQL, Python, etc), and have the final results in a Powerpoint format (limit 3 slides)
   *Hint*: This is open ended, but you could look at sales trend, category insights, customers insights
