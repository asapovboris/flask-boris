pipeline {
    environment {
     image_name = "api-python:0.1"
     cs_local_folder = "/var/lib/jenkins/tests/restapi/api-python"
     branch = "master"
   }

    agent {label 'main'}
       stages {
        stage('changing branch') {
            steps {
                dir("${cs_local_folder}") {
                    git branch: "${branch}", url: 'https://github.com/asapovboris/flask-boris.git'
                }
            }
        }

        stage('copy init file'){
            steps {
                sh 'cp -v /var/lib/jenkins/tests/restapi/__init__.py "${cs_local_folder}"/'
            }
        }

        stage('build docker image'){
            steps {
                dir("${cs_local_folder}") {
                    sh 'docker build -t "${image_name}" .'
                }
            }
        }

        stage('docker run'){
            steps {
                sh 'docker-compose -f /var/lib/jenkins/tests/restapi/docker-compose.yml up -d'
            }
        }

      }
}
