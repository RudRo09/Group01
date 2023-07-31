<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p align="center"><strong><img src="https://github.com/RudRo09/Group01/blob/main/Documentation/project_report_images/nsu_logo.png" alt=""/></strong></p>
<p align="center"><strong>North South University</strong></p>
<p align="center">Department of Electrical &amp; Computer Engineering</p>
<p align="center"><strong>Project Report</strong></p>
<p align="center"><strong>Group No</strong>: 01</p>
<p align="center"><strong>Summer 2021</strong></p>
<p align="center"><strong>Project Name</strong>: E-commerce Website on Tech Gadgets</p>
<p align="center"><strong>Course No</strong>: CSE 299 <strong>Sec</strong><strong>:</strong> 06</p>
<p align="center"><strong>Faculty</strong>: Shaikh Shawon Arefin Shimon (Sas3)</p>
<p align="center"><strong><u>Member 1</u></strong><u>:</u></p>
<p align="center"><strong>Name</strong><strong>:</strong> MD Shafin Islam Rudro</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1821054</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:shafin.rudro@northsouth.edu">shafin.rudro@northsouth.edu</a></p>
<p align="center"><strong><u>Member 2</u></strong><strong><u>:</u></strong></p>
<p align="center"><strong>Name</strong><strong>:</strong> Sadia Aktar</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1821516</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:akter.sadia@northsouth.edu">akter.sadia@northsouth.edu</a></p>
<p align="center"><strong><u>Member 3</u></strong><strong><u>:</u></strong></p>
<p align="center"><strong>Name</strong><strong>:</strong> Shadmanul Islam</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1822132</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:shadmanul.islam@northsouth.edu">shadmanul.islam@northsouth.edu</a></p>
<p align="center"><strong>Git Repository</strong><strong>: </strong><a href="https://github.com/NSU-SU21-CSE299-6/Group01.git/">https://github.com/NSU-SU21-CSE299-6/Group01.git/</a></p>
<p align="center"><strong>Date Prepared</strong><strong>: </strong>11/09/2021</p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<div align="justify">
<p><strong>Introduction</strong></p>
<p>Physical stores have a lot of restrictions. Fixed business hours, stock limitation, limited clients, excessive bills are just a few of them. On top of that, in special times like this, when the whole world is quarantined, the physical shop owners are suffering the most. Having a place where store owners can continue their business uninterrupted and more efficiently is now a hot demand.</p>
<p>This project aims to create an E-commerce website on tech and gadgets to give the tech shop owners a secure platform to sell their products, even in the absence of a physical store. This website will provide better deployment of the shop's products, accessibility, global customers, effortless track of buyer's preferences, and 24x7 selling opportunity. So that all the business problems are solved with just a click.</p>
<p><strong>Features</strong></p>
<ul>
  <li>Authentication based login-logout system.</li>
  <li>Token based verification and message alerts.</li>
  <li>Forgot password with secure validation link.</li>
  <li>Category based product browsing and pagination.</li>
  <li>Search option to search for products easily.</li>
  <li>Product gallery with unlimited images.</li>
  <li>Add to cart and after order functionalities with easy-to-understand UI.</li>
  <li>Unique order and order number generation.</li>
  <li>Interactive review and rating system.</li>
  <ul>
    <li>Two factor checks for submitting reviews (Login check & product purchase check)</li>
    <li>Average rating and review count calculation.</li>
  </ul>
  <li>Multiple payment options flexibility.</li>
  <li>Website security measures to prevent hacking attempts.</li>
</ul>

<p><strong>Feature Details</strong></p>
<p>I. USer/Customer:</p>
<ul>
  <li>Customers can browse and search for products without registering to the site or without logging in.</li>
  <li>Customers can browse products by their category.</li>
  <li>Customers can add or remove a product to the cart without logging in.</li>
  <li>In order to purchase a product, the customer must log in to their account.</li>
  <li>After placing an order, the customer must confirm their order after they completing the payment by submitting the payment_id code on the confirm order page.</li>
  <li>If the payment is successful, the order will be placed and the customer will be sent an order confirmation mail.</li>
  <li>Customers can check their order status on their account.</li>
  <li>Customers can update their profile information.</li>
  <li>Customers can also give ratings and review product, only if he/she has bought it.</li>
</ul>

<p>II. Admin:</p>
<ul>
  <li>Admin has to log in using their email and password.</li>
  <li>In the admin panel, admin can see how many people are registered to the site, how many products are in stock, how many orders have been placed and some other useful things.</li>
  <li>Admin can perform 'CRUD' operation on the products, orders, and other users.</li>
  <li>Admin can change the status of the orders.</li>
  <li>Admin can view the ratings and reviews of customers about the products.</li>
</ul>

<p>III. Other Features:</p>
<ul>
  <li>If the user tries to review any product without logging in, he/she will have to log in first.</li>
  <li>If someone attempts to log into admin panel without authorization, the login data will be recorded in the database.</li>
</ul>
<p></p>
<p><strong>System Design</strong></p>
<p>1. Design</p>
<p>The whole system is divided into small modules, like registration system, log in-log out system, browse product by category, search for products, add products to cart, place order and payment system, ratings and review system with SQLite database, representing the development server.</p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/erd.JPG" alt="" width="827" height="916" /></strong></p>
<p align="center"><strong>Figure 1: Entity Relationship Diagram System Database</strong></p>
<p>2. System Information</p>
<p>This system will help the seller to provide the selling service and the buyers to take that service. They are the primary users of this web-app. They can visit the website and find their preferable products. This website will be a place to connect the buyers to the sellers. Another help of this system will be rating and reviewing the products, this feature will meet what a buyer needs to connect with the seller easily. It has the following advantages</p>
<ul>
  <li>User friendly interface</li>
  <li>Fast access to database</li>
  <li>Category-wise product browsing and search functionality.</li>
</ul>
<p></p>
<p><strong>Technology</strong></p>
<p><strong>Hardware Requirements:</strong></p>
<ul>
  <li>Processor: Pentium IV or above</li>
  <li>Ram: 2GB or above</li>
  <li>Hard Drive: 50GB or above</li>
  <li>Device(s): Keyboard, Mouse, Monitor, Smartphone</li>
</ul>
<p></p>
<p><strong>Software Requirements:</strong></p>
<p><em><strong>Front-end:</strong></em></p>
<p>Like any other website, we will be using HTML for the structure and content of our website. Then we will apply CSS and Bootstrap to it, for styling and formatting the website. We will also use some JavaScript for the client-side interface. Our website will have a responsive web design.</p>
<p><em><strong>Backend:</strong></em></p>
<p>For the backend of our website, we are using Python-based web framework Django. In the backend, we will expose a bunch of services that will be accessible via the HTTP protocol. The client/front-end then can directly call the services by sending HTTP requests.</p>
<p></p>
<p><strong>Project Database and Table</strong></p>
<p><em><strong>Database</strong></em></p>
<p>In the beta version of our project, we are going to use the SQLite database in the development server. In the final version, we will migrate to PostgreSQL DB.</p>
<p><em><strong>Database Design</strong></em></p>
<p>Database design is really critical for all types of websites. A good database does not allow any form of inconsistency and stores data in an ordered way. If a database has inconsistency, it will affect the efficiency and data integrity of the website.</p>
<p>Database files are the key source of information into the system. It is the process of designing database files, which are the key source of information to the system. The files should be properly designed and planned for collection, accumulation, editing and retrieving the required information. </p>
<p>The organization of data in database aims to achieve three major objectives:</p>
<ul>
  <li>Data integration</li>
  <li>Data integrity</li>
  <li>Data independence</li>
</ul>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/database_workflow.png" alt="" width="500" height="500"/></strong></p>
<p align="center"><strong>Figure 2: Database Workflow in Django</strong></p>
<p></p>
<p><em><strong>Database Tables</strong></em></p>
<p><strong>Table 1. Customer/User Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/user_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.1: Customer/User Table</strong></p>
<p></p>
<p><strong>Table 2. Product Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/product_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.2: Product Table</strong></p>
<p></p>
<p><strong>Table 3. Review-Rating Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/ratingreview_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.3: Review-Rating Table</strong></p>
<p></p>
<p><strong>Table 4. Cart Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/cart_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.4: Cart Table</strong></p>
<p></p>
<p><strong>Table 5. Cart-Item Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/carte_items_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.5: Cart-Item Table</strong></p>
<p></p>
<p><strong>Table 6. Category Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/category_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.6: Category Table</strong></p>
<p></p>
<p><strong>Table 7. Order Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/order_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.7: Order Table</strong></p>
<p></p>
<p><strong>Table 8. Ordered Product Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/orderproduct_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.8: Ordered Product Table</strong></p>
<p></p>
<p><strong>Table 9. Payment Table</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/payment_table.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 3.9: Payment Table</strong></p>
<p></p>
<p></p>
<p></p>
<p><strong>Project Model View</strong></p>
<p></p>

<p><strong>1. Home Page:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/homepage.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 4: Home Page</strong></p>
<p></p>
<p></p>

<p><strong>2. Admin Login Page:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/admin_login.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 5: Admin Login Page</strong></p>
<p></p>
<p></p>

<p><strong>3. Admin Panel:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/admin_panel.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 6: Admin Panel</strong></p>
<p></p>
<p></p>

<p><strong>4. Unauthorized Login Attempts:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/login_attempts.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 7: Unauthorized login attempts</strong></p>
<p></p>
<p></p>

<p><strong>5. Customer Sign Up Page:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/sign_up.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 8: Customer Sign Up Page</strong></p>
<p></p>
<p></p>

<p><strong>6. Customer Login Page:</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/login.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 9: Customer Login Page</strong></p>
<p></p>
<p></p>

<p><strong>7. Category-wise Product Browsing</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/category.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 10: Category wise Product Browsing</strong></p>
<p></p>
<p></p>

<p><strong>8. Search Functionality</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/search.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 11: Search for Products</strong></p>
<p></p>
<p></p>

<p><strong>9. Single Product Details with Rating & Review</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/single.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 12: Single Product Details Page with Rating and Review</strong></p>
<p></p>
<p></p>

<p><strong>10. Cart Page</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/cart_page.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 13: Cart Page</strong></p>
<p></p>
<p></p>

<p><strong>11. Checkout Page</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/checkout_page.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 14: Checkout Page</strong></p>
<p></p>
<p></p>

<p><strong>12. Confirm Order Page</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/confirm_order.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 15: Confirm Order Page</strong></p>
<p></p>
<p></p>

<p><strong>13. Confirm Payment Page</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/confirm_payment.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 16: Confirm Payment Page</strong></p>
<p></p>
<p></p>

<p><strong>14. Order Confirmed Page</strong></p>
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/blob/main/Documentation/project_report_images/success.JPG" alt=""/></strong></p>
<p align="center"><strong>Figure 17: Order Confirmed Page</strong></p>
<p></p>
<p></p>
<p></p>

<p><strong>Monetization:</strong></p>
<ul>
  <li>We will ask the seller to pay a commission of 5% for product sold more than 100 BDT.</li>
  <li>Introduce affiliate marketing.</li>
  <li>Google AdSense</li>
</ul>

<p></p>
<p><strong>Social Impacts:</strong></p>
<p>The goal of this website is to make shopping easier and in the palm of the user’s hand. Nowadays people of all ages are used to the modern technologies that can connect them to the internet.  And it's on the internet, where the modern era of shopping is making its mark. Everything from a hairpin to a helicopter can be purchased online these days. Products are put into the websites by sellers to be browsed or bought by customers, and the convenience of the e-commerce trend also benefits both buyers and sellers alike. Our website aims to serve as the bridge that connects the buyers and sellers to ensure fair trade.</p>
<p></p>
<p><strong>Future Aspect:</strong></p>
<p>This project has a huge future potential. It can be modified to meet the needs of the future client expectations. More functionalities will be added in the future. The followings are the future targets for the project:</p>
<ul>
  <li>Adding the Wishlist.</li>
  <li>Adding Payment system & gateway</li>
  <li>Adding the Shipping form</li>
  <li>Adding the Third party(seller) functionalities</li>
  <li>User profile customization</li>
  <li>Adding dashboard functionality.</li>

</ul>
<p>&nbsp;</p>
</div>
