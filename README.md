
# AWS Enterprise DevOps Platform

## Project Overview

This project demonstrates a production-grade AWS DevOps platform built using:

- AWS
- Terraform
- Docker
- Kubernetes (EKS)
- Jenkins
- GitHub Actions
- Helm
- Prometheus
- Grafana
- Python

## Architecture

## Features

- Infrastructure as Code
- Continuous Integration
- Continuous Deployment
- Containerization
- Kubernetes Orchestration
- Monitoring & Alerting
- Automation

## Status

Phase 1 Completed
## Terraform Infrastructure

Current Infrastructure:

- VPC
- Internet Gateway
- Public Subnets
- Terraform Variables
- Terraform Outputs

Upcoming:

- NAT Gateway
- Private Subnets
- ECR
- EKS
- IAM Roles


## Application

Containerized Flask application.

### Endpoints

GET /

GET /health

### Container Platform

- Docker
- Amazon ECR


## CI/CD Pipeline

Implemented using GitHub Actions.

Pipeline Stages:

- Source Checkout
- Dependency Installation
- Docker Build
- AWS Authentication
- ECR Push

Deployment Target:

- Amazon ECR
- Amazon EKS (Upcoming)
## Jenkins CI/CD

Implemented using Jenkins Declarative Pipeline.

Pipeline Stages:

- Checkout
- Build
- Validation
- Deployment Preparation
 
## Kubernetes Deployment

Components:

- Namespace
- Deployment
- Service
- Ingress

## Helm

Implemented reusable Helm chart for application deployment.

Features:

- Configurable replicas
- Configurable image versions
- Configurable services

## Monitoring & Observability

Tools:

- Prometheus
- Grafana

Features:

- Metrics Collection
- Dashboard Visualization
- Service Monitoring
- Kubernetes Monitoring
