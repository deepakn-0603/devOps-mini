pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/deepakn-0603/devOps-mini.git'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Build') {
            steps {
                bat "docker compose -f %COMPOSE_FILE% build"
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    docker compose down
                    docker compose up -d --build
                """
            }
        }

    }

    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Build failed'
        }
    }
}