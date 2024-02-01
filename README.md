# Library Management System

This project is a web application made with the help of the Python Language using the Django Framework.

## 1. Project Setup

1. Install Python from the official [site](https://www.python.org/).
    > Make sure to add Python to the PATH
2. Install the virtualenv package using the following command:
    ```shell
    python -m pip install virtualenv
    ```
3. Create a virtual environment, so that there are no conflicting packages.
    ```shell
    python -m venv lms_env
    ```
4. Activate the environment.
    ```shell
    cd lms_env
    Scripts\activate
    ```
5. Once the virtual environment is activated, run the following command:
    ```shell
    python -m pip install requirements.txt
    ```

## 2. Running the program

Once the setup process is completed, run the following command:

```shell
python manage.py runserver
```

The server should be up and running on http://127.0.0.1:8000.
