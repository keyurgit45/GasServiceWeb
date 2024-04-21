# Gas Utilities Consumer Services Application

This Django application provides a platform for customers of gas utilities to submit service requests, track the status of their requests, and view account information. It also enables customer support representatives to manage and respond to service requests.

## Features

- **Service Requests:** Customers can submit requests online, choose the type of service needed, provide detailed descriptions, and attach files.
- **Request Tracking:** Customers can track the progress of their service requests, including submission timestamps and resolution times.

## Note
To create a support staff account, create a new group "SupportStaff" in Django admin and assign it to a particular user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.8 or newer)
- pip (Python package manager)
- Virtualenv (optional but recommended for environment management)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/keyurgit45/GasServiceWeb.git
   cd gas_service
   ```

2. **Set up a Virtual Environment** (Optional)

   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   Make migrations and migrate the database setup:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**

   To access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

   This will start the local development server on http://127.0.0.1:8000/.

2. **Access the Application**

   Open your web browser and go to http://127.0.0.1:8000/ to start using the application.
