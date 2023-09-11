# ArgusWatcher

A Django Portfolio Project.

- Log for branch `ec_deploy`
  - Easy deploy django on ec2 on hold
  - TODO:
    - 1. prevent the usage of RSAKey
    - 2. environment variable should be reorganized, including django_secret
    - 2. learn CI/CD, using aws pipline
    - 3. learn the role in aws
    - 4. bash script should be modified to adapt CI/CD

---

## V 1.1.1: Deploy ArgusWatcher.net

- **Restructure files**
  
  - repo_name/
    - manage.py
    - requirements.txt
    - project_name/
      - AppShowcase/

- **environment variables**




---

## V 1.0.1: Project Showcase

- Task:
  - Connect front-end project: `tic-tac-toe` and `connect-four`.

---

## V 1.0: Django-EC2 Deployment

- Task:
  - Create a django app to deploy a Github django project on an EC2 Instance.

- Functionalities:
  - Create EC2 instance
  - List all instances
  - Retrieve instance info
  - Terminate an instance

- Tech:
  - Bash script(Ubuntu)
  - EC2 template, User data
  - boto3 SDK
  - django-environ
  - JS + JsonResponse (Refresh instance status asynchronously)
  - paramiko package: connect to an instance with ssh (For update github code after deployed)

- [x] Template:
  - [x] base
  - [x] Navbar

- [x] Create App: AppEC2
  - [x] List
  - [x] Create
  - [x] Detail
  - [x] Terminate

---

## V 0.0: Baseline

- [x] Create project: ArgusWatcher
- [x] Template:
  - [x] Home
- [x] Test: deploy EC2
- [x] Test: database MySQL

