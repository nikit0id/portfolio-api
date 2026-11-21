## 2. Описания для Settings → Description каждого репо

**compose-app-cicd**
> CI/CD для FastAPI + PostgreSQL: lint, pytest, сборка в GHCR, Trivy (fail на CRITICAL), деплой по SSH с health check и автооткатом, окружения staging/production

**monitoring-stack**
> Prometheus, Grafana, Loki и Alertmanager в Docker Compose: дашборды и правила алертов в коде (provisioning), алерты в Telegram, мониторинг SSL-сертификатов и доступности

**ansible-linux-baseline**
> Ansible-роли для Ubuntu: пользователи, SSH-hardening, ufw, fail2ban, unattended-upgrades, Docker, node_exporter; секреты в Ansible Vault, тесты Molecule, CI на каждый PR

**terraform-yc-infra**
> Terraform-модули для Yandex Cloud (VPC, ВМ с cloud-init, DNS), remote state в Object Storage с блокировкой, plan в pull request; выходные данные → Ansible inventory

**pg-backup-toolkit**
> Автоматические бэкапы PostgreSQL в S3-совместимое хранилище: ротация 7/4/3, еженедельная автоматическая проверка восстановления, systemd timer, уведомления в Telegram, метрики для Prometheus

**kubernetes-ops-lab**
> K8s-лаборатория на kind, трёхузловой k3s в плане, Helm, ArgoCD (GitOps), ingress-nginx + cert-manager, kube-prometheus-stack; диагностика ImagePullBackOff и rollback

**vpn-server-ansible**
> Ansible-роль для VPN-сервера Xray + Hysteria 2: генерация конфигов из шаблонов, systemd, ufw; развёртывание личного VPS воспроизводимым кодом

**portfolio-api**
> Базовый сервис (FastAPI + PostgreSQL) для портфолио: multi-stage Dockerfile, non-root, pytest; точка приложения для compose-app-cicd, monitoring-stack, pg-backup-toolkit и kubernetes-ops-lab

---

## 3. Порядок pinned-репозиториев (Profile → Pinned → Customize)

1. compose-app-cicd
2. monitoring-stack
3. ansible-linux-baseline
4. terraform-yc-infra
5. kubernetes-ops-lab
6. pg-backup-toolkit

(portfolio-api и vpn-server-ansible остаются видны в списке репо, но не зашиваются: они вспомогательные для истории.)

---

