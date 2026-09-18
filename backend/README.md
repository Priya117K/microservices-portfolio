# Learning Backend

Express and Mongoose backend for users, uploaded documents, and generated learning artifacts.

## Setup

```powershell
cd backend
npm install
Copy-Item .env.example .env
npm start
```

Set `MONGODB_URI` and `JWT_SECRET` in `.env` before starting the server.

## Endpoints

- `GET /api/health`
- `POST /api/auth/register` with `{ "name", "email", "password" }`
- `POST /api/auth/login` with `{ "email", "password" }`

The `Document` and `LearningArtifact` models are ready for protected document and artifact routes. Use `requireAuth` from `src/middleware/auth.js` for routes requiring a JWT.
