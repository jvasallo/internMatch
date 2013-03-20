/* Edit Profile Form */
$(function(){
    $.fn.editable.defaults.mode = 'inline';  // turn to inline mode

    /* Both Edit Forms */
    $('#name').editable({ // name field
		validate: function(value) { // required
			if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-large'
    });
	
	$('#city').editable({ // city field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-medium'
    });
	
	$('#state').editable({ // state field (required)
		type: 'select',
		inputclass: 'input-large',
		source: stateList // stateList defined below
	});
	
    $('#email').editable({ // private email field
        validate: function(value) { // required
			if($.trim(value) == '') return 'This field is required';
		},
		type: 'email',
		inputclass: 'input-large'
    });
	
    $('#description').editable({ // experience field for intern profile and description field for company (optional)
		type: 'textarea',
		inputclass: 'input-xxlarge'
    });

	
    /* Intern Edit Form */
    $('#school').editable({ // school name field
		validate: function(value) {  // required
			if($.trim(value) == '') return 'This field is required';
		},
		type: 'text',
		inputclass: 'input-large'
    });
	
    $('#graduation_date').editable({ // graduation date field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		type: 'date',
		format: 'yyyy-mm-dd',
		datepicker: {
			weekstart: 1
		}
    });
	
    $('#major').editable({ // major field (required)
		type: 'select',
		inputclass: 'input-large',
		source: [
			{value: 1, text: 'Applied Network Systems'},
			{value: 2, text: 'Computer Engineering'},
			{value: 3, text: 'Computer Science'},
			{value: 4, text: 'Information Assurance'},
			{value: 5, text: 'Information Technology'},
			{value: 6, text: 'Project Management'},
			{value: 7, text: 'Software Engineering'},
			{value: 8, text: 'Systems Analysis'}
		]
    });
	
    $('#status').editable({ // status field (required)
		type: 'select',
		inputclass: 'input-large',
		source: [
			{value: 1, text: 'Freshman'},
			{value: 2, text: 'Sophomore'},
			{value: 3, text: 'Junior'},
			{value: 4, text: 'Senior'},
			{value: 5, text: 'Masters Candidate'},
			{value: 6, text: 'PhD Candidate'}
		]
    });
	
	$('#skills').editable({ // skills field (optional)
		type: 'select2',
		inputclass: 'input-large',
		select2: {
			tags: [""],
			tokenSeparators: [",", " "]
		}
	});
	
    /* Company Edit Form */
    $('#industry').editable({ // industry field (required)
		type: 'select',
		inputclass: 'input-large',
		source: [
			{value: 1, text: 'Agriculture'},
			{value: 2, text: 'Banking'},
			{value: 3, text: 'Construction'},
			{value: 4, text: 'Chemical Development'},
			{value: 5, text: 'Communications'},
			{value: 6, text: 'Computer Hardware'},
			{value: 7, text: 'Consumer Goods'},
			{value: 8, text: 'Energy Advancement'},
			{value: 9, text: 'Entertainment'},
			{value: 10, text: 'Food and Beverage'},
			{value: 11, text: 'Healthcare'},
			{value: 12, text: 'IT Services'},
			{value: 13, text: 'Insurance'},
			{value: 14, text: 'Media Relations'},
			{value: 15, text: 'Medical Facilities'},
			{value: 16, text: 'Political'},
			{value: 17, text: 'Real Estate'},
			{value: 18, text: 'Services'},
			{value: 19, text: 'Software Development'},
			{value: 20, text: 'Transportation'},
			{value: 21, text: 'Utilities'}
		]
    });
	
    $('#address').editable({ // address field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-large'
    });
	
    $('#zip').editable({ // zip field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		type: 'number'
    });
	
    $('#phone').editable({ // contact phone field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		type: 'tel',
		maxlength: '25',
		inputclass: 'input-medium'
    });
	
    $('#contactEmail').editable({ // contact email field
		validate: function(value) {	// required
				if($.trim(value) == '') return 'This field is required';
		},
		type: 'email',
		inputclass: 'input-large'
    });
	
    $('#website').editable({ // website field (optional)
		type: 'url',
		inputclass: 'input-large'
    });
});

/* Save Intern update */
function onSubmitIntern() {
	var editableObjects = $('.editable'); // all editable fields
	
	// fixes issue with xeditable
	for (var i = 0; i < editableObjects.length; i++) { // iterate over editableObjects
		if (editableObjects[i].text == 'Empty' && editableObjects[i].text.length == 5) { // if editable field contains an 'Empty' string value
			editableObjects[i].text = '' // keep it as an empty value
		}
		if (i == 6) { // check the state field
			for (state in stateList) { // iterate over stateList
				if (stateList[state].text == editableObjects[i].text) { // if the state in the list compares true with the state selected
					editableObjects[i].text = stateList[state].value; // change state field into the state initials (value)
				}
			}
		}
	}
	
	// for (state in stateList) {
		// alert('Value: ' + stateList[state].value);
		// alert('Text: ' + stateList[state].text); 
		// alert('EO: ' + editableObjects[6].text);
		// alert('Compare: ' + (stateList[state].text == editableObjects[6].text));
	// }
   
	$.ajax({ // create an AJAX call...
		data: {'name' : editableObjects[0].text,
			  'school' : editableObjects[1].text,
			  'graduation_date' : editableObjects[2].text,
			  'major' : editableObjects[3].text,
			  'status' : editableObjects[4].text,
			  'city' : editableObjects[5].text,
			  'state' : editableObjects[6].text,
			  'email' : editableObjects[7].text,
			  'description' : editableObjects[8].text,
			  'skills' : editableObjects[9].text
			  },
		type: 'POST', // GET or POST
		url: '/profile/update/', // the file to call
		success: function(response) { // on success..
			window.location = "/profile"; // redirect to view profile page
		}
	});
}

/* Save Company update */
function onSubmit() {
   var editableObjects = $('.editable'); // all editable fields
   
   	// fixes issue with xeditable
	for (var i = 0; i < editableObjects.length; i++) { // iterate over editableObjects
		if (editableObjects[i].text == 'Empty' && editableObjects[i].text.length == 5) { // if editable field contains an 'Empty' string value
			editableObjects[i].text = '' // keep it as an empty value
		}
		if (i == 6) { // check the state field
			for (state in stateList) { // iterate over stateList
				if (stateList[state].text == editableObjects[i].text) { // if the state in the list compares true with the state selected
					editableObjects[i].text = stateList[state].value; // change state field into the state initials (value)
				}
			}
		}
	}

	$.ajax({ // create an AJAX call...
		data: {'name' : editableObjects[0].text,
			  'description' : editableObjects[1].text,
			  'industry' : editableObjects[2].text,
			  'address' : editableObjects[3].text,
			  'city' : editableObjects[4].text,
			  'state' : editableObjects[5].text,
			  'zip' : editableObjects[6].text,
			  'email' : editableObjects[7].text,
			  'contactPhone' : editableObjects[8].text,
			  'contactEmail' : editableObjects[9].text,
			  'companyWebsite' : editableObjects[10].text
			  },
		type: 'POST', // GET or POST
		url: '/profile/update/', // the file to call
		success: function(response) { // on success..
			window.location = "/profile"; // redirect to view profile page
		}
	});
}

/* Cancel profile update */
function exitApp() {
	window.location = "/profile"; // redirect to view profile page
}

var stateList = [
		{value: 'AL', text: 'Alabama'},
		{value: 'AK', text: 'Alaska'},
		{value: 'AZ', text: 'Arizona'},
		{value: 'AR', text: 'Arkansas'},
		{value: 'CA', text: 'California'},
		{value: 'CO', text: 'Colorado'},
		{value: 'CT', text: 'Connecticut'},
		{value: 'DE', text: 'Delaware'},
		{value: 'DC', text: 'Dist of Columbia'},
		{value: 'FL', text: 'Florida'},
		{value: 'GA', text: 'Georgia'},
		{value: 'HI', text: 'Hawaii'},
		{value: 'ID', text: 'Idaho'},
		{value: 'IL', text: 'Illinois'},
		{value: 'IN', text: 'Indiana'},
		{value: 'IA', text: 'Iowa'},
		{value: 'KS', text: 'Kansas'},
		{value: 'KY', text: 'Kentucky'},
		{value: 'LA', text: 'Louisiana'},
		{value: 'ME', text: 'Maine'},
		{value: 'MD', text: 'Maryland'},
		{value: 'MA', text: 'Massachusetts'},
		{value: 'MI', text: 'Michigan'},
		{value: 'MN', text: 'Minnesota'},
		{value: 'MS', text: 'Mississippi'},
		{value: 'MO', text: 'Missouri'},
		{value: 'MT', text: 'Montana'},
		{value: 'NE', text: 'Nebraska'},
		{value: 'NV', text: 'Nevada'},
		{value: 'NH', text: 'New Hampshire'},
		{value: 'NJ', text: 'New Jersey'},
		{value: 'NM', text: 'New Mexico'},
		{value: 'NY', text: 'New York'},
		{value: 'NC', text: 'North Carolina'},
		{value: 'ND', text: 'North Dakota'},
		{value: 'OH', text: 'Ohio'},
		{value: 'OK', text: 'Oklahoma'},
		{value: 'OR', text: 'Oregon'},
		{value: 'PA', text: 'Pennsylvania'},
		{value: 'RI', text: 'Rhode Island'},
		{value: 'SC', text: 'South Carolina'},
		{value: 'SD', text: 'South Dakota'},
		{value: 'TN', text: 'Tennessee'},
		{value: 'TX', text: 'Texas'},
		{value: 'UT', text: 'Utah'},
		{value: 'VT', text: 'Vermont'},
		{value: 'VA', text: 'Virginia'},
		{value: 'WA', text: 'Washington'},
		{value: 'WV', text: 'West Virginia'},
		{value: 'WI', text: 'Wisconsin'},
		{value: 'WY', text: 'Wyoming'}
	]