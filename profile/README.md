# Никита Никитин

Занимаюсь Linux и автоматизацией эксплуатации. В этом портфолио один сервис задач на FastAPI и PostgreSQL проходит путь от Docker Compose до Kubernetes. Для каждого этапа есть код, команда запуска и проверка результата в GitHub Actions.

**Стек** — Python, Bash, PostgreSQL, Docker Compose, Ansible, Terraform, Prometheus, Grafana, Helm и Argo CD.

| Проект | Что можно проверить | CI |
|---|---|---|
| [portfolio-api](https://github.com/nikit0id/portfolio-api) | Создание задачи, запись в PostgreSQL, готовность API | [Проверки закреплённой версии](https://github.com/nikit0id/compose-app-cicd/actions/workflows/ci.yml) |
| [compose-app-cicd](https://github.com/nikit0id/compose-app-cicd) | Публикация в GHCR, сканирование образа и пробный релиз по SSH | [![CI доставки](https://github.com/nikit0id/compose-app-cicd/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/compose-app-cicd/actions/workflows/ci.yml) |
| [ansible-linux-baseline](https://github.com/nikit0id/ansible-linux-baseline) | Семь ролей Ubuntu, повторный converge и проверка работающих служб | [![CI Ubuntu](https://github.com/nikit0id/ansible-linux-baseline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/ansible-linux-baseline/actions/workflows/ci.yml) |
| [vpn-server-ansible](https://github.com/nikit0id/vpn-server-ansible) | Передача файла через Xray и Hysteria 2 на временной ВМ | [![CI VPN](https://github.com/nikit0id/vpn-server-ansible/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/vpn-server-ansible/actions/workflows/ci.yml) |
| [terraform-yc-infra](https://github.com/nikit0id/terraform-yc-infra) | VPC, ВМ, DNS, генерация inventory и четыре офлайн-плана | [![CI Terraform](https://github.com/nikit0id/terraform-yc-infra/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/terraform-yc-infra/actions/workflows/ci.yml) |
| [monitoring-stack](https://github.com/nikit0id/monitoring-stack) | Дашборд Grafana и доставка HostDown после остановки экспортера | [![CI мониторинга](https://github.com/nikit0id/monitoring-stack/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/monitoring-stack/actions/workflows/ci.yml) |
| [pg-backup-toolkit](https://github.com/nikit0id/pg-backup-toolkit) | Бэкап в MinIO и восстановление задач с проверкой SHA-256 и числа строк | [![CI восстановления](https://github.com/nikit0id/pg-backup-toolkit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/nikit0id/pg-backup-toolkit/actions/workflows/ci.yml) |
| [kubernetes-ops-lab](https://github.com/nikit0id/kubernetes-ops-lab) | StatefulSet PostgreSQL, HPA, TLS и доставка через Argo CD | [![CI Kubernetes](https://github.com/nikit0id/kubernetes-ops-lab/actions/workflows/portfolio.yml/badge.svg?branch=main)](https://github.com/nikit0id/kubernetes-ops-lab/actions/workflows/portfolio.yml) |
