$(document).ready(function () {
  // Initialize an object to track the selected status of amenities
  const amenities = {};

  // Add a change event listener to all checkboxes
  $("input[type=checkbox]").change(function () {
    // Retrieve the amenity identifier from the 'data-name' attribute of the checkbox
    const amenity_id = $(this).data("name");

    // Determine whether the checkbox is checked
    if ($(this).is(":checked")) {
      // Add the amenity_id to the 'amenities' object with a value indicating it is selected
      amenities[amenity_id] = true;
    } else {
      // Remove the amenity_id from the 'amenities' object if it is deselected
      delete amenities[amenity_id];
    }

    // Create a string to hold the list of currently selected amenities
    let amenitiesList = "";

    // Iterate through the 'amenities' object to build a string of selected amenity identifiers
    for (const id in amenities) {
      // Concatenate the amenity_id to 'amenitiesList', separating each with a comma if needed
      if (amenitiesList === "") amenitiesList += id;
      else amenitiesList += ", " + id;
    }

    // Set the content of the <h4> tag inside the 'div.amenities' element to the updated list
    $("div.amenities h4").text(amenitiesList);
  });
});
