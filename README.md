    
# Registration Using Face Recognition System


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


## 🚀 About Me
A passionate and results-driven AI/ML Developer with expertise in designing, developing, and deploying machine learning models and AI-driven solutions. Skilled in MLOps practices for scalable and efficient model deployment and lifecycle management. Proficient in Python and popular frameworks like TensorFlow, PyTorch, and Scikit-learn. Experienced in data preprocessing, model evaluation, and visualization tools such as Pandas, Seaborn, and Matplotlib. Dedicated to leveraging AI/ML to solve real-world challenges and deliver impactful results through innovative and robust solutions.


## Author

- [@Akash Modi](https://www.github.com/Akashmodi258)


## License

[MIT](https://choosealicense.com/licenses/mit/)


    
