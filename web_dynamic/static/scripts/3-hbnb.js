$(document).ready(init);

// Define the server host and an object to store selected amenities
const HOST = "0.0.0.0";
const amenityObj = {};

// Initialize the page by setting up event listeners and API status check
function init() {
  // Set up a change event listener for amenity checkboxes
  $(".amenities .popover input").change(function () {
    // Check if the checkbox is checked or unchecked
    if ($(this).is(":checked")) {
      // Add the amenity to the object if checked
      amenityObj[$(this).attr("data-name")] = $(this).attr("data-id");
    } else if ($(this).is(":not(:checked)")) {
      // Remove the amenity from the object if unchecked
      delete amenityObj[$(this).attr("data-name")];
    }
    // Update the displayed list of selected amenities
    const names = Object.keys(amenityObj);
    $(".amenities h4").text(names.sort().join(", "));
  });

  // Check the API status and perform the initial search
  apiStatus();
  searchPlacesAmenities();
}

// Function to check the status of the API and update the UI
function apiStatus() {
  // Define the API URL to check the status
  const API_URL = `http://${HOST}:5001/api/v1/status/`;
  $.get(API_URL, (data, textStatus) => {
    // Update the API status element based on the API response
    if (textStatus === "success" && data.status === "OK") {
      $("#api_status").addClass("available");
    } else {
      $("#api_status").removeClass("available");
    }
  });
}

// Function to search for places based on selected amenities
function searchPlacesAmenities() {
  // Define the URL for the places search API
  const PLACES_URL = `http://${HOST}:5001/api/v1/places_search/`;
  $.ajax({
    url: PLACES_URL,
    type: "POST",
    headers: { "Content-Type": "application/json" },
    // Send the selected amenities in the request body
    data: JSON.stringify({ amenities: Object.values(amenityObj) }),
    success: function (response) {
      // Clear the current list of places
      $("SECTION.places").empty();
      // Iterate over the response and create HTML for each place
      for (const r of response) {
        const article = [
          "<article>",
          '<div class="title_box">',
          `<h2>${r.name}</h2>`,
          `<div class="price_by_night">$${r.price_by_night}</div>`,
          "</div>",
          '<div class="information">',
          `<div class="max_guest">${r.max_guest} Guest(s)</div>`,
          `<div class="number_rooms">${r.number_rooms} Bedroom(s)</div>`,
          `<div class="number_bathrooms">${r.number_bathrooms} Bathroom(s)</div>`,
          "</div>",
          '<div class="description">',
          `${r.description}`,
          "</div>",
          "</article>",
        ];
        // Append the generated HTML to the places section
        $("SECTION.places").append(article.join(""));
      }
    },
    error: function (error) {
      // Log any errors encountered during the request
      console.log(error);
    },
  });
}
