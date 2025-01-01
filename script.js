document.addEventListener('DOMContentLoaded', () => {
    const searchIcon = document.getElementById('search-icon');
    const searchBar = document.getElementById('search-bar');

    // Toggle the search bar on icon click
    searchIcon.addEventListener('click', () => {
        searchBar.classList.toggle('active');
    });

    // Close the search bar when clicking outside
    document.addEventListener('click', (event) => {
        if (!searchBar.contains(event.target) && !searchIcon.contains(event.target)) {
            searchBar.classList.remove('active');
        }
    });
});


// Login Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPassword').value.trim();

            if (!email || !password) {
                alert('Please fill in both email and password.');
            } else if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
            } else {
                alert('Login successful!');
                // Redirect or perform login action
            }
        });
    }
});

// Helper function to validate email
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Register Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registrationForm');

    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const username = document.getElementById('username').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            const confirmPassword = document.getElementById('confirmPassword').value.trim();

            if (!username || !email || !password || !confirmPassword) {
                alert('All fields are required.');
            } else if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
            } else if (password !== confirmPassword) {
                alert('Passwords do not match.');
            } else {
                alert('Registration successful!');
                // Redirect or perform registration action
            }
        });
    }
});

// Dynamic Hero Message Rotation
document.addEventListener('DOMContentLoaded', () => {
    const heroMessage = document.querySelector('.hero-section p');

    if (heroMessage) {
        const messages = [
            'Discover the latest trends in fashion!',
            'Upgrade your wardrobe today!',
            'Shop stylish and affordable outfits!'
        ];

        let currentMessageIndex = 0;

        function rotateHeroMessage() {
            currentMessageIndex = (currentMessageIndex + 1) % messages.length;
            heroMessage.textContent = messages[currentMessageIndex];
        }

        setInterval(rotateHeroMessage, 5000);
    }
});

// Shopping Cart Management
document.addEventListener('DOMContentLoaded', () => {
    const cartItems = document.querySelectorAll('.cart-item');
    const totalItemsEl = document.getElementById('total-items');
    const totalCostEl = document.getElementById('total-cost');

    function updateCartTotals() {
        let totalItems = 0;
        let totalCost = 0;

        cartItems.forEach((item) => {
            const quantity = parseInt(item.querySelector('input[type="number"]').value, 10);
            const price = parseFloat(item.querySelector('.item-price').textContent.replace('$', ''));
            totalItems += quantity;
            totalCost += quantity * price;
        });

        if (totalItemsEl && totalCostEl) {
            totalItemsEl.textContent = totalItems;
            totalCostEl.textContent = totalCost.toFixed(2);
        }
    }

    if (cartItems.length > 0) {
        cartItems.forEach((item) => {
            const quantityInput = item.querySelector('input[type="number"]');
            const removeButton = item.querySelector('.remove-item');

            if (quantityInput) {
                quantityInput.addEventListener('change', updateCartTotals);
            }

            if (removeButton) {
                removeButton.addEventListener('click', () => {
                    item.remove();
                    updateCartTotals();
                });
            }
        });
    }

    updateCartTotals();
});

// Redirect to Cart Page on Add to Cart Button Click
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Redirect to shopping cart page
            window.location.href = 'shopping-cart.html';
        });
    });
});

// Checkout Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const checkoutForm = document.getElementById('checkout-form');

    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const fullName = document.getElementById('full-name').value.trim();
            const address = document.getElementById('address').value.trim();
            const paymentMethod = document.querySelector('input[name="payment-method"]:checked');

            if (!fullName || !address || !paymentMethod) {
                alert('Please fill in all required fields and select a payment method.');
            } else {
                alert('Order placed successfully!');
                // Proceed with order placement
            }
        });
    }
});