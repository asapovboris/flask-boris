pipeline {
    environment {
     environment = "internal"
     cs_server = "192.168.1.71"
     ssh_user = "in4matic"
     ssh_port = "33322"
     cs_remote_folder = "/home/in4matic/bafi-cs"
     cs_local_folder = "/var/lib/jenkins/repos/cs_pre_build"
     branch = "develop"
   }

    agent {label 'main'}
       stage('SCM Checkout'){
           git credentialsId: 'git-creds', url: 'https://github.com/javahometech/my-app'
       }
       stage('Mvn Package'){
         def mvnHome = tool name: 'maven-3', type: 'maven'
         def mvnCMD = "${mvnHome}/bin/mvn"
         sh "${mvnCMD} clean package"
       }
       stage('Build Docker Image'){
         sh 'docker build -t kammana/my-app:2.0.0 .'
       }
       stage('Push Docker Image'){
         withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
            sh "docker login -u kammana -p ${dockerHubPwd}"
         }
         sh 'docker push kammana/my-app:2.0.0'
       }
       stage('Run Container on Dev Server'){
         def dockerRun = 'docker run -p 8080:8080 -d --name my-app kammana/my-app:2.0.0'
         sshagent(['dev-server']) {
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.31.18.198 ${dockerRun}"
         }
       }
    }
}