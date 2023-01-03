pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build'){
            steps{
                sh 'python test.py'
        }
    }
}
