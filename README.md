# 📌 Project Management Lite (Backend with Django REST Framework)

## 📖 Overview
Project Management Lite is a simplified project management system built using **Django** and **Django REST Framework (DRF)**.  
It allows users to create projects, assign tasks, collaborate with team members, and track progress through a RESTful API.

---

## 🚀 Features
- **User Authentication & Authorization**
  - Django’s built-in `User` model
  - Token-based authentication (DRF)
- **Project Management**
  - Create and manage projects
  - Add members with different roles (Owner / Member)
- **Task Tracking**
  - Tasks linked to projects
  - Status (`TODO`, `DOING`, `DONE`)
  - Priority (`LOW`, `MED`, `HIGH`)
  - Assign tasks to users
- **Comments**
  - Add comments to tasks
  - Track discussions
- **Filtering & Searching**
  - Filter tasks by status, due date, priority
  - Search tasks by title or description
  - Order results by priority or due date

---

## 🗂️ Data Models
- **User** → Django’s built-in User model
- **Project**
  - `name`, `description`, `owner`, `created_at`
- **ProjectMember**
  - `project`, `user`, `role (OWNER/MEMBER)`
- **Task**
  - `project`, `title`, `description`, `status`, `priority`, `due_date`, `assignee`, `created_by`, `created_at`, `updated_at`
- **Comment**
  - `task`, `author`, `text`, `created_at`

---

## 🔑 API Endpoints (Core Examples)

### Authentication
- `POST /api/token/` → Obtain auth token
- `POST /api/token/refresh/` → Refresh token

### Projects
- `GET /api/projects/` → List all projects
- `POST /api/projects/` → Create new project
- `GET /api/projects/{id}/` → Retrieve project details
- `PUT /api/projects/{id}/` → Update project
- `DELETE /api/projects/{id}/` → Delete project

### Tasks
- `GET /api/tasks/` → List tasks (filterable & searchable)
- `POST /api/tasks/` → Create a task
- `GET /api/tasks/{id}/` → Retrieve task
- `PUT /api/tasks/{id}/` → Update task
- `DELETE /api/tasks/{id}/` → Delete task

### Comments
- `GET /api/comments/` → List all comments
- `POST /api/comments/` → Add comment
- `GET /api/comments/{id}/` → Retrieve comment
- `DELETE /api/comments/{id}/` → Delete comment

---

