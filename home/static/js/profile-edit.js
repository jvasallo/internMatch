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

var countries = [];
$.each({"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Bartelemey", "BM": "Bermuda", "BN": "Brunei Darussalam", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", "O1": "Other Country", "LV": "Latvia", "RW": "Rwanda", "RS": "Serbia", "TL": "Timor-Leste", "RE": "Reunion", "LU": "Luxembourg", "TJ": "Tajikistan", "RO": "Romania", "PG": "Papua New Guinea", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "BZ": "Belize", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "TM": "Turkmenistan", "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "RU": "Russian Federation", "EE": "Estonia", "EG": "Egypt", "TK": "Tokelau", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "EU": "Europe", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova, Republic of", "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", "UG": "Uganda", "TZ": "Tanzania, United Republic of", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", "FX": "France, Metropolitan", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands (Malvinas)", "FM": "Micronesia, Federated States of", "FO": "Faroe Islands", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "CI": "Cote d'Ivoire", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", "CC": "Cocos (Keeling) Islands", "CA": "Canada", "CG": "Congo", "CF": "Central African Republic", "CD": "Congo, The Democratic Republic of the", "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CV": "Cape Verde", "CU": "Cuba", "SZ": "Swaziland", "SY": "Syrian Arab Republic", "KG": "Kyrgyzstan", "KE": "Kenya", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", "KR": "Korea, Republic of", "SI": "Slovenia", "KP": "Korea, Democratic People's Republic of", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "Virgin Islands, British", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Lao People's Democratic Republic", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", "A1": "Anonymous Proxy", "TO": "Tonga", "LT": "Lithuania", "A2": "Satellite Provider", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libyan Arab Jamahiriya", "VA": "Holy See (Vatican City State)", "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "Virgin Islands, U.S.", "IS": "Iceland", "IR": "Iran, Islamic Republic of", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AN": "Netherlands Antilles", "AQ": "Antarctica", "AP": "Asia/Pacific Region", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}, function(k, v) {
	countries.push({id: k, text: v});
}); 
$('#country').editable({
	inputclass: 'input-large',
	source: countries 
}); 

/*
var states = [];
$.each({"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "Dist of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}, function(k, v) {
	states.push({id: k, text: v});
});
// Working - Uses Select2.js
$('#state').editable({
	type: 'select2',
	inputclass: 'input-large',
	source: states
});
*/

// Working
$('#state').editable({
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