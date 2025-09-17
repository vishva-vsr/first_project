pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/vishva-vsr/first_project.git'
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t flask-backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t react-frontend ./frontend'
            }
        }

        stage('Run with Docker Compose') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished!"
        }
    }
}
