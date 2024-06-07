document.addEventListener("DOMContentLoaded", function () {
  var searchInput = document.querySelector(".search-input");
  searchInput.addEventListener("input", function () {
  searchMovies(this.value);
  });
  var arrow = document.querySelector(".arrow");
  var movieList = document.querySelector(".movie-list");
  arrow.addEventListener("click", function () {
  movieList.scrollLeft += 200; // Adjust the scroll distance as 
 desired
  });
  window.addEventListener("DOMContentLoaded", function () {
  var addToCartButtons = document.querySelectorAll(".featured-button");
  addToCartButtons.forEach(function (button) {
  button.addEventListener("click", function (event) {
  event.preventDefault(); // Prevent the default form  submission behavior
  addToCart(event);
  });
  });
  });
  // Function to handle the add to cart button click
  function addToCart(event) {
  var button = event.target; // Get the clicked button
  var movieItem = button.closest('.movie-list-item'); // Find the parent movie list item
  var movieId = movieItem.dataset.movieId; // Get the movie id
  var movieTitle = movieItem.querySelector('.movie-list-item-title').textContent; // Get the movie title
  var movieprice = movieItem.querySelector('.movie-list-item-price').textContent; // Get the movie price
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/add_to_cart", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest"); // Set X-Requested-With header to indicate AJAX request
  xhr.onreadystatechange = function () {
  if (xhr.readyState === XMLHttpRequest.DONE) {
  if (xhr.status === 200) {
  // Show the success message
  alert('Item added successfully to cart');
  window.location.href = '/cart';
  } else {
  alert('Failed to add item to cart');
  }
  }
  };
  var formData = "movie_id=" + encodeURIComponent(movieId) + 
 "&movie_title=" + encodeURIComponent(movieTitle) + "&movie_price="
 + encodeURIComponent(movieprice); // Include the movieprice in the form data
  xhr.send(formData);
  }
  document.addEventListener('DOMContentLoaded', function() {
  const removeButtons = document.querySelectorAll('.cart-item-remove');
  
  removeButtons.forEach(function(button) {
  button.addEventListener('click', function() {
  const movieId = this.getAttribute('data-movie-id');
  const cartItem = this.parentElement.parentElement;
  
  removeFromCart(movieId, cartItem);
  });
  });
  });
  
  function removeFromCart(movieId, cartItem) {
  fetch('/removeFromCart', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json'
  },
  body: JSON.stringify({ movieId: movieId })
  })
  .then(response => {
  // Refresh the page to update the cart
  location.reload();
  })
  .catch(error => {
  console.error('Error:', error);
  alert('An error occurred while removing the item from the cart.');
  });
  }
  
  
  function searchMovies(query) {
  var searchInput = document.querySelector(".search-input");
  var searchText = query.toLowerCase();
  var movieItems = document.querySelectorAll(".movie-list-item");
  movieItems.forEach(function (item) {
  var title = item.querySelector(".movie-list-item-title").textContent.toLowerCase();
  var desc = item.querySelector(".movie-list-item-desc").textContent.toLowerCase();
  if (title.includes(searchText) || desc.includes(searchText)) 
 {
  item.style.display = "block";
  } else {
  item.style.display = "none";
  }
  });
  }
 });
 // JavaScript code for handling the checkout process
 // Get the checkout button element
 const checkoutButton = document.getElementById('checkout-button');
 // Add a click event listener to the checkout button
 checkoutButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent the default form submission
  // Send an AJAX request to the server to initiate the checkout 
 process
  fetch('/checkout')
  .then(response => response.text())
  .then(html => {
  // Create a temporary element to hold the response HTML
  const tempElement = document.createElement('div');
  tempElement.innerHTML = html;
  // Extract the items purchased and total price from the 
 response
  const itemsPurchased = tempElement.querySelector('#items_purchased').innerHTML;
  const totalprice = tempElement.querySelector('#total_price').innerHTML;
  // Update the content of the current page with the items purchased and total price
  document.getElementById('items-purchased').innerHTML = 
 itemsPurchased;
  document.getElementById('total-price').innerHTML = 
 totalprice;
  })
  .catch(error => {
  console.error('Error:', error);
  });
 });
 function showPopupMessage(message) {
  var popupElement = document.getElementById("popup-message");
  popupElement.textContent = message;
  popupElement.style.display = "block";
  
  // Automatically hide the message after 3 seconds
  setTimeout(function() {
  popupElement.style.display = "none";
  }, 3000);
 }