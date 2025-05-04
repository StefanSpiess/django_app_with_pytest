# pytest_udemy_django

A Django-based web application created for educational purposes, showcasing best practices in Django development and testing using `pytest` and `pytest-django`. This project is ideal for developers looking to learn or improve their skills in building and testing Django applications.

## Features

- **Django Framework**: Implements a robust and scalable web application using Django.
- **Testing Integration**: Comprehensive test suite leveraging `pytest` and `pytest-django` for unit and integration testing.
- **Educational Focus**: Designed to demonstrate practical examples of Django development and testing workflows.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pytest_udemy_django.git
   cd pytest_udemy_django
   ```

2. **Set Up the Environment**:
   Install dependencies using `pipenv`:
   ```bash
   pip install pipenv
   pipenv install --default
   ```

3. **Apply Database Migrations**:
   ```bash
   pipenv run python manage.py migrate
   ```

4. **Run the Development Server**:
   ```bash
   pipenv run python manage.py runserver
   ```

## Usage

- Access the application in your browser at `http://127.0.0.1:8000/`.
- Explore the features and functionality provided by the application.

## Testing

Run the test suite to ensure everything is working as expected:
```bash
pipenv run pytest
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

