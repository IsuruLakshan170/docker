const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(bodyParser.json());
app.use(cors());

app.get('/api', (req, res) => {
  res.send('Hello, world2!');
});

app.listen(3000, () => {
  console.log('API listening on port 3000');
});
