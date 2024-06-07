// search.js
// app.js
function searchMovies() {
    var searchInput = document.querySelector(".search-input");
    var searchText = searchInput.value.toLowerCase();
    var movieItems = document.querySelectorAll(".movie-list-item");
    movieItems.forEach(function (item) {
    var title = item.querySelector(".movie-list-item-title").textContent.toLowerCase();
    var desc = item.querySelector(".movie-list-item-desc").textContent.toLowerCase();
    if (title.includes(searchText) || 
   desc.includes(searchText)) {
    item.style.display = "block";
    } else {
    item.style.display = "none";
    }
    });
   }
    
   function displayResults(results) {
    const resultsContainer = document.getElementById('search_results');
    resultsContainer.innerHTML = '';
    
    if (results.length === 0) {
    resultsContainer.textContent = 'No results found.';
    return;
    }
    
    results.forEach(function (result) {
    const movieResult = document.createElement('div');
    movieResult.classList.add('movie-result');
    
    const image = document.createElement('img');
    image.src = result.image_path;
    movieResult.appendChild(image);
    
    const movieDetails = document.createElement('div');
    movieDetails.classList.add('movie-details');
    
    const movieTitle = document.createElement('h3');
    movieTitle.classList.add('movie-title');
    movieTitle.textContent = result.title;
    movieDetails.appendChild(movieTitle);
    
    const movieDirectedBy = document.createElement('p');
    movieDirectedBy.classList.add('movie-desc');
    movieDirectedBy.textContent = `Directed by: $
   {result.director}`;
    movieDetails.appendChild(movieDirectedBy);
    
    const movieRunningTime = document.createElement('p');
    movieRunningTime.classList.add('movie-desc');
    movieRunningTime.textContent = `Running time: $
   {result.running_time}`;
    movieDetails.appendChild(movieRunningTime);
    
    movieResult.appendChild(movieDetails);
    resultsContainer.appendChild(movieResult);
    });
   }