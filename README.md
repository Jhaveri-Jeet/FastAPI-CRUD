# FastAPI Project

This project is a FastAPI application for managing user data.

## Getting Started

Follow these instructions to set up and run the FastAPI project locally.

### Prerequisites

- Python 3.7 or higher
- `pip` package manager
- MySQL or MariaDB server
- phpMyAdmin (optional, for database management through a web interface)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Open phpMyAdmin in your web browser.

2. Log in with your MySQL or MariaDB credentials.

3. Create a new database named `testing`.

### Running the FastAPI Application

1. Ensure your virtual environment is activated.

2. Navigate to the project directory if you're not already there.

3. Run the FastAPI application using the following command:

   ```bash
   uvicorn main:app --reload
   ```

4. Once the server starts, you can access the FastAPI documentation at `http://localhost:8000/docs`.

## Usage

- Use the provided endpoints to perform CRUD operations on user data.
- Refer to the FastAPI documentation for details on available endpoints and request/response formats.

Please replace `<repository_url>` and `<project_directory>` with the appropriate values for your project. Additionally, adjust the instructions according to your specific setup if necessary.
