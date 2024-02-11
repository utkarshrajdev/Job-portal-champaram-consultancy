# Job Portal

Welcome to our Job Portal! This project provides a platform for both businesses and individuals to connect for job opportunities, manage job listings, and facilitate candidate recruitment. The portal is designed to cater to both Business-to-Business (B2B) and Business-to-Customer (B2C) needs, offering a comprehensive set of features for job seekers and recruiters alike.

## Setup

1. Clone this repository:

    ```
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create a virtual environment (optional but recommended):

    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

    ```
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Apply migrations to create the database schema:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Start the Django development server:

    ```
    python manage.py runserver
    ```
    
## Features

### For Job Seekers (B2C Dashboard):
- **User Authentication**: Users can sign up and log in using email/password or via Google authentication for convenience and security.
- **Personalized Job Recommendations**: Our system analyzes user profiles and suggests relevant job openings based on their skills, experience, and preferences.
- **Job Search**: Users can search for jobs based on keywords, location, industry, and other filters to find the perfect match for their career aspirations.
- **Application Management**: Job seekers can keep track of their applications, view application status, and receive notifications about interview requests and job updates.
- **DSA Learning Resources**: Access a curated collection of Data Structures and Algorithms YouTube videos to enhance skills and prepare for technical interviews.

### For Recruiters (B2B Dashboard):
- **Recruiter Authentication**: Recruiters can register and authenticate using email/password or via Google authentication.
- **Job Posting**: Recruiters can create, edit, and manage job listings, providing detailed descriptions and requirements to attract suitable candidates.
- **Candidate Management**: Recruiters can review job applications, shortlist candidates, schedule interviews, and communicate with applicants seamlessly within the platform.
- **Analytics and Insights**: Gain valuable insights into job performance metrics, applicant demographics, and recruitment trends to optimize hiring strategies.

## Getting Started

To explore the Job Portal and its features, visit our deployed website: [Job Portal](https://utkarshraj432k.pythonanywhere.com/)

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django (Python)
- **Authentication**: Django AllAuth, Google OAuth
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Deployment**: PythonAnywhere

## How to Contribute

Contributions to the Job Portal project are welcome! If you have suggestions for improvements, find any issues, or want to add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make changes and test thoroughly.
4. Commit your changes: `git commit -m "Description of changes"`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request.

## Acknowledgements

We would like to thank all the contributors and open-source projects that have inspired and assisted us in building this Job Portal.

Happy job hunting!
