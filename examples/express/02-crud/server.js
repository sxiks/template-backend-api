const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

let students = [];
let nextId = 1;

app.post("/api/v1/students", (req, res) => {
  const student = {
    id: nextId++,
    first_name: req.body.first_name,
    last_name: req.body.last_name,
    email: req.body.email,
    is_active: true
  };

  students.push(student);

  res.status(201).json(student);
});

app.get("/api/v1/students", (req, res) => {
  res.json(students);
});

app.get("/api/v1/students/:id", (req, res) => {
  const student = students.find(
    s => s.id === parseInt(req.params.id)
  );

  if (!student) {
    return res.status(404).json({
      error: "Student not found"
    });
  }

  res.json(student);
});

app.delete("/api/v1/students/:id", (req, res) => {
  const index = students.findIndex(
    s => s.id === parseInt(req.params.id)
  );

  if (index === -1) {
    return res.status(404).json({
      error: "Student not found"
    });
  }

  students.splice(index, 1);

  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});