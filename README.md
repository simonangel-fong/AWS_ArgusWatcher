# ArgusWatcher

A Django Portfolio Project.

---

## V 0.0: Baseline

- [x] Create project: ArgusWatcher
- [x] Template:
  - [x] Home
- [x]Test: deploy EC2
- [x]Test: database MySQL

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
