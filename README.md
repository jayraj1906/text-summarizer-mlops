
# 🧠 Text Summarizer MLOps Project

An end-to-end, production-ready **Text Summarization** system powered by modern MLOps practices. This project leverages a modular architecture with configurable pipelines, version control, and seamless deployment using Docker, GitHub Actions, and AWS (EC2 + ECR).

---

## 🚀 Features

* 🏗 Modular component-based design
* ⚙️ Configurable training/inference pipelines
* 🧪 Notebook-based research (`research/research.ipynb`)
* 🐳 Dockerized for production
* 🔁 CI/CD with GitHub Actions
* ☁️ AWS Deployment (EC2 + ECR)
* ⚡ FastAPI web interface for inference

---

## 🧾 Project Structure

```
text-summarizer-mlops/
├── .github/
│   └── workflows/
│       └── .gitkeep
├── config/
│   └── config.yaml
├── params.yaml
├── app.py                 # FastAPI app for inference
├── main.py                # Pipeline runner script
├── Dockerfile             # Docker setup
├── requirements.txt       # Project dependencies
├── setup.py               # Package metadata
├── research/
│   └── research.ipynb     # Prototyping and exploration
├── src/
│   └── text_summarizer/
│       ├── __init__.py
│       ├── components/    # Modular ML pipeline components
│       │   └── __init__.py
│       ├── utils/
│       │   ├── __init__.py
│       │   └── common.py
│       ├── logging/
│       │   └── __init__.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── pipeline/
│       │   └── __init__.py
│       ├── entity/
│       │   └── __init__.py
│       └── constants/
│           └── __init__.py
```

---

## 🛠️ Getting Started

### 📥 Clone the Repository

```bash
git clone https://github.com/jayraj1906/text-summarizer-mlops.git
cd text-summarizer-mlops
```

### 🧪 Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Unix/macOS
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Application

```bash
python app.py
```

Then open your browser:

```
http://127.0.0.1:8000
```

---

## ⚙️ MLOps Pipeline Steps

1. Configure `config.yaml` and `params.yaml`
2. Define schemas and entities in `src/text_summarizer/entity/`
3. Configure logic via `src/text_summarizer/config/configuration.py`
4. Build components inside `src/text_summarizer/components/`
5. Define and manage the pipeline via `src/text_summarizer/pipeline/`
6. Run everything with `main.py`
7. Serve inference via `app.py`

---

## 🐳 Docker & CI/CD with AWS

### ✅ IAM Policy Requirements

* `AmazonEC2ContainerRegistryFullAccess`
* `AmazonEC2FullAccess`

### 📌 GitHub Secrets

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME=text-summarizer-mlops
```

### 🔄 Deployment Flow

1. **Build Docker Image**
2. **Push to ECR**
3. **Launch EC2 Instance (Ubuntu)**
4. **Install Docker on EC2**
5. **Pull Image & Run Container**

Use GitHub Actions + EC2 self-hosted runner for continuous deployment.

---

## ✍️ Author

**Jayraj Chaudhary**
*Designation*: AI/ML Engineer
📧 [jayrajchaudhary02@gmail.com](mailto:jayrajchaudhary02@gmail.com)

---

