# 🚀 Enterprise MLOps Pipeline

> **Production-grade MLOps infrastructure demonstrating end-to-end ML system engineering, automation, and cloud-native deployment patterns**

[![MLOps](https://img.shields.io/badge/MLOps-Production%20Ready-blue.svg)](https://github.com/MANJESH-ctrl/MLOPS)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions)](https://github.com/MANJESH-ctrl/MLOPS/actions)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://hub.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5?logo=kubernetes)](https://kubernetes.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud%20Native-FF9900?logo=amazon-aws)](https://aws.amazon.com/)
[![DVC](https://img.shields.io/badge/DVC-Data%20Versioning-13ADC7?logo=dvc)](https://dvc.org/)

---

## 🎯 What This Project Demonstrates

This repository showcases **production-ready MLOps engineering practices**, not just another ML model. The focus is on building robust, scalable, and maintainable ML systems using industry-standard DevOps and MLOps tools.

**This is MLOps as it should be done in production:**
- Automated CI/CD pipelines with zero-touch deployments
- Reproducible experiments and data lineage tracking
- Container orchestration at scale with Kubernetes
- Cloud-native architecture on AWS
- Infrastructure as Code principles
- Comprehensive experiment tracking and model versioning

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         DEVELOPMENT LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│  DVC Pipeline    │    MLflow Tracking    │    DagsHub Remote   │
│  Data Versioning │    Experiment Logs    │    Collaboration    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         CI/CD LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│         GitHub Actions → Automated Testing & Building            │
│         - Pipeline Validation    - Docker Image Creation         │
│         - Code Quality Checks    - ECR Push                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CONTAINERIZATION LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│  Docker          │    Amazon ECR          │    Image Registry   │
│  Multi-stage     │    Private Registry    │    Version Control  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  Kubernetes (EKS) │  Auto-scaling  │  Load Balancing  │ Health  │
│  Pod Management   │  Self-healing  │  Service Mesh    │ Checks  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         CLOUD INFRASTRUCTURE                     │
├─────────────────────────────────────────────────────────────────┤
│  AWS S3          │    AWS EC2            │    AWS EKS           │
│  Data Lake       │    Compute Resources  │    Managed K8s       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ MLOps Tech Stack

### **Version Control & Collaboration**
- **Git**: Source code version control
- **DVC (Data Version Control)**: Large file and dataset versioning
- **DagsHub**: Collaborative ML experiment tracking and data management

### **CI/CD & Automation**
- **GitHub Actions**: Automated pipeline execution, testing, and deployment
- **Makefile**: Reproducible command automation and workflow standardization

### **Containerization & Orchestration**
- **Docker**: Application containerization with multi-stage builds
- **Kubernetes**: Production-grade container orchestration
- **Amazon EKS**: Managed Kubernetes service for high availability
- **Amazon ECR**: Private Docker container registry

### **Cloud Infrastructure (AWS)**
- **S3**: Scalable object storage for datasets, models, and artifacts
- **EC2**: Compute instances for training and inference
- **EKS**: Managed Kubernetes for production deployments
- **ECR**: Container image management and versioning

### **Experiment Tracking & Model Management**
- **MLflow**: Centralized experiment tracking, model registry, and metadata management
- **DVC Pipelines**: Reproducible ML pipelines with dependency tracking
- **params.yaml**: Centralized parameter management

### **Testing & Quality**
- **pytest**: Automated unit and integration testing
- **tox**: Testing automation across multiple environments

---

## 🔥 Key MLOps Features

### 1. **Automated CI/CD Pipeline**
Every code push triggers a fully automated pipeline:
- ✅ Automated testing and validation
- ✅ Docker image building with optimization
- ✅ Push to Amazon ECR
- ✅ Kubernetes deployment to EKS
- ✅ Zero-downtime rolling updates

### 2. **Data Versioning & Lineage**
- Complete data and model versioning with DVC
- Reproducible pipelines from any historical point
- S3-backed remote storage for team collaboration
- Automated artifact tracking and caching

### 3. **Experiment Tracking at Scale**
- MLflow integration for comprehensive experiment logging
- Centralized model registry with versioning
- Parameter comparison across experiments
- DagsHub for team collaboration and visualization

### 4. **Cloud-Native Architecture**
- **Containerized deployment**: Consistent environments from dev to prod
- **Kubernetes orchestration**: Auto-scaling, self-healing, and load balancing
- **AWS-native services**: Leveraging managed services for reliability
- **Infrastructure as Code**: Reproducible infrastructure deployments

### 5. **Production-Ready Design**
- Multi-stage Docker builds for optimized images
- Health checks and readiness probes
- Horizontal pod autoscaling
- Centralized logging and monitoring hooks
- Graceful shutdown handling

---

## 📁 Project Structure

```
MLOPS/
├── .github/workflows/       # CI/CD automation with GitHub Actions
│   └── *.yml               # Pipeline definitions for testing, building, deploying
├── .dvc/                   # DVC configuration and cache
├── src/                    # Source code (modular, production-ready)
│   ├── data/              # Data ingestion and processing modules
│   ├── features/          # Feature engineering pipelines
│   ├── models/            # Model training and evaluation logic
│   └── visualization/     # Reporting and visualization utilities
├── flask_app/             # REST API service for model serving
├── Scripts/               # Automation and deployment scripts
├── tests/                 # Comprehensive test suite
├── dvc.yaml               # DVC pipeline definition
├── dvc.lock               # Pipeline state and reproducibility
├── params.yaml            # Centralized hyperparameter configuration
├── dockerfile             # Multi-stage containerization
├── deployment.yaml        # Kubernetes deployment manifests
├── Makefile               # Command automation and workflow
└── requirements.txt       # Python dependencies with pinned versions
```

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required tools
- Docker >= 20.10
- kubectl >= 1.24
- AWS CLI >= 2.0
- Python >= 3.8
- DVC >= 2.0
```

### 1. Clone & Setup
```bash
git clone https://github.com/MANJESH-ctrl/MLOPS.git
cd MLOPS

# Install dependencies
pip install -r requirements.txt

# Initialize DVC
dvc pull  # Pull data from remote storage
```

### 2. Run DVC Pipeline Locally
```bash
# Execute the entire ML pipeline
dvc repro

# Or use Makefile commands
make train
make evaluate
```

### 3. Build & Run with Docker
```bash
# Build the Docker image
docker build -t mlops-app:latest .

# Run locally
docker run -p 5000:5000 mlops-app:latest
```

### 4. Deploy to Kubernetes
```bash
# Configure kubectl for EKS
aws eks update-kubeconfig --region us-east-1 --name mlops-cluster

# Deploy to Kubernetes
kubectl apply -f deployment.yaml

# Check deployment status
kubectl get pods
kubectl get services
```

---

## 🔄 CI/CD Pipeline Flow

```
┌──────────────┐
│  Git Push    │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│  GitHub Actions Triggered    │
│  - Lint & Test               │
│  - Build Docker Image        │
│  - Push to ECR               │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Kubernetes Deployment       │
│  - Pull image from ECR       │
│  - Rolling update            │
│  - Health checks             │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Production Service          │
│  - Auto-scaling enabled      │
│  - Load balanced             │
│  - Monitored                 │
└──────────────────────────────┘
```

---

## 📊 DVC Pipeline

The project uses DVC to create reproducible ML pipelines:

```yaml
# dvc.yaml structure
stages:
  data_ingestion:
    cmd: python src/data/make_dataset.py
    deps:
      - src/data/make_dataset.py
    outs:
      - data/raw

  feature_engineering:
    cmd: python src/features/build_features.py
    deps:
      - src/features/build_features.py
      - data/raw
    outs:
      - data/processed

  train:
    cmd: python src/models/train_model.py
    deps:
      - src/models/train_model.py
      - data/processed
    params:
      - train
    outs:
      - models/model.pkl
    metrics:
      - reports/metrics.json

  evaluate:
    cmd: python src/models/evaluate_model.py
    deps:
      - src/models/evaluate_model.py
      - models/model.pkl
    outs:
      - reports/evaluation.json
```

**Key Benefits:**
- 🔄 Automatic caching and incremental execution
- 📊 Parameter tracking across experiments
- 🔗 End-to-end pipeline reproducibility
- 🤝 Team collaboration with shared remote storage

---

## ☁️ AWS Infrastructure

### **S3 Buckets**
- `mlops-data-lake`: Raw and processed datasets
- `mlops-models`: Trained models and artifacts
- `mlops-dvc-remote`: DVC remote storage

### **EC2 Configuration**
- Instance Type: Optimized for ML workloads (e.g., ml.c5.xlarge)
- Auto Scaling Groups for dynamic capacity
- Spot instances for cost optimization during training

### **EKS Cluster**
- Managed Kubernetes with version 1.24+
- Multi-AZ deployment for high availability
- Node groups with auto-scaling
- IAM roles for service accounts (IRSA)

### **ECR Registry**
- Private repository: `mlops-app`
- Image scanning enabled for security
- Lifecycle policies for image management

---

## 🔐 Security & Best Practices

- ✅ **No secrets in code**: All credentials via environment variables or AWS Secrets Manager
- ✅ **IAM role-based access**: Principle of least privilege
- ✅ **Container image scanning**: Automated vulnerability detection
- ✅ **Network policies**: Kubernetes network segmentation
- ✅ **Immutable infrastructure**: Infrastructure as Code with versioning

---

## 📈 Monitoring & Observability (Ready for Integration)

The architecture is designed to integrate with:
- **CloudWatch**: Application and infrastructure metrics
- **Prometheus + Grafana**: Custom metrics and dashboards
- **ELK Stack**: Centralized logging
- **X-Ray**: Distributed tracing

---

## 🧪 Testing Strategy

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Run with coverage
pytest --cov=src tests/

# Test DVC pipeline
dvc repro --dry
```

---

## 📚 Makefile Commands

Standardized commands for common operations:

```bash
make install          # Install dependencies
make test             # Run test suite
make lint             # Code quality checks
make format           # Auto-format code
make train            # Train model locally
make docker-build     # Build Docker image
make docker-push      # Push to ECR
make k8s-deploy       # Deploy to Kubernetes
make clean            # Clean generated files
```

---

## 🎓 What You'll Learn from This Project

### **MLOps Engineering Skills**
- Building reproducible ML pipelines with DVC
- Implementing CI/CD for ML systems
- Container orchestration with Kubernetes
- Cloud infrastructure management (AWS)
- Model versioning and experiment tracking

### **Software Engineering Practices**
- Infrastructure as Code
- Automated testing and deployment
- API design for model serving
- Configuration management
- Production monitoring patterns

### **DevOps & Cloud**
- Docker multi-stage builds
- Kubernetes deployments and services
- AWS services integration (S3, EC2, EKS, ECR)
- CI/CD pipeline design
- Scalability and reliability patterns

---

## 🤝 Contributing

Contributions are welcome! This project demonstrates best practices, so please maintain:
- Code quality standards (linting, formatting)
- Comprehensive tests
- Updated documentation
- Semantic versioning for releases

---

## 🌟 Why This Project Stands Out

This isn't just another ML project with a model trained in a Jupyter notebook. This is a **production-ready MLOps system** that demonstrates:

✨ **End-to-end automation** from code commit to production deployment  
✨ **Cloud-native architecture** leveraging AWS managed services  
✨ **Reproducible research** with complete experiment and data lineage  
✨ **Production-grade infrastructure** with Kubernetes orchestration  
✨ **Team collaboration** with proper versioning and tracking  
✨ **Industry best practices** in MLOps and DevOps  

**This project shows I can build and maintain ML systems at scale, not just train models.**

---

## 📫 Connect

Built by [MANJESH](https://github.com/MANJESH-ctrl)

⭐ **Star this repo** if you find it helpful!  
🔗 **Share** to help others learn MLOps!  

---

<div align="center">

**[Documentation](docs/)** • **[Issues](https://github.com/MANJESH-ctrl/MLOPS/issues)** • **[Pull Requests](https://github.com/MANJESH-ctrl/MLOPS/pulls)**

</div>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
