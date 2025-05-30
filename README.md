# Infra-Assessment-OCS

Infra-Assessment-OCS è una soluzione containerizzata per generare automaticamente report formali di assessment infrastrutturale IT basati sui dati raccolti da un server OCS Inventory NG.

## Componenti

- OCS Inventory NG (MySQL DB e Server esistenti)
- Ollama AI container per generazione linguaggio naturale
- Report Worker Python per estrazione dati e generazione report Word
- Web UI Flask con login e log attività

## Avvio

```bash
docker-compose up -d
```

Accesso Web UI: `http://localhost:5001`  
Utente default: admin / changeme

## Personalizzazione

Modifica `.env` per cambiare credenziali e configurazioni DB e UI.

## Requisiti

- Docker e Docker Compose installati
- OCS Inventory NG attivo e accessibile
- Porta 5001 aperta per la UI

## Licenza

MIT License
