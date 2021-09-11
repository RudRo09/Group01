<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p align="center"><strong><img src="https://media.dhakatribune.com/uploads/2016/11/nsulogo.jpg" alt="" width="307" height="172" /></strong></p>
<p align="center"><strong>North South University</strong></p>
<p align="center">Department of Electrical &amp; Computer Engineering</p>
<p align="center"><strong>Project Proposal</strong></p>
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
<p align="center"><strong>Date Prepared</strong><strong>: </strong>27/06/2021</p>
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
<p align="center"><strong><img src="https://github.com/NSU-SU21-CSE299-6/Group01/tree/main/Documentation/project_repor_images/erd.JPG" alt="" width="641" height="481" /></strong></p>
<p>2. System Information</p>
<p>This system will help the seller to provide the selling service and the buyers to take that service. They are the primary users of this web-app. They can visit the website and find their preferable products. This website will be a place to connect the buyers to the sellers. Another help of this system will be rating and reviewing the products, this feature will meet what a buyer needs to connect with the seller easily. It has the following advantages</p>
<p align="center"><strong>Figure 1: Entity Relationship Diagram System Database</strong></p>
<ul>
  <li>User friendly interface</li>
  <li>Fast access to database</li>
  <li>Category-wise product browsing and search functionality.</li>
</ul>
<p></p>
<p><strong>Technology</strong></p>
<p><em>Front-end:</em></p>
<p>Like any other website, we will be using HTML for the structure and content of our website. Then we will apply CSS and Bootstrap to it, for styling and formatting the website. We will also use some JavaScript for the client-side interface. Our website will have a responsive web design.</p>
<p><em>Backend:</em></p>
<p>For the backend of our website, we are using Python-based web framework Django. In the backend, we will expose a bunch of services that will be accessible via the HTTP protocol. The client/front-end then can directly call the services by sending HTTP requests.</p>
<p><em>Database:</em></p>
<p>In the beta version of our project, we are going to use the SQLite database in the development server. In the final version, we will migrate to PostgreSQL DB.</p>
<p><em>Payment Method:</em></p>
<p>For the payment method we will be using SSLCOMMERZ, which is a secure and authorized online Payment Gateway. It enables to perform secured transactions from the customer’s card, mobile wallet or bank account. But if we face any issue implementing it properly in our project, we plan to use Stripe Python library as an alternative approach. It is also a technology to accept payments online and build economic infrastructure for the internet.</p>
<p><strong>Social Impacts:</strong></p>
<p>The goal of this website is to make shopping easier and in the palm of the user’s hand. Nowadays people of all ages are used to the modern technologies that can connect them to the internet.  And it's on the internet, where the modern era of shopping is making its mark. Everything from a hairpin to a helicopter can be purchased online these days. Products are put into the websites by sellers to be browsed or bought by customers, and the convenience of the e-commerce trend also benefits both buyers and sellers alike. Our website aims to serve as the bridge that connects the buyers and sellers to ensure fair trade.</p>
<p>&nbsp;</p>
</div>
