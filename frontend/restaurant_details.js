document.addEventListener('DOMContentLoaded', () => {
    const restaurantDetailsJson = sessionStorage.getItem('restaurantDetails');
    if (restaurantDetailsJson) {
        console.log('Data retrieved from sessionStorage:', restaurantDetailsJson); // Debugging statement
        // displayRestaurantDetails(JSON.parse(restaurantDetails));
        const restaurantDetails = JSON.parse(restaurantDetailsJson);
        console.log('Parsed restaurantDetails:', restaurantDetails); // Debugging statement
        displayRestaurantDetails(restaurantDetails);
    } else {
        console.error('No restaurant details found in sessionStorage');
    }
});

function displayRestaurantDetails(restaurant) {
    console.log(restaurant);
    // console.log(restaurant.name);
    const detailsDiv = document.getElementById('restaurant-details');
    console.log('detailsDiv:', detailsDiv);
    detailsDiv.innerHTML = `
        <center>
            <h1>${restaurant.name}</h1>
        </center>
        <p><strong>City:</strong> ${restaurant.city}</p>
        <p><strong>Locality:</strong> ${restaurant.locality}</p>
        <p><strong>Cuisine:</strong> ${restaurant.cuisine}</p>
        <p><strong>Address:</strong> ${restaurant.address}</p>
        <p><strong>Country-Code:</strong> ${restaurant.country_code}</p>
        <p><strong>Average Cost for two:</strong> ${restaurant.avg_cost_for_two}</p>
        <p><strong>Accepted Currency:</strong> ${restaurant.currency}</p>
        <p><strong>Restaurant Rating:</strong> ${restaurant.rating}</p>
        <p><strong>Price range:</strong> ${restaurant.price_range}</p>
        <p><strong>Online Delivery:</strong> ${restaurant.has_online_delivery}</p>
        <p><strong>Table Booking:</strong> ${restaurant.has_table_booking}</p>
        <p><strong>Number of Votes:</strong> ${restaurant.votes}</p>
        <p><strong>Rating color:</strong> ${restaurant.rating_color}</p>
        <p><strong>Rating Text:</strong> ${restaurant.rating_text}</p>
        
    `;
}
