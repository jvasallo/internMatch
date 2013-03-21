/* Edit Job Posting Form */
$(function(){
    $.fn.editable.defaults.mode = 'inline'; // turn to inline mode

    $('#headline').editable({
		validate: function(value) {
			if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-large'
    });

    $('#position').editable({
        validate: function(value) {
            if($.trim(value) == '') return 'This field is required';
        },
        inputclass: 'input-large'
    });

    $('#description').editable({
		type: 'textarea',
		inputclass: 'input-xxlarge'
    });

    $('#company_bio').editable({
        type: 'textarea',
        inputclass: 'input-xxlarge'
    });

    $('#required').editable({
		type: 'select2',
		inputclass: 'input-large',
		select2: {
			tags: [""],
			tokenSeparators: [",", " "]
		}
    });

    $('#desired').editable({
		type: 'select2',
		inputclass: 'input-large',
		select2: {
			tags: [""],
			tokenSeparators: [",", " "]
		}
    });
    
    $('#city').editable({
		validate: function(value) {
				if($.trim(value) == '') return 'This field is required';
		},
		inputclass: 'input-medium'
    });

	$('#state').editable({
		type: 'select',
		inputclass: 'input-large',
		source: stateList // stateList defined below
	});
	
	$('#url').editable({
        type: 'url',
        inputclass: 'input-large'
    });

    $('#end_date').editable({
        validate: function(value) {
            if($.trim(value) == '') return 'This field is required';
        },
        type: 'date',
        format: 'yyyy-mm-dd',    
        datepicker: {
			weekstart: 1
		}
    });

});

function onSubmit() {
   var editableObjects = $('.editable');
   var postingid = document.getElementById('postingid').value;
   
   	// fixes issue with xeditable
	for (var i = 0; i < editableObjects.length; i++) { // iterate over editableObjects
		if (editableObjects[i].text == 'Empty' && editableObjects[i].text.length == 5) { // if editable field contains an 'Empty' string value
			editableObjects[i].text = '' // keep it as an empty value
		}
	}
   
   	$.ajax({ // create an AJAX call...
		data: {'id' : postingid,
              'headline' : editableObjects[0].text,
              'position' : editableObjects[1].text,
              'description' : editableObjects[2].text,
              'company_bio' : editableObjects[3].text,
              'required' : editableObjects[4].text,
              'desired' : editableObjects[5].text,
              'city' : editableObjects[6].text,
              'state' : editableObjects[7].text,
              'url' : editableObjects[8].text,
              'end_date' : editableObjects[9].text
			  },
		type: 'POST', // GET or POST
		url: '/job-post/update/', // the file to call
		success: function(response) { // on success..
			window.location = "/profile/jobs"; // redirect to view jobs page
		}
	});
}

function exitApp() {
    window.location = "/profile/jobs";
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
