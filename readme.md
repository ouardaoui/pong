
## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ouardaoui/pong.git
    cd pong
    ```

2. Build and start the containers using Docker Compose:
    ```sh
    docker-compose up --build
    ```
   

### Running the Project

 ```sh
    chmod +x start.sh
    ./start.sh
```

### File Descriptions

- **[backend/Dockerfile](backend/Dockerfile)**: Dockerfile for the backend service.
- **[front/Dockerfile](front/Dockerfile)**: Dockerfile for the frontend service.
- **[server/Dockerfile](server/Dockerfile)**: Dockerfile for the server service.
- **[docker-compose.yml](docker-compose.yml)**: Docker Compose configuration file.
- **[backend/authentication/manage.py](backend/authentication/manage.py)**: Entry point for the Django backend.
- **[start.sh](start.sh)**: Script to start the entire project.
- **[front/start.sh](front/start.sh)**: Script to start the frontend.
- **[backend/start.sh](backend/start.sh)**: Script to start the backend.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
