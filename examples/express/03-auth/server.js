const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

const VALID_TOKEN = "my-secret-token";

function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(401).json({
      error: "Authorization header missing"
    });
  }

  const token = authHeader.replace("Bearer ", "");

  if (token !== VALID_TOKEN) {
    return res.status(401).json({
      error: "Invalid token"
    });
  }

  req.user = {
    user_id: 1,
    role: "admin"
  };

  next();
}

app.get("/api/v1/public", (req, res) => {
  res.json({
    message: "This endpoint is open to everyone."
  });
});

app.get("/api/v1/protected", authenticate, (req, res) => {
  res.json({
    message: "This endpoint is secured.",
    user_data: req.user
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});