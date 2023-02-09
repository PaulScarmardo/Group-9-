# Group9
SE Lab Project
## Team Members
Paul Scarmardo - PaulScarmardo (Lead)

Yuexin Xu - yx155

Jessica Oramous - jessoramous

Ayden Kilpatrick - Ayden-Kilpatrick

## Objective - create a succefully working e-commerce site with specific requirements
## Description:
Our e-commerce site, Anazom, allows different users (buyers, sellers, admins) to login and perform their desired actions before logging out. Buyers can search and purchase products from sellers, and admins can oversee the actions of these buyers and sellers. More details regarding the functionalities of the software are listed below.

## Features:
### Stores Online Transactions 

	3.1.1	Description and Priority  

	Whenever a buyer purchases an item from a seller, the information regarding that transaction is recorded and stored in the system database. This information is then kept available for reference purposes to both the buyer and the seller. This feature is of low priority. 

	3.1.2	Stimulus/Response Sequences  

	Buyer confirms the purchase of an item -> the system gathers the information for that purchase -> the system stores that information as an entry in the database -> the buyer chooses to view their order history -> the system searches through the database to find entries that matches to the buyer’s name -> the system displays those entries -> the seller chooses to view their transaction history -> the system searches through the database to find entries that matches to the seller’s name -> the system displays those entries 

	3.1.3	Functional Requirements 

	REQ-1: Add a transaction to buyer’s order history 

	REQ-2: Add a transaction to seller’s transaction history 

	REQ-3: Displays all of the buyer’s order history upon request 

	REQ-4: Displays all of the seller’s transaction history upon request 

	REQ-5: Provide a notice message if the buyer or seller’s transaction history is empty when display is requested 

### Seller Management 

	3.2.1	Description and Priority 

	Sellers will have the ability to add an item to the site and customize a variety of categories of the item such as: price, name, and description. Once added, the item will be available to buyers for purchase. This feature is medium priority. 

	3.2.2	Stimulus Response/Sequences 

	Seller chooses to add item -> Asked for name, price, description of product -> product gets added to the store with those categories filled -> Seller receives payment when the product is bought 

	3.2.3 Functional Requirements 

	REQ-1: Add item to site 

	REQ-2: Change product categories 

	REQ-3: Be able to accept payment 

### Login/Logout 

	3.3.1 Description and Priority 

	Users will have the ability to login and logout of their accounts using a username and password. This feature is of high priority. 

	3.3.2 Stimulus Response/Sequences 

	User navigates to the website -> User enters a valid username and password to login to their account -> User will be able to logout after logging in 

	3.3.3 Functional Requirements 

	REQ-1: Program will search through database to for user account and password match 

	REQ-2: On login, user will be granted permissions based on their account type 

	REQ-3: User will be able to logout of their account successfully 

### Admin Permissions
	3.4.1 Description and Priority 

	Admins can oversee the actions of different users and perform the operations necessary to maintain a positive shopping environment. Admins can also manage what categories of items Anazom sells. This feature is of medium priority. 

	3.4.2 Stimulus Response/Sequences 

	Buyer buys an item -> the purchase is recorded in transaction history -> admin views recent transaction histories -> admin notes any suspicious activities and suspend accounts accordingly -> admin decides on whether a new product category should be created 

	A new user account/product is registered -> admin views the request -> admin approve/block the request  

	3.4.3 Functional Requirements 

	REQ-1: add a new product category 

	REQ-2: remove an existing product category 

	REQ-3: view recent transactions 

	REQ-4: suspend a user 

	REQ-5: approve/block new user account 

	REQ-6: approve/block new product item 

### Buyer Management
	3.5.1 Description and Priority 

	Buyers are able to search for their desired product and purchase it from the product’s seller. Buyers also have the option to return the product for a full refund. This feature is of high priority. 

	3.5.2 Stimulus Response/Sequences 

	Buyer wishes to browse through all items within a product category -> system displays all items available under the specified category -> buyer decides to search for a specific product -> system provides the buyer with all the options available for that product -> buyer adds an item to cart -> buyer checks out their cart -> system performs the transaction process described in section 3.2 -> the buyer wishes to return the item -> the system notifies the seller of the request 

	3.5.3 Functional Requirements 

	REQ-1: browse products within a category 

	REQ-2: search for a specific product 

	REQ-3: add a product to cart 

	REQ-4: checkout 

	REQ-6: return a product 

## Languages
* Python
* MySQL
* Django
