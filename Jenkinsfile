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

        stage('Build') {
            steps {
                sh 'docker-compose -f $COMPOSE_FILE build'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down
                    docker compose up -d --build
                '''
            }
        }

    }

    post {
        success {
            echo 'Deployment successfull'
        }
        failure {
            echo 'Build failed'
        }
    }
}