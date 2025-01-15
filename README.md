# API Task

## Overview
This project is designed to demonstrate the implementation of a simple Kitchen API. The API provides various endpoints to perform CRUD operations.

## Features
- Create, Read, Update, and Delete operations
- RESTful endpoints
- JSON-based responses

## Requirements
- Python 3.8+
- Flask
- Requests

## Installation
1. Clone the repository:
	```sh
	git clone https://github.com/kc-allan/kitchen-api.git
	```
2. Navigate to the project directory:
	```sh
	cd kitchen-api
	```
3. Create a virtual environment with venv
	```sh
	python -m venv venv
	```
4. Activate the virtual environment

	Windows
	```sh
	./venv/Scripts/activate
	```

	Linux
	```sh
	source ./venv/bin/activate
	```

5. Install the required dependencies:
	```sh
	pip install -r requirements.txt
	```

## Usage
1. Start the Flask server:
	```sh
	python -m server
	```
2. Access the API at `http://127.0.0.1:4000`

## Endpoints
- `GET /items` - Retrieve all items
- `GET /items/<id>` - Retrieve a specific item by ID
- `POST /items/create` - Create a new item
- `PUT /items/update/<id>` - Update an existing item by ID
- `DELETE /items/delete/<id>` - Delete an item by ID

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact the project maintainer at [kiruiallan401@gmail.com].
