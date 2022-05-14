console.log('Profitability Calculator');
let recyclecost = 12; // variable can be reassigned
const feedInTariff = 40; // assigned value is constant
let country = null; // explicitly clears value of variable
let quota = null;

let customer = {
    location: 'Italy',
    panelType: 'c-Si'
};

// Dot notation changes values of variables in objects
customer.location = 'France';
// Bracket notation - another way of changing variable values
let selection = 'location';
customer [selection] = 'Germany'

let materials = ['silicon','glass'];
materials[2] = 'aluminium'; // added to materials array

function panelinfo() {
    console.log(customer.panelType);
    console.log(cost);
    console.log(materials);
}

// performing a display task
function panelinfo(generation, volume, age) {
    console.log('Panel Generation: ' + generation);
    console.log('Volume of panels: ' + volume);
    console.log('Age of panels: ' + age);
}

// calculating a value
function cost(value) {
    return value - feedInTariff
}

document.getElementById('countryButton').onclick = function(){
    var country = document.getElementById('countryInput').value
    console.log('Manufacturer country: ',country);
}

document.getElementById('quotaButton').onclick = function(){
    var quota = document.getElementById('quotaInput').value
    console.log('Minimum recycling quota: ',quota);
}

//console.log(materials[2]); // calls 3rd element in array
panelinfo('CdTe','500 panels','20 years');
console.log(cost(100));


