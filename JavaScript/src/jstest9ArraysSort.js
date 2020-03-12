var trucks = [
    {type:"Volvo", year:2016},
    {type:"MAN", year:2017},
    {type:"Scania", year:2018},
    {type:"DAF", year:2020},
    {type:"Renault", year:2019},
    {type:"Mercedes-Benz", year:2020}
  ];
  
  displayTrucks();
  
  function myFunction() {
    trucks.sort(function(a, b){return a.year - b.year});
    displayTrucks();
  }
  
  function displayTrucks() {
    document.getElementById("demo").innerHTML =
    trucks[0].type + " " + trucks[0].year + "<br>" +
    trucks[1].type + " " + trucks[1].year + "<br>" +
    trucks[2].type + " " + trucks[2].year + "<br>" +
    trucks[3].type + " " + trucks[3].year + "<br>" +
    trucks[4].type + " " + trucks[4].year + "<br>" +
    trucks[5].type + " " + trucks[5].year;
  }