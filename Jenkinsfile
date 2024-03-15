pipeline{
    agent any
    stages {
        stages("api_autotest"){
            steps{
                bat 'python run.py'
            }
        }
    }
}