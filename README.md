# Haplagz Web Application

This repository contains a web application named "Haplagz" for detecting plagiarism in text. The application allows users to input a question and its corresponding answer, and then scans the web to identify potential instances of plagiarism.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/haplagz-webapp.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd haplagz-webapp
   ```

3. **Install Dependencies:**

   Before running the application, make sure you have all the dependencies installed. You can install them using pip:

   ```bash
   pip install Flask google googlesearch-python requests beautifulsoup4
   ```

4. **Run the Application:**

   ```bash
   python haplagz-webapp.py
   ```

5. **Access the Application:**

   Once the application is running, open your web browser and go to [http://localhost:8080](http://localhost:8080).

6. **Input Question and Answer:**

   - Enter your question in the provided input field.
   - Enter the corresponding answer.
   - Choose the options for search engines, advanced search, and the number of links to scan.
   - Click on the "Search" button.

7. **View Results:**

   - The application will display the results, including the sites searched, search summary, success rate, time taken, and whether plagiarism was found.
   - If plagiarism is detected, the application will provide a list of sites where the plagiarized content was found.

## Repository Structure

- **`haplagz-webapp.py`**: This is the main Python file containing the Flask web application.
- **`templates/`**: This directory contains HTML templates for rendering the web pages.
- **`static/`**: This directory contains static files such as CSS and JavaScript.

## Application Workflow

1. **Home Page ("/")**:
   - Displays a form for inputting the question and answer.

2. **Results Page ("/results")**:
   - Executes the plagiarism detection algorithm based on the provided question and answer.
   - Displays the search summary, including the sites searched, success rate, and time taken.
   - If plagiarism is found, provides a list of sites where the plagiarized content was found.

## Security Note

- This application relies on web scraping to fetch content from external websites. It's essential to use it responsibly and ensure compliance with the terms of service of the websites being scraped.
- The plagiarism detection algorithm implemented in this application is for educational purposes and may not be suitable for detecting all forms of plagiarism accurately.
