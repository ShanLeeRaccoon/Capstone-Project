var express = require('express');
var app = express();
var fs = require("fs");
var bodyParser = require('body-parser');
var cors = require('cors');
app.use(cors());
//data sample
let get_GPS_status = {"status": "Fetch"}
let cal_route_status = {"status":"Cal"}
let run_nav_status = {"status": "Stop"}
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
    fs.writeFile('/home/pi/Desktop/Capstone/backend/destinationGPS.json', data, (err) => {
        if (err) throw err;
        console.log('Data written to file');
        res.end(data);

    });
    let cal_route_command = JSON.stringify(cal_route_status);
    fs.writeFile('/home/pi/Desktop/Capstone/backend/cal_route_command.json', cal_route_command, (err) => {
        if (err) throw err;
        console.log('Data written to cal_route_command file:Cal');
    });


})


app.get('/getGPS', (req, res) => {

    //change status
    let get_GPS_command = JSON.stringify(get_GPS_status);
    fs.writeFile('/home/pi/Desktop/Capstone/backend/getGPScommand.json', get_GPS_command, (err) => {
        if (err) throw err;
        console.log('Data written to get GPS command file:fetch');
    });
    setTimeout(() => { 
        console.log("5 sec!")
        let rawdata = fs.readFileSync('/home/pi/Desktop/Capstone/originGPS.json');
        let coordinate = JSON.parse(rawdata);
        return res.send(coordinate); }, 3000);
   
    
    

    let run_nav_command = JSON.stringify(run_nav_status);
    fs.writeFile('/home/pi/Desktop/Capstone/backend/run_nav_command.json', run_nav_command, (err) => {
        if (err) throw err;
        console.log('Data written to run nav command file:STOP');
    });

    
  });

var server = app.listen(8081, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("SafeCycle app listening at http://%s:%s", host, port)
})
