//turn to inline mode
$.fn.editable.defaults.mode = 'inline';

// $('#name').editable({
	// type: 'text',
	// pk: 1,
	// url: '/post',
	// title: 'Enter username'
// });

//enable / disable
// $('#enable').click(function() {
   // $('#user .editable').editable('toggleDisabled');
// }); 

/* Both Edit Forms */
$('#name').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	inputclass: 'input-large'
});
$('#email').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'email',
	inputclass: 'input-large'
});
$('#skills').editable({
	type: 'select2',
	inputclass: 'input-large',
	select2: {
		tags: ['ajax','C','C++', 'CSS','Django','HTML','Java','JavaScript','JQuery','Linux','OS X','Python','Ruby','Windows'],
		tokenSeparators: [",", " "]
	}
}); 

/* Intern Edit Form */
$('#school').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'text',
	inputclass: 'input-large'
});
$('#graduation_date').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'date',
	format: 'MM dd, yyyy',
	inputclass: 'input-medium'
});
$('#major').editable({
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

/* Company Edit Form */
$('#description').editable({
	type: 'text',
	inputclass: 'input-xlarge'
});
$('#industry').editable({
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
$('#address').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	inputclass: 'input-large'
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

// Working - No Search/Predictive Text (type: select)
$('#state1').editable({
	type: 'select',
	inputclass: 'input-large',
	source: [
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
});

/*
$('#state1').editable({
	type: 'select',
	inputclass: 'input-large',
	source: [
		{value: 1, text: 'Alabama'},
		{value: 2, text: 'Alaska'},
		{value: 3, text: 'Arizona'},
		{value: 4, text: 'Arkansas'},
		{value: 5, text: 'California'},
		{value: 6, text: 'Colorado'},
		{value: 7, text: 'Connecticut'},
		{value: 8, text: 'Delaware'},
		{value: 9, text: 'Dist of Columbia'},
		{value: 10, text: 'Florida'},
		{value: 11, text: 'Georgia'},
		{value: 12, text: 'Hawaii'},
		{value: 13, text: 'Idaho'},
		{value: 14, text: 'Illinois'},
		{value: 15, text: 'Indiana'},
		{value: 16, text: 'Iowa'},
		{value: 17, text: 'Kansas'},
		{value: 18, text: 'Kentucky'},
		{value: 19, text: 'Louisiana'},
		{value: 20, text: 'Maine'},
		{value: 21, text: 'Maryland'},
		{value: 22, text: 'Massachusetts'},
		{value: 23, text: 'Michigan'},
		{value: 24, text: 'Minnesota'},
		{value: 25, text: 'Mississippi'},
		{value: 26, text: 'Missouri'},
		{value: 27, text: 'Montana'},
		{value: 28, text: 'Nebraska'},
		{value: 29, text: 'Nevada'},
		{value: 30, text: 'New Hampshire'},
		{value: 31, text: 'New Jersey'},
		{value: 32, text: 'New Mexico'},
		{value: 33, text: 'New York'},
		{value: 34, text: 'North Carolina'},
		{value: 35, text: 'North Dakota'},
		{value: 36, text: 'Ohio'},
		{value: 37, text: 'Oklahoma'},
		{value: 38, text: 'Oregon'},
		{value: 39, text: 'Pennsylvania'},
		{value: 40, text: 'Rhode Island'},
		{value: 41, text: 'South Carolina'},
		{value: 42, text: 'South Dakota'},
		{value: 43, text: 'Tennessee'},
		{value: 44, text: 'Texas'},
		{value: 45, text: 'Utah'},
		{value: 46, text: 'Vermont'},
		{value: 47, text: 'Virginia'},
		{value: 48, text: 'Washington'},
		{value: 49, text: 'West Virginia'},
		{value: 50, text: 'Wisconsin'},
		{value: 51, text: 'Wyoming'}
	]
});
*/

$('#zip').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'number'
});
$('#phone').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'number',
	maxlength: '11',
	inputclass: 'input-medium'
});
$('#contactEmail').editable({
	validate: function(value) {
		if($.trim(value) == '') return 'This field is required';
	},
	type: 'email',
	inputclass: 'input-large'
});
$('#website').editable({
	type: 'url',
	inputclass: 'input-large'
});