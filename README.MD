# Nowatorski Projekt Indywidualny 51719

## Opis

Projekt przedstawia proste API stworzone w FastAPI z bazą danych PostgreSQL,
uruchamiane w kontenerach Docker przy użyciu docker-compose.

Repozytorium zawiera pipeline CI/CD oparty o GitHub Actions z reusable workflow
oraz osobnymi pipeline’ami dla main i pull requestów.

## Technologie

- Python / FastAPI
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions

## Uruchomienie lokalne

```bash
docker compose up --build
```

Po uruchomieniu wpisujemy w przeglądarkę : http://localhost:8000
