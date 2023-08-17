JWT Utility

This repository contains a Python utility that allows you to generate and validate JSON Web Tokens (JWT) with a customizable payload.

Files:

1. `secret.txt`: This text file contains the secret key used for signing the JWTs. The utility reads the secret key from this file. Keep this file secure and do not share it with others.

2. `jwt_utility.py`: This Python script provides functions to generate and validate JWTs. It uses the secret key from `secret.txt` to sign and verify the tokens.

3. `Dockerfile`: This file contains instructions to build a Docker image for the JWT utility.

4. `Makefile`: This file provides the necessary targets to build and run the application using Docker.

5. `docker-compose.yml`: This file defines the Docker services and their configuration.

Dependencies:

The utility requires the PyJWT library for JWT encoding and decoding. To install the required dependencies, run the following command in your terminal or command prompt:
`pip install pyjwt`

Make sure you have Python and `pip` installed on your system before running the above command. If you don't have `pip` installed, you can install it by following the instructions for your operating system: https://pip.pypa.io/en/stable/installing/

Docker Setup:

The JWT utility can be run inside a Docker container. To set up the Docker environment for the JWT utility, follow these steps:

1. Install Docker:
   If you don't have Docker installed, download and install it for your operating system from the official Docker website: https://www.docker.com/get-started

2. Build the Docker Image:
   Open a terminal or command prompt.
   Navigate to the root directory of your project (where the `Dockerfile` is located).
   Run the following command to build the Docker image:
   `docker build -t jwt_utility .`

3. Run the JWT Utility in a Docker Container:
   After building the Docker image, you can run the JWT utility inside a Docker container. Run the following command:
   `docker run --rm -v "$(pwd)/secret.txt:/app/secret.txt" jwt_utility`

   The JWT utility will be executed inside the Docker container, and the output will be displayed in the terminal.

Docker Compose:

Alternatively, you can use `docker-compose` to manage the Docker setup for the JWT utility. The `docker-compose.yml` file defines the Docker services and their configuration.

To use `docker-compose`:

1. Install Docker Compose:
   If you don't have Docker Compose installed, download and install it for your operating system by following the official documentation: https://docs.docker.com/compose/install/

2. Build and Run with Docker Compose:
   Open a terminal or command prompt.
   Navigate to the root directory of your project (where the `docker-compose.yml` file is located).
   Run the following command to build and run the Docker containers:
   `docker-compose up --build`

   The JWT utility will be executed inside the Docker container, and the output will be displayed in the terminal.

Usage:

1. Set the Secret Key:
   - Open the `secret.txt` file using a text editor.
   - Add your secret key as a single line of text in the file.
   - Keep this file secure and do not share it with others, as it contains the secret key used for signing the JWTs.

2. Customize the Payload Data (Optional):
   - If you want to generate a JWT with custom input data, open the `jwt_utility.py` file in a text editor.
   - Locate the line that says `input_data = 'example data'`.
   - Replace `'example data'` with your desired input data enclosed in single quotes.

3. Generate a JWT:
   - To generate a JWT, you have two options:
     - Without Docker: Open a terminal or command prompt, navigate to the root directory of your project, and run the following command:
       `python jwt_utility.py`

       The script will generate a JWT based on the input data (if customized) and the secret key from `secret.txt`. It will then print the generated JWT in the console output.

     - With Docker: Follow the steps under the "Docker Setup" section to build the Docker image and run the JWT utility inside a Docker container.

4. Validate a JWT (Optional):
   - The utility code includes a `validate_jwt` function to validate a JWT.
   - If you have a JWT that you want to validate, follow these steps:
     1. Open the `jwt_utility.py` file in a text editor.
     2. After the line `# Usage example`, you can add code to validate a JWT.
     3. Replace `<your JWT>` in the line `jwt_token = '<your JWT>'` with the actual JWT you want to validate.
     4. Save the changes to `jwt_utility.py`.
     5. Run the JWT utility using either the `python jwt_utility.py` command (without Docker) or the Docker container (with Docker). The script will print whether the JWT is valid or invalid in the console output.

Security Note:

Keep the `secret.txt` file containing the secret key secure and do not share it with others.
