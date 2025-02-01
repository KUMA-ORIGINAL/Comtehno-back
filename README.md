

Добро пожаловать! Следуйте инструкциям ниже, чтобы настроить и запустить приложение.


1. **Скопируйте файл конфигурации**

   Сначала скопируйте файл `.env.example` в файл `.env`. Это сделает его доступным для Docker:
   
   ```bash
   cp .env.example .env

2. **Запустите контейнеры**

   Используйте docker-compose для сборки и запуска контейнеров:

   ```bash
   docker-compose up

3. **Остановка и удаление контейнеров**

   Если вам нужно остановить и удалить контейнеры, используйте:

   ```bash
   docker-compose down
   
# Документация 
- **GET docs/**
- **GET schema/**



Tag - name, photo

Program - title, description, logo, photo, special, tag_id
StudyProgram - term_of_study,
StudyProgramItem - number, name,
StudentProject - photo, name

Resume - full_name, position, tools, skills
Tool - photo, name
Skill - name

Salary - salary, name, sub_name,

review - full_name, photo,
partner - name, photo
staff - photo, full_name, направление, about_me, achievements

news - title, photo, created_at,
event - title, photo, place, date, created_at,


FAQ - name
FAGItem - text
