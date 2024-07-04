let currentPage = 1;
const perPage = 10;

document.addEventListener('DOMContentLoaded', () => {
    // fetchRandomRestaurants();
    fetchRestaurants(currentPage);
});

function fetchRandomRestaurants() {
    fetch('http://localhost:5000/restaurants/random')
        .then(response => response.json())
        .then(data => displayRestaurants(data))
        .catch(error => console.error('Error fetching data:', error));
}

function fetchRestaurants(page) {
    fetch(`http://localhost:5000/restaurants?page=${page}&per_page=${perPage}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.restaurants_data);
            displayRestaurants(data.restaurants_data);
            updatePaginationControls(data);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function updatePaginationControls(data) {
    currentPage = data.page;
    document.getElementById('page-info').textContent = `Page ${currentPage} of ${data.total_pages}`;
    document.getElementById('prev-page').disabled = currentPage === 1;
    document.getElementById('next-page').disabled = currentPage === data.total_pages;
}

function displayRestaurants(restaurants) {
    console.log(restaurants)
    restaurants.forEach((restaurant, index) => {
        const restaurantElement = document.getElementById(`restaurant-${index + 1}`);
        if (restaurantElement) {
            restaurantElement.innerHTML = 
            `<h3><center>${restaurant.name}</center></h3>
            <button onclick="handleButtonClick(${restaurant.id})">View Details</button> `;
        }
    });
} 

function handleButtonClick(restaurantId) {
    console.log('Button clicked for restaurant ID:', restaurantId);
    fetch(`http://localhost:5000/restaurant/${restaurantId}`)
        .then(response => response.json())
        .then(data => {
            console.log('Data to store in sessionStorage:', data);
            sessionStorage.setItem('restaurantDetails', JSON.stringify(data));
            window.location.href = `restaurant_details.html`;
        })
        .catch(error => console.error('Error fetching data:', error));
}

