// import Inputs from "./Components/Inputs";
const { PythonShell } = require("python-shell");
const functions = require("firebase-functions");
const express = require("express");
const app = express();
const cors = require("cors");
app.use(cors());
app.use(express.json()); // to support JSON-encoded bodies
app.use(express.urlencoded({ extended: true })); // to support URL-encoded bo

app.get("/api", (req, res) => {
  res.send("hello world!");
  // let options = {
  //   mode: "text",
  //   pythonPath: "functions/calculator.py",
  //   pythonOptions: ["-u"],
  //   scriptPath: "my-app/src/index.js",
  //   args: ["manufacturer", "country"],
  // };
});

app.post("/api/generateDiagram", (req, res) => {
  const manufacturer = req.body.inManufacturer;
  const country = req.body.inCountry;
  const volume = req.body.inVolume;
  const mass = req.body.inMass;
  const fit = req.body.isFitToggled;
  const fitAmount = req.body.inFitAmount;
  const recycler = req.body.isRecyclerToggled;
  const recyclerAmount = req.body.inRecyclerAmount;
  console.log(manufacturer);
  console.log(country);
  console.log(volume);
  console.log(mass);
  console.log(fit);
  console.log(fitAmount);
  console.log(recycler);
  console.log(recyclerAmount);

  let options = {
    args: [
      manufacturer,
      country,
      volume,
      mass,
      fit,
      fitAmount,
      recycler,
      recyclerAmount,
    ],
    scriptPath: "../my-app/public/",
  };

  // PythonShell.run("calculator.py", { args: [] }, function (err) {
  PythonShell.run("calculator.py", options, function (err, results) {
    // if (err) throw err;
    if (err) {
      console.log(err);
    }
    console.log("results: ", results);
    // console.log("finished", result.toString());
    // res.send(result.toString());
  });
  res.send("Done");
});

// let pyshell = new PythonShell("calculator.py");
// pyshell.send(inCountry);
// pyshell.on("message", function (message) {
//   console.log(message);
// });

// exports.app = functions.https.onRequest(app); -> for firebase

app.listen(5000, () => {
  //server starts listening for any attempts from a client to connect at port: {port}
  console.log(`Now listening on port ${5000}`);
});
