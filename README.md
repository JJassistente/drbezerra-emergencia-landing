# Dr. Bezerra — Landing Page

Landing page estática (single-file, sem backend) de atendimento domiciliar do Dr. Bezerra,
clínico geral em Campina Grande/PB. Servida via nginx dentro de um container.

## Deploy na VPS (Traefik compartilhado)

1. Copie `.env.example` para `.env` (o domínio já vem preenchido:
   `drbezerraemergencia.jjassistentebot.tech`, um subdomínio de `jjassistentebot.tech`).
2. Suba o container:
   ```bash
   docker compose -f docker-compose.yml -f docker-compose.prod-traefik.yml up -d --build
   ```
3. Acesse `https://drbezerraemergencia.jjassistentebot.tech`.

### Atualizações futuras

```bash
git pull
docker compose -f docker-compose.yml -f docker-compose.prod-traefik.yml up -d --build
```

Como é conteúdo estático puro (um `index.html`), qualquer atualização é só um rebuild da imagem —
não há migration, seed nem variável de ambiente sensível envolvida.
