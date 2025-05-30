# Infra-Assessment-OCS

Infra-Assessment-OCS è una soluzione containerizzata per generare automaticamente report formali di assessment infrastrutturale IT basati sui dati raccolti da un server OCS Inventory NG.  
La soluzione integra:

- Accesso diretto al database MySQL di OCS Inventory NG per estrarre inventario e dati infrastrutturali
- Utilizzo di Ollama AI (modello Mistral) per generare analisi e raccomandazioni in linguaggio naturale
- Web UI con autenticazione per generare, visualizzare e scaricare report in formato `.docx`
- Storicizzazione delle richieste di report con log e gestione utenti base
- Docker Compose per facilitare l’installazione e gestione di tutti i servizi

## Architettura

- `ocsinventory-server` e `ocsinventory-db` (esistenti)
- `ollama` (container AI locale)
- `report-worker` (estrae dati e genera report Word)
- `web-ui` (Flask app per UI e autenticazione)

## Come usare

1. Clona il repository
2. Configura `.env` con credenziali OCS e utente web
3. Avvia con `docker-compose up -d`
4. Accedi a `http://localhost:5001` (default admin/changeme)
5. Genera e scarica report

## Requisiti

- Docker e Docker Compose
- OCS Inventory NG funzionante
- Connessione tra stack tramite rete Docker `localocs`
- Ollama AI image (preinstallata o scaricata al primo avvio)

---

## Estensioni future

- Output PDF
- Report multipli e schedulazione automatica
- Integrazione con altri sistemi CMDB o CM Tools

---

### License

MIT License
