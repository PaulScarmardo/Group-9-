# Group9
SE Lab Project
### Team Members
Paul Scarmardo - PaulScarmardo (Lead)

Yuexin Xu - yx155

Jessica Oramous - jessoramous

Ayden Kilpatrick - Ayden-Kilpatrick

### Objective - create a succefully working e-commerce site with specific requirements

### Requirements
# Stores Online Transactions 

3.1.1	Description and Priority  

Whenever a buyer purchases an item from a seller, the information regarding that transaction is recorded and stored in the system database. This information is then kept available for reference purposes to both the buyer and the seller. This feature is of medium priority. 

3.1.2	Stimulus/Response Sequences  

Buyer confirms the purchase of an item -> the system gathers the information for that purchase -> the system stores that information as an entry in the database -> the buyer chooses to view their order history -> the system searches through the database to find entries that matches to the buyer’s name -> the system displays those entries -> the seller chooses to view their transaction history -> the system searches through the database to find entries that matches to the seller’s name -> the system displays those entries 

3.1.3	Functional Requirements 

REQ-1: Add a transaction to buyer’s order history 

REQ-2: Add a transaction to seller’s transaction history 

REQ-3: Displays all of the buyer’s order history upon request 

REQ-4: Displays all of the seller’s transaction history upon request 

REQ-5: Provide a notice message if the buyer or seller’s transaction history is 				   empty when display is requested 

# Seller Management 

	3.2.1	Description and Priority 

	Sellers will have the ability to add an item to the site and customize a variety of categories 	of the item such as: price, name, and description. Once added, the item will be available to 	buyers for purchase. This feature is medium priority. 

	3.2.2	Stimulus Response/Sequences 

	Seller chooses to add item -> Asked for name, price, description of product -> product gets 	added to the store with those categories filled -> Seller receives payment when the product 	is bought 

	3.2.3 Functional Requirements 

	REQ-1: Add item to site 

	REQ-2: Change product categories 

	REQ-3: Be able to accept payment 

# Login/Logout 

	3.3.1 Description and Priority 

	Users will have the ability to login and logout of their accounts using a username and 		password. 

	3.3.2 Stimulus Response/Sequences 

	User navigates to the website -> User enters a valid username and password to login to their 	account -> User will be able to logout after logging in 

	3.3.3 Functional Requirements 

	REQ-1: Program will search through database to for user account and password match 

	REQ-2: On login, user will be granted permissions based on their account type 

	REQ-3: User will be able to logout of their account successfully 

### Languages
* Python
* MySQL
* Django
