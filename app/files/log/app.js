const express = require('express');
const { spawn } = require('child_process');
const app = express();
const ip = "0.0.0.0";
const port = 5000;


app.get('/', (req, res) => {
    res.send('Hello World!');
});


app.use(function (req, res, next) {
    res.setTimeout(500000, function () {
        // call back function is called when request timed out.
    });
    next();
}).get('/log', (req, res) => {

    var startDate = req.query.startDate
    var endDate = req.query.endDate

    var result;
    const python = spawn('python', ['log.py', startDate, endDate]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        result = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(result)
    });

})

app.all("*", (req, res) => {
    return res.status(404).json({
        success: false,
        msg: "404 Error - Not Found"
    });
});


app.listen(port, ip, () => {
    console.log(`Server is running on ${ip}:${port}`)
})