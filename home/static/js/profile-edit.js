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
	
    $('#skills').editable({ // skills field (optional)
        type: 'textarea',
        inputclass: 'input-xxlarge'
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
	
    $('#city').editable({ // city field
		validate: function(value) { // required
				if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-medium'
    });
	
	var states = []; // states list
    $.each({"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "Dist of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}, function(k, v) {
        states.push({id: k, text: v});
    });
    $('#state').editable({ // state field (required)
		type: 'select2', // select2.js
		inputclass: 'input-large',
		source: states
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

   $.ajax({ // create an AJAX call...
       data: {'name' : editableObjects[0].text,
              'school' : editableObjects[1].text,
              'graduation_date' : editableObjects[2].text,
              'major' : editableObjects[3].text,
              'email' : editableObjects[4].text,
              'description' : editableObjects[5].text,
              'skills' : editableObjects[6].text
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