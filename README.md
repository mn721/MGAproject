# Projekt na praktyki wykorzystujący Django REST framework oraz PostgreSQL

Poniżej znajduje się instrukcja instalacji i uruchomienia projektu.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz zainstalowane:

- Python 3.11 lub nowszy
- pip (instalator pakietów Pythona)
- Działającą instalację PostgreSQL

## Instalacja

1. Sklonuj repozytorium na swój komputer korzystając z terminala:

   - git clone https://github.com/mn721/MGAproject.git
   - cd MGAproject

2. Zainstaluj wymagane pakiety:

   - pip install -r requirements.txt


## Ustawienie bazy dancyh

1. Do uruchomienia potrzebny jest serwer PostgreSQL oraz stworzona baza danych zgodnie z ustawieniami w pliku `mga_project/settings.py`:

Zaloguj się do PostgreSQL jako użytkownik z uprawnieniami administracyjnymi

Kroki do stworzenia bazy:
   - psql -U <nazwa_uzytkownika>
   - CREATE DATABASE taskdb WITH ENCODING 'UTF8';
   - CREATE USER taskuser WITH PASSWORD 'taskpass';
   - GRANT ALL PRIVILEGES ON DATABASE taskdb TO taskuser;

## Uruchamianie projektu

1. Następnie warto zastosować migrację:

   - python manage.py migrate

2. Uruchamianie serwera developerskiego:

   - python manage.py runserver

3. Otwórz przeglądarkę i przejdź pod adres [http://127.0.0.1:8000/](http://127.0.0.1:8000/), aby zobaczyć działający projekt.

## Dostępne końcówki API

Po uruchomieniu serwera wszystkie zasoby dostępne są pod adresem `http://127.0.0.1:8000/api/`. Najważniejsze końcówki to:

- **Lista zadań:**  
  `GET /api/tasks/`

- **Szczegóły zadania:**  
  `GET /api/tasks/<id>/`

- **Tworzenie nowego zadania:**  
  `POST /api/tasks/`

- **Aktualizacja zadania:**  
  `PUT /api/tasks/<id>/`

- **Usuwanie zadania:**  
  `DELETE /api/tasks/<id>/`

- **Historia zmian zadania:**  
  `GET /api/tasks/<id>/history/`

- **Historia wszystkich zadań:**  
  `GET /api/task-history/`

- **Rejestracja użytkownika:**  
  `POST /api/register/`  