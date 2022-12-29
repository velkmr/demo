pipeline {
    agent {
		  dockerfile {
			dir 'scripts'
			filename 'Dockerfile'
			label 'docker'
		   }
			}

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'e4269673-0849-4c88-9bb2-ddbad6e14c04', url: 'https://github.com/velkmr/demo.git']]])
            }
        }
        stage('Build'){
            steps{
                git branch:'master',credentialsId: 'e4269673-0849-4c88-9bb2-ddbad6e14c04', url: 'https://github.com/velkmr/demo.git'
                script {
						  sh """
						  
						  /usr/bin/python3 test.py
						  """
						  }
            }
        }
    }
}
