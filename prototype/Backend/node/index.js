const exec = require("child_process").exec;
const request = require("request");
const fs = require("fs");
const express = require('express');
const app = express();
var bodyParser = require('body-parser');
var cors = require('cors')
var urlencodedParser = bodyParser.urlencoded({ extended: false })
const port = 3000;

app.listen(port, () => {
    console.log("server Started on port 3000");
})

app.use(cors());
app.get('/query/:query', urlencodedParser, (req, res) => {
    var inp = req.params.query;
    console.log(inp);
    inp += "\n";
    fs.writeFileSync("query.txt", inp);
    var child = exec(
        'python ../python_files/scrapeCode.py < query.txt', { maxBuffer: 1024 * 100 },
        function(err, stdout, stderr) {
            if (err) throw err;
            if (stderr) console.log("stdder:" + stderr);
            // socket.emit("Refined query", stdout);
            var desired = stdout.replace(/[^\w{}";=,()+-./<>?':@!$%*&\s]/gi, '')
            var output = [];
            // console.log("stdout:"+desired);
            output.push(desired);
            fs.writeFileSync('output.txt', desired);
            console.log(output);
            res.send(output);
        }
    );

})