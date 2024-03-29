# 8Bit Bazaar

Introducing 8Bit Bazaar: your go-to platform for all things retro gaming. With our marketplace, you can effortlessly browse, buy, review, and wishlist classic games from various eras and platforms. Explore nostalgia-filled adventures with ease through intuitive navigation and user-friendly features. Start your retro gaming journey today with 8Bit Bazaar.
<br>

![8BitBAzaar](documentation/responsive_image.png)

### [Link to live site](https://eight-bit-bazaar-8c5cb6f7cbb6.herokuapp.com/)

## User Experience

### User Stories

I embraced the Agile methodology and made use of a GitHub project board to streamline the organization and development of my user stories. To improve clarity and structure, I crafted a template that meticulously details each user story. This template not only ensures precision but also contributes to a well-defined framework for effective project management.

<details><summary>Issues Template</summary>


![issue template](documentation/issues_template.png)

</details>

<details><summary>Issues List</summary>

![issues](documentation/issues_list.png)
</details>

<details><summary>Milestones</summary>

![project board](documentation/milestones.png)

</details>

<details><summary>Project Board</summary>

![project board](documentation/project_board.png)

</details>

### MoSCoW Prioritization

I used MoSCow priotitization to organise each iteration of my project

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration


#### Developer


As a **developer**, I can **create an entity relationship diagram** so that I can **plan my database models**.(ITERATION 1)(MUST HAVE)

    Acceptance Criteria:

    1. Use DrawSQL to plan database schema
    2. The ERD should accurately represent the relationships between different entities in the database, helping plan the overall structure and connections.
    3. The ERD should include essential details such as tables, primary and foreign keys, and relationships between entities, providing a clear visual representation for database modeling.

As a **developer**, I can **implement logic** so that I can **mark games as on sale, and the price is reduced**.(ITERATION 3)(SHOULD HAVE)

    Acceptance Criteria:

    1. The platform should provide a backend mechanism or interface that allows developers to mark specific games as "on sale."
    2. Once a game is marked as "on sale," the platform should dynamically update the displayed price to reflect the reduced, discounted price.
    3. Developers should have the flexibility to easily toggle the "on sale" status for games, allowing for seamless management of promotional periods and pricing changes.

As a **developer**, I can **create wireframes** so that I can **plan the appearance and structure of my site**.(ITERATION 2)(MUST 
 HAVE)

    Acceptance Criteria 

    1. Developers should have access to wireframing tools or resources to create visual representations of the website's appearance and structure.
    2. The wireframes should encompass key elements such as layout, navigation, and placement of essential components, providing a comprehensive plan for the site's design.
    3. The wireframes should serve as a reliable reference for the development team, aiding in the efficient implementation of the website's visual and structural elements.

As a **developer**, I can **create user stories** so that I can **plan my project**.(ITERATION 2)(MUST HAVE)

    Acceptance Criteria:

    1. Use GitHub projects for the creation, tracking, and management of user stories.
    2.  User stories should be clearly defined, outlining the intended functionality or feature from the user's perspective.
    3. Each user story should include acceptance criteria, specifying the conditions that must be met for the story to be considered complete.

As a **developer**, I can **add robots.txt , sitemap.xml file, descriptive meta tags and
rel attributes on links to external resources** so that I can **enhance SEO**.(ITERATION 7)(MUST HAVE)

    Acceptance Criteria:

    1. A robots.txt file is created and implemented to guide web crawlers on page indexing.
    2. A sitemap.xml file is generated and submitted to search engines for efficient content indexing.
    3. Descriptive meta tags, including title and meta descriptions, are added to key pages for improved search engine visibility.


As a **developer**, I can **test my code** so that I can **ensure everything works as it should**.(ITERATION 7)(MUST HAVE)

    Acceptance Criteria:

    1. The developer should conduct manual testing to evaluate the user interface, user experience, and overall functionality of the application.
    2. Automated tests, including unit tests and integration tests, should be implemented to ensure the correctness and stability of individual components and their interactions.
    3. End-to-end testing should be carried out, both manually and through automated tools, to validate the complete flow of the application and identify potential issues in a real-world scenario.


#### Admin

As an **admin**, I can **add games to the site** so that I can **update the catalog**.(ITERATION 4)(MUST HAVE)

    Acceptance Criteria

    1. The admin should have access to a user-friendly interface allowing them to add new games to the site.
    2.  The game addition process should include essential details such as title, description, cover image, price, and any relevant categorization.
    3. Once a game is added, it should seamlessly integrate into the site's catalog, ensuring it is visible to shoppers.

As an **admin**, I can **edit and delete games** so that I can **manage the store effectively**.

    ### Acceptance Criteria

    1. The admin should be able to access a user-friendly interface to edit existing game details, including title, description, cover image, price, and categorization.
    2. The editing process should ensure that changes made to a game are accurately reflected in the catalog, maintaining consistency across the platform.
    3. The admin should have the capability to delete games from the catalog, removing them from the site effectively.

#### Shopper

As a **shopper**, I can **view a list of games** so that I can **see which I would like to purchase**. (ITERATION 2)(MUST HAVE)

    Acceptance Criteria:

    1. Upon accessing the homepage, I should see a well-organized list of games with their titles, cover images, and prices, facilitating a quick overview.
    2. The list should be easily navigable, allowing me to scroll through and identify games of interest without any usability issues.
    3. Clicking on a game in the list should promptly redirect me to a detailed page providing additional information about the selected game, such as a description, reviews, and specifications.



As a **shopper**, I can **search for a game by name or description** so that I can **find the game I am looking for**.(ITERATION 3)(SHOULD HAVE)

    Acceptance Criteria:

    1. There should be a clearly visible search bar on the homepage, enabling me to input the name or a relevant description of the game I am looking for.
    2. Upon entering a search query, the platform should promptly display relevant results, including games with titles or descriptions matching the entered keywords.
    3. The search results should be presented in an easily comprehensible format, showcasing essential details such as game title, cover image, and price, allowing me to quickly identify and select the desired game.

As a **shopper**, I can **view the details of the game** so that I can **see the price, description, game play, rating and image**. (ITERATION 2)(SHOULD HAVE)

    Acceptance Criteria:

    1. Upon selecting a game, I should see a dedicated page with clear and prominently displayed pricing information.
    2. The game details page must provide a concise yet informative description, offering key insights into the game's features.
    3. The page should present any additional information, such as if it is on sale and associated reviews

As a **shopper**, I can **view different categories of games** so that I can **filter the ones I like**.(ITERATION 3)(MUST HAVE)

    Acceptance Criteria 

    1. The platform should display distinct categories of games on the homepage, allowing me to easily identify and access a variety of genres.
    2. Upon selecting a specific category, the list of games should dynamically update to showcase only those belonging to the chosen category.
    3. The category filter should be intuitive and user-friendly, enabling me to efficiently navigate through different genres and find games that align with my preferences.

As a **shopper**, I can **receive and email confirmation after registering ** so that I can **ensure my account was registered **.

    Acceptance Criteria: 

    1. Following the successful purchase of a game, the shopper should receive an email confirmation in their registered email inbox.
    2. The confirmation email should explicitly state that the purchase was successful, providing assurance that the transaction has been completed.
    3. The email content should include essential details such as a confirmation message, itemized list of purchased games, transaction summary, and any relevant information regarding accessing or downloading the games.

As a **shopper**, I can **receive email confirmations** so that I can **ensure my account was registered and purchases verified**.(ITERATION 4)(SHOULD HAVE)

    Acceptance Criteria:

    1. Upon successfully completing the account registration process, the shopper should receive a confirmation email in their registered inbox, clearly communicating that the registration was successful and providing assurance that their account is now active.
    2. Following a successful purchase, another email confirmation should be sent to the shopper's registered email inbox, explicitly stating that the purchase was successful and offering details such as a confirmation message, an itemized list of purchased items, transaction summary, and any relevant information regarding accessing or downloading the purchased content.
    3. The email content for both registration and purchase confirmations should be comprehensive, including necessary details and instructions, and designed to provide a seamless and reassuring user experience.

As a **shopper**, I can **view games in my bag** so that I can **see what I have added and make any adjustments before checkout**.(ITERATION 3)(MUST HAVE)

    Acceptance Criteria 

    1. The platform should have a clearly visible and easily accessible section where shoppers can view the games they have added to their shopping bag.
    2. The list of games in the shopping bag should display essential details such as titles, quantities, and prices, providing a concise overview for shoppers.
    3. Shoppers should have the ability to easily adjust the quantity of each game or remove items from their shopping bag, facilitating last-minute adjustments before proceeding to checkout.

As a **shopper**, I can **See the running total of my purchases** so that I can **avoid overspending**.(ITERATION 3)(SHOULD HAVE)

    Acceptance Criteria:

    1. The platform should display a running total prominently on the shopping page, allowing shoppers to see the accumulated cost of their selected items.
    2. The running total should dynamically update in real-time as shoppers add or remove items from their shopping bag, providing an accurate reflection of their current purchases.
    3. The running total should be clear and easily noticeable, helping shoppers to monitor and manage their spending throughout the shopping experience.

As a **shopper**, I can **see special offers** so that I can **take advantage of them**.(ITERATION 3)(SHOULD HAVE)

    Acceptance Criteria:

    1. A dedicated section for special offers should be prominently displayed on the platform's homepage, ensuring easy visibility for shoppers.
    2. Special offers must be presented with clear visuals, concise descriptions, and any applicable discounts or unique selling points.
    3. Shoppers should have the ability to click on each special offer to access more detailed information.

As a **shopper**, I can **easily login/ logout** so that I can **access my account information/ keep my account secure**.(ITERATION 1)(SHOULD HAVE)

    Acceptance Criteria:

    1. Shoppers should find a visible and easily accessible login button on the homepage for a quick login process.
    2. The login/logout process should be straightforward, requiring minimal steps for shoppers to access their account or log out securely.
    3. Once logged in, shoppers should have immediate access to their account information, ensuring a convenient and efficient user experience.

As a **shopper**, I can **checkout my bag** so that I can **purchase my items**.(ITERATION 3)(MUST HAVE)

    Acceptance Criteria

    1. A clearly visible and easily accessible "Checkout" button should be present on the shopping page for shoppers to proceed to the checkout process.
    2. Shoppers should be able to review the items in their bag, including titles, quantities, and prices, before initiating the checkout.
    3. The checkout process should be user-friendly, guiding shoppers through the necessary steps such as providing shipping information, selecting payment methods, and confirming the purchase.

As a **shopper**, I can **receive feedback on my actions** so that I can **feel secure and confident in choices**.(ITERATION 3)(MUST HAVE)

    Acceptance Criteria: 

    1. The platform should provide real-time feedback to shoppers when they perform actions such as adding items to the shopping bag, updating quantities, or completing a purchase.
    2. Feedback messages should be clear, concise, and displayed prominently, ensuring shoppers are informed about the outcome of their actions.
    3. In case of errors or issues during the shopping process, shoppers should receive informative error messages that guide them on how to resolve the issue.

As a **shopper**, I can **register for an account** so that I can **have a personal profile**.(ITERATION 3)(SHOULD HAVE)

    Acceptance Criteria

    1. The platform should feature a user-friendly and easily accessible registration process on the homepage or a dedicated registration page for shoppers.
    2. Shoppers should be able to provide necessary information such as a valid email address and password to create their account during the registration process.
    3. Upon successful registration, shoppers should receive a confirmation message or email, ensuring they are aware that their account has been created successfully.

As a **shopper**, I can **make a payment** so that I can **order and receive my games**.(ITERATION 4)(MUST HAVE)

    Acceptance Criteria:

    1. Shoppers should be guided through a secure and straightforward payment process, allowing them to provide necessary payment details such as credit card information or use alternative payment methods.
    2. The payment process should clearly communicate the total cost, including the prices of selected games, discount and any other fees. 
    3. Upon successful payment, shoppers should receive a confirmation message or email detailing the order, including a summary of purchased games, total cost, and any relevant order tracking information.

As a **shopper**, I can **have a personalized profile** so that I can **see my order history and save payment information**.(ITERATION 4)(MUST HAVE)

    Acceptance Criteria:

    1. Users should be able to create and access a personalized profile on the platform, providing details such as a username, password, and email address.
    2. Upon logging into their personalized profile, users should have easy access to their order history, displaying a comprehensive list of past purchases.
    3. Users should have the option to securely save and manage their payment information within their personalized profile for quicker and more convenient future transactions.

As a **shopper**, I can **add products to my wish list** so that I can **purchase at a later date**.(ITERATION 5)(COULD HAVE)

    Acceptance Criteria:

    1. Shoppers should have the option to add products to a wish list while browsing the platform.
    2. The wish list functionality should be easily accessible, allowing shoppers to add or remove items with minimal effort.
    3. Shoppers should be able to view their wish list at any time, providing a convenient way to monitor and manage items for potential future purchases.

As a **shopper**, I can **use a discount code** so that I can **make use of offers**.(ITERATION 5)(SHOULD HAVE)

    Acceptance Criteria 

    1. The platform should provide a clearly visible field during the checkout process where shoppers can input a discount code.
    2. Shoppers should be able to apply the discount code easily, with the platform validating and adjusting the total cost accordingly.
    3. If the discount code is valid, the platform should display the updated total cost, reflecting the applied discount.

As a **shopper**, I can **recover my password in case I forget it** so that I can **recover my account**.(ITERATION 4)(SHOULD HAVE)

    Acceptance Criteria 

    1. Users should have access to a "Forgot Password" feature on the login page or within their account settings.
    2. When initiating the password recovery process, users should receive a prompt to enter their registered email address.
    3. The platform should send a secure password reset link to the user's registered email address, allowing them to create a new password.

As a **shopper**, I can **sign up for a newsletter** so that I can **receive updates**.(ITERATION 6)(MUST HAVE)

    Acceptance Criteria 

    1. Shoppers should have the option to sign up for the newsletter, either during the account registration process or through a dedicated newsletter sign-up feature.
    2. The newsletter sign-up process should be user-friendly, requiring minimal information such as an email address.
    3. Shoppers who sign up for the newsletter should receive regular updates, promotions, and relevant information via email.

As a **shopper**, I can **explore the websites facebook page** so that I can **stay up to date with offers and new releases**.( ITERATION 7)(MUST HAVE)

    Acceptance Criteria:

    - The platform should provide a prominent and easily accessible link or button for shoppers to explore the website's Facebook page.
    - Shoppers should be able to access the Facebook page seamlessly, whether through an external link or an integrated social media feature.
    - The Facebook page should  feature updates on offers, promotions, and new releases, providing shoppers with timely and relevant information.

As a **shopper**, I can **see custom error pages** so that I can **know I have visited the wrong url and can navigate back to the home page**. (ITERATION 7)(SHOULD HAVE)

    Acceptance Criteria:

    1. In the event of encountering an incorrect or non-existent URL, the platform should display a custom error page.
    2. The custom error page should clearly communicate that the shopper has visited an incorrect URL or encountered an error, providing a user-friendly message.
    3. he custom error page should include a prominent link or button that allows shoppers to easily navigate back to the home page.

As a **shopper**, I can **view, add and edit reviews** so that I can **decide whether to buy a game, and provide feedback on games I have purchased**.(ITERATION 5)(SHOULD HAVE)

    Acceptance Criteria:

    1. Users should be able to view existing reviews for a game, providing insights into the experiences of other shoppers.
    2. Users should have the option to add a review to a game, including a rating and written feedback, contributing to the community's collective knowledge.
    3. The platform should allow users to edit their reviews, providing flexibility for users to update or refine their feedback over time.

## Design

### Colour Scheme

#eeb8b6 (Light Coral): Main background color for a nostalgic and warm feel.
#2d55a6 (Dark Blue): Accent color, evoking the classic gaming atmosphere.
#ca4727 (Rust Red): Highlight color, adding vibrancy and emphasis.
#ffffff (White): Text color for clarity and readability.
#000000 (Black): Also used for text color.
#f2e9df (Beige): Additional background color, enhancing contrast and visual appeal.
This color palette aims to capture the essence of retro gaming while providing a clean and visually engaging experience for users on the website.

This color palette aims to capture the essence of retro gaming while providing a clean and visually engaging experience for users on the website.

![Colour scheme](documentation/colour_scheme.png)



### Typography

I used Google Fonts to browse fonts that fit my theme. 

* [VT323](https://fonts.google.com/specimen/VT323) was used for all of the sites text as it is pixelated and enhances the retro theme throughout the website. 

* [Font Awesome](https://fontawesome.com) icons were used for the mobile navigation menu icons, and for buttons across the site.

### Entity Relationship Diagram

My Entity relationship diagram was create using [DrawSQL] for the planning stage. The ERD represents my database structure visually, and enabled me to plan my
models and database interactions. 

<details><summary>Click to view the planning ERD</summary>

![Planning ERD](documentation/planning_ERD.png)

</details>

<details><summary>Click to view the final ERD</summary>

![Final ERD](documentation/ERD.png)
</details>

### Wireframes

I used [Figma](https://www.figma.com/) to create the wireframes for this project.

* The desktop wireframes are tailored to the widely adopted screen resolution of 1920 x 1080, constituting 22.18% of screens.

* The tablet wireframes are designed to fit the dimensions of the iPad Pro (1024 x 1366).

* For mobile devices, the wireframes are crafted to the specifications of the iPhone SE, with dimensions set at 375 x 667.
#### Home Page

<details><summary>Click to view Home Page wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/home_wireframe_desktop.png)

#### Tablet
![wireframe](documentation/wireframes/home_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/home_wireframe_mobile.png)

</details>

#### Sign Up Page

<details><summary>Click to view Sign Up Page wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/signup_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/signup_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/signup_wireframe_mobile.png)

</details>

#### Login Page

<details><summary>Click to view Login Page wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/login_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/login_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/login_wireframe_mobile.png)

</details>

#### Logout Page

<details><summary>Click to view Logout Page wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/signout_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/signout_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/signout_wireframe_mobile.png)
</details>

#### Games Page

<details><summary>Click to view Games wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/games_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/games_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/games_wireframe_mobile.png)
</details>


#### Game Details

<details><summary>Click to view Game Details wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/game-details_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/game-details_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/game-details_wireframe_mobile.png)
</details>

#### Product management: Add game

<details><summary>Click to view add game wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/add_game_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/add_game_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/add_game_wireframe_mobile.png)
</details>

#### Product management: Edit game

<details><summary>Click to view edit game wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/edit_game_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/edit_game_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/edit_game_wireframe_mobile.png)
</details>

#### Wishlist

<details><summary>Click to view the wishlist wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/wishlist_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/wishlist_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/wishlist_wireframe_mobile.png)
</details>

#### My reviews

<details><summary>Click to view the my reviews wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/reviews_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/reviews_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/reviews_wireframe_mobile.png)
</details>

#### Add review

<details><summary>Click to view the add review wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/add_review_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/add_review_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/add_review_wireframe_mobile.png)
</details>

#### Edit review

<details><summary>Click to view the edit review wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/edit_review_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/edit_review_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/edit_review_wireframe_mobile.png)
</details>

### Bag

<details><summary>Click to view the bag wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/bag_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/bag_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/bag_wireframe_mobile.png)
</details>

### Checkout

<details><summary>Click to view the checkout wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/checkout_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/checkout_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/checkout_wireframe_mobile.png)
</details>

#### Checkout Success

<details><summary>Click to view the checkout success wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/checkout_success_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/checkout_success_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/checkout_success_wireframe_mobile.png)
</details>

### Profile

<details><summary>Click to view the profile wireframes</summary>

#### Desktop
![screenshot](documentation/wireframes/profile_wireframe_desktop.png)
#### Tablet
![wireframe](documentation/wireframes/profile_wireframe_tablet.png)
#### Mobile
![wireframe](documentation/wireframes/profile_wireframe_mobile.png)
</details>

## Existing Features

### Home Page

![home](documentation/existing_features/features_home.png)

### Games Page

![games](documentation/existing_features/features_games.png)


### Game Detail

![game detail](documentation/existing_features/features_game_detail.png)

### Add Review

![add review](documentation/existing_features/features_add_review.png)

### Edit Review

![Edit review](documentation/existing_features/features_edit_review.png)

### My Reviews

![All reviews](documentation/existing_features/features_all_reviews.png)

### Bag

![Bag](documentation/existing_features/features_bag.png)

### Checkout

![Checkout](documentation/existing_features/features_checkout.png)

### Checkout Success

![Checkout success](documentation/existing_features/features_checkout_success.png)

### Product Management - Add game

![Add game](documentation/existing_features/features_add_game.png)

### Product Management - Edit game

![Edit game](documentation/existing_features/features_edit_game.png)

### My Profile 

![Profile](documentation/existing_features/features_profile.png)

### Wishlist

![Wishlist](documentation/existing_features/features_wishlist.png)

### Login

![Checkout success](documentation/existing_features/features_login.png)

### Signup

![Signup](documentation/existing_features/features_signup.png)

### Logout

![Logout](documentation/existing_features/features_logout.png)


### Password reset

![Checkout success](documentation/existing_features/features_password_reset.png)

### Password reset done

![Checkout success](documentation/existing_features/password_reset_done.png)

## Future Development

I aimed to introduce additional features into my project, some of which were initially planned but have been categorized as "Won't Have" on my GitHub project board, following MoSCoW prioritization.

### Social Login

* Streamline the user sign-up process by integrating social login options, such as Google and Facebook. This not only expedites registration but also enhances user experience.

### Email Notifications

* Implement email notifications for users, notifying them when a game on their wishlist goes on sale. This feature aims to keep users engaged and informed about relevant updates.

### Review Moderation

* Create an admin page for review moderation, enabling administrators to review and moderate customer reviews for inappropriate content or spam.

### Active Rating

* Introduce real-time rating logic where users' ongoing ratings dynamically influence the overall rating for a particular game.

### Auto Complete

* Enhance the user search experience by incorporating Google autocomplete functionality. This improvement aims to provide users with a more efficient and convenient game search process.

### Filtering

* Enhance filtering mechanisms to accurately sort games on sale into price order, ensuring a more effective and user-friendly sorting process.

### Bundle Deals

* Integrate logic to enable users to purchase multiple specific games as a bundle, offering an overall discount for the bundled items.

### Notifications

* Improve notification messages throughout the site. For example, redirect non-admin users attempting to access the "add games" URL to the login page with a clear notification, enhancing user guidance and communication.

### Styling

* Refine the platform's visual appeal and responsiveness. Prioritize improvements to styling, aiming for a polished and user-friendly interface. 

## Technologies
![My Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?lineCount=3&line1=postgresql%2Cpostgresql%2C6cc7a1%3Bbootstrap%2Cbootstrap%2C7b86c0%3Bamazon%2Camazon%2C62161a%3B3B&line2=django%2Cdjango%2C344312%3Bjavascript%2Cjavascript%2Cecf398%3Bpython%2Cpython%2C9b9ebf%3B&line3=html5%2Chtml5%2C73a4ea%3Bcss3%2Ccss3%2C8983cc%3B)

* **HTML:** Employed for structuring the content of the website, providing the foundational structure for web pages.
* **CSS:** Utilized for designing and organizing the layout of the site, ensuring a visually appealing and well-organized user interface.
* **Bootstrap:** Applied as a CSS framework to establish an adaptive grid layout for responsiveness and integrate preset styles and components, streamlining the design process.
* **Python + Django:** Formed the backend development stack, providing a robust server-side foundation for seamless functionality and data management.
* **JavaScript:**
   * Displayed and enabled interactivity in the game deletion modal, improving the user experience during game management.
   * Overwrote the default image selection from Django admin, allowing for customized image handling.
   * Implemented animation for custom retro buttons, enhancing the visual appeal and user engagement.
   * Enabled the removal of games from the wishlist and bag, providing users with a seamless shopping experience.
* **PostgreSQL:** Selected as the relational database management system, ensuring efficient data storage and retrieval.
* **ElephantSQL:** Deployed to host the PostgreSQL database online, facilitating remote access and management of the database.
* **Amazon Web Services:** Employed to host static files, ensuring reliable and scalable storage for website assets.
* **Stripe:** Integrated for handling payments, providing a secure and seamless payment processing solution.
* **Figma:** Played a pivotal role in the project by facilitating the creation of wireframes, allowing for collaborative design and planning.
* **GitHub + Git:** Utilized for version control and efficient code management, enabling collaborative development and tracking of code changes.
* **WebAIM Contrast Checker:** Ensured sufficient color contrast for enhanced accessibility, promoting inclusivity in design.
* **Heroku:** Selected as the hosting platform for the site, providing a scalable and reliable hosting solution.
* **WAVE:** Employed to evaluate the accessibility of the site, identifying and addressing potential accessibility issues for a user-friendly experience.
* **DrawSQL** Used to design my ERD in the planning stage of my project.
* **Gmail** Email service used to send emails to users.
* **XML Sitemaps** This was employed to create a sitemap
## Database

I created an entity relationship diagram using [DrawSQL](https://drawsql.app/). This allowed me to plan out my database interactions more easily. 

![entity relationship](documentation/ERD.png)

### Game App
#### Game Model

| Field Name      | Field Type            | Relationship                |
| --------------- | --------------------- | --------------------------- |
| id (PK)         | AutoField             |                             |
| genre           | ManyToManyField(Genre)| Many-to-Many with User      |
| category        | ForeignKey(Category)  |                             |
| sku             | CharField (nullable)  |                             |
| name            | CharField             |                             |
| friendly_name   | CharField             |                             |
| description     | TextField             |                             |
| price           | DecimalField          |                             |
| rating          | DecimalField          |                             |
| image_url       | URLField              |                             |
| image           | ImageField            |                             |
| on_sale         | BooleanField          |                             |
| wishlist        | ManyToManyField(Wishlist)|                          |

#### Genre Model

| Field Name      | Field Type    | Relationship |
| --------------- | ------------- | ------------ |
| id (PK)         | AutoField     |              |
| name            | CharField     |              |
| friendly_name   | CharField     |              |

#### Category Model

| Field Name      | Field Type    | Relationship |
| --------------- | ------------- | ------------ |
| id (PK)         | AutoField     |              |
| name            | CharField     |              |
| friendly_name   | CharField     |              |

#### Review Model

| Field Name      | Field Type            | Relationship                |
| --------------- | --------------------- | --------------------------- |
| id (PK)         | AutoField             |                             |
| title           | CharField             |                             |
| rating          | DecimalField          |                             |
| body            | TextField             |                             |
| game            | ForeignKey(Game)      | on_delete=models.CASCADE    |
| author          | ForeignKey(User)      | on_delete=models.CASCADE    |
| date            | DateTimeField         |                             |
| approved        | BooleanField          |                             |

### Checkout App

#### Order Model

| Field Name       | Field Type            | Relationship                |
| ---------------- | --------------------- | --------------------------- |
| id (PK)          | AutoField             |                             |
| order_number     | CharField             |                             |
| user_profile     | ForeignKey(UserProfile)| related_name='orders'      |
| full_name        | CharField             |                             |
| email            | EmailField            |                             |
| phone_number     | CharField             |                             |
| country          | CountryField          |                             |
| postcode         | CharField             |                             |
| town_or_city     | CharField             |                             |
| street_address1  | CharField             |                             |
| street_address2  | CharField             |                             |
| county           | CharField             |                             |
| date             | DateTimeField         | auto_now_add=True           |
| discount_amount  | DecimalField          |                             |
| total            | DecimalField          |                             |
| original_bag     | TextField             |                             |
| stripe_pid       | CharField             |                             |

#### OrderLineItem Model

| Field Name       | Field Type            | Relationship                |
| ---------------- | --------------------- | --------------------------- |
| id (PK)          | AutoField             |                             |
| order            | ForeignKey(Order)     | on_delete=models.CASCADE    |
| game             | ForeignKey(Game)      | on_delete=models.CASCADE    |
| quantity         | IntegerField          | default=0                   |
| lineitem_total   | DecimalField          | editable=False              |

#### Discount Model

| Field Name       | Field Type            | Relationship                |
| ---------------- | --------------------- | --------------------------- |
| id (PK)          | AutoField             |                             |
| code             | CharField             | unique=True                 |
| percentage       | PositiveIntegerField  |                             |
| start_date       | DateField             |                             |
| end_date         | DateField             |                             |
| for_new_users    | BooleanField          | default=False               |

#### Applied Discount Model

| Field Name       | Field Type            | Relationship                |
| ---------------- | --------------------- | --------------------------- |
| id (PK)          | AutoField             |                             |
| user             | ForeignKey(User)      | on_delete=models.CASCADE    |
| discount         | ForeignKey(Discount)  | on_delete=models.CASCADE    |
| purchase_date    | DateTimeField         | auto_now_add=True           |

### UserProfile Model

| Field Name              | Field Type            | Relationship                |
| ----------------------- | --------------------- | --------------------------- |
| id (PK)                 | AutoField             |                             |
| user                    | OneToOneField(User)   | on_delete=models.CASCADE    |
| default_full_name       | CharField             | null=True, blank=True       |
| default_email           | EmailField            | null=True, blank=True       |
| default_phone_number    | CharField             | null=True, blank=True       |
| default_street_address1 | CharField             | null=True, blank=True       |
| default_street_address2 | CharField             | null=True, blank=True       |
| default_town_or_city    | CharField             | null=True, blank=True       |
| default_county          | CharField             | null=True, blank=True       |
| default_postcode        | CharField             | null=True, blank=True       |
| default_country         | CountryField          | blank_label='Country', null=True, blank=True |

### Wishlist Models

#### Wishlist

| Field Name   | Field Type               | Relationship                |
| ------------ | ------------------------ | --------------------------- |
| id (PK)      | AutoField                |                             |
| user         | OneToOneField(User)      | on_delete=models.CASCADE    |
| date_added   | DateTimeField            | auto_now_add=True           |
| games        | ManyToManyField(Game)    | related_name='wishlist_games'|


### User

* Allauth User Model
* The User model was built using Django's Allauth library

| Field Name   | Field Type              | Relationship      |
| ------------ | ----------------------- | ----------------- |
| id (PK)      | AutoField               |                   |
| username     | CharField (from AbstractUser)|                 |
| email        | EmailField (from AbstractUser)|                |
| password     | CharField (from AbstractUser)|                |
| ...          | ...                     |                   |
| saved_events  | ManyToManyField(Event)  | Many-to-Many with Event |
| comments     | ManyToManyField(EventComment) | Many-to-Many with EventComment |

## Business Model

The website operates as a Business-to-Consumer (B2C) platform specializing in the sale of retro games to customers. The responsibilities of staff members encompass adding new games to the site's inventory, managing sales, and implementing discount codes. Customers, in turn, enjoy the freedom to browse and select games, adding them to their bag before seamlessly proceeding through the checkout process.

Encouraging user participation, customers who have made purchases can actively contribute to the platform by leaving reviews for the games they've acquired.

To foster and sustain a strong connection with the customer base, the website strategically places a newsletter signup form on the home page. Collected email addresses from this form are then leveraged to curate mailing lists, instrumental in conducting customer outreach and executing marketing initiatives.

<details><summary>Signup Form</summary>

![Mailchimp signup](documentation/mailchimp_signup.png)
</details>
<br>

Additionally, the business maintains a vibrant presence on Facebook through a dedicated business page. This platform serves as a hub for posting engaging content that customers can readily access. The website also incorporates a wishlist feature, enabling users to save games of interest. Customers can receive notifications through mailing lists or the Facebook page, alerting them to special offers, discounts, or promotions for the games in their wishlist, thereby incentivizing potential sales.

<details><summary>Facebook page</summary>

<img src="documentation/facebook_page.jpg" alt="Facebook screenshot" width="30%">
</details>

### Search Engine Optimization (SEO) and Marketing

#### SEO

##### Keywords

I used [Wordstream](https://www.wordstream.com/keywords) to generate keywords with low competition, using a combination of short and long-tail keywords to include in my site
meta tags.

These are the keywords I used:
* retro games
* vintage video games
* classic gaming
* old school games
* nostalgic gaming
* collectible games
* classic arcade games
* gaming memorabilia
* 8-bit games
* 16-bit games
* video game collectors
* rare retro games
* gaming nostalgia
* gaming culture
* retro game store
* timeless games
* retro gaming community

##### Sitemap

I used [XML Sitemaps](https://www.xml-sitemaps.com/) to create a sitemap. This improves SEO.

#### Robots.txt file

I generated a robots.txt file to improve SEO. This file dictates to search engines which pages are available to crawl and which to ignore.

```
User-agent: *
Disallow:
Sitemap: https://eight-bit-bazaar-8c5cb6f7cbb6.herokuapp.com/

```

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

### Database Setup with ElephantSQL

This project uses [ElephantSQL](https://www.elephantsql.com) for its PostgreSQL Database.

### Steps to Obtain Your Postgres Database:

1. Register using your GitHub account.
2. Generate a new database instance by selecting **Create New Instance**.
3. Provide a name (typically the project name: 8-bit-bazaar).
4. Choose the **Tiny Turtle (Free)** plan.
5. Keep the **Tags** field empty.
6. Pick the nearest **Region** and **Data Center**.

### Amazon Web Services

This project uses AWS to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged in, follow these series of steps to get your project connected. Make sure you're on the AWS Management Console page.

### S3 Bucket

1. Search for S3 in the AWS Management Console.
2. Create a new bucket, name it (matching your Heroku app name), and choose your region.
3. Untick "Block all public access," acknowledging the bucket will be public.
4. Ensure ACLs are enabled with "Bucket owner preferred."
5. In the Properties tab, enable static website hosting, set index.html and error.html, and click Save.
6. In the Permissions tab, paste the provided CORS configuration.
7. Copy your ARN string.
8. In the Bucket Policy tab, use the Policy Generator to allow GetObject actions for your ARN.
9. Before saving, add /* to the end of the Resource key.
10. Save and in the ACL section, edit, enable List for Everyone, and accept the warning.

### IAM

1. Open IAM from the AWS Services Menu.
2. Create a new group, e.g., "group-eight-bit-bazaar."
3. In the Permissions tab, attach policies, including AmazonS3FullAccess.
4. Create a new policy, e.g., "policy-eight-bit-bazaar," allowing S3 access to your bucket.
5. Attach the policy to your group.
6. Create a new user, e.g., "user-eight-bit-bazaar," with programmatic access, and add it to the group.
7. Download the .csv containing the user's Access Key ID and Secret Access Key.

### Final AWS Setup

1. If DISABLE_COLLECTSTATIC is in Heroku Config Vars, remove it.
2. In S3, create a "media" folder, upload existing media images, and grant public read access.
3. Click Upload to complete.

## Stripe API

1. Obtain your test API keys from the Stripe dashboard.
2. Use these keys:
   - STRIPE_PUBLIC_KEY = Publishable Key
   - STRIPE_SECRET_KEY = Secret Key
   - STRIPE_WH_SECRET = Webhook Signing Secret

## Gmail API

1. Enable 2-Step Verification in Gmail.
2. Navigate to Security > App passwords, generate a 16-character password for "Mail" with a custom name.
3. Save the generated password.
4. Use these keys:
   - EMAIL_HOST_USER = user's Gmail email address
   - EMAIL_HOST_PASS = user's 16-character API key


### Heroku Deployment


This project employs Heroku, a platform-as-a-service (PaaS) that empowers developers to construct, execute, and manage applications exclusively in the cloud.

### Deployment Steps:

1. After setting up your account, select **New** in the top-right corner of your Heroku Dashboard and choose **Create new app** from the dropdown menu.
2. Ensure your app name is unique, choose a region (EU or USA), and select **Create App**.
3. In the new app **Settings**, click **Reveal Config Vars** and set your environment variables:

   | Key | Value |
   | --- | --- |
   | `AWS_ACCESS_KEY_ID` | Insert your AWS access key ID here |
   | `AWS_SECRET_ACCESS_KEY` | Insert your AWS secret access key ID here |
   | `DATABASE_URL` | Insert your ElephantSQL database URL here |
   | `EMAIL_HOST_PASSWORD` | Insert your Email host password here |
   | `EMAIL_HOST_USER` | Insert your Email host username here |
   | `SECRET_KEY` | Any random secret key |
   | `STRIPE_PUBLIC_KEY` | Insert your Stripe public key here |
   | `STRIPE_SECRET_KEY` | Insert your Stripe secret key here |
   | `STRIPE_WH_SECRET` | Insert your Stripe webhook secret here |
   | `USE_AWS` | Set to True |
   | `DISABLE_COLLECTSTATIC` | 1 (*temporary; can be removed for final deployment*) |

4. Heroku requires two additional files for deployment: *requirements.txt* and *Procfile*.

   Install project **requirements** using:
   - `pip3 install -r requirements.txt`

   Update the requirements file if needed:
   - `pip3 freeze --local > requirements.txt`

   Create the **Procfile**:
   - `echo web: gunicorn app_name.wsgi > Procfile`
   - Replace **app_name** with your primary Django app name.

5. For Heroku deployment, connect your GitHub repository:

   - Either choose **Automatic Deployment** from the Heroku app.
   - Or in the Terminal/CLI, connect to Heroku using: `heroku login -i`
   - Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
   - After Git `add`, `commit`, and `push` to GitHub, type: `git push heroku main`

6. The project should now be connected and deployed to Heroku!

Note: My project contains a runtime.txt file stating the python version. This ensures my application runs
in a consistent environment. 

## Local Deployment


This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os


os.environ['STRIPE_PUBLIC_KEY'] = 'Stripe public key'
os.environ['STRIPE_SECRET_KEY'] = 'Stripe secret key'
os.environ['STRIPE_WH_SECRET'] = 'Stripe webhook secret key'
os.environ['SECRET_KEY'] = 'Your secret key'

```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C`
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
-  run the Django app: `python3 manage.py runserver`

### Cloning

Follow these steps to clone the repository:

1. Visit the [GitHub repository](https://github.com/KTC96/8-Bit-Bazaar).
2. Click on the "Code" button above the list of files.
3. Choose your preferred cloning method (HTTPS, SSH, or GitHub CLI) and copy the URL.
4. Open Git Bash or Terminal.
5. Navigate to the directory where you want to clone the repository.
6. In your IDE Terminal, enter the following command to clone the repository:
   - `git clone https://github.com/KTC96/8-Bit-Bazaar.git`
7. Press Enter to create your local clone.

### Forking

Forking the GitHub Repository allows you to create a copy on your GitHub account, enabling you to view and make changes without affecting the original owner's repository.

Follow these steps to fork the repository:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/KTC96/8-Bit-Bazaar).
2. Above the "Settings" Button on the menu, find the "Fork" Button.
3. Click the "Fork" button, and you will now have a copy of the original repository in your own GitHub account!

## Credits

### Code

| Source | Location | Notes |
| --- | --- | --- |
| [YouTube](https://www.youtube.com/watch?v=yc2olxLgKLk&t) | All | I followed this tutorial to help get my footer to stay at the bottom of my page when there was not enough content|
| [CodePen](https://codepen.io/) | Login/ Logout/ Buttons/ Loader | I used code from CodePen for the CSS gameboys on the login an signup pages, as well as for the retro Javascript buttons and heart loading overlay|
| Code Institute Boutique Ado project | All  | Used to create foundations of the project |
| [YouTube](https://www.youtube.com/watch?v=otoKdW-lYc8) | Checkout | I followed this walkthrough to help me build my discount logic |
| [MailChimp](https://mailchimp.com/) | Home | I used the mailchimp signup content for users to signup to my newsletter |
| [Stack Overflow](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django) | Wishlist | I used this post to help inspire my wishlist logic |
| [Stripe](https://stripe.com/gb) | Checkout | I used Stripe for payment processing|

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Canva](https://www.canva.com/)| All pages | I used Canva for the logo design|
| [RedKetchup Favicon Generator](https://redketchup.io/favicon-generator) | All pages | Used to create my favicon|
| [Unsplash](https://unsplash.com/)||  |
| [Fontawesome](https://fontawesome.com/) | All pages | I used font awesome icons |
| [Wikipedia](https://www.wikipedia.org/) | Games, Game Detail | I used Wikipedia to source my game images|
| [Termly](https://termly.io/products/privacy-policy-generator/) | Privacy Policy | I used Termly to generate the Privacy Policy|
| [Kaggle](https://www.kaggle.com/datasets) | Fixtures content | Used kaggle for games datasets |


### Acknowledgements

I would like to thank my mentor Jack for his help during this project, and also my parents for supporting me on this career changing journey. 












