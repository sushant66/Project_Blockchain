var express = require('express');
var app = express();

app.get('/data', function(req, res){
  res.send('hello world'); //replace with your data here
});

app.listen(3000);
