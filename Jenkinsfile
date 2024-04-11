pipeline {
    agent any

    environment {
        GIT_COMMITTER_NAME = 'Yauheni Shaludzko'
        GIT_COMMITTER_EMAIL = 'shell.marko@gmail.com'
    }

    stages {
        stage('Set Git Configuration') {
            steps {
                // Set Git configuration
                sh "git config user.name '${GIT_COMMITTER_NAME}'"
                sh "git config user.email '${GIT_COMMITTER_EMAIL}'"
            }
        }

        stage('Checkout Feature Branch') {
            steps {
                // Checkout the feature1 branch
                git branch: 'new_feature', url: 'https://github.com/yauhenishaludzko/dqe_int_HW6'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt within the virtual environment
                sh './venv/bin/python3 -m pip install -r requirements.txt'
            }
        }

        stage('Testing') {
            steps {
                // Run tests on the feature branch
                sh './venv/bin/python3 -m pytest tests/test_cases.py'
            }
        }

        stage('Merge into Main') {
            steps {
                // Switch to the main branch
                sh 'git checkout main'
                // Merge feature branch into main
                sh 'git merge new_feature'
            }
        }
    }
}