pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Build') { 
            steps {
                echo "build app"
            }
        }
        stage('Test') { 
            steps {
                echo "test app"
                sh 'python --version'
            }
        }
        stage('Deploy') { 
            steps {
                echo "deploy app"
            }
        }
    }
}