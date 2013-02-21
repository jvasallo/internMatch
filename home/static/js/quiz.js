$(function() {
   $( "#sortable" ).sortable();
   $( "#sortable" ).disableSelection();
});
     
function onSubmit() {    
   var sortedQuizObjects = $('#sortable .quiz-option');
   var n = sortedQuizObjects.length; // total quiz items
   var quizData = ""; // initialize new string to put quiz results

   for (var i=0; i<n; i++) {
       // only add space between id's if not last id in list
       if (i < n-1) {
           quizData = quizData + sortedQuizObjects[i].id + " "
       }
       // add no extra space if last id in list
       else {
           quizData = quizData + sortedQuizObjects[i].id
       }
   }
   $.ajax({ // create an AJAX call...
       data: {'userID' : "user.id",
              'quizID' : 1, 
              'quizString' : quizData},
       type: 'POST', // GET or POST
       url: 'submit/', // the file to call
       success: function(response) { // on success..
           window.location.href = "quiz/complete";
           //alert('Success -- STATUS: 200');
       }
   });
}

function exitApp() {
    window.location = "/";
}
