pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
        DB_NAME = 'devOps-mini-project'
        DB_USER = 'root'
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/deepakn-0603/devOps-mini.git'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
                sh 'docker-compose --version || docker compose version'
            }
        }

        stage('Build & Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'pgadmin', 
                                                  usernameVariable: 'PGADMIN_EMAIL', 
                                                  passwordVariable: 'PGADMIN_PASSWORD')]) {
                    sh '''
                        docker compose --file $COMPOSE_FILE build
                        docker compose --file $COMPOSE_FILE down
                        docker compose --file $COMPOSE_FILE up -d --build
                    '''
                }
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
