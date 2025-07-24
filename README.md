# 🚀 Cloud-Native URL Shortener

A full-stack URL Shortener service built using **FastAPI**, **PostgreSQL**, and **Redis**, fully containerized with **Docker** and orchestrated using **Kubernetes (Minikube)**. The project is productionized with **Helm** charts and monitored using **Prometheus** and **Grafana**.

---

## 📦 Features

- Shorten and redirect URLs with custom slugs
- FastAPI-based RESTful API
- PostgreSQL for persistent storage
- Redis for caching
- Dockerized services for local development
- Kubernetes deployment using `kubectl` and `helm`
- Observability using Prometheus + Grafana
- Minikube for local cluster
- CI/CD ready structure

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Cache:** Redis (Optional)
- **Containerization:** Docker
- **Orchestration:** Kubernetes + Helm
- **Monitoring:** Prometheus + Grafana
- **Platform:** Minikube

---

## 📁 Project Structure


---

## ⚙️ Setup Instructions

### 1. 🚀 Clone the Repo

```bash
git clone https://github.com/your-username/url-shortener-k8s.git
cd url-shortener-k8s
docker build -t shortener-app .
docker run -d -p 8000:8000 --name shortener-app shortener-app
minikube start
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/shortener-deployment.yaml
kubectl apply -f k8s/shortener-service.yaml
minikube service shortener-service
kubectl apply -f k8s/prometheus/prometheus-config.yaml
kubectl apply -f k8s/prometheus/prometheus-deployment.yaml
kubectl port-forward deployment/prometheus-deployment 9090:9090
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install grafana grafana/grafana \
  --set adminPassword=admin \
  --set service.type=NodePort
kubectl get svc grafana
minikube service grafana
cd helm/shortener-chart
helm install shortener ./
