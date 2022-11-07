let sub = document.getElementById("sub");
        sub.addEventListener("click", displayDitails);

        let row = 1;

        // <th>F_name</th><br>
        // <th>L_name</th><br>
        // <th>Email</th><br>
        // <th>Mobile</th><br>
        // <th>Gender</th><br>
        // <th>Address</th><br>
        // <th>Text_Area</th><br>


        function displayDitails(){
            let F_name = document.getElementById("F_name").value;
            let L_name = document.getElementById("L_name").value;
            let Email = document.getElementById("Email").value;
            let Mobile = document.getElementById("Mobile").value;
            let Gn = document.getElementById("Gender").value;
            let Address = document.getElementById("Address").value;
            let Text_Area = document.getElementById("Text_Area").value;

            let display = documnet.getElementById("displya");

            let newRow = display.insertRow(row);

            let cell1 = newRow.insertCell(0);
            let cell2 = newRow.insertCell(1);
            let cell3 = newRow.insertCell(2);
            let cell4 = newRow.insertCell(3);
            let cell5 = newRow.insertCell(4);
            let cell6 = newRow.insertCell(5);
            let cell7 = newRow.insertCell(6);


            // cell1.innerHTML = Fnm;
            // cell2.innerHTML = Lnm;
            // cell3.innerHTML = Em;
            // cell4.innerHTML = Mo;
            // cell5.innerHTML = Gn;
            // cell6.innerHTML = Add;
            // cell7.innerHTML = Ta;

            // row++;
        }