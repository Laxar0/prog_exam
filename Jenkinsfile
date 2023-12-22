pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('main') {
      steps {
        bat 'python main.py'
      }
    }
    stage('test_os') {
      steps {
        bat 'python test.py'
      }
    }
  }
}
