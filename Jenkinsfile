pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t world-of-games .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 --name world-of-games world-of-games'
            }
        }
        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop world-of-games'
                sh 'docker rm world-of-games'
                sh 'docker tag world-of-games your-dockerhub-username/world-of-games:latest'
                sh 'docker push your-dockerhub-username/world-of-games:latest'
            }
        }
    }
}
