# World of Games

## Description
World of Games is a Python-based application that offers three exciting games:
1. **Memory Game** - Test your memory by recalling a sequence of numbers.
2. **Guess Game** - Guess the number generated by the computer.
3. **Currency Roulette** - Estimate the value of a random USD amount in ILS.

The application is deployed using Docker and managed with Jenkins pipelines for CI/CD.

---

## Prerequisites
- Python 3.9+
- Docker
- Docker Compose
- Jenkins
- ChromeDriver (for Selenium)

---

## Setup Instructions

### Local Setup
1. Clone the repository:
  ```bash
    git clone https://github.com/your-username/world-of-games.git
    cd world-of-games
 ```
2. Install dependencies:
 ```bash
 pip install -r requirements.txt
 ```
3. Run the application:
```bash
 python app.py
 	```

### Docker Setup
1. Build the Docker image:
  ```bash
  docker build -t world-of-games .
  ```
2. Run the container:
  ```bash
 docker run -d -p 8777:8777 --name world-of-games world-of-games
  ```
Access the application at http://localhost:8777.

## Testing
### To test the application:

- Ensure the app is running.
- Run the e2e.py script:

```bash
python e2e.py
```

## Jenkins Pipeline
### To automate deployment and testing:

1.  Add the provided Jenkinsfile to your repository.
2.  Configure your Jenkins project with the Git repository.
3.  Trigger a build to execute the pipeline.

## File Structure

```bash
world-of-games/
├── app.py                # Main Flask application
├── games/
│   ├── memory_game.py    # Memory Game logic
│   ├── guess_game.py     # Guess Game logic
│   ├── currency_roulette_game.py # Currency Roulette logic
├── e2e.py                # End-to-end testing
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose file
├── Jenkinsfile           # Jenkins pipeline
├── Scores.txt            # Score storage
└── README.md             # Project documentation
```
## Future Improvements
- Add a leaderboard feature.
- Enhance user interface with a web framework like React.
- Add more games to the platform.

## Author
Created by [Batel Yerushalmi](http://https://www.linkedin.com/in/batel-yerushalmi/ "Batel Yerushalmi") Feedback is welcome!
