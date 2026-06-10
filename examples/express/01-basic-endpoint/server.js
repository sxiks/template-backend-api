const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

app.get("/api/v1/health", (req, res) => {
  res.status(200).json({
    status: "success",
    message: "API is operational",
    timestamp: new Date().toISOString()
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});