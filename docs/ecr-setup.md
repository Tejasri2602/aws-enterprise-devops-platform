
# Amazon ECR Setup

## Create Repository

```bash
aws ecr create-repository \
--repository-name enterprise-devops-platform
```

## Authenticate Docker

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

## Build Image

```bash
docker build -t enterprise-devops-platform .
```

## Tag Image

```bash
docker tag enterprise-devops-platform:latest \
ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/enterprise-devops-platform:latest
```

## Push Image

```bash
docker push \
ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/enterprise-devops-platform:latest
```
