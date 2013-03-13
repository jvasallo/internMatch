$(function(){
    // turn to inline mode
    $.fn.editable.defaults.mode = 'inline';

    $('#name').editable({
	validate: function(value) {
  	    if($.trim(value) == '') return 'This field is required';
	},
	inputclass: 'input-large'
    });

    $('#relationship').editable({
        validate: function(value) {
            if($.trim(value) == '') return 'This field is required';
        },
        inputclass: 'input-large'
    });

    $('#email').editable({
	type: 'textarea',
	inputclass: 'input-large'
    });

});

function onSubmit() {
   var editableObjects = $('.editable');
   var referenceid = document.getElementById('referenceid').value;
   var n = editableObjects.length; // total quiz items
   $.ajax({ // If the field is empty send '', instead of 'Empty', which will get saved in the respective database fields
       data: {'id' : referenceid,
              'name' : editableObjects[0].text == 'Empty' ? '' : editableObjects[0].text,
              'relationship' : editableObjects[1].text == 'Empty' ? '' : editableObjects[1].text,
              'email' : editableObjects[2].text == 'Empty' ? '' : editableObjects[2].text,
              },
       type: 'POST', // GET or POST
       url: '/resume/update/', // the file to call
       success: function(response) { // on success..
           window.location.href = "../../../profile/references/";
       }
   });
}

function exitApp() {
    window.location = "/profile/references";
}
