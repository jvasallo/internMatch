// Allow sortable container items
$(function() {
	$('#sortable').sortable();
	$('#sortable').disableSelection();
});

window.onload = function(){
	// Send button action
	var quizObjectResults; 				// Quiz Object Results
	var quizArrayResults = new Array(); // Quiz Array Results
	//var quizStringResults; 				// Quiz String Results
	var quizData;						// Quiz Data to POST
	
	$('#send-quiz').on('click', function() { 
	quizObjectResults = $('#sortable .quiz-category');
		var numberOfItems = quizObjectResults.length;
		quizStringResults = new String();
		for (var i=0; i<numberOfItems; i++) {
			quizArrayResults[i] = quizObjectResults[i].id
			// if (i < numberOfItems) {
				// quizStringResults = quizStringResults + quizObjectResults[i].id + " "
			// }
			// else {
				// quizStringResults = quizStringResults + quizObjectResults[i].id
			// }
		}
		//alert('Quiz Results (Object): ' + quizObjectResults);
		//alert('Quiz Results (Array): ' + quizArrayResults);
		//alert('Quiz Results (String): ' + quizStringResults);
		quizData = JSON.stringify(quizArrayResults);
	
		alert('Data to POST: ' + quizData);
		$.post('quiz/send/', function(quizData) { // data is the the data we want to send
			//handle any other tasks once the server returns with status
			alert("Data Loaded: " + quizData);
		});
	});
};