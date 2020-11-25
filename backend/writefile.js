var express = require('express');
var app = express();
var fs = require("fs");
var bodyParser = require('body-parser');
var cors = require('cors');
app.use(cors());
//data sample
var user = {
    "user4": {
        "name": "mohit",
        "password": "password4",
        "profession": "teacher",
        "id": 4
    }
};
//data sample
let student = {
    name: 'Mike',
    age: 23,
    gender: 'Male',
    department: 'English',
    car: 'Honda'
};

let mapRequest = {
    currentLat: 10.12345,
    currentLng: 106.12345,
    targetLat: 10.456789,
    targetLng: 106.877452
};

app.use(bodyParser.json());

app.post('/saveData', function (req, res) {
    //Read the data from API request and write file
    console.log("Post method called");
    reqData = req.body;
    console.log(reqData);
    let data = JSON.stringify(reqData, null, 2);
    fs.writeFile('GPSrequest.json', data, (err) => {
        if (err) throw err;
        console.log('Data written to file');
        res.end(data);

    });
})


app.get('/getGPS', (req, res) => {
    let rawdata = fs.readFileSync('/home/pi/Desktop/Capstone/GPS.json');
    let coordinate = JSON.parse(rawdata);
    
    return res.send(coordinate);
  });

var server = app.listen(8080, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("SafeCycle app listening at http://%s:%s", host, port)
})
