$(function(){
    // turn to inline mode
    $.fn.editable.defaults.mode = 'inline';

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
        type: 'textarea',
        inputclass: 'input-xxlarge'
    });

    $('#desired').editable({
        type: 'textarea',
        inputclass: 'input-xxlarge'
    });


    $('#city').editable({
	validate: function(value) {
            if($.trim(value) == '') return 'This field is required';
	},
	inputclass: 'input-medium'
    });

    var states = [];
    $.each({"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "Dist of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}, function(k, v) {
        states.push({id: k, text: v});
    });

    // Working - Search/Predictive Text (type: select2.js)
    $('#state').editable({
	type: 'select2',
	inputclass: 'input-large',
	source: states
    });

    $('#end_date').editable({
        validate: function(value) {
            if($.trim(value) == '') return 'This field is required';
        },
        type: 'date',
        format: 'yyyy-mm-dd',    
        datepicker: {
                weekStart: 1
           }
    });

});

function onSubmit() {
   var editableObjects = $('.editable');
   var postingid = document.getElementById('postingid').value;
   var n = editableObjects.length; // total quiz items
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
              'end_date' : editableObjects[8].text
              },
       type: 'POST', // GET or POST
       url: '/job-post/update/', // the file to call
       success: function(response) { // on success..
           window.location.href = "../../../profile/jobs/";
       }
   });
}

function exitApp() {
    window.location = "/profile/jobs";
}
