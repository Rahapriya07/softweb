# Ex.07 Restuarant Website
## Date:03-11-2025

## AIM:
To develop a static Resturant website to display the menu and services provided by the resturant.

## DESIGN STEPS:

### Step 1:
Requirement collection.

### Step 2:
Creating the layout using HTML and CSS.

### Step 3:
Updating the sample content.

### Step 4:
Choose the appropriate style and color scheme.

### Step 5:
Validate the layout in various browsers.

### Step 6:
Validate the HTML code.

### Step 7:
Publish the website in the given URL.

## PROGRAM:

### index.html
```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aroma Restaurant</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Aroma Restaurant</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="hero">
    <h2>Delicious Food, Cozy Ambience</h2>
    <p>Experience the best dishes made with love and fresh ingredients.</p>
    <a href="menu.html" class="btn">Explore Menu</a>
  </section>

  <footer>
    <p>© 2025 Aroma Restaurant | Designed by Raha Priya Dharshini </p>
  </footer>
</body>
</html>
```
### menu.html
```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Menu - Aroma Restaurant</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Our Menu</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="menu">
    <div class="menu-item">
      <h3>Grilled Chicken</h3>
      <p>Served with garlic sauce and fries — ₹250</p>
    </div>
    <div class="menu-item">
      <h3>Paneer Butter Masala</h3>
      <p>Creamy tomato-based curry with soft paneer cubes — ₹200</p>
    </div>
    <div class="menu-item">
      <h3>Veg Fried Rice</h3>
      <p>Spicy and flavorful rice loaded with veggies — ₹150</p>
    </div>
    <div class="menu-item">
      <h3>Chocolate Lava Cake</h3>
      <p>Warm and gooey chocolate delight — ₹180</p>
    </div>
  </section>

  <footer>
    <p>© 2025 Aroma Restaurant</p>
  </footer>
</body>
</html>
```

### about.html
```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About - Aroma Restaurant</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>About Us</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="about">
    <h2>Welcome to Aroma</h2>
    <p>We are passionate about serving delicious and freshly prepared meals that bring people together. 
    Our chefs use only the finest ingredients to create mouth-watering dishes that satisfy every craving.</p>

    <p>From Indian classics to continental delights, we believe every plate tells a story. 
    Come, experience food made with love and served with warmth.</p>
  </section>

  <footer>
    <p>© 2025 Aroma Restaurant</p>
  </footer>
</body>
</html>
```
### gallery.html
```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gallery - Aroma Restaurant</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Our Gallery</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="gallery">
    <h2>Delicious Moments Captured</h2>
    <div class="gallery-grid">
      <img src="https://images.unsplash.com/photo-1600891964599-f61ba0e24092?w=800" alt="Pasta Dish">
      <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800" alt="Fresh Salad">
      <img src="https://images.unsplash.com/photo-1594007654729-407eedc4be65?w=800" alt="Pizza">
      <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800" alt="Burger">
      <img src="https://images.unsplash.com/photo-1551024601-bec78aea704b?w=800" alt="Dessert">
      <img src="https://images.unsplash.com/photo-1551782450-a2132b4ba21d?w=800" alt="Grilled Chicken">
    </div>
  </section>

  <footer>
    <p>© 2025 Aroma Restaurant</p>
  </footer>
</body>
</html>
```

### contact.html
```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact - Aroma </title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Contact Us</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="contact">
    <h2>Get in Touch</h2>
    <p>📍 Location: Millerpuram,Tuticorin</p>
    <p>📞 Phone: +91 4567341100</p>
    <p>✉️ Email: info@aroma.com</p>

    <h3>Reserve a Table</h3>
    <form class="reservation-form">
      <input type="text" placeholder="Your Name" required>
      <input type="email" placeholder="Email Address" required>
      <input type="tel" placeholder="Phone Number" required>
      <input type="date" required>
      <input type="time" required>
      <textarea placeholder="Special Requests"></textarea>
      <button type="submit">Book Now</button>
    </form>
  </section>

  <footer>
    <p>© 2025 TAroma Restaurant</p>
  </footer>
</body>
</html>
```



## OUTPUT:

![alt text](<Screenshot 2025-11-03 191348.png>)

![alt text](<Screenshot 2025-11-03 191421.png>)

![alt text](<Screenshot 2025-11-03 191437.png>)

![alt text](<Screenshot 2025-11-03 191452.png>)

![alt text](<Screenshot 2025-11-03 191503.png>)


## RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
