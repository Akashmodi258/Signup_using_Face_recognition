    
# Signup using Face recognition

**Project Status: Under Maintenance**  
We are currently addressing a database-related issue. Some features may not work as expected. The system will be fully functional once the maintenance is complete.

## Overview
- A Django-based system ensures secure and unique user registration using face recognition.
- Prevents duplicate accounts by verifying uploaded profile photos against existing users.
## Deployment

To deploy this project run
1.  Clone the repository

```bash
    git clone https://github.com/your-username/registration-face-recognition.git  
```
2.  Install dependencies
```bash
    pip install -r requirements.txt  
```
3. Apply migrations
```bash
    python manage.py migrate  
```
4.  Run the server
```bash
    python manage.py runserver  
```
## Workflow
-   Registration: Upload a profile photo for face detection and duplicate verification.
-   Login: Authenticate with email and password.
-   Dashboard: Manage profile and posts.
-   Post Management: Create and view posts.



## Features

-   Face Verification During Registration:
    -   Ensures each face is unique to a single account.
    -   Validates uploaded photos for quality and supported formats.
-   Account Management:
    -   Update profile details.
    -   Secure login/logout functionality.
    -   Delete accounts when needed.
-   Dashboard & Posts:
    -   User-specific dashboard for account management.
    -   Create, view, and manage posts.
    -   Filtered views for users' own posts and community posts.
-   Responsive Web Pages:
    -   User-friendly UI for registration, login, and dashboard interactions.
    -   Additional pages for "Contact Us" and "About" sections.


## About Our Team
We are a passionate and results-driven team of AI/ML Developers, dedicated to designing, developing, and deploying cutting-edge machine learning models and AI-driven solutions. Our collective expertise spans MLOps practices for scalable and efficient model deployment and lifecycle management. We are proficient in Python and industry-standard frameworks such as TensorFlow, PyTorch, and Scikit-learn. As a team, we bring strong capabilities in data preprocessing, model evaluation, and visualization using tools like Pandas, Seaborn, and Matplotlib. United by a common goal, we strive to solve real-world challenges through innovative, robust, and impactful AI/ML solutions.

## Author

- [@Akash Modi](https://www.github.com/Akashmodi258)

- [@Prajwal Rayar](https://www.github.com/Prajwal-0103)



## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.




    
