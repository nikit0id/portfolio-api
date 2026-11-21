# Никита Никитин — DevOps

DevOps-инженер. 2,5 года был единственным специалистом по IT-инфраструктуре в транспортной логистической компании: 10+ серверов Linux/Windows, CI/CD, PostgreSQL/MS SQL с бэкапами и DR, мониторинг, DNS/VPN.

**Стек:** Docker · Kubernetes (k3s, Helm, ArgoCD, GitOps) · GitHub Actions · Terraform (Yandex Cloud) · Ansible · Prometheus / Grafana / Loki · Python · Bash

**Проекты** — не учебные, а рабочие практики, переупакованные в код (CI, тесты, IaC):

| Проект | Что это |
|---|---|
| [compose-app-cicd](https://github.com/nikit0id/compose-app-cicd) | Полный CI/CD: тесты → сборка в GHCR → Trivy → деплой по SSH с health check и автооткатом |
| [monitoring-stack](https://github.com/nikit0id/monitoring-stack) | Prometheus + Grafana + Loki + Alertmanager: дашборды и алерты в коде, уведомления в Telegram |
| [ansible-linux-baseline](https://github.com/nikit0id/ansible-linux-baseline) | Ansible-роли для Ubuntu (SSH-hardening, ufw, fail2ban, node_exporter), тесты Molecule |
| [terraform-yc-infra](https://github.com/nikit0id/terraform-yc-infra) | Terraform-модули для Yandex Cloud: VPC, ВМ, DNS, remote state, plan в PR |
| [pg-backup-toolkit](https://github.com/nikit0id/pg-backup-toolkit) | Бэкапы PostgreSQL с ротацией и **автоматической проверкой восстановления** |
| [kubernetes-ops-lab](https://github.com/nikit0id/kubernetes-ops-lab) | K8s-лаба на kind (k3s в плане): Helm, ArgoCD (GitOps), ingress-nginx + cert-manager, kube-prometheus-stack; диагностика ImagePullBackOff и rollback |

Контакты: Telegram [@Helchion](https://t.me/Helchion) · nikitoid709@gmail.com

Английский: чтение документации, B1+.
