pipeline{
    agent any
    
    environment{
        JobName = "柠檬班项目"
    }

    stages {
        stage("api_autotest"){
            steps{
                bat 'python run.py'
            }
        }
    }

    post {
    always {
        
        junit stdioRetention: '', testResults: 'outputs/result.xml'
        
        emailext body: 
        '''<html>
        <h1>total cases:${TEST_COUNTS,var="total"}</h1> 
        <h1>pass cases:${TEST_COUNTS,var="pass"}</h1> 
        <h1>fail cases:${TEST_COUNTS,var="fail"}</h1> 
        </html>''', 
        subject:"job ${env.JobName},result:${currentBuild.currentResult}",
        to: '1293947641@qq.com'
  }
}

}