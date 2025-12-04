pipeline 
{
    agent any
    stages 
    {
        stage('Docker Build Image') 
        {
            steps 
            {
                echo "Docker Image Building"
                bat "docker build -t exampyapp:v1 ."
            }
        }
        stage('Docker push image to Docker Hub')
        {
            steps{
                echo 'push images to docker hub'
                bat 'docker tag exampyapp:v1 siri2409/exampy:v1'
                bat 'docker push siri2409/exampy:v1'
            }
        }
        stage('Containerize and Run') 
        {
            steps 
            {
                echo "Containerize and Run"
                bat "docker pull siri2409/exampy:v1"
                bat "docker run -d -p 5000:5000 siri2409/exampy:v1"
            }
        }
    }
    post 
    {
        success 
        {
            echo 'Succesfull Pipeline executed!'
        }
        failure 
        {
            echo 'Failure of pipeline'
        }
    }
}
