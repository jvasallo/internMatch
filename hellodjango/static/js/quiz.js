/**
 * Allow sortable container items
 */
$(function() {
	$('#sortable').sortable();
	$('#sortable').disableSelection();
});

window.onload = function(){
	/**
	 * Submit button click action
	 */
	$('#submit-quiz').on('click', function() { 
		var quizObjectResults = $('#sortable .quiz-category');	// sortable quiz object
		var numberOfItems = quizObjectResults.length;			// total quiz items
		var quizData = "[%USER_ID_HERE%] ";					// initialize new string to put quiz results
		
		// loop through quiz object to retrieve id order and store as string
		for (var i=0; i<numberOfItems; i++) {
			// only add space between id's if not last id in list
			if (i < numberOfItems-1) {
				quizData = quizData + quizObjectResults[i].id + " "
			}
			// add no extra space if last id in list
			else {
				quizData = quizData + quizObjectResults[i].id
			}
		}
		
//	        connectWith: '.object',
  //              update: function() {
    //                $.ajax({
      //                    type: "POST",
        //                  data: quizData,
          //                url: "quiz/submit"
            //            });		

		alert('Data to POST: ' + quizData);
		$.post('quiz/submit', function(quizData) { // data is the the data we want to submit
			//handle any other tasks once the server returns with status
		});
	});
};
