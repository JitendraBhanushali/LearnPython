$(function(){
    var validation=$("#validation");

    validation.validate({
        rules:{
            fname:{
                required:true,
                lattersonly:true
            },
            lname:{
                required:true,
                lattersonly:true
            },
            email:{
                required:true,
                email:true
            },
            mobile:{
                required:true,
                numericonly:true
            },
            gender:{
                required:true
            },
            adrs:{
                required:true
            },
            country:{
                required:true
            },
            hobbies:{
                required:true
            }

        },
        message:{
            fname:{
                required:'First Name must be required',
                lattersonly:'Invalid Name'
            },
            lname:{
                required:'Last Name must be required',
                lattersonly:'Invalid Last Name'
            },
            email:{
                required:'Email must be required',
                email:'Email Invalid'

            },
            mobile:{
                required:'Mobile must be required',
                numericonly:'Enter Valid Number'
            },
            gender:{
                required:'Gender must be required'
            },
            adrs:{
                required:'Address must be required'
            },
            country:{
                required:'Country must be required'
            },
            hobbies:{
                required:'Hobbies must be required'
            }
        },
        errorPlacement:function(error,element){
            if(element.is(":radio")){
                error.appendTo(element.parents(".gen"));
            }else{
                error.insertAfter(element);
            }
        },
        errorPlacement:function(error,element){
            if(element.is(":checkbox")){
                error.appendTo(element.parents(".hob"));
            }else{
                error.insertAfter(element);
            }
        }
    })

    jQuery.validator.addMethod('lattersonly', function(value, element) {
        return /^[^-\s][a-zA-Z_\s-]+$/.test(value);
    });

    jQuery.validator.addMethod('numericonly', function(value, element) {
        return /^[0-9]+$/.test(value);
    });

    jQuery.validator.addMethod('all', function(value, element) {
        return /^[^-\s][a-zA-Z0-9_\s-]+$/.test(value);
    });
})
