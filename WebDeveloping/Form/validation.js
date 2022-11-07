var isvalid = true;
var isemailValid = true;

$(document).ready(function () {
    console.log("ready!");
    // localStorage.clear();
    `var x = tablejas.rows.length;
    while(--x){
        tablejas.deleteRow(x)
    }`
    showTableData();
});


// This is a Validation Checker
$(".submitform").click(function () {

    var validation = $("#validation");
    validation.validate({
        rules: {
            fname: {
                required: true,
                lattersonly: true
            },
            lname: {
                required: true,
                lattersonly: true
            },
            email: {
                required: true,
                email: true
            },
            mobile: {
                required: true,
                numericonly: true,
                minlength: 10,
                maxlength: 13
            },
            gender: {
                required: true
            },
            adrs: {
                required: true
            },
            country: {
                required: true

            },
            ststes: {
                required: true
            },
            hobbies: {
                required: true
            }


        },
        messages: {
            fname: {
                required: 'First Name must be required',
                lattersonly: 'Invalid Name'
            },
            lname: {
                required: 'Last Name must be required',
                lattersonly: 'Invalid Last Name'
            },
            email: {
                required: 'Email must be required',
                email: 'Email Invalid'

            },
            mobile: {
                required: 'Mobile must be required',
                numericonly: 'Enter Valid Number',
                minlength: 'Min 10 digits',
                maxlength: 'Max 13 digits'
            },
            gender: {
                required: 'Gender must be required'
            },
            adrs: {
                required: 'Address must be required'
            },
            country: {
                required: 'Country must be required'

            },
            ststes: {
                required: 'states must be required'
            },
            hobbies: {
                required: 'Select Checkbox'
            }

        },
        errorPlacement: function (error, element) {
            // debugger;
            if (element.is(":radio")) {
                error.appendTo(element.parents(".gen"));
            } else if (element.attr('type') == 'checkbox') {
                // debugger;
                error.appendTo(element.parents(".col-sm-6"));

            } else {
                error.insertAfter(element);
            }
        },

    });


    // isvalid = $("#validation").valid();
    // console.log('isvalid :: ', isvalid);


    jQuery.validator.addMethod('lattersonly', function (value, element) {
        return /^[^-\s][a-zA-Z_\s-]+$/.test(value);
    });

    jQuery.validator.addMethod('numericonly', function (value, element) {
        return /^[+0-9]+$/.test(value);
    });


});

// Creating a State list
var countryList = {

    India: ['select defualt', 'Gujrat', 'Panjab', 'Delhi', 'Maharashtra', 'Rajashthan'],
    Austrailya: ['select defualt', 'Aus', 'New South Wales', 'Queensland', 'South Australia', 'Tasmania'],
    UAE: ['select defualt', 'Dubai', 'Abu Dhabi', 'Sharjah'],
    UK: ['select defualt', 'Scotland', 'Northern Ireland', 'Wales', 'Northern Ireland']
}

country = document.getElementById("country"); //parent select element
states = document.getElementById("states"); //child select element

for (key in countryList) { //populate the parent select element with array key
    country.innerHTML = country.innerHTML + '<option>' + key + '</option>';
}

country.addEventListener('change', function populate_child(e) {
    states.innerHTML = '';
    itm = e.target.value;
    if (itm in countryList) {
        for (i = 0; i < countryList[itm].length; i++) {
            states.innerHTML = states.innerHTML + '<option>' + countryList[itm][i] + '</option>';
        }
    }
});

// Create a main Insert Function
function insert() {
    // debugger;
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var mobile = document.getElementById('mobile').value;
    var gender = document.querySelector('input[name="gender"]:checked').value;
    var adrs = document.getElementById('adrs').value;
    var country = document.getElementById('country').value;
    var states = document.getElementById('states').value;
    //var hobbies1 = document.getElementById('hobbies1').value;
    var hobbies = "";
    var checkboxes = document.getElementsByName('hobbies');
    var vals = "";
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        if (checkboxes[i].checked) {
            vals += "," + checkboxes[i].value;
        }
    }
    if (vals) vals = vals.substring(1);

    hobbies = vals;
    console.log('value of hobbies', hobbies);

    console.log("this from hobbies :: " + hobbies);


    // // Locat Storage
    var user_records = new Array();
    user_records = JSON.parse(localStorage.getItem("users")) ? JSON.parse(localStorage.getItem("users")) : []
    if (user_records.some((v) => { return v.email == email })) {
        alert("Duplicate Data")
        clearForm();
        return false;
    }
    else {
        user_records.push({
            "fname": fname,
            "lname": lname,
            "email": email,
            "mobile": mobile,
            "gender": gender,
            "adrs": adrs,
            "country": country,
            "states": states,
            "hobbies": hobbies
        });
        localStorage.setItem("users", JSON.stringify(user_records));
    }


    showTableData();
    clearForm();





}
// show data in table
function showTableData() {
    console.log(localStorage.getItem("users"));
    var documents = document.getElementById('tbl');
    var local_user = new Array();
    local_user = JSON.parse(localStorage.getItem("users")) ? JSON.parse(localStorage.getItem("users")) : [];
    console.log('hello' + local_user);
    var tablejas = "";
    deleteTableRow();
    local_user.forEach(item =>

        tablejas = tablejas + `<tr>
        <td>${item.fname}</td>
        <td>${item.lname}</td>
        <td>${item.email}</td>
        <td>${item.mobile}</td>
        <td>${item.gender}</td>
        <td>${item.adrs}</td>
        <td>${item.country}</td>
        <td>${item.states}</td>
        <td>${item.hobbies}</td>
        <td>${`<button onClick='onDelete(this)'>Delete</button`}</td>    
        
    </tr>`


    );
    // cleare dtata
    document.getElementById('tbl').innerHTML += tablejas;

}

//Delete Data from table
function onDelete(td){
    if(confirm("Do you want to delete this Record?")){
        row = td.parentElement.parentElement;
        document.getElementById('tbl').deleteRow(row.rowIndex);
    }
    clearForm();
}

// Delte data from the local storage
// function onDelete() {
//     if (confirm("Do you want to delete this Record?")) {
//         // row = td.parentElement.parentElement;
//         // document.getElementById('tbl').deleteRow(row.rowIndex);
//         var content = localStorage.getItem("users");
//         localStorage.removeItem(JSON.stringify(user_records[0]));
//         localStorage.removeItem(content);
//     }
//     clearForm();
// }


// Clear Function
function clearForm() {

    document.getElementById("validation").reset();


}

// Delte table row
function deleteTableRow() {
    var tbl1 = document.getElementById("tbl")

    var x = tbl1.rows.length;
    while (--x) {
        tbl1.deleteRow(x);
    }
}


// Validation use to call insert function
$(document).ready(
    function () {
        $('.submitform').on('click', function (event) {
            // console.log('test by jitu ', $("#validation").valid());
            if ($("#validation").valid()) {
                console.log('we are inside insert function');
                insert();
            }
        });
    });