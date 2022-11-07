console.log("This is JsFunctionEx.js File")
console.log("This is External JavaScript File")


// Creating a function
// This function is not give a return value
function greet(name, greetText) {

    console.log(greetText + " "+ name)

    console.log(name + " is a good boy")
    
}
// Reusebalty of function
let greetText = "Good Morning"
let names = "Jerry"
greet(names, greetText);

let name1 = "Herry"
greet(name1, greetText);

let name2 = "Perry"
greet(name2, greetText);

let name3 = "Lerry"
greet(name3, greetText);


// Creating a function and return the value 

function sum(a, b, c1, d, e, f){
    let c = a * b * c1 * d * e * f
    return c

    // This line is never Execute
    // console.log("Function is give return value")
}
 let returnvalue1 = sum(1,2,3,4,5,6)
 console.log("Sum of given number is:-" + returnvalue1)