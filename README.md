Saucedemo UI Automation Framework

This repository contains a robust, scalable UI automation framework built to test the Saucedemo web application. It implements industry-standard software engineering practices, specifically the Page Object Model (POM) architecture and data-driven testing.

◉ Tech Stack

Language: Python 3.11

Testing Framework: Pytest

Browser Automation: Playwright

CI/CD: GitHub Actions (Automated cloud execution)

◉ Key Features

Page Object Model (POM): UI locators and test execution logic are strictly separated for high maintainability and cleaner code.

Data-Driven Testing: Edge cases (e.g., valid user vs. locked-out user scenarios) are handled dynamically via @pytest.mark.parametrize to eliminate code duplication.

Continuous Integration: Fully integrated with GitHub Actions to trigger automated test runs in the cloud on every push.

◉ Local Setup

To run this project on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/Sivanesh4321/Saucedemo-UI-Automation.git
cd Saucedemo-UI-Automation


Install dependencies:

pip install -r requirements.txt


Install Playwright browsers:

playwright install


◉ Running the Tests

To execute the automation suite, use the following Pytest commands:

Run headlessly (Invisible mode, best for speed):

pytest tests/test_sauce_login.py


Run in headed mode (Visible browser, best for debugging):

pytest tests/test_sauce_login.py --headed
