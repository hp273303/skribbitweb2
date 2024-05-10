
let altCurrentSlide = 0;

function altShowSlide(index) {
  const altSlides = document.querySelector('.alternate-slides');
  const altTotalSlides = document.querySelectorAll('.alternate-slide').length;
  altCurrentSlide = (index + altTotalSlides) % altTotalSlides;
  const altOffset = -altCurrentSlide * 100;
  altSlides.style.transform = `translateX(${altOffset}%)`;
}

function altPrevSlide() {
  altShowSlide(altCurrentSlide - 1);
}

function altNextSlide() {
  altShowSlide(altCurrentSlide + 1);
}

setInterval(altNextSlide, 3000); // Auto slide every 3 seconds

function openDetails(item, imageSrc) {
  document.getElementById('itemName').innerText = item;
  document.getElementById('itemImage').src = imageSrc;

  // You can add specific details for each item here
  switch (item) {
    case 'Marker':
      document.getElementById('itemDetails').innerText = 'Details about the marker.';
      break;
    case 'Sticky Notes':
      document.getElementById('itemDetails').innerText = 'Details about the sticky notes.';
      break;
    case 'Pencil':
      document.getElementById('itemDetails').innerText = 'Details about the pencil.';
      break;
    case 'Diary':
      document.getElementById('itemDetails').innerText = 'Details about the diary.';
      break;
    case 'Punching Machine':
      document.getElementById('itemDetails').innerText = 'Details about the punching machine.';
      break;
    // Add more cases for other items
  }

  document.getElementById('detailsModal').style.display = 'flex';
}

function closeDetails() {
  document.getElementById('detailsModal').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function() {
  // Show the pop-up
  showPopup();

  // Automatically close the pop-up after 3 seconds
  setTimeout(function() {
    hidePopup();
  }, 3000);
});

function showPopup() {
  document.getElementById("popup").style.display = "block";
}

function hidePopup() {
  document.getElementById("popup").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function() {
  const profileDropdown = document.getElementById("profileDropdown");
  const dropimg = document.querySelector(".dropimg");

  dropimg.addEventListener("click", function() {
    if (profileDropdown.style.display === "none" || profileDropdown.style.display === "") {
      profileDropdown.style.display = "block";
    } else {
      profileDropdown.style.display = "none";
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const name = "{{ profile_data.name }}";
  const slicedName = document.getElementById("slicedName");

  // Slice the name to the first character and convert to uppercase
  if (name) {
    slicedName.textContent = name.slice(0, 1).toUpperCase();
  }

  slicedName.addEventListener("click", function() {
    toggleSubMenu('profileDropdown');
  });
});

function toggleSubMenu(submenuId) {
  var submenu = document.getElementById(submenuId);
  submenu.style.display = (submenu.style.display === 'block') ? 'none' : 'block';
}



function openModal(imageUri, name, brand, quantity, price) {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
  document.getElementById("popup-image").src = imageUri;
  document.getElementById("popup-name").innerHTML = "Product Name: " + name;
  document.getElementById("popup-brand").innerHTML = "Brand: " + brand;
  document.getElementById("popup-quantity").innerHTML = "In Stock: " + quantity;
  document.getElementById("popup-price").innerHTML = "Price: " + price;
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

// Function to change main image when clicking on thumbnails
function changeMainImage(thumbnail) {
  document.getElementById('popup-image').src = thumbnail.src;
}

// Close the modal when clicking on the close button
document.getElementsByClassName('close')[0].addEventListener('click', closeModal);

// Close the modal when clicking anywhere outside the modal content
window.addEventListener('click', function(event) {
  if (event.target == document.getElementById('myModal')) {
    closeModal();
  }
});

function openModal(product_image_uri, product_left_img_uri, product_right_img_uri, product_specifications_image_uri, product_category, product_brand, product_quantity, product_price) {
  // Set the main product image
  document.getElementById('popup-image').src = product_image_uri;

  // Set product details
  document.getElementById('popup-name').innerHTML = "Product Name: " + product_category;
  document.getElementById('popup-brand').innerHTML = "Brand: " + product_brand;
  document.getElementById('popup-quantity').innerHTML = "In Stock: " + product_quantity;
  document.getElementById('popup-price').innerHTML = "Price: " + product_price;

  // Set thumbnails src
  document.getElementsByClassName('thumbnail')[0].src = product_left_img_uri;
  document.getElementsByClassName('thumbnail')[1].src = product_right_img_uri;
  document.getElementsByClassName('thumbnail')[2].src = product_specifications_image_uri;
  document.getElementsByClassName('thumbnail')[3].src = product_image_uri;

  // Display the modal
  document.getElementById('myModal').style.display = "block";
}

function addToCart(productId, authToken) {
  // Log the authentication token and the product ID
  console.log("Auth Token:", authToken);
  console.log("Product ID:", productId);

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Define the request method and URL
  xhr.open("POST", "http://192.168.1.35:8000/add_to_cart/", true);

  // Set the request headers including the authentication token
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("Authorization", "Token " + authToken);

  // Create a JSON payload with the product ID
  var data = JSON.stringify({ "id": productId });

  // Define the callback function to handle the response
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        // If the request is successful, show a success message
        alert("Successfully added to cart!");
      } else {
        // If there's an error, show an error message
        alert("Error: Failed to add to cart. Please try again.");
      }
    }
  };

  // Send the request with the JSON payload
  xhr.send(data);
}


function toggleImage(img) {
  if (img.src.includes("grey.png")) {
    img.src = "/static/images/red.png";
  } else {
    img.src = "/static/images/grey.png";
  }
}
/* 
// Define the toggleWishlist function in the global scope
function toggleWishlist(productId, authToken) {
  // Check if the product is already in the wishlist
  var isInWishlist = Implement logic to check if the product is in the wishlist ;

  // If the product is in the wishlist, remove it; otherwise, add it
  if (isInWishlist) {
    removeFromWishlist(productId, authToken);
  } else {
    addToWishlist(productId, authToken);
  }
}
*/

var addToWishlistActive = true;

function toggleWishlistAction(productId, authToken, imageElement) {
  if (addToWishlistActive) {
    addToWishlist(productId, authToken);
    imageElement.src = "/static/images/red.png"; // Change image to red when adding
  } else {
    removeFromWishlist(productId, authToken);
    imageElement.src = "/static/images/grey.png"; // Change image to grey when removing
  }
  addToWishlistActive = !addToWishlistActive;
}

function addToWishlist(productId, authToken) {
  // Log the authentication token and the product ID
  console.log("Auth Token:", authToken);
  console.log("Product ID:", productId);

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Define the request method and URL for adding to wishlist
  xhr.open("POST", "http://192.168.1.35:8000/add_to_wishlist/", true);

  // Set the request headers including the authentication token
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("Authorization", "Token " + authToken);

  // Create a JSON payload with the product ID
  var data = JSON.stringify({ "id": productId });

  // Define the callback function to handle the response
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        // If the request is successful, show a success message
        alert("Successfully added to wishlist!");
      } else {

        alert("Error: Failed to add to wishlist. Please try again.");
      }
    }
  };

  xhr.send(data);
}


function removeFromWishlist(productId, authToken) {
  // Log the authentication token and the product ID
  console.log("Auth Token:", authToken);
  console.log("Product ID:", productId);

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Define the request method and URL for removing from wishlist
  xhr.open("DELETE", "http://192.168.1.35:8000/remove-from-wishlist/", true);

  // Set the request headers including the authentication token
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("Authorization", "Token " + authToken);

  // Create a JSON payload with the product ID
  var data = JSON.stringify({ "id": productId });

  // Define the callback function to handle the response
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {

        alert("Successfully removed from wishlist!");
      } else {

        alert("Error: Failed to remove from wishlist. Please try again.");
      }
    }
  };

  xhr.send(data);
}

