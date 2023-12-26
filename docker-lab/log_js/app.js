const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

let logs = [];

app.use(bodyParser.json());

app.get("/getLog", (req, res) => {
  res.json(logs);
});

app.post("/addLog", (req, res) => {
  const logEntry = req.body;
  logs.push(logEntry);
  console.log("Received log entry:", logEntry);
  res.send("Log entry added successfully.");
});

app.listen(PORT, () => {
  console.log(`Log service is running on port ${PORT}`);
});
