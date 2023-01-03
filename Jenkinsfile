pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'e4269673-0849-4c88-9bb2-ddbad6e14c04', url: 'https://github.com/velkmr/demo.git']]])
            }
        }
        stage('Checkout'){
            steps {
                git credentialsId: 'e4269673-0849-4c88-9bb2-ddbad6e14c04', url: 'https://github.com/velkmr/demo.git'
                bat 'Python test.py'
            }
        }
    }
}
