// Ensure that the document is fully loaded before executing the script
$(document).ready(function () {
  // Set the URL for the API endpoint to check the status
  const url = "http://0.0.0.0:5001/api/v1/status/";

  // Make a GET request to the specified API endpoint
  $.get(url, function (data) {
    // Check if the API response status is "OK"
    if (data.status === "OK") {
      // Apply the "available" class to the element with id "api_status" if the status is "OK"
      $("#api_status").addClass("available");
    } else {
      // Remove the "available" class from the element with id "api_status" if the status is not "OK"
      $("#api_status").removeClass("available");
    }
  });
});
